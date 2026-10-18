# REAUDIT-f01b41d-viewer4-r7: band168 T10P126 (n<=60676, 808 tiers) — PASS

Interim turf-starved re-confirm (GATE+VERIFY on file;
viewer-r13 filed unsuffixed REAUDIT-f01b41d PASS
mid-run — this is an independent second first-hand
battery, not a contest; their file untouched).
First-hand in fresh WS detached tree
WS/tmp/encode-viewer4/reaudit-f01b41d/tree (detached HEAD
f01b41d, clean), seat-private build .../build/rgramc
(cc -O2 -Wall -Wextra -std=c11 rc=0 0 warnings, 1827000
bytes; PINS 7686 + 2 header).

- PYID (RGRAMC=own C, corpus seeded own-seat b183
  cache 8076 hardlinks, 0 regen needed): RGRAMC-PYID
  3843/3843 covered=3843/3843, RGRAMC-GREEN, rc=0,
  0 FAIL.
- CBAT (RGRAM_BIN=own C, fresh oracle): 7686 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail g-z60676.
- PYBAT (python impl, same suite, fresh oracle): 7686
  PASS / 0 FAIL, RGRAM-GREEN, rc=0, tail g-z60676.
- PINS-RGRAM set-eq 7686/7686 (csv g-z rows 7686,
  C/PY PASS-name sets cmp-equal, both all-PASS).
- Own-loop fresh-oracle 60585..60676: pass=92 fail=0
  pins=12 pinfail=0, OWN-GREEN, rc=0. (Pin convention:
  closed-rows in range; viewer-r13 reports 24/24 =
  12x2 closed+open — same range, both pinfail=0.)
- Tables-EQ own script r4: NEW 10/10 EQ
  (AC/BC/QC/AM/BM/M/QR/QT/S0/S1); FULL 2155/2155
  0-skip. (Script-scope note: r4 enumerates STRARR
  tables where r13/GATE count NEW 8 / FULL 1193;
  both 0-mismatch, conventions differ only.)
- Wall-grep PARENT-032 scope on band diff vs 5314e97
  (src/c/rgramc.c only, +1439/-989,
  cpat|libcompression|depload|dlopen|dylib|CPAT): 0 hits.
  HYGIENE/CONTAM/LIBCOMPRESSION inherit OBSERVED (none in
  lane diff).

VERDICT: PASS (re-confirm; VERIFY stands; agrees with
viewer-r13 on every leg modulo table/pin-count
conventions).
