# A-86 (Q-80): T10P105 P-head geometry — DERIVED

Bed: census cells N=53277..53368 on disk (own bed, payload
.rav[12:-4]). First-hand this shift.

## 1. shape: CONFIRM
- PB0 53277 sig 9d8b2600 (96B/80B); PB1 53278 sig
  48f86c4b; PBA 53279..53294 (16, 100B/84B sig
  04000000); PBB 53295..53304 (10, SINGLE sig 48f86c2b,
  no single); QUAD 53305..53368 (64=4x16, ALL 100B/84B,
  SINGLE sig 02000000 all rows — 1st 100B QUAD,
  first-hand).
- PBA100 VPOS [4,48,49,50,51,76,77,78,79] EXACT; PBB
  VPOS [4,40,41,42,43,45,46,47,76,77,78,79] EXACT.

## 2. quad rows: CONFIRM
- M 7B pos[6,7,12,76,77,78,79] row-indep 16/16 x4,
  16/16 distinct, ALL NEW.
- row-bytes b44,45,46,47,49,50,51: row1==row2
  a89ca02af0c54f; row0 unique 48b61d2d50e3ff; row3
  unique a8052e28906837.
- tails at b80..83: 6e2e06ae/f07aff3c/697bff3c/
  d23b8785; rows1,2 share ff3c. All single-valued.

## 3. counters + dips: CONFIRM, NONE
- b4 whole-tier linear (0x3b+2off) 92/92 (b5 whole set
  {160}); quad-local (0x73+2off) 64/64, max 0xf1,
  NO wrap; b5=0xa0 const 64/64.
  NO D-class dips.

## geometry agrees on all 3 legs
