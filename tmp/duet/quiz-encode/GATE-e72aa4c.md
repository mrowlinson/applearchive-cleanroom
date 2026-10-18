# GATE-e72aa4c (encode-writer tip): PASS, C port byte-identical both backends

- build (per-gate NVME BUILDDIR): C-BUILD PASS warnings=0
  (-Wall -Wextra; zero-warnings claim corroborated). binary
  never in repo (Makefile BUILDDIR default NVME ✓).
- python (unchanged impl, re-verified on tip): RAWENC 12/12,
  PBZE 10/10, SMOKE 6/6, SMOKE-IMPL 6/6, UNITS 22/22,
  PINS-PBZE 10/10, PINS-RAWENC 10/10 + c13 supplement MATCH.
- C parity (ENC_BIN legs, gate-tip 2b177a2): RAWENC-C 12/12,
  PBZE-C 10/10, PINS-PBZE-C 10/10 (same pins), PINS-RAWENC-C
  10/10 + supplements: c13 oracle==py==C byte-EQ, sha
  1ed45ee9.../4831838433 MATCH pin; c11-c socket PASS 186B
  byte-EQ. NOTE-10 "socket/C IDENTICAL" corroborated.
- code read first-hand (aae.c 484 lines): record shapes,
  sorted entries/xattrs, 15/16 rule (comp*16>unc*15 store),
  zlib L5, block 1..128m, --threads accepted. lzfse via
  dlopen nominated dylib + LZFSE_DYLIB override (PARENT-003
  clean); system -lz; NO new OSS. contam 0.
- hygiene: PASS (no tmp/scratch- on w1; PARENT-005 clean).
  ADOPT match. incident: first c13 workdir vanished mid-gate
  (concurrent seat ran RUN_BIG in this gate dir); evidence
  re-secured isolated-dir, verdict rests on re-run only.
- minor (non-blocking): c11/c13 battery blocks bypass
  _IMP (direct python calls) — C parity there needs manual
  runs; suggest routing via _IMP for self-serve C gates.
- verdict: PASS. no FLAG.
- repro: gate-tip.sh e72aa4c $WS/gate-w1-e72aa4c + sweep
  c13/c11 supplement blocks (isolated dirs).
