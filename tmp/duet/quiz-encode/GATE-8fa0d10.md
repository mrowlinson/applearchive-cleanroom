# GATE-8fa0d10 sweep: PASS-functional (cport band36; T10P400..P40Q ->30748)

- tip: lanes/encode-cport @8fa0d10 (parent merge 0303b7a P40-partial).
  rgramc.c +1035/-459: P40 5-tier port plain-xor-lencode (P400/P401
  76/76B + P40A 16x7B b14,26,27,68-71 + P40B 10x18B b2,14,15,25-35,
  72-75 + P40Q 4x16 P40M-16x5B b32,68-71 + P40Q-tab 4x11B
  b14,15,25-29,72-75), top bound 30748.
- code read (FULL): all 5 dispatch blocks line-for-line vs w2 55dcb98
  (bounds 30657/30658/30674/30684/30748, offs, xor l16, b-sets incl
  18-byte P40B copy). tables P40A/P40B/P40M/P40Q EXACT; consts
  74/74/67/56/58 EXACT numeric (9/9).
- battery: legs green incl OUTER2 + PINS-OUTER2 set-eq + RGRAM 3672
  + PINS-RGRAM set-eq 3672; C-BUILD w=0. HYGIENE/CONTAM/
  LIBCOMPRESSION FAIL = OBSERVED-inherited (diff rgramc.c only;
  same-cause 032/033, no FLAG).
- parity: RGRAMC-PYID 1836/1836 GREEN; RGRAM_BIN=C RGRAM-GREEN
  (message-exact 1836/1836, 3672/3672).
- storm diligence: 5 EXTRA unpinned cells py=C byte-identical rc=0
  on FRESH oracle bytes: 30666 P40A, 30680 P40B, 30692/30720/30740
  P40Q.
- boundaries: 30657 P400 + 30748 P40Q-off63 py=C CLOSED; 30749 rc=2
  scope both. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 233/233 PASS-individual (w2) + cport 37 PASS-functional.
