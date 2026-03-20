#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────
# PreHook: Graph Intelligence Loader
# Runs BEFORE an OSINT investigation begins.
# Scans the workspace for existing knowledge graph files,
# runs NetworkX analysis, and outputs a JSON summary so the
# investigating agent knows what's already been mapped.
# ─────────────────────────────────────────────────────────────
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
NETWORK_ANALYSIS="$SCRIPT_DIR/network_analysis.py"

# Where to look for graph files — search common locations
SEARCH_DIRS=("." "./mnt" "$HOME")
GRAPH_PATTERNS=("*graph*.json" "*supply_chain*.json" "*network*.json" "*knowledge*.json")

OUTPUT_DIR="${1:-./.osint_prehook_output}"
mkdir -p "$OUTPUT_DIR"

found_graphs=()

# Scan for existing graph JSON files
for dir in "${SEARCH_DIRS[@]}"; do
  if [ -d "$dir" ]; then
    for pattern in "${GRAPH_PATTERNS[@]}"; do
      while IFS= read -r -d '' f; do
        # Validate it's actually a JSON with nodes/edges structure
        if python3 -c "
import json, sys
try:
    d = json.load(open('$f'))
    assert 'nodes' in d or 'entities' in d or 'directed' in d
except:
    sys.exit(1)
" 2>/dev/null; then
          found_graphs+=("$f")
        fi
      done < <(find "$dir" -maxdepth 3 -name "$pattern" -print0 2>/dev/null)
    done
  fi
done

# Deduplicate
mapfile -t found_graphs < <(printf '%s\n' "${found_graphs[@]}" | sort -u)

echo "=== OSINT PreHook: Graph Intelligence Loader ==="
echo "Found ${#found_graphs[@]} existing graph file(s)"

if [ ${#found_graphs[@]} -eq 0 ]; then
  # No existing graphs — output minimal summary
  cat > "$OUTPUT_DIR/prehook_summary.json" <<'ENDJSON'
{
  "status": "no_existing_graphs",
  "message": "No prior knowledge graph found. Starting fresh investigation.",
  "existing_entities": [],
  "existing_entity_count": 0,
  "existing_edge_count": 0,
  "priority_targets": [],
  "investigation_gaps": []
}
ENDJSON
  echo "No existing graphs found. Agent will start fresh."
  cat "$OUTPUT_DIR/prehook_summary.json"
  exit 0
fi

# Run analysis on each found graph and merge results
all_entities=()
all_priorities=()
total_nodes=0
total_edges=0
primary_graph=""

for graph_file in "${found_graphs[@]}"; do
  echo "Analyzing: $graph_file"
  analysis_out="$OUTPUT_DIR/analysis_$(basename "$graph_file" .json)"
  mkdir -p "$analysis_out"

  if python3 "$NETWORK_ANALYSIS" \
    --input "$graph_file" \
    --output-dir "$analysis_out" 2>/dev/null; then

    # If this is the largest graph, mark it as primary
    node_count=$(python3 -c "
import json
d = json.load(open('$graph_file'))
nodes = d.get('nodes', d.get('entities', []))
print(len(nodes))
" 2>/dev/null || echo "0")

    if [ "$node_count" -gt "$total_nodes" ]; then
      total_nodes=$node_count
      primary_graph="$graph_file"
    fi
  fi
done

# Generate consolidated summary from the primary graph
python3 - "$primary_graph" "$OUTPUT_DIR" <<'PYTHON_SCRIPT'
import json, sys, os

graph_file = sys.argv[1]
output_dir = sys.argv[2]

with open(graph_file) as f:
    graph = json.load(f)

nodes = graph.get("nodes", graph.get("entities", []))
edges = graph.get("edges", graph.get("links", []))
events = graph.get("events", [])

# Extract entity names and types
entities = []
for n in nodes:
    name = n.get("name", n.get("id", "unknown"))
    ntype = n.get("type", n.get("category", "unknown"))
    entities.append({"name": name, "type": ntype})

# Try to load metrics if available
metrics_file = os.path.join(output_dir, f"analysis_{os.path.basename(graph_file).replace('.json','')}", "network_metrics.json")
priorities = []
top_central = []
communities = []
gaps = []

if os.path.exists(metrics_file):
    with open(metrics_file) as mf:
        metrics = json.load(mf)

    # Extract priority targets
    if "investigation_priorities" in metrics:
        for p in metrics["investigation_priorities"].get("high_priority", []):
            priorities.append(p)

    # Top central nodes
    if "centrality_analysis" in metrics:
        degree = metrics["centrality_analysis"].get("degree_centrality", {})
        sorted_nodes = sorted(degree.items(), key=lambda x: x[1], reverse=True)[:5]
        top_central = [{"name": k, "centrality": round(v, 4)} for k, v in sorted_nodes]

    # Communities
    if "community_detection" in metrics:
        communities = metrics["community_detection"].get("communities", [])

    # Gaps (low-data nodes)
    if "investigation_priorities" in metrics:
        for g in metrics["investigation_priorities"].get("data_gaps", []):
            gaps.append(g)

summary = {
    "status": "graph_loaded",
    "primary_graph": graph_file,
    "existing_entity_count": len(nodes),
    "existing_edge_count": len(edges),
    "existing_event_count": len(events),
    "existing_entities": entities,
    "top_central_nodes": top_central,
    "communities": communities,
    "priority_targets": priorities,
    "investigation_gaps": gaps,
    "message": f"Found existing graph with {len(nodes)} entities, {len(edges)} relationships, {len(events)} events. Review the entities and gaps before starting new investigation to avoid redundant work and to follow up on identified leads."
}

out_path = os.path.join(output_dir, "prehook_summary.json")
with open(out_path, "w") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)

print(json.dumps(summary, ensure_ascii=False, indent=2))
PYTHON_SCRIPT

echo "=== PreHook complete. Summary saved to $OUTPUT_DIR/prehook_summary.json ==="
