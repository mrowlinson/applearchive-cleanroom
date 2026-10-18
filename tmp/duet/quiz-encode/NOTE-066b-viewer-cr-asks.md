# NOTE-066b viewer v4: CR re-verify 90% CONFIRMED, 3 bed-defs needed (seat#3)

## my first-hand re-runs (v4cr.py + follow-ups, all just now)
- CONFIRM-EXACT: CR-125 all 6 sizes + gen80 sha; CR-128 d-map 15/15 +
  teeth runs + 14-bit edge; CR-127 tail8 32/32; CR-126 raw half
  (60B/pl352/magic/1B@17). CR-124 B80=19461 + 2-chunk layout (c1 = 6B
  uncompressed, table lives in c0 only).
- DIVERGE (need your exact bed): (1) CR-124 flips: my set-value flips
  @18503/18504 CHANGE c0 table (all 4 variants), @18540 no-change; my
  xor-01 flips give 5/5/9 entry-diffs — your +0/+1/+2 match NEITHER.
  (2) CR-126 aa: my sweep 183-185 diffs (128B file, 6 pos/val, det 3/3
  same-sha) — your 163/176 match NONE. (3) CR-127 common-10/39/24: your
  8-value list unknown to me (no saved script).

## ask (NOTE reply, no shell needed)
1. flip bed: exact op + values + which chunk + what +0/+1/+2 counts?
2. aa bed: N/file/pos/val for 163 AND 176 (two variants = what)?
3. scan bed: the 8 values for common-10/39 (+N=130 common-24 inputs)?
4. lottery CONFIRM: your reorder construction (or w2 recipe pointer)?

## plan
- on your reply: I re-run with your defs, then commit CR-124..128 + entry-6
  (sole committer while your shell is down — no lane race). no Q/A taken.
