# REAUDIT-07533a3 (viewer r14): band188 T10P136 (n<=64156, 848 tiers) — PASS

Interim canonical re-confirm of filed
VERIFY-07533a3 (filed VERIFY stands).
Full first-hand re-battery in fresh WS
detached tree tmp/encode-viewer/
07533a3-r14/tree (HEAD 07533a3
confirmed, status clean), seat-private
build build/rgramc-r14 (cc -O2 -Wall
-Wextra -std=c11 rc=0, 0 warnings,
1929816 bytes == VERIFY == GATE),
NVME TMPDIR, all legs fresh r14.

- RGRAMC-PYID 4090/4090 covered=4090/4090
  GREEN rc=0 (corpus 8180 hardlink-seeded
  from r12 b188 cache, py+C freshly
  executed per pin, 0 FAIL).
- C-leg RGRAM-GREEN 8180 PASS / 0 FAIL rc=0
  (RGRAM_BIN=own r14, fresh oracle, tail
  g-z64156).
- py-leg RGRAM-GREEN 8180 PASS / 0 FAIL rc=0
  (fresh oracle, tail g-z64156).
- PINS-RGRAM set-eq 8180/8180 (C/py PASS-name
  sets cmp-identical; csv 8180 g-z rows,
  both legs all-PASS).
- own-loop fresh-oracle 64065..64156: 92/0
  pins 28/28, OWN-GREEN rc=0 (== GATE;
  expect 14 closed-rows x2 = 28 derived
  from PINS numerically first-hand).
- Tables-EQ own script r14: NEW 9/9 EQ
  (AC/BC/QC + _N 75/71/63 derived-consistent
  + S0/S1/S2 strings); FULL 1260/0 (1D 166 +
  2D 836 + STR 258; 11 _KEYS C-only out of
  scope, 166+11=177 == VERIFY 1D raw).
- Wall-grep PARENT-032 scope on lane diff vs
  be21af9 = 07533a3^ (src/c/rgramc.c only,
  +1516/-1055 == GATE): 0 hits (cpat/
  libcompression/depload/dlopen/dylib each
  0). HYGIENE/CONTAM/LIBCOMPRESSION inherit
  OBSERVED (none in lane diff).

Verdict: PASS (re-confirmed). No commits, no push.
