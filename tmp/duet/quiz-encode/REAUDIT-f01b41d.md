# REAUDIT-f01b41d (viewer r13): band168 T10P126 (n<=60676, 808 tiers) — PASS

Interim canonical re-confirm of filed
VERIFY-f01b41d during VERIFY-starved wait
(13 real opens: 12 writer-era no-c-port
battery-N/A + 920e187 PARENT-032 no-action;
b189 viewer2-claimed, b170 viewer3-staged;
yields per PARENT-070). Filed VERIFY stands
regardless. Full first-hand re-battery in
fresh WS detached tree tmp/encode-viewer/
f01b41d/tree (HEAD f01b41dbe6124 confirmed,
status clean), seat-private build
build/rgramc-r13 (cc -O2 -Wall -Wextra
-std=c11 rc=0, 0 warnings, 1827000 bytes ==
VERIFY exactly), NVME TMPDIR, all legs
fresh r13.

- RGRAMC-PYID 3843/3843 covered=3843/3843
  GREEN rc=0 (corpus 8180 hardlink-seeded
  from b188 cache, py+C freshly executed
  per pin, 0 FAIL).
- C-leg RGRAM-GREEN 7686 PASS / 0 FAIL rc=0
  (RGRAM_BIN=own r13, fresh oracle, tail
  g-z60676).
- py-leg RGRAM-GREEN 7686 PASS / 0 FAIL rc=0
  (fresh oracle, tail g-z60676).
- PINS-RGRAM set-eq 7686/7686 (C/py PASS-name
  sets cmp-identical; csv 7686 g-z rows,
  both legs all-PASS).
- own-loop fresh-oracle 60585..60676: 92/0
  pins 24/24, OWN-GREEN rc=0 (== GATE;
  expect 12 closed-rows x2 = 24 derived
  from PINS first-hand).
- Tables-EQ own script r13: NEW 8/8 EQ
  (AC/BC/QC + _N 75/72/62 derived-consistent
  + S0/S1 strings); FULL 1193/0 (1D 166 +
  2D 796 + STR 231; 11 _KEYS C-only dict
  helpers out of scope, == GATE dicts 11).
- Wall-grep PARENT-032 scope on lane diff vs
  f01b41d^ (src/c/rgramc.c only, +1439/-989
  == GATE): 0 hits (cpat/libcompression/
  depload/dlopen/dylib each 0). HYGIENE/
  CONTAM/LIBCOMPRESSION inherit OBSERVED
  (none in lane diff).

Verdict: PASS (re-confirmed). No commits, no push.
