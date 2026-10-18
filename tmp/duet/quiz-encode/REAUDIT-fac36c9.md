# REAUDIT-fac36c9 (viewer r15): band189 T10R134 (n<=64412, 850 tiers) — PASS

Interim canonical re-confirm of filed
VERIFY-fac36c9 (filed VERIFY stands).
Full first-hand re-battery in fresh WS
detached tree tmp/encode-viewer/
fac36c9-r15/tree (git-archive at
fac36c9bcc3270170a9edb3e420d25da6eb5a163
confirmed, rgramc.c cmp-identical to git),
seat-private build build/rgramc-r15
(cc -O2 -Wall -Wextra -std=c11 rc=0,
0 warnings, 1929880 bytes == VERIFY ==
GATE), NVME TMPDIR, all legs fresh r15.

- RGRAMC-PYID 4101/4101 covered=4101/4101
  GREEN rc=0 (corpus 8180 hardlink-seeded
  from r14 b188 cache, 11 fresh-oracle
  new N, py+C freshly executed per pin,
  0 FAIL).
- C-leg RGRAM-GREEN 8202 PASS / 0 FAIL rc=0
  (RGRAM_BIN=own r15, fresh oracle, tail
  g-z64412).
- py-leg RGRAM-GREEN 8202 PASS / 0 FAIL rc=0
  (fresh oracle, tail g-z64412).
- PINS-RGRAM set-eq 8202/8202 (C/py PASS-name
  sets cmp-identical; both legs all-PASS).
- own-loop fresh-oracle 64157..64412: 256/0
  pins 22/22, OWN-GREEN rc=0 (== GATE;
  expect 11 pinned cells x2 derived from
  PINS numerically first-hand).
- Tables-EQ own script r15: NEW 2/2 EQ
  (_T10R134C 67/67 pairs + _T10R134C_N=67
  row-consistent); FULL 1261/0 (1D 166 +
  2D 837 + STR 258; M/Q under FULL;
  11 _KEYS C-only out of scope).
- Wall-grep PARENT-032 scope on lane diff vs
  d335153 = fac36c9^ (src/c/rgramc.c only,
  +1220/-1061 == GATE): 0 hits (cpat/
  libcompression/depload/dlopen/dylib each
  0). py + PINS + tests byte-identical to
  d335153 (8204 PINS lines = 8202 + 2 hdr).
  HYGIENE/CONTAM/LIBCOMPRESSION inherit
  OBSERVED (none in lane diff).

Verdict: PASS (re-confirmed). No commits, no push.
