# PRE-024b 56B-tier head 3953..4208: 21 fields + 4096 reframe (w2 map)

## 56B holds all 256 rows (v5h first-hand)
- nvar=21: b0/4/5/6/7/8/9/10/11/12/13/14/15/38/39/46/47/52/53/54/55.
- 35 consts: 1:00 2:00 3:00 16:34 17:91 18:d1 19:8a 20:ef 21:5b 22:40
  23:73 24:4b 25:92 26:82 27:3c 28:6d 29:aa 30:c8 31:56 32:ee 33:39
  34:a1 35:ff 36:2f 37:d8 40:e2 41:df 42:ee 43:fe 44:ec 45:f8 48:70
  49:5a 50:d8 51:dd.

## 4096 = hard reframe (head bytes flip together)
- b0: 06 -> 0d. b5: ff -> e0 (was fe@3953-3967, ff@3968-4095).
- b6..b15 all flip @4096: 91/b5/94/78/87/d8/6f/9e/03/10 ->
  23/6b/15/f1/0e/b1/df/3c/07/20.
- b4: L10-lo +2/row continues through (e3@3953..., unbroken).

## tail structure
- b38/39/46/47: 16-plateaus from 3953 (b39/b46 merge 4161-4192: 32-row).
- b52/55: 192 runs (1-2 plateaus); b53/54: every-row change (256 runs).
