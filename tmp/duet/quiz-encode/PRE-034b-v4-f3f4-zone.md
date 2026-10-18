# PRE-034b F3/F4 zone 2497..2560: 11 fields + tabs + quads (w2 next commit)

## only 11 var (b4/5/13/14/15/16/17/18/20/21/22; 41 const, v5m 64 rows)
## 16-tabs from 2497 (verify all 4 cycles)
- b20: d7 5a ab fc 4d 9e ef 40 91 e2 33 84 d5 26 77 c8 (first step
  +0x83, then +0x51 x14 — same counter shape as F-band b20).
- b21: 5f 5a da 5a db 5b db 5c dc 5c dd 5d dd 5e de 5e.
- b22: 86 8c 91 97 9c a2 a7 ad b2 b8 bd c3 c8 ce d3 d9 (+6/+5 ramp,
  same shape as F-band b22).
- b18: 32-duty (05x16 / 04x16 alternating).

## 16-row quads (2497/2513/2529/2545)
- b13: 44 14 74 82. b14: fc fc bc 3c. b15: 60 61 62 87.
- b16: f3 93 f3 d3. b17: 7f ee 7f 5d.
- b4: L10-lo +2/row. b5: 53 -> 54 @2560 (lone flip at edge).
