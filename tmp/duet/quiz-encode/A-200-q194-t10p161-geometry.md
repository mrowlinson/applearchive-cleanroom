# A-200 (Q-194): T10P161 P-head geometry — DERIVED

Bed: census N=72765..72856 own bed (.rav[12:-4]).
First-hand; P160-M tails from own P160 census
row0 72445..72460 (this seat).

## 1. shape: CONFIRM (2B-sig mixed PBB)
- 72765 100B/84B sig 07000000 (PB0); 72766
  100B/84B fat sig e30f0000 NEW; PBA
  72767..72782 sig a2fa0000 NEW; SINGLETON
  72783 sig d00d0000 NEW.
- PBB9 72784..72792 MIXED 2B-sig per-N exact:
  d006,d007,5007,5007,d007,d006,5007,5007,
  5007 (b2,3 const 0000; 8th mixed-sig PBB,
  3rd 2B-sig).
- QUAD 72793..72856 single sig 0c750000 NEW.
- 92x100B exact. PBA VPOS [4,48-51,76-79]
  exact (b5 const 0x38); PBB VPOS [0,1,4,
  44-47,49-51,80-83] exact (13B M incl 2B
  sig).

## 2. quad rows: CONFIRM
- M 8B pos[6,7,8,9,76,77,78,79] row-indep
  16/16 x4, 16/16 distinct each row (heads
  16/16 quads each row, full-heads), shared
  all 4 rows 16/16 positional (3rd 8B quad M).
- R-band 7B b44-47,49-51 row-only: rows0==2
  exact 49f339ca239cef (1st 0==2 pairing);
  row1 c9940b5e6313ff; row3 c9383f2a23278f,
  64/64.
- Tails b80..83 row-const 7c820b72/87d38340/
  06830b72/bec7c248 (rows0,2 share 830b72,
  differ b0).
- M-novelty vs P160M tails: ALL NEW (0/16).
  PBA M 8B 16/16; PBB M 13B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 const 0x38 PBA/PBB; quad 0x38->0x39
  step exactly at 72832 (72831=38, 72832=39;
  row2 spans).
- Varpos partitioned exact (PBA 9 = b4+8tab;
  PBB 14 = b4+13tab; quad 21 = b4+b5+R7+M8+
  tails), 0 stragglers. NO D-class dips.
- Next tier @72857 sig c0d00700.

## geometry agrees on all 3 legs
