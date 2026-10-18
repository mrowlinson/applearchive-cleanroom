# GATE 7c2e8d4 b185 T10R132 n<=63716 (842 tiers) PASS-functional

- Seat encode-sweep r10, first-hand, seat-private logs
  r10-7c2e8d4* under NVME encode-sweep. CLAIM filed
  pre-gate, backstop clear.
- Lane-diff vs prep-merge parent 260016a: rgramc.c only
  +1188/-1047; wall 0. Range 63461..63716.
- gate-tip (sweep lane, own extract): RGRAM py PASS
  n=8100 FAIL 0, PINS-RGRAM set-eq 8100/8100;
  RAWENC 13/13, PBZE 10/10, LZMA 6/6, LZ4 4/4
  (+ -C legs 13/10/6/4), SMOKE 6/6 (+ IMPL 6),
  OUTER2 284/284, RB2 47/47, RAVFRAME 181/181,
  UNITS 22, LZ4C 5, OSS nominated-only,
  C-BUILD warnings=0.
- RGRAMC-PYID 4050/4050 GREEN (corpus seeded r9
  + fresh oracle regen for new N only).
- C-batt RGRAM-GREEN rc=0 live 8100 PASS over
  fresh oracle (own binary).
- own-loop 63461..63716 fresh-oracle 256/0,
  pins 12/12 (12 new pin-N), py-agree 256/256.
  Prior b184 binary out-of-scope on new LAP
  256/256 as designed ("N out of scope").
- Added 3/3 EQ (C n=66, C_N=66 derived-consistent,
  M n=16 str; R132 no QH in C or py, 0/0);
  audit 1D 166/0 + 2D 829/0 + dicts 11/0 +
  STR 252/0 + STRARR 1016/0.
- Scoped OBSERVED-inherited (PARENT-032 shape):
  HYGIENE/CONTAM/LIBCOMPRESSION FAIL raw; lane file
  0/0/0, HYG .aar 13 hash-identical b184->b185,
  CONTAM 43 lines all records (docs/notes/spec/
  README attestations) + 1 ZBM_DYLIB known-FP comment,
  0 in src, 0 mach-o, file sets identical
  parent->band, LIBCOMP src/aad.c 3 lines
  (file untouched by band). ADOPT WARN diff carried
  (c8f52713/c5f921d5 const).
- Verdict: PASS-functional. No RED. Run cap 1/2.
