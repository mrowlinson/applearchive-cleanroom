# PRE-035b 68B-tier head 11957..12212: minimal 14-field + tabs (w2 map)

## 68B holds all 256 rows, 54 const (v5n first-hand)
- consts: 0:01 1:00 2:00 3:00 6:16 7:29 8:e2 9:36 10:15 11:74 12:01
  13:58 14:f2 15:d1 16:bf 17:56 18:04 19:0b 20:c9 21:5f 22:d0 23:6e
  24:fa 25:10 26:a5 27:75 34:79 35:d4 42:e2 43:e1 44:8b 45:da 46:d4
  47:f1 48:35 49:77 50:ac 51:5c 52:8e 53:bc 54:07 55:83 56:18 57:d6
  58:6e 59:ee 60:ee 61:d7 62:d7 63:24 64:98 65:5f 66:5f 67:5a.

## 16-tabs from 11957 (verify full span)
- b36: 34 4a ba d0 81 7d d1 6b 9a 4b ed 1a 7f 45 5b 2e (16 unique).
- b37: fc fc bf bf fc fc bf fc bf fc bf fc fc fc fc bf (2 values!).
- b38: 53 5b b7 bf 8f ab 7f db 8b 3b 27 a3 f7 e3 eb 8b.
- b39: 05 05 15 15 9d 1e 3a e0 e1 19 79 5a 13 3e 3e 43.
- b40: bc bc bc bc dc fc 1c 1c 1c 5c bc dc bc bc bc bc (5 values).
- b41: d2x5 d7 d8x3 d9x3 dex4 (5 values, plateau-duty).

## ramps + plateaus
- b4: L10-lo +2/row (6b@11957 = L10-lo EXACT, unbroken from 1517).
- b5: 128-plateaus 5d/5e/5f (11957/12032/12160).
- b28-33: 16/32-plateaus (v5n follow-up runs; b28 15 runs, b29 12,
  b30 16, b31 15, b32 12, b33 8).
