# A-74 (Q-68): T10P99 P-head geometry — DERIVED

Bed: census cells N=51189..51280 on disk (own bed, payload
.rav[12:-4]). All 80B. First-hand this shift.
(ACK PARENT-044/045: Q-68 missed in poll gap — answered
now, then Q-69 same turn.)

## 1. shape: CONFIRM
- PB0 51189 sig 19870300; PB1 51190 sig 6ebcc303; PBA
  51191..51206 (16, sig 6ebcc33d); QUAD 51217..51280
  (64=4x16, SINGLE sig 6ebcc31e all 4 rows). All 96B/80B.
- PBB 51207..51216 alternating sigs EXACTLY as writer:
  6ebcc301/19e7f800/6ebcc301/19e7f800/6ebcc301/
  6ebcc301/6ebcc301/19e7f800/6ebcc301/6ebcc301.
  28 VPOS first-hand: [0,1,2,3,4,11-19,25,26,27,
  33-39,76,77,78,79].

## 2. quad rows: CONFIRM (1+3 inverted)
- M 7B pos[40,41,42,72,73,74,75] row-indep 16/16 x4,
  16/16 distinct, ALL NEW.
- row1 rb unique 351979a08b04; rows0,2,3 share
  95ff199e5b00 (pos[25,26,33,34,35,37]).
- tails 8656a903/82a174a3/0858a903/8a58a903; rows0,2,3
  share last2B a903. All single-valued per row.

## 3. counters + dips: CONFIRM, NONE
- b4 whole-tier linear (0xeb+2off) 92/92 (b5 set
  {143,144}); PBA wrap 51199 255/143 -> 51200 1/144.
- quad-local b4=(0x23+2off) 64/64 no wrap; b5=0x90
  const 64/64.
- PBA VPOS [4,5,34,35,72,73,74,75] EXACT.
  NO D-class dips.

## geometry agrees on all 3 legs
