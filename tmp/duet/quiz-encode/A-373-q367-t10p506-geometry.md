# A-373 (viewer r26): Q-367 T10P506 192825..193172 — CONFIRM all

First-hand bed 191085..193522 (own
2438-cell census shared with A-372,
oracle regen rc=0). Payload
.rav[12:-4]. Bed + scripts: NVME
encode-viewer/q362-r26/.

## 1. shape: CONFIRM
- 350 cells 192825..193174 ALL raw104/
  pay88. PB0 192825 d4020000 NEW; PB1
  192826 e2ab0500 NEW links C10.
- PBA16-PLAIN 192827..842 sig
  22be5a00; M7 b20-22,80-83 16/16;
  b5-const e2; consts 79 (base 86).
- C10 192843..852 sig e2ab0500; M4
  b84-87 10/10; b5-const e2; consts 82.
- QUAD88 192853..916 2-sig-BY-
  COLHALF: m0-7 96124000 / m8-15
  9e124000 in ALL 4 rows EXACT; M7
  b0,19,27,80-83 16/16 per row,
  row-seqs IDENTICAL; R3 b84-86 rows
  f1a3c8/11a4c8/6132d5/8132d5
  row-const (b87 const dd all rows);
  b5 e2x43+e3x21 (no Q claim); consts 76.
- T88-RING 192917..193172 2-sig-BY-
  ROWHALF: rows0-7 9612a005 /
  rows8-15 9e12a005 EXACT; TAILS-
  SWAPPED: TM8 b32-35,76-79 = f(m)
  16 distinct; TR7 b0,19,27,80-83 =
  g(row) 16 distinct; UNPAIRED; b5 =
  e3+(o>=107)+(o>=235) all 256;
  b84-87 = c032d5dd all 256; consts 71.
- Next: P507 PB0 @193173 aa050000
  NEW; PB1 @193174 74590b00 NEW.

## 2. verdict: CONFIRM (25/25 checks)
- Every Q-367 byte claim reproduces
  from own bed. w2d tier cut SAFE.
