# GATE-0294f8b sweep: PASS-functional (cport band41; T10P430..P43Q+R42 ->32048)

- tip: lanes/encode-cport @0294f8b (parent merge bb05dd4 P43+R42-partial).
  rgramc.c +1213/-477: double-band port plain-xor — P43 5 tiers
  (P430/P431 76/76B + P43A 16x6B b32,33,68-71 + P43B 10x12B
  b28,29,32-37,72-75 + P43Q 4x16 P43M-16x7B b37-39,72-75 +
  P43Q-tab 4x9B b32-36,68-71) + R42 16x16 (m-tab b33,42,43,64-67
  CODE truth + qhead R42QH b36-38 + qtab P43M-tail [6:] @b72-75).
  top bound 32048.
- code read (FULL): all 6 dispatch blocks line-for-line vs w2
  25b36b0+cf113e3 (bounds/offs/xor-l16/b-sets; R42 m-tab follows
  CODE b33,42,43 — cport correctly ignores w2 msg slip "b0,1,2";
  suffix +(6) ≡ [6:]). tables P43A/P43B/P43M/P43Q/R42M/R42QH
  EXACT; consts 74/74/68/62/58/60 EXACT numeric (12/12).
- battery: legs green incl OUTER2 + PINS-OUTER2 set-eq + RGRAM 3812
  + PINS-RGRAM set-eq 3812; C-BUILD w=0. HYGIENE/CONTAM/
  LIBCOMPRESSION FAIL = OBSERVED-inherited (diff rgramc.c only;
  same-cause 032/033, no FLAG).
- parity: RGRAMC-PYID 1906/1906 GREEN; RGRAM_BIN=C RGRAM-GREEN
  (message-exact 1906/1906, 3812/3812).
- storm diligence: 5 EXTRA unpinned cells py=C byte-identical rc=0
  on FRESH oracle bytes spanning BOTH bands: 31736 P43Q,
  31820/31910/32000/32040 R42.
- boundaries: 31701 P430 + 32048 R42-off255 py=C CLOSED; 32049 rc=2
  scope both. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 239/239 PASS-individual (w2) + cport 42 PASS-functional.
