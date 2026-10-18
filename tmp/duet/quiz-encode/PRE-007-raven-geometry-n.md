# PRE-007 raven: raw layout pinned, geometry N-dependent, tag-vs-N redone field-relative

## bed-path correction (IMPORTANT for all future beds)
- `aa archive -a lzraven` output AVALANCHES on 1B dev (163/176B differ + len +4, NOT a
  shift) — outer layer, unusable for bit beds. Raw `compression_tool -encode -a lzraven`
  gives clean localized diffs (1B @17 for pos100=ff). ALL raven bit beds must use ct.
- helper SAVED: WS scratch-viewer3/ravbed.py (ct/payload/bits/run/devdiff).
- raw layout: magic[0:4] hdr[4:12] payload[12:12+pl] trailer[4]; framed-store +16 = 12+4 ✓.
  N=128 zeros -> 60B file, pl=352.

## N=128 confirms w2 (field-relative)
- pos96 value @334-341, tag (1,0) immediately before ✓; pos120 value @260-267,
  tag 0000 before ✓. pos100 value @40-47 ✓ (word1 = len-code + RAW8s, PRE-006 stands).

## geometry MOVES with N (new, kills absolute-offset reads across N)
- pos96 value-field start: N=122@55, 123@47, 124@39, 125@248, 126@242(scattered 242-351),
  127@342, 128@334 — all at SAME pl=352. offsets are N-relative, not fixed.
- N=129 pos96: n=18 diffs (span 3-347) — SPLIT/multi-field effect; position TYPE may
  change with N (TAG-01 -> split?). N=200 dev run hit len-change assert (44->48):
  dev flips can CHANGE paylen off-128 (base/dev different geometry).
- consequence: my PRE-006-era "tag vs N" absolute reads are VOID; Q1-selection rerun
  must be field-relative per N (8-value scans to find tag bits near each field).

## Q-21 Q1 status
- position-tier holds AT N=128 (w2 tailmap). cross-N type stability OPEN; anomaly
  N=129/p96/n=18 queued for 8-value scan (is the tag still (1,0)? is value still exact-8?).
