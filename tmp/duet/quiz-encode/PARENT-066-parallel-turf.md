# PARENT-066: parallel expansion — writer2b + viewer2 turf (2026-10-15)

Owner approved +2 seats to speed the two bottlenecks (map
velocity, VERIFY throughput). Effective immediately; all
seats poll this dir every turn.

## Map writers (disjoint turf, shared viewer)
- writer2 (lanes/encode-writer2): R-rows + gap backfills
  ONLY (R127 done; R133 next per hb-100). STOP cutting new
  P-rows — P136+ belongs to writer2b. Overlap = rework.
- writer2b (lanes/encode-writer2b, NEW, branched from
  writer2@8aaeccb): P-rows P136+ forward ONLY, oldest-first.
  Same lane discipline: LOCAL-ONLY commits, RGRAM-GREEN
  first-hand per commit, Qs to quiz when blocked.
- cport pulls BOTH lanes oldest-first (merge --no-ff
  partials as before); on CSV adjacent-append conflicts,
  union rows, never drop a side.

## Viewers (disjoint ranges)
- viewer (r7): VERIFY bands 160-163 (oldest-first) +
  backlog Q-321..Q-361 drain (answer or MOOT-with-cause).
- viewer2 (r1, NEW): VERIFY bands 164+ (start 164
  0133498, then 165 7f4db2c, 167 86ae4e6, 169 b902356,
  enumerate at runtime) + NEW questions Q-362+ only.
  Same VERIFY battery shape (own tree, own build, own
  runs, wall-grep) + heartbeats NOTE-viewer2-hb-r1-NN.md.
- VERIFY filename CLAIM backstop: both check CLAIM-*.md
  before starting a battery; write CLAIM-viewer2-<sha>.md.

## Unchanged
Sweep turf (odds/evens), wall scope PARENT-032, no-push,
TMPDIR-on-NVME rule. Parent merges oldest-first as
VERIFYs land.
