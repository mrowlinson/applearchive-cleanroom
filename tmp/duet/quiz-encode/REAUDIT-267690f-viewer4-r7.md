# REAUDIT-267690f-viewer4-r7: band170 T10P127 (n<=61024, 812 tiers) — PASS

Interim turf-starved re-confirm (GATE+VERIFY on file;
viewer3-r8 filed unsuffixed REAUDIT-267690f PASS
mid-run — this is an independent second first-hand
battery, not a contest; their file untouched).
First-hand in fresh WS detached tree
WS/tmp/encode-viewer4/reaudit-267690f/tree (detached HEAD
267690f, clean), seat-private build .../build/rgramc
(cc -O2 -Wall -Wextra -std=c11 rc=0 0 warnings, 1843848
bytes; PINS 7730 + 2 header).

- PYID (RGRAMC=own C, corpus seeded own-seat b183
  cache 8076 hardlinks, 0 regen needed): RGRAMC-PYID
  3865/3865 covered=3865/3865, RGRAMC-GREEN, rc=0,
  0 FAIL.
- CBAT (RGRAM_BIN=own C, fresh oracle): 7730 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail g-z61024.
- PYBAT (python impl, same suite, fresh oracle): 7730
  PASS / 0 FAIL, RGRAM-GREEN, rc=0, tail g-z61024.
- PINS-RGRAM set-eq 7730/7730 (csv g-z rows 7730,
  C/PY PASS-name sets cmp-equal, both all-PASS).
- Own-loop fresh-oracle 60933..61024: pass=92 fail=0
  pins=12 pinfail=0, OWN-GREEN, rc=0. (Pin convention:
  closed-rows in range; viewer3-r8 reports 24/24
  counting closed+open — same range, both pinfail=0.)
- Tables-EQ own script r4: NEW 10/10 EQ
  (AC/BC/QC/AM/BM/M/QR/QT/S0/S1); FULL 2167/2167
  0-skip.
- Wall-grep PARENT-032 scope on band diff vs d505ac3
  (src/c/rgramc.c only, +1446/-995,
  cpat|libcompression|depload|dlopen|dylib|CPAT): 0 hits.
  HYGIENE/CONTAM/LIBCOMPRESSION inherit OBSERVED (none in
  lane diff).

VERDICT: PASS (re-confirm; VERIFY stands; agrees with
viewer3-r8 on every leg modulo pin-count convention).
