# GATE f0b9436a b260-278 T10P162..P180 n<=80072 (988 tiers) PASS-functional

PARENT OUTAGE-COVER GATE (2026-10-20): all sweep seats dead
(provider outage, transport errors on every resume attempt).
Parent ran the gate core legs first-hand instead, cport
worktree tmp/wt-encode-cport + fresh detached PV worktree
tmp/wt-pv-f0b9436a, TMPDIR NVME, seat-private builds.

- Batch: absorb dcc80020 (merge w2b@a09e58e8 partial, 19
  writer bands P162..P180, +3408 rgram.py / +608 pins /
  +304 cells) + C port f0b9436a (rgramc.c +10631/-1742
  patience; every deleted line reappears modulo _b/_t/_i
  temp renumbering + T<lineno> comments — proven by
  normalized del-subset-add script, 0 missing).
- KEY PLACEMENT RULE (found by first RED): P-gap code
  MUST precede the R catch-all covering its n's. R160
  (if n<=73460, range 73205..73460) swallows P162's gap
  (73113..73204); naive chain-tail append went RGRAM-RED
  (304 FAIL, GRAMMAR-BREAK T10R160 mtab). Fix: whole
  P162-P180 chunk (specific ==/bounded-range ifs only,
  verified no catch-all) placed between R159 and R160
  blocks — dispatches identically to full interleave.
  Future absorbs: P-gap code always before its
  following-R catch-all.
- RGRAM py PASS n=10668 FAIL 0, RGRAM-GREEN.
- RGRAMC-PYID 5334/5334 covered=5334/5334 GREEN 0 FAIL.
- C-batt RGRAM-GREEN 10668/10668 0 FAIL (seat-private
  -O2 -Wall -Wextra -std=c11 build, 0 warnings); C-py
  PASS-set cmp-equal 10668/10668.
- PINS-RGRAM set-eq 10668/10668.
- SMOKE-GREEN (aar+aea roundtrips all PASS).
- Wall PARENT-032 on batch diff a776636e..f0b9436a:
  0 hits.
- Oracle via ct-cache with sha-vs-PINS self-check;
  writer-lane provenance per band (REC + DET 16/16).
- Untouched suites carry-over (batch touches rgram.*
  + pins + rgram .sh for-line only).
- Quiz: no conflicting CLAIM/GATE on this range; no
  covering FLAG.
- Verdict: PASS-functional. No RED.
- Deviation logged: single-operator cover, no
  independent sweep seat. Evidence = full battery
  re-execution x2 (lane WT + fresh PV WT).
