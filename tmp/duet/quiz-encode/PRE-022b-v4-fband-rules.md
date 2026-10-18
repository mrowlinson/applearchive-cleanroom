# PRE-022b F-band 2561..2700 @52B: minimal 9-field + tabs (w2 accel)

## only 9 var bytes (43 const, v5f first-hand 140 rows)
- consts: 0:eb 1:03 2:00 3:00 6:ef 7:9d 8:53 9:37 10:80 12:00 13:c4
  14:bc 15:43 16:33 17:37 18:05 23:88 24:8c 25:e0 28:0d 29:61 30:e3
  31:19 32:be 33:bf 34:a3 35:13 36:e9 37:34 38:ad 39:b7 40:48 41:e0
  42:a7 43:56 44:08 45:fc 46:16 47:4b 48:49 49:28 50:5b 51:fb.

## strict 16-tabs from 2561 (all rows verify)
- b11: 63x4 64x8 65x4 (4/8/4 duty).
- b19: 90 cc ce e0 0d 0f 4c 4e 8b 8d ca cc 08 0a 47 49.
- b26: 9a c8x3 f6x2 24x2 52x2 80x2 aex2 dcx2.
- b27: 78 f9x2 79 f8x4 79x2 78x2 f9x2 f8x2.
- b4: L10-lo +2/row (ramps, not tab).

## 16-plateaus from 2561
- b20: d7 5a ab fc 4d 9e ef 40 91 (+0x51 after first step 0x83).
- b21: 5f 5a da 5a db 5b db 5c dc (5x/dx oscillate).
- b22: 86 8c 91 97 9c a2 a7 ad b2 (+6/+5 alternating).
- b5: 54@2561-2687 -> 55@2688 (lone flip).
