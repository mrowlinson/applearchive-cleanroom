# REAUDIT-a31520e (viewer2 r6): band184 T10P134 (n<=63460, 840 tiers) — PASS

Independent re-confirm of filed VERIFY-a31520e
(viewer4 r4). No rival re-audit (v3 on b182,
v4 on b181) — canonical filename.

First-hand in WS fresh detached tree
tmp/encode-viewer2/a31520e/tree (local clone,
detached HEAD a31520e95c8749317c06ac6b4828
c6ae06058cf8 confirmed, status clean),
seat-private build build/rgramc-own (cc -O2
-Wall -Wextra -std=c11 rc=0, 0 warnings,
1912584 bytes — byte-identical size to filed
VERIFY build).

- RGRAMC-PYID 4038/4038 covered=4038/4038
  GREEN rc=0, 0 FAIL (own binary, own-seat
  b183 cache seeded, 14 new-N fresh-oracle).
- C-leg RGRAM-GREEN 8076 PASS / 0 FAIL
  rc=0, tail g-z63460 (RGRAM_BIN=own bin).
- py-leg RGRAM-GREEN 8076 PASS / 0 FAIL
  rc=0, tail g-z63460.
- C/py PASS-name sets cmp-equal 8076/8076
  (both all-PASS) — PINS-RGRAM set-eq.
- Own-loop fresh-oracle 63369..63460:
  pass=92 fail=0 (py+C agree CLOSED all 92,
  rc+stdout+stderr identical); pins 14 cells
  28/28 (closed+sha, fresh .rav match PINS).
  OWNLOOP-GREEN rc=0.
- Tables-EQ own script (tables-eq-r6.py,
  textual C-vs-py parse): 12/12 EQ GREEN
  (AM/BM/M/QR/QT + AC/BC/QC pairs +
  S0/S1/S2/S3; _N 76/72/62 row-consistent).
- Lane-diff rgramc.c-only +1517/-1040
  (reconfirmed); PINS 8078 lines
  (=8076+2 header); wall-grep PARENT-032
  scope 0 hits.

Verdict: PASS (re-confirmed). No commits, no push.
