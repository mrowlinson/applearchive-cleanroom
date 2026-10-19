# A-370 (viewer r26): Q-364 T10P503 191781..192128 — CONFIRM all

First-hand bed 191085..192478 (own
1394-cell census, oracle regen rc=0;
10/10 re-probe stable on P501/P502
half). Payload .rav[12:-4]. Bed +
scripts: NVME encode-viewer/q362-r26/.

## 1. shape: CONFIRM
- 350 cells 191781..192130 ALL raw104/
  pay88. PB0 191781 bc020000 NEW; PB1
  191782 83780500 NEW.
- MID16 191783..798: 6-sig c28c5700
  x1 + c38c5700 x4 + c48c5700 x3 +
  c58c5700 x6 + c68c5700 x1 +
  818f5700 x1 EXACT order; M8
  b0,1,10,11,80-83 16/16; b5-const
  da; consts 78 (base 86).
- C10 191799..808 sig c0780500; M5
  b13,84-87 10/10; b5-const da;
  consts 81.
- QUAD88 191809..872 sig b08c5700:
  M8 b20-23,80-83 16/16 per row,
  row-seqs IDENTICAL; R1 b84 rows
  0c/2c/4c/6c (+0x20) row-const, NO
  pairing; b5 dax63+dbx1 (single
  step last cell, no Q claim); consts 77.
- T88-RING 191873..128 5-sig-BY-COL
  (m=o%16): m0-2 70cfc305 / m3-5
  f0cfc305 / m6 f0e5d905 / m7-14
  70e6d905 / m15 f0e6d905, each col-
  stable 16/16 EXACT; TM9 b0-2,26,
  27,80-83 = f(m) 16 distinct; TR8
  b20-23,76-79 = g(row) 16 distinct;
  UNPAIRED; b5 db+(o>=127)+(o>=255)
  all 256; b84-87 = 0b2c361d all
  256; consts 69.
- Next: P504 PB0 @192129 bc020000
  REPEAT-sig; PB1 @192130 00740500 NEW.

## 2. verdict: CONFIRM (25/25 checks)
- Every Q-364 byte claim reproduces
  from own bed. w2d tier cut SAFE.
