# A-375 (viewer r26): Q-369 T10P508 193521..193868 — CONFIRM all

First-hand bed 191085..193870 (own
2786-cell census, oracle regen rc=0).
Payload .rav[12:-4]. Bed + scripts:
NVME encode-viewer/q362-r26/.

## 1. shape: CONFIRM
- 350 cells 193521..193870 ALL raw104/
  pay88. PB0 193521 aa050000 + PB1
  193522 74590b00: head pair fully
  repeats P507 sigs (bodies differ
  32/84 + 55/84 — fills writer TBD).
- PBA16-PLAIN 193523..538 sig
  4e97b500; M8 b52-55,80-83 16/16;
  b5 e7x13+e8x3 (step inside ✓);
  consts 78 (base 86).
- C10 193539..548 sig dba50b00; M5
  b52,84-87 10/10; b5 e8x10 const
  (no Q claim); consts 81.
- QUAD88 193549..612 5-sig-BY-COL
  (m=o%16 in-row): m0-1 c34fba00 /
  m2-5 d04fba00 / m6-7 d14fba00 /
  m8-12 d44eba00 / m13-15 904dba00
  in ALL 4 rows EXACT; M10 b0,1,
  10-13,80-83 16/16 per row,
  row-seqs IDENTICAL; R4 b84-87 rows
  73aaa739/93aaa739/b3aaa739/
  7f6c2544 row-const; b5-const e8;
  consts 72.
- T88-RING 193613..868 5-sig-BY-
  ROWBAND (rows=o//16): rows0-1
  c3dba40b / rows2-5 d0dba40b /
  rows6-7 d1dba40b / rows8-12
  d4daa40b / rows13-15 90d9a40b
  EXACT; TM7 b16-18,80-83 = f(m)
  16 distinct; TR10 b0,1,10-13,
  76-79 = g(row) 16 distinct;
  UNPAIRED; b5 = e8+(o>=51)+
  (o>=179) all 256; b84-87 =
  bc282745 all 256; consts 69.
- Next P509: PB0 @193869 d2050000
  NEW; PB1 @193870 daa40b00 NEW.

## 2. verdict: CONFIRM (27/27 checks)
- Every Q-369 byte claim reproduces
  from own bed. w2d tier cut SAFE.
