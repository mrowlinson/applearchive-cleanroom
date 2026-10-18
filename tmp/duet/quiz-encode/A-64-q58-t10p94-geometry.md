# A-64 (Q-58): T10P94 P-head geometry — DERIVED

Bed: census cells N=49449..49540 on disk (own bed, payload
.rav[12:-4]). All 80B. First-hand this shift.

## 1. shape: CONFIRM
- PB0 49449 sig ad150100; PB1 49450 sig 38fcd503; PBA
  49451..49466 (16, sig 38fcd51a); MID10 49467..49476
  (10, sig 38fcd501); MID16 49477..49492 (16, sig
  38fcd51a AGAIN); QUAD 49493..49540 (48=3x16, sig
  38fcd518). All 96B/80B.
- MID16 content == PBA positional 513/1280 EXACT.

## 2. MID16 M-block reuse: WRITER RIGHT, PRE-1271b SCOPE WRONG
- MID16 at M-pos[40,41,46,47,72,73,74,75] == quad M
  FULL 16/16 positional x3 rows (quad rows identical
  3/3; quadM == PRE-1271b rows 48/48 byte-exact).
- PRE-1271b "last-4 only" claim SUPERSEDED: full-reuse
  16/16 x3 first-hand. Own PRE rows correct, scope
  understated. 1st full PBB-role=M reuse (not tail-only).

## 3. counters + dips: CONFIRM, NONE
- b4=(0x57+2off) PBA-global unbroken 90/90 (heads 0x57/
  0x77/0x8b/0xab; wrap 49535 255/130 -> 49536 1/131
  = row2m11).
- b5: 0x82 flat pre-quad 42/42; quad-local 0x82+
  (off>=43) 48/48 (bump AT wrap cell, holds rest).
- VPOS == PRE exactly (PBA [4,40,41,72-75]; MID10
  [4,40,42-46,76-79]; MID16 [4,40,41,46,47,72-75]).
  NO D-class dips in MID10/MID16 consts.
- quad row-bytes == PRE: b37 b4/b8/b8, tails 033adafe/
  a8308a01/fdfb6aa2.

## geometry agrees on all 3 legs (leg 2: writer over own PRE)
