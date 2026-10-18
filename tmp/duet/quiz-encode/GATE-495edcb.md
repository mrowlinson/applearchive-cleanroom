# GATE 495edcb b181 T10R130 n<=63020 (834 tiers) PASS-functional

- Seat encode-sweep r8, first-hand, seat-private logs
  r8-495edcb* under NVME encode-sweep.
- Lane-diff vs writer-merge parent aef8ee6: rgramc.c only
  +1174/-1033; wall 0. Range 62765..63020.
- gate-tip (own extract): RGRAM py PASS n=8004 FAIL 0,
  PINS-RGRAM set-eq 8004/8004; RAWENC 13/13,
  PBZE 10/10, LZMA 6/6, LZ4 4/4 (+ -C legs),
  SMOKE 6/6, OUTER2 284/284, RB2 47/47,
  RAVFRAME 181/181, UNITS 22, LZ4C 5,
  OSS nominated-only, C-BUILD warnings=0.
- RGRAMC-PYID 4002/4002 GREEN (corpus seeded r7 seat
  cache + fresh oracle regen for new N only).
- C-batt RGRAM-GREEN rc=0 live + recount closed 4002/0,
  pins 8004/8004 over cached corpus.
- own-loop 62765..63020 fresh-oracle 256/0,
  pins 24/24, py-agree 256/256. REPIN fresh2 24/24.
- Added 3/3 EQ (M str n=16, C 2D n=69,
  C_N=69 derived-consistent; R130 has no QH
  in C or py, verified);
  audit 1D 166/0 + 2D 821/0 + dicts 11/0 +
  STR 246/0 + STRARR 1004/0.
- Scoped OBSERVED-inherited (PARENT-032 shape):
  HYGIENE/CONTAM/LIBCOMPRESSION FAIL raw; lane file
  0/0/0, HYG .aar 13 identical 180->181, CONTAM sets
  identical 43/43 normalized, LIBCOMP aad.c only
  (3 lines identical). ADOPT WARN diff carried
  (c8f52713/c5f921d5 const).
- Verdict: PASS-functional. No RED. Run cap 1/2.
