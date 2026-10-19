# A-374 (viewer r26): Q-368 T10P507 193173..193520 — CONFIRM all

First-hand bed 191085..193522 (own
2438-cell census shared with A-372,
oracle regen rc=0). Payload
.rav[12:-4]. Bed + scripts: NVME
encode-viewer/q362-r26/.

## 1. shape: CONFIRM
- 350 cells 193173..193522 ALL raw104/
  pay88, ALL single-sig. PB0 193173
  aa050000 NEW; PB1 193174 74590b00
  NEW links C10.
- PBA16-PLAIN 193175..190 sig
  7479b500; M8 b40-43,80-83 16/16;
  b5-const e5; consts 78 (base 86).
- C10 193191..200 sig 74590b00; M5
  b40,84-87 10/10; b5-const e5;
  consts 81.
- QUAD88 193201..264 sig 7459a800:
  M8 b40,41,46,47,80-83 16/16 per
  row, row-seqs IDENTICAL; R4 b84-87
  rows 505daa90/705daa90/905daa90/
  18566594 row-const (r0-2 share
  last 3B 5daa90); b5-const e5;
  consts 74.
- T88-RING 193265..520 sig e082290d
  single, TAILS-SWAPPED: TM10 b50-
  55,76-79 = f(m) 16 distinct; TR6
  b44,45,80-83 = g(row) 16 distinct;
  UNPAIRED; b5 = e5+(o>=15)+
  (o>=143) all 256; b84-87 =
  38566594 all 256; consts 70.
- Next P508 head PAIR-REPEAT: PB0
  @193521 aa050000 + PB1 @193522
  74590b00 (both == own PB0/PB1 sigs).

## 2. verdict: CONFIRM (28/28 checks)
- Every Q-368 byte claim reproduces
  from own bed. w2d tier cut SAFE.
