# GATE 5f9f5a8 b175 T10R127 n<=61976 (822 tiers) PASS-functional

- Seat encode-sweep r5, first-hand, seat-private logs
  r5-5f9f5a8* under NVME encode-sweep.
- Lane-diff vs P127 cport base: rgramc.c only
  +1154/-1013; wall 0. Range 61721..61976.
- gate-tip: RGRAM py PASS n=7852 FAIL 0,
  PINS-RGRAM set-eq 7852/7852; RAWENC 13/13,
  PBZE 10/10, LZMA 6/6, LZ4 4/4 (+ -C legs),
  SMOKE 6/6, OUTER2 284/284, RB2 47/47,
  RAVFRAME 181/181, UNITS 22, LZ4C 5,
  OSS nominated-only, C-BUILD warnings=0.
- RGRAMC-PYID 3926/3926 GREEN.
- C-batt 7852/0 GREEN.
- own-loop 61721..61976 fresh-oracle 256/0,
  pins 22/22, py-agree 256/256.
- Added 3/3 EQ (M str n=16, C 2D n=69,
  C_N=69 derived-consistent);
  audit 1D 166/0 + 2D 809/0 + dicts 11/0 +
  STR 238/0 + STRARR 984/0.
- Scoped OBSERVED-inherited (PARENT-032 shape):
  HYGIENE/CONTAM/LIBCOMPRESSION FAIL; lane file
  0/0/0, HYG 13 identical 173->175, CONTAM fileset
  identical b173, LIBCOMP aad.c only. ADOPT WARN
  diff carried (oracle-adapter lane/tip const).
- Verdict: PASS-functional. No RED.
