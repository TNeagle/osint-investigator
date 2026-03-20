#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────
# PostHook: Graph Intelligence Merger
# Runs AFTER an OSINT investigation completes.
# Collects new findings (entities, edges, events) from the
# investigation output and merges them into the existing
# knowledge graph, then re-runs analysis.
# ─────────────────────────────────────────────────────────────
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
NETWORK_ANALYSIS="$SCRIPT_DIR/network_analysis.py"

# Input: path to new findings JSON (produced by the agent during investigation)
NEW_FINDINGS="${1:-./.osint_new_findings.json}"
# Where to search for existing graph
SEARCH_DIRS=("." "./mnt" "$HOME")
GRAPH_PATTERNS=("*graph*.json" "*supply_chain*.json" "*network*.json" "*knowledge*.json")
OUTPUT_DIR="${2:-./.osint_posthook_output}"

mkdir -p "$OUTPUT_DIR"

echo "=== OSINT PostHook: Graph Intelligence Merger ==="

# ── Step 1: Locate existing graph ──────────────────────────
existing_graph=""
largest_size=0

for dir in "${SEARCH_DIRS[@]}"; do
  if [ -d "$dir" ]; then
    for pattern in "${GRAPH_PATTERNS[@]}"; do
      while IFS= read -r -d '' f; do
        size=$(python3 -c "
import json
try:
    d = json.load(open('$f'))
    nodes = d.get('nodes', d.get('entities', []))
    print(len(nodes))
except:
    print(0)
" 2>/dev/null || echo "0")
        if [ "$size" -gt "$largest_size" ]; then
          largest_size=$size
          existing_graph="$f"
        fi
      done < <(find "$dir" -maxdepth 3 -name "$pattern" -print0 2>/dev/null)
    done
  fi
done

# ── Step 2: Check for new findings ────────────────────────
if [ ! -f "$NEW_FINDINGS" ]; then
  echo "Warning: No new findings file at $NEW_FINDINGS"
  echo "The investigating agent should save new entities/edges/events as JSON."
  echo "Expected format:"
  cat <<'EXAMPLE'
{
  "new_entities": [
    {"name": "Company X", "type": "company", "metadata": {...}}
  ],
  "new_edges": [
    {"source": "Company X", "target": "Company Y", "relation": "supplies_to", "metadata": {...}}
  ],
  "new_events": [
    {"date": "2026-03-01", "description": "...", "entities": ["Company X"], "source": "..."}
  ]
}
EXAMPLE
  exit 1
fi

echo "New findings: $NEW_FINDINGS"
echo "Existing graph: ${existing_graph:-none}"

# ── Step 3: Merge new findings into graph ──────────────────
python3 - "$existing_graph" "$NEW_FINDINGS" "$OUTPUT_DIR" <<'PYTHON_MERGE'
import json, sys, os
from datetime import datetime

existing_path = sys.argv[1] if sys.argv[1] else None
new_path = sys.argv[2]
output_dir = sys.argv[3]

# Load existing graph or create empty one
if existing_path and os.path.exists(existing_path):
    with open(existing_path) as f:
        graph = json.load(f)
    print(f"Loaded existing graph from {existing_path}")
else:
    graph = {
        "directed": True,
        "multigraph": False,
        "graph": {"created": datetime.now().isoformat(), "description": "OSINT Knowledge Graph"},
        "nodes": [],
        "edges": [],
        "events": []
    }
    print("No existing graph found. Creating new one.")

# Load new findings
with open(new_path) as f:
    findings = json.load(f)

# Build lookup of existing entity names
existing_names = set()
nodes = graph.get("nodes", [])
for n in nodes:
    existing_names.add(n.get("name", n.get("id", "")))

# Merge new entities
added_entities = 0
for entity in findings.get("new_entities", []):
    name = entity.get("name", "")
    if name and name not in existing_names:
        node = {
            "name": name,
            "id": name,
            "type": entity.get("type", "unknown"),
            **{k: v for k, v in entity.items() if k not in ("name", "type")}
        }
        nodes.append(node)
        existing_names.add(name)
        added_entities += 1
        print(f"  + Entity: {name} ({entity.get('type', 'unknown')})")
    elif name in existing_names:
        # Update metadata for existing entity
        for n in nodes:
            if n.get("name") == name or n.get("id") == name:
                meta = entity.get("metadata", {})
                if meta:
                    n.setdefault("metadata", {}).update(meta)
                    print(f"  ~ Updated: {name}")
                break

graph["nodes"] = nodes

# Merge new edges
edges = graph.get("edges", graph.get("links", []))
existing_edges = set()
for e in edges:
    key = (e.get("source", ""), e.get("target", ""), e.get("relation", e.get("label", "")))
    existing_edges.add(key)

added_edges = 0
for edge in findings.get("new_edges", []):
    key = (edge.get("source", ""), edge.get("target", ""), edge.get("relation", ""))
    if key not in existing_edges and key[0] and key[1]:
        edge_obj = {
            "source": edge["source"],
            "target": edge["target"],
            "relation": edge.get("relation", "related_to"),
            "label": edge.get("relation", "related_to"),
            **{k: v for k, v in edge.items() if k not in ("source", "target", "relation")}
        }
        edges.append(edge_obj)
        existing_edges.add(key)
        added_edges += 1
        print(f"  + Edge: {edge['source']} --[{edge.get('relation','')}]--> {edge['target']}")

graph["edges"] = edges

# Merge new events
events = graph.get("events", [])
added_events = 0
for event in findings.get("new_events", []):
    # Simple dedup by description similarity
    desc = event.get("description", "")
    if desc and not any(e.get("description", "") == desc for e in events):
        events.append(event)
        added_events += 1
        print(f"  + Event: {desc[:60]}...")

graph["events"] = events

# Update graph metadata
graph.setdefault("graph", {})["last_updated"] = datetime.now().isoformat()
graph["graph"]["total_merges"] = graph["graph"].get("total_merges", 0) + 1

# Save merged graph
# Write back to original location if it exists, also save to output
if existing_path:
    with open(existing_path, "w") as f:
        json.dump(graph, f, ensure_ascii=False, indent=2)
    print(f"\nUpdated existing graph: {existing_path}")

output_graph = os.path.join(output_dir, "merged_graph.json")
with open(output_graph, "w") as f:
    json.dump(graph, f, ensure_ascii=False, indent=2)

# Summary
summary = {
    "status": "merge_complete",
    "added_entities": added_entities,
    "added_edges": added_edges,
    "added_events": added_events,
    "total_entities": len(graph["nodes"]),
    "total_edges": len(graph["edges"]),
    "total_events": len(graph.get("events", [])),
    "output_graph": output_graph,
    "original_graph_updated": existing_path or "N/A"
}

summary_path = os.path.join(output_dir, "posthook_summary.json")
with open(summary_path, "w") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)

print(f"\n=== Merge Summary ===")
print(f"Added: {added_entities} entities, {added_edges} edges, {added_events} events")
print(f"Total: {len(graph['nodes'])} entities, {len(graph['edges'])} edges, {len(graph.get('events',[]))} events")
print(json.dumps(summary, ensure_ascii=False, indent=2))
PYTHON_MERGE

# ── Step 4: Re-run network analysis on merged graph ───────
merged_graph="$OUTPUT_DIR/merged_graph.json"
if [ -f "$merged_graph" ]; then
  echo ""
  echo "Running network analysis on merged graph..."
  analysis_out="$OUTPUT_DIR/analysis"
  mkdir -p "$analysis_out"
  python3 "$NETWORK_ANALYSIS" \
    --input "$merged_graph" \
    --output-dir "$analysis_out" 2>/dev/null || echo "Warning: Network analysis had issues (non-fatal)"
  echo "Analysis saved to $analysis_out/"
fi

echo "=== PostHook complete ==="
