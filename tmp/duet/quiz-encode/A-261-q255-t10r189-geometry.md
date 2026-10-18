# A-261 (Q-255): T10R189 R-ring geometry — DERIVED (TRANSPOSE CONFIRM)

Bed: census N=83297..83552 own bed (.rav[12:-4]). First-hand; P191-M from own P191
census row0 83233..83248 (this seat).

## 1. shape: CONFIRM
- Single RING 83297..83552: 256x100B/84B, single sig de652003.
- Next @83553: PB0 sig 20030000 NEW, PB1 83554 sig 47a20700 NEW, PBA
  83555..83556 sig 47a26700 — all 3 as writer.
- VPOS [4,5,11,19,20,21,22,26,27,72,73,74,75,76,77,78,79] EXACT (17; 67 consts).

## 2. orientation: TRANSPOSED CONFIRM — first transpose ring
- M 8B b11,19,26,27,76-79 by COL (off&15): constant within each col 16/16,
  16/16 distinct cols. Q 7B b20,21,22,72-75 by ROW (off>>4): constant within
  each row 16/16, 16/16 distinct rows.
- Normal framing REFUTED first-hand: M-constant rows 0/16, Q-constant cols
  0/16 (my refutation test; writer's "1/17" figure not reproduced as stated
  but conclusion agrees — transpose holds, normal fails).
- M-heads: (b11,b26) PAIRS 15/16 (matches writer's 15/16 number); full M-head
  quad 16/16, triple (b11,b19,b26) 16/16 — writer's "triples" label fits the
  pair count, noted, no geometry impact. b26 14-distinct CONFIRM: b0 repeats
  at cols 0+9, 30 repeats at cols 5+15; full M8 16/16. (b11 alone 2-valued.)
- Q-head triple (b20,b21,b22) 16/16 CONFIRM. M-tail quad 16/16 and triple
  16/16; novel-vs-P191M 16/16 (0 overlap).

## 3. counters: CONFIRM, NONE
- b4==(0xc3+2*off)&FF all 256 (even-lo). b5 = 0x8a+(off>=31)+(off>=159) exact;
  edges 83327->83328 ff/8a->01/8b, 83455->83456 ff/8b->01/8c as writer.
- varpos exact (17), 0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs (transpose verified first-hand)
