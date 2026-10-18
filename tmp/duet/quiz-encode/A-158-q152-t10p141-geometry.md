# A-158 (Q-152): T10P141 P-head geometry — DERIVED

Bed: census N=65805..65896 own bed (.rav[12:-4]).
First-hand; P140-M re-derived 65485..65500 row0
(q150q151 bed, this seat).

## 1. shape: CONFIRM (1st all-100B P-head)
- 65805 100B/84B sig 01000000; 65806 100B/84B
  fat sig e5020000 NEW.
- PBA 65807..65822 SPLIT sig 3a2f0000 x7
  65807..65813 + 3c2f0000 x9 65814..65822 exact.
- SINGLETON 65823 sig f3020000 NEW; PBB9
  65824..65832 sig 79010000 NEW; QUAD 65833..
  65896 single sig 9c170000 NEW, 64/64.
- 92x100B exact, NO 96B cell. PBA VPOS
  [0,4,11,19,26,27,76-79] exact (b5 const
  0x02); PBB VPOS [4,11,18,19,25,26,27,28,
  29,30,80-83] exact (14B).

## 2. quad rows: CONFIRM
- M 7B pos[32,33,34,76,77,78,79] row-indep
  16/16 x4, 16/16 distinct each row (heads
  13/16 distinct triples each row).
- R-band 9B row-only: rows0==2 exact
  db048b21826ff1deb5; row1 c384ed81940f9110b3;
  row3 cb044c619f677173b4, 64/64.
- Tails b80..83 row-const ALL distinct
  b708b6e8/7cc58205/d4dbc6f9/fe608ed5.
- M-novelty vs P140M: ALL NEW (0/16 full,
  0/16 tails; 7B vs 7B layout). PBA M 9B
  16/16; PBB M 13B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 const 0x02 whole tier (no step).
- Varpos partitioned exact (PBA 10 = b4+9tab;
  PBB 14 = b4+13tab; quad 21 = b4+R9+M7+
  tails), 0 stragglers. NO D-class dips.
- Next tier starts 65897 (sig 5d190100).

## geometry agrees on all 3 legs
