# GATE-d3247df sweep: PASS-functional (cport band25; T10PX0..PXQ+R32 ->28568)

- tip: lanes/encode-cport @d3247df (parent merge 3ada400 P33+R32-partial).
  rgramc.c +1133/-417: double-band port — P33 5 tiers (PX0/PX1 76/76B
  + PXA 16x7B b29,46,47,68-71 + PXB 10x11B b0,1,26,27,45-47,72-75 +
  PXQ 4x16 PXM-16x5B b6,72-75 + PXQ-tab 4x10B b1,26,27,45-47,68-71,
  b5-mbit m-set) + R32 16x16 (m-tab b13,14,64-67 + q=PXM + b5-qbit
  q-set). top bound 28568.
- code read (FULL): all 6 dispatch blocks line-for-line vs w2
  8da8428+b689490 (bounds/offs/l16/b-sets; b5 m-set PXQ + q-set R32
  both {0-4,6,12,14} ternary-chains ≡ py). tables PXA/PXB/PXM/PXQ/
  R32M EXACT; consts 74/74/67/63/59/63 EXACT numeric (11/11).
- battery: legs green (RGRAM 3412, PINS set-eq 3412; C-BUILD w=0,
  all incl -C pass). HYGIENE/CONTAM/LIBCOMPRESSION FAIL =
  OBSERVED-inherited (diff rgramc.c only; same-cause 032/033, no FLAG).
- parity: RGRAMC-PYID 1706/1706 GREEN; RGRAM_BIN=C RGRAM-GREEN
  (message-exact 1706/1706, 3412/3412).
- storm diligence: 5 EXTRA unpinned cells py=C byte-identical rc=0
  on FRESH oracle bytes spanning BOTH bands: 28230 PXA, 28290 PXQ,
  28330/28440/28560 R32.
- boundaries: 28221 PX0 + 28568 R32-off255 py=C CLOSED; 28569 rc=2
  scope both. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 219/219 PASS-individual (w2) + cport 26 PASS-functional.
