# A-216 (Q-210): T10P169 P-head geometry — DERIVED

Bed: census N=75549..75640 own bed (.rav[12:-4]).
First-hand; P168-M tails from own P168 census
row0 75229..75244 (this seat).

## 1. shape: CONFIRM (b1-varying mixed PBB)
- 75549 100B/84B sig 23000000 (PB0; NEW PB0
  sig); 75550 100B/84B fat sig cd5e0000 NEW;
  PBA 75551..75566 sig 0be40400 NEW.
- SINGLETON 75567 sig cd5e0000 (== PB1 sig,
  3rd PB1-echo).
- PBB9 75568..75576 MIXED b1 per-N exact =
  21,27,21,25,23,23,23,23,23 (b0 const 0x73,
  b2,3 const 0000; 11th mixed-sig PBB, 1st
  b1-varying).
- QUAD 75577..75640 single sig 33370200 NEW.
- 92x100B exact. PBA VPOS [4,48-51,76-79]
  exact (b5 const 0x4e); PBB VPOS [1,4,44-47,
  49-51,80-83] exact (12B M incl sig b1).

## 2. quad rows: CONFIRM
- M 7B pos[6,7,9,76,77,78,79] row-indep 16/16
  x4, 16/16 distinct each row (heads 15/16
  triples each row), shared all 4 rows 16/16
  positional.
- R-band 7B b44-47,49-51 row-only: rows0==2
  exact 6959cddb23f03e (3rd 0==2 pairing);
  row1 c9817695e3819f; row3 2972170fe33cff,
  64/64.
- Tails b80..83 row-const dd18d476/789a4f37/
  5e19d476/f9d7c1bd (rows0,2 differ b0 only).
- M-novelty vs P168M tails: ALL NEW (0/16).
  PBA M 8B 16/16; PBB M 12B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 const 0x4e WHOLE tier (no step anywhere).
- Varpos partitioned exact (PBA 9 = b4+8tab;
  PBB 13 = b4+12tab; quad 19 = b4+R7+M7+
  tails), 0 stragglers. NO D-class dips.
- Next tier @75641 sig 37732500.

## geometry agrees on all 3 legs
