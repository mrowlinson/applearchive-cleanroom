# GATE-b14a45b sweep: PASS-functional (cport band32; T10R36+P380..P38Q ->30052)

- tip: lanes/encode-cport @b14a45b (parent merge d605333 R36+P38-partial).
  rgramc.c +1185/-446: double-band port raw-lencode — R36 16x16
  (m-tab b32-34,68-71 + qhead R36QH + qtab P37M-tail [6:]) + P38
  5 tiers (P380/P381 76/76B + P38A 16x7B b37-39,68-71 + P38B 10x11B
  b29,36-41,72-75 + P38Q 4x16 P38M-16x7B b30,42,43,68-71 +
  P38Q-tab 4x10B b36-41,72-75 + b29 rule QB[q]+(m>=13?0x40)).
  top bound 30052.
- code read (FULL): all 6 dispatch blocks line-for-line vs w2
  34f853f+1b1e2f3 (bounds/offs/raw-l16/b-sets; suffix +(6) ≡ [6:];
  b29 ternary (m>=13)?64:0 ≡ py; QB {18,22,38,18} ≡ py).
  tables R36M/R36QH/P38A/P38B/P38M/P38Q EXACT; consts
  58/74/74/67/63/56 EXACT numeric; QB EXACT (13/13).
- battery: legs green incl OUTER2 + PINS-OUTER2 set-eq + RGRAM 3592
  + PINS-RGRAM set-eq 3592; C-BUILD w=0. HYGIENE/CONTAM/
  LIBCOMPRESSION FAIL = OBSERVED-inherited (diff rgramc.c only;
  same-cause 032/033, no FLAG).
- parity: RGRAMC-PYID 1796/1796 GREEN; RGRAM_BIN=C RGRAM-GREEN
  (message-exact 1796/1796, 3592/3592).
- storm diligence: 5 EXTRA unpinned cells py=C byte-identical rc=0
  on FRESH oracle bytes spanning BOTH bands, b29 BOTH ways: 29820
  R36, 29970 P38A, 29995 off6/m6 no-add, 30002 off13/m13 +0x40,
  30040 off51 P38Q.
- boundaries: 29705 R36-off0 + 30052 P38Q-off63 py=C CLOSED; 30053
  rc=2 scope both. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 228/228 PASS-individual (w2) + cport 33 PASS-functional.
