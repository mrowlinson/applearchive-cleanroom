# A-254 (Q-248): T10P188 P-head geometry — DERIVED

Bed: census N=82161..82252 own bed (.rav[12:-4]). First-hand; P187-M from own P187
census row0 81841..81856 (this seat).

## 1. shape: CONFIRM
- 92/92 100B/84B exact. PB0 f6020000 (REPEAT x3 of P186/P187 PB0 sig); PB1
  fat 3b070500 (== P187 PB1 sig, own bed ref).
- PBA 82163..82178 single sig b7735000 NEW (b5 step INSIDE PBA @82176: 82175
  ff/81->82176 01/82, P177-style CONFIRM; PBA b5 {0x81,0x82}).
- SING 82179 sig e83d0600 NEW; MID9 82180..82188 single-sig-byte, per-N sigs
  EXACTLY fb1e0300,f91e0300,fd1e0300,f81e0300,fa1e0300,f91e0300,f91e0300,
  fa1e0300,f91e0300 (b0 varies fb/f9/fd/f8/fa, b1-3 const 1e0300; new MID
  variant CONFIRM).
- QUAD 82189..82252 MULTI-SIG: rows0,2,3 e9ef3100, row1 eaef3100 (per-row
  singletons 16/16).
- PBA VPOS [4,5,6,7,8,9,76,77,78,79] EXACT (10 = b4+b5+8tab; 8B M);
  MID VPOS [0,4,6,7,8,9,10,11,80,81,82,83] EXACT (12 = b4+11tab; 11B M incl
  sig b0; b5 const 0x82).

## 2. quad rows: CONFIRM
- M 6B pos[13,15,76,77,78,79] row-indep 16/16 x4, 16/16 distinct each row
  (heads 13/16 pairs each row), shared all 4 rows 16/16.
- sigR 7B b0,6,7,8,9,10,11 row-only, 64/64: rows2==3 exact e952bc1f862776;
  row0 e92cb1ff6b8cea; row1 eae6b1df7b2c63.
- tails b80..83 row-const cab05d9f/e83c3ebc/48775fe7/81775fe7 (rows2,3 share
  b1..3 775fe7, differ b0 48/81).
- M-novelty vs P187M tails: ALL NEW (0/16). PBA M 8B 16/16 (heads 15/16
  quads); MID M 11B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 tier {0x81,0x82} via lencode (PBA-internal step @82176).
- varpos partitioned exact (PBA 10=b4+b5+8tab; MID 12=b4+11tab; quad 18=
  b4+sigR7+M6+tails), 0 stragglers. NO D-class dips. Next tier @82253 sig
  aafe1e03 (82253+82254 both).

## geometry agrees on all 3 legs
