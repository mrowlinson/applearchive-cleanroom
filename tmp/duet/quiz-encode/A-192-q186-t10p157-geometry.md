# A-192 (Q-186): T10P157 P-head geometry — DERIVED

Bed: census N=71373..71464 own bed (.rav[12:-4]).
First-hand; P156-M tails from own P156 census
row0 71053..71068 (this seat).

## 1. shape: CONFIRM
- 71373 100B/84B sig 07000000 (PB0); 71374
  100B/84B fat sig b60f0000 NEW; PBA
  71375..71390 sig eafa0000 NEW; SINGLETON
  71391 sig ae0f0000 NEW; PBB9 71392..71400
  sig d7070000 NEW; QUAD 71401..71464 single
  sig 737d0000 NEW.
- 92x100B exact. PBA VPOS [4,11,19,26,27,
  76-79] exact (b5 const 0x2d); PBB VPOS
  [4,11,18,19,25-30,80-83] exact (13B M).

## 2. quad rows: CONFIRM
- M 7B pos[32,33,34,76,77,78,79] row-indep
  16/16 x4, 16/16 distinct each row (heads
  14/16 each row), shared all 4 rows 16/16
  positional.
- R-band 9B b11,18,19,25-30 row-only:
  rows0==1 exact 269159ad9dbfb24e37 (3rd
  0==1 pairing); row2 3ed1b48d9957d2c234;
  row3 3ed1b48d9a57d2c234 (rows2,3 differ
  exactly 1B), 64/64.
- Tails b80..83 row-const ALL distinct
  503b204d/67723c4d/bc3ec4d4/89b0658e.
- M-novelty vs P156M tails: ALL NEW (0/16).
  PBA M 8B 16/16; PBB M 13B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 const 0x2d PBA/PBB; quad 0x2d->0x2e
  step exactly at 71424 (71423=2d, 71424=2e;
  row1 spans).
- Varpos partitioned exact (PBA 9 = b4+8tab;
  PBB 14 = b4+13tab; quad 22 = b4+b5+R9+M7+
  tails), 0 stragglers. NO D-class dips.
- Next tier @71465 sig c4050700.

## geometry agrees on all 3 legs
