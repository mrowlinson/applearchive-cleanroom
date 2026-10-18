# PRE-029b 60B-tier head 6041..6296: minimal 12-field + tabs (w2 map)

## 60B holds all 256 rows, 48 const (v5i first-hand)
- consts: 1:00 2:00 3:00 8:1d 14:f0 15:19 16:9b 17:5f 18:3c 19:f9
  22:93 23:d0 24:8e 25:af 26:33 27:6b 28:16 29:ee 30:19 31:0f 32:92
  33:b5 34:98 35:3b 36:21 37:bf 38:67 39:53 40:91 41:f7 42:eb 43:cb
  44:4e 45:ee 46:f1 47:15 48:2a 49:41 50:24 51:0f 52:51 53:14 54:a9
  55:1c 56:2d 57:e4 58:cf 59:5a.

## 16-tabs from 6041 (all verify full span)
- b0: 09 0b 08 0b 0b 09 09 08 09 0b 09 09 08 0b 0b 08 (3 values).
- b9: 7c b0 20 54 54 c8 c8 fc 6c 80 b4 b4 e8 bc bc 2c.
- b10: f0 f1 f2 f3 f3 f2 f2 f3 f0 f1 f2 f2 f3 f3 f3 f0 (4 values).
- b11: 0f ce 42 01 05 d1 d5 94 09 1c db df 9e 87 8b 00 (16 unique).
- b20: f3 f3 f4 f4 f4 fd fd fe fe 04 05 05 06 0e 0e 0f (ramp-ish).
- b21: 20x9/21x7 duty-16. b4: L10-lo +2/row (33@6041...).

## plateaus + flips
- b5/b6: 16-plateaus (v5i.log full runs). b7: 16s + one 32-merge
  (6185-6216:cb). b12: 16/32-mix (12 runs). b13: ONE flip @6137 (6f->70).
