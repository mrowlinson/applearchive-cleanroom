# GATE-81c73cb sweep: PASS-functional (cport band29; T10P360..P36Q ->29356)

- tip: lanes/encode-cport @81c73cb (parent merge a2070eb P36-partial).
  rgramc.c +1014/-435: P36 5-tier port (P360/P361 singletons 76/76B +
  P36A 16x6B b6,7,68-71 + b5 off-set rule + P36B 10x9B b6-10,72-75 +
  P36Q 4x16 P36M-16x6B b13,14,64-67 + P36Q-tab 4x9B b6-10,72-75),
  top bound 29356.
- code read (FULL): all 5 dispatch blocks line-for-line vs w2 c108d1e
  (bounds 29265/29266/29282/29292/29356, offs, l16, b-sets; b5
  off-set {1,5,6,9,10,11,12,13,14,15} ternary-chain ≡ py).
  tables P36A/P36B/P36M/P36Q EXACT; consts 74/74/68/65/59 EXACT
  numeric (9/9).
- battery: legs green incl OUTER2 n=284 + PINS-OUTER2 set-eq (this
  run; confirms R35 flake theory) + RGRAM 3512 + PINS-RGRAM set-eq
  3512; C-BUILD w=0. HYGIENE/CONTAM/LIBCOMPRESSION FAIL =
  OBSERVED-inherited (diff rgramc.c only; same-cause 032/033, no FLAG).
- parity: RGRAMC-PYID 1756/1756 GREEN; RGRAM_BIN=C RGRAM-GREEN
  (message-exact 1756/1756, 3512/3512).
- storm diligence: 5 EXTRA unpinned cells py=C byte-identical rc=0
  on FRESH oracle bytes, b5 rule BOTH ways: 29269 off2 OUT, 29272
  off5 IN, 29275 off8 OUT (P36A) + 29288 P36B + 29320 P36Q.
- boundaries: 29265 P360 + 29356 P36Q-off63 py=C CLOSED; 29357 rc=2
  scope both. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 224/224 PASS-individual (w2) + cport 30 PASS-functional.
