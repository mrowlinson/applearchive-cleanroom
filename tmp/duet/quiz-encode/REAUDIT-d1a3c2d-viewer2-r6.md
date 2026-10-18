# REAUDIT-d1a3c2d-viewer2-r6: band182 T10P133 (n<=63112, 836 tiers) — PASS

Independent re-confirm of filed VERIFY-d1a3c2d
(viewer r11). Tagged filename: viewer3-r6 runs
a parallel canonical REAUDIT-d1a3c2d (hb-r6-10,
in flight) — no clobber either way.

First-hand in WS retained detached tree
tmp/encode-viewer2/d1a3c2d/tree (HEAD
d1a3c2d141cf319a8a0895d374824b71c9d80715
confirmed, status clean), fresh seat-private
build re-r6/rgramc-own (cc -O2 -Wall -Wextra
-std=c11 rc=0, 0 warnings, 1895688 bytes —
byte-identical size to filed VERIFY build).

- RGRAMC-PYID 4014/4014 covered=4014/4014
  GREEN rc=0, 0 FAIL (own binary, own-seat
  b183 cache seeded, missing fresh-oracle).
- C-leg RGRAM-GREEN 8028 PASS / 0 FAIL
  rc=0, tail g-z63112 (RGRAM_BIN=own bin).
- py-leg RGRAM-GREEN 8028 PASS / 0 FAIL
  rc=0, tail g-z63112.
- C/py PASS-name sets cmp-equal 8028/8028
  (both all-PASS) — PINS-RGRAM set-eq.
- Own-loop fresh-oracle 63021..63112:
  pass=92 fail=0 (py+C agree CLOSED all 92,
  rc+stdout+stderr identical); pins 12 cells
  24/24 (closed+sha, fresh .rav match PINS).
  OWNLOOP-GREEN rc=0.
- Tables-EQ own script (tables-eq-r6.py,
  textual C-vs-py parse): 10/10 EQ GREEN
  (AM/BM/M/QR/QT + AC/BC/QC pairs +
  S0/S1; _N 75/71/62 row-consistent).
- Lane-diff rgramc.c-only +1484/-1034
  (reconfirmed); PINS 8030 lines
  (=8028+2 header); wall-grep PARENT-032
  scope 0 hits.

Verdict: PASS (re-confirmed). No commits, no push.
