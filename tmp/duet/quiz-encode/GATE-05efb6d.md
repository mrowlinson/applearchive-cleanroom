# GATE 05efb6d b190 T10P137 n<=64504 (852 tiers) PASS-functional

- Seat encode-sweep2 r17, first-hand,
  seat-private logs r17-05efb6d/*
  under NVME encode-sweep2.
- Lane-diff vs writer-merge parent
  8079ebb: rgramc.c only +1523/-1062;
  wall 0. Range 64413..64504.
- gate-tip (wt-encode-sweep2 harness @
  d56ce19): RGRAM py PASS n=8230 FAIL 0,
  PINS-RGRAM set-eq 8230/8230; RAWENC
  13/13, PBZE 10/10, LZMA 6/6, LZ4 4/4
  (+ -C legs all PASS), SMOKE 6/6,
  SMOKE-IMPL 6/6, RB2 47/47, RAVFRAME
  181/181, UNITS 22, LZ4C 5,
  PINS-RAWENC 11/11 (+C), PINS-PBZE
  10/10 (+C), PINSET RB2/RAVFRAME
  set-eq 47/47 + 181/181, OSS
  nominated-only, C-BUILD warnings=0.
- OUTER2 oracle flake (shipped run):
  a-nondet "got char 14 want char 13"
  283/284 + PINS-OUTER2 FAIL rows=284
  (PINSET-NEVER-PASS:a-nondet). Cause:
  pin compares first-diff-char of TWO
  fresh /usr/bin/aea oracle outputs;
  lane file rgramc.c-only cannot
  influence AEA bytes. Precedent:
  GATE-965f4dd identical + GATE-7081fd5.
  PROOF: same-tree rerun rc=0 284/284
  GREEN PASS a-nondet first-hand
  (r17-05efb6d.outer2-rerun.log). No FLAG.
- RGRAMC-PYID 4115/4115 GREEN rc=0 0
  FAIL covered=4115/4115 (corpus seeded
  r16-b188 8180 hardlinks + 25 fresh-
  oracle new N, py+C freshly executed
  per pin).
- C-batt RGRAM-GREEN rc=0 8230/8230 0
  FAIL (RGRAM_BIN=seat-private -O2 -Wall
  -Wextra -std=c11 build, 0 warnings,
  1946696 B); C-py PASS-set cmp-equal
  8230/8230.
- own-loop 64413..64504 fresh-oracle
  92/92 py-agree, pins 28/28, rc=0.
- Added 3/3 EQ (C 2D _T10P137AC 76 rows
  = py-pairs, _T10P137BC 71/71,
  _T10P137QC 63/63); full audit 1D
  166/0 + 2D 840/0 + dicts 11/0 + STR
  261/0 + STRARR 1034/0.
- Scoped OBSERVED-inherited (PARENT-032
  shape): HYGIENE/CONTAM/LIBCOMPRESSION
  FAIL raw; lane file 0/0/0, HYG .aar
  13 identical b188->b190, CONTAM CHIT
  43/43 identical + depload raw survivor
  proto/impl-adapter.sh ZBM_DYLIB
  known-FP, Mach-O empty, LIBCOMP aad.c
  3 lines identical (aad.c 0 diff).
  ADOPT WARN diff carried (c8f52713/
  c5f921d5 const).
- Verdict: PASS-functional. No RED. Run
  cap 1/2.
