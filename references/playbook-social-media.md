# Social Media & Digital Footprint Investigation Playbook

**This playbook is fully automated** — every technique below uses WebSearch (site: operators) or WebFetch (public archive services). No login required.

## Mandatory Execution Rule

When investigating ANY person, execute ALL six phases below in order. Do not skip phases. If a phase returns zero results, record "Phase X: no public results found" in the report — this is itself a finding (unusually low digital footprint may indicate scrubbing).

---

## Phase 1: Platform-by-Platform Public Content Search

For each target person, run ALL of the following searches. Replace `[NAME]` with the target's full name and known aliases.

### Facebook (公開貼文 & 粉專)
```
WebSearch: site:facebook.com "[NAME]"
WebSearch: site:facebook.com "[NAME]" (each alias separately)
WebSearch: site:facebook.com/[username] (if username known)
```
What to extract: public posts, page likes, check-ins, tagged photos, public group memberships, page creation date, follower count.

### Instagram
```
WebSearch: site:instagram.com "[NAME]"
WebSearch: "[NAME]" instagram.com
```
What to extract: bio text, post captions, tagged locations, hashtag usage, follower/following ratio.

### X (Twitter)
```
WebSearch: site:x.com "[NAME]"
WebSearch: site:twitter.com "[NAME]"
WebSearch: "[NAME]" from:twitter.com
```
What to extract: pinned tweet, bio, posting frequency, who they reply to, retweet patterns.

### YouTube
```
WebSearch: site:youtube.com "[NAME]"
WebSearch: site:youtube.com "[NAME]" 直播 OR 質詢 OR 記者會
```
What to extract: channel info, upload frequency, video titles, comment sections (public), view counts, subscriber count.

### LinkedIn
```
WebSearch: site:linkedin.com/in "[NAME]"
WebSearch: site:linkedin.com "[NAME]" [COMPANY]
```
What to extract: job title history, education, connections count, endorsements, activity posts. Compare claimed career timeline with official registry records.

### TikTok
```
WebSearch: site:tiktok.com "[NAME]"
```

### Threads
```
WebSearch: site:threads.net "[NAME]"
```

---

## Phase 2: Taiwan-Specific Forum & Community Search

These platforms are heavily indexed by search engines and contain high-value public discussion.

### PTT (批踢踢實業坊)
```
WebSearch: site:ptt.cc "[NAME]"
WebSearch: site:ptt.cc/bbs/HatePolitics "[NAME]"
WebSearch: site:ptt.cc/bbs/Gossiping "[NAME]"
```
What to extract: discussion threads, leaked info, insider comments, public sentiment timeline.

### Dcard
```
WebSearch: site:dcard.tw "[NAME]"
```

### Mobile01
```
WebSearch: site:mobile01.com "[NAME]"
```

### LINE Today 留言 (indexed by Google)
```
WebSearch: site:today.line.me "[NAME]"
```

### 噗浪 Plurk
```
WebSearch: site:plurk.com "[NAME]"
```

---

## Phase 3: Cross-Platform Username Correlation

If you find a username on one platform, immediately search for the SAME username on all other platforms:

```
WebSearch: "[username]" site:facebook.com OR site:instagram.com OR site:x.com OR site:github.com OR site:medium.com
WebSearch: "[username]" site:youtube.com OR site:tiktok.com OR site:linkedin.com OR site:plurk.com
```

Also search for the username as plain text — it may appear in:
- Forum signatures
- Code repositories (GitHub, GitLab)
- Domain WHOIS records
- App store developer profiles
- Podcast directories

**Automated cross-reference:** If Person A's LinkedIn says they worked at Company X from 2018-2020, search `site:facebook.com "[Person A]" "Company X"` for photos/posts from that period. Discrepancies between social media activity and claimed employment are red flags.

---

## Phase 4: Deleted & Historical Content Recovery

### Wayback Machine (Internet Archive)
```
WebFetch: https://web.archive.org/web/*/[target URL]
```
For each social media profile URL found in Phase 1, check Wayback Machine for:
- Old bio versions (job title changes, deleted affiliations)
- Deleted posts or pages
- Follower count changes over time
- Profile photo history

### Archive.today
```
WebSearch: site:archive.today "[NAME]" OR site:archive.ph "[NAME]"
WebSearch: site:archive.today [known profile URL]
```

### Google Cache
```
WebSearch: cache:[known profile URL]
```

### Key pattern: When someone scrubs their profile AFTER a scandal breaks, the timeline of deletion is itself intelligence:
- Compare Wayback snapshots from before vs. after scandal date
- Note what was removed — that's what they consider incriminating

---

## Phase 5: Network & Interaction Analysis

This phase maps the social connections AROUND the target, not just the target's own posts.

### Mutual tagging / mentions
```
WebSearch: site:facebook.com "[NAME_A]" "[NAME_B]"    (for each known associate)
WebSearch: site:instagram.com "[NAME_A]" "[NAME_B]"
WebSearch: "@[username_A]" "@[username_B]" site:x.com
```

### Event co-attendance
```
WebSearch: "[NAME_A]" "[NAME_B]" 餐會 OR 聚會 OR 活動 OR 尾牙 OR 記者會
WebSearch: "[NAME_A]" "[NAME_B]" site:facebook.com 照片 OR photo
```

### Group & organization memberships
```
WebSearch: site:facebook.com/groups "[NAME]"
WebSearch: "[NAME]" 協會 OR 商會 OR 扶輪社 OR 獅子會 OR 同鄉會 OR 校友會
```

### Contradiction detection
For each relationship claim in the investigation (e.g., "Person A says they don't know Person B"):
1. Search for co-appearances: `"[NAME_A]" "[NAME_B]"` across all platforms
2. Search for tagged photos: `site:facebook.com "[NAME_A]" 標註 "[NAME_B]"`
3. Check event guest lists, group memberships, mutual friends visible in public posts
4. If social media shows interaction but the person claims "不熟", flag as **credibility issue**

---

## Phase 6: Behavioral Pattern Analysis

### Posting time analysis
From the posts found in Phases 1-2, note the timestamps. Patterns to detect:
- **Timezone inconsistency**: Claims to be in Taiwan but posts at 3am consistently → may be in a different timezone
- **Work-hour activity**: Government official posting personal content during office hours → attendance issue
- **Sudden silence**: A usually active poster goes silent for days → may coincide with arrest, hospitalization, travel, or legal proceedings
- **Burst posting**: Sudden increase in posting frequency around a specific event → crisis management or counter-narrative effort

### Content evolution analysis
Track how the target's messaging changes over time:
- Topic shifts (e.g., suddenly starts posting about a policy area they never mentioned before → may signal new financial interest)
- Tone changes around key dates
- Deleted content patterns

### Bot / fake follower indicators
If the target has public social media:
- Follower spike without corresponding content quality → purchased followers
- Comments that are generic or repetitive → bot engagement
- Follower accounts with no profile pictures, random usernames, zero posts → fake accounts

---

## Output Format

After completing all six phases, produce a structured summary:

```
### Social Media & Digital Footprint Summary

**Accounts found:**
- [Platform]: [URL] — [follower count, creation date if visible]
- ...

**Key findings:**
1. [Most significant finding with source URL]
2. ...

**Cross-platform contradictions:**
- [If any claims contradict registry/court records]

**Deleted/scrubbed content:**
- [What was found on Wayback/archive that's no longer live]

**Network interactions:**
- [Key social connections confirmed or denied by social media evidence]

**Behavioral anomalies:**
- [Timezone, work-hour, silence patterns]

**Investigation gaps (could not automate):**
- [List anything that would require login to verify]
```
