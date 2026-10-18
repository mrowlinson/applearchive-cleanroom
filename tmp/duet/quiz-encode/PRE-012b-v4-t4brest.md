# PRE-012b T4B-rest pre-bed: B123 3-forms + B5 minimal (w2 B-rest accel)

## B123 = N 1078..1104 (48B, 27 rows, v4t4b.py)
- THREE sub-forms: 1078 singleton | 1079-1094 (16) | 1095-1104 (10).
  (boundaries from head bytes b0/b10/b11/b18-27 flipping together.)
- b4 = L10 low byte EXACT (6d..a1 step 2 = 109..161 ✓); b5 const 0
  (L10>>8 = 0 throughout ✓ — concurs w2s7-11 L10 unified).
- b37 = +4/row counter with jumps (@1087:40, @1095:80); b38 sparse
  (00 | 16/4f/8c); b36 hash-like from 1095 (43/35/07/d9/ab/51/50/22/f4/9a).
- 21 const bytes (incl b5/b42? no: b42 const here — listed varying? B123
  varying lacks 42/43: j-counter PARKED in B123, cf B4/B5 live).

## B5 = N 1153..1168 (48B, 16 rows, MINIMAL: 3 varying bytes)
- b4 = L10 lo (03..21 = 259..289 ✓); b42 = +0x20/row mod 0x100 period 8
  (07..e7 x2 — j-counter continues); b43 = 00 (1153-1160) -> 01 (1161-1168)
  (j-high/carry). 45 const bytes.

## for w2's B-rest commit
- suggested split: B1=1078 literal, B2=1079-1094, B3=1095-1104, B5=formulas
  (b4/b42/b43 above + 45 consts). my bytes are zeros-input only; dev/hole
  mapping still theirs. full runs in WS scratch-viewer4/v4t4b.log.
