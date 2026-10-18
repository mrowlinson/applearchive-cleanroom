# GATE fe4c199 b177 T10R128 n<=62324 (826 tiers) PASS-functional

- Seat encode-sweep r6, first-hand, seat-private logs
  r6-fe4c199* under NVME encode-sweep.
- Lane-diff vs writer-merge parent 2479628: rgramc.c only
  +1166/-1019; wall 0. Range 62069..62324.
- gate-tip: RGRAM py PASS n=7900 FAIL 0,
  PINS-RGRAM set-eq 7900/7900; RAWENC 13/13,
  PBZE 10/10, LZMA 6/6, LZ4 4/4 (+ -C legs),
  SMOKE 6/6, OUTER2 284/284, RB2 47/47,
  RAVFRAME 181/181, UNITS 22, LZ4C 5,
  OSS nominated-only, C-BUILD warnings=0.
- RGRAMC-PYID 3950/3950 GREEN (corpus seeded r5 seat
  cache 7852f + fresh oracle regen for new N only).
- C-batt 7900/0 GREEN.
- own-loop 62069..62324 fresh-oracle 256/0,
  pins 24/24, py-agree 256/256.
- Added 3/3 EQ (M str n=16, C 2D n=69,
  C_N=69 derived-consistent);
  audit 1D 166/0 + 2D 813/0 + dicts 11/0 +
  STR 240/0 + STRARR 991/0.
- Scoped OBSERVED-inherited (PARENT-032 shape):
  HYGIENE/CONTAM/LIBCOMPRESSION FAIL raw; lane file
  0/0/0, HYG+CONTAM sets identical 175->177 (58/58
  normalized), LIBCOMP aad.c only (3 lines identical).
  ADOPT WARN diff carried (c8f52713/c5f921d5 const).
- Verdict: PASS-functional. No RED. Run cap 1/2.
