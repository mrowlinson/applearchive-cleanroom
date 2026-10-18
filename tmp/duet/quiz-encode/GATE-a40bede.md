# GATE-a40bede sweep: PASS-functional (cport band37; T10R39+P410..P41Q ->31096)

- tip: lanes/encode-cport @a40bede (parent merge 5918420 R39+P41-partial).
  rgramc.c +1177/-464: double-band port — R39 16x16 (m-tab b37,38,
  68-71 + q=P40M @b32,64-67 + 63 consts) + P41 5 tiers (P410/P411
  76/76B + P41A 16x6B b42,43,68-71 + P41B 10x11B b15,29-31,41-43,
  72-75 + P41Q 4x16 P41M-16x6B b6,7,68-71 + P41Q-tab 4x9B
  b30,31,41-43,72-75 + mixed-base b5: pay[5] vs RAW-high ^
  (m in {0,1,6,8,9} ? 0x80)). top bound 31096.
- code read (FULL): all 6 dispatch blocks line-for-line vs w2
  0cda438+47eb5fa (bounds/offs/l16/b-sets; mixed-base b5
  raw-high+m-set ternary-chain ≡ py). tables R39M/P41A/P41B/P41M/
  P41Q EXACT; consts 63/74/74/68/63/59 EXACT numeric (11/11).
- battery: legs green incl OUTER2 + PINS-OUTER2 set-eq + RGRAM 3712
  + PINS-RGRAM set-eq 3712; C-BUILD w=0. HYGIENE/CONTAM/
  LIBCOMPRESSION FAIL = OBSERVED-inherited (diff rgramc.c only;
  same-cause 032/033, no FLAG).
- parity: RGRAMC-PYID 1856/1856 GREEN; RGRAM_BIN=C RGRAM-GREEN
  (message-exact 1856/1856, 3712/3712).
- storm diligence: 5 EXTRA unpinned cells py=C byte-identical rc=0
  on FRESH oracle bytes spanning BOTH bands, b5 BOTH ways: 30860
  R39, 31014 P41A, 31034 off1/m1 IN, 31035 off2/m2 OUT, 31060
  off27/m11 OUT.
- boundaries: 30749 R39-off0 + 31096 P41Q-off63 py=C CLOSED; 31097
  rc=2 scope both. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 234/234 PASS-individual (w2) + cport 38 PASS-functional.
