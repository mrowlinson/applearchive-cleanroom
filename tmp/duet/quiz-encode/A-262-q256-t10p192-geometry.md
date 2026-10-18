# A-262 (Q-256): T10P192 P-head geometry — DERIVED

Bed: census N=83553..83900 own bed (.rav[12:-4]). First-hand; R189-M tails from own
R189 census (M-by-col tails 83297..83312, this seat).

## 1. shape: CONFIRM
- 83553..83900 = 348/348 100B/84B exact: PB0 83553 sig 20030000 (as R189-next);
  PB1 83554 sig 47a20700; PBA 83555..83570 sig 47a26700 (VPOS [4,32,33,34,35,
  76,77,78,79] = b4+M8 EXACT).
- 10 SINGLES 83571..83580 sigs EXACTLY 47a20700 (links PB1), 0f010300,
  b7a00300, 9bb60300, 47be0300, a7030300, 338e0300, b7a00300 (=83573),
  a7030300 (=83576), f39d0300.
- Sig-sharers DIVERGE bodies: 83571-vs-PB1 27B / 83573-vs-83578 6B /
  83576-vs-83579 3B — all 3 diffs EXACT.
- QUAD 83581..83644 single sig 47a23300 (VPOS 19 EXACT); T-RING 83645..83900
  256x single sig 47a2af03 (VPOS 14 EXACT).
- Next @83901: PB0 sig 20030000 (REPEAT of own PB0!), PB1 83902 47a20700,
  PBA 83903..83904 sig 47a26700 (probed 2 cells, both match).

## 2. quad + T-ring: CONFIRM
- Quad M6 b36,37,76-79: row-indep 16/16 x4, shared 16/16; tails 16/16
  distinct, ALL NEW vs R189M (0/16).
- R7 b22,23,30-34 PAIRED r1==r2 e980eefc73438f (3/4 distinct: row0
  91af79fcf30081, row3 619b42bfd33f7a); tails 4/4 distinct
  66d7433b/90c49285/c6c49285/875cfecd, 13/16 bytes (r1/r2 share last 3B
  c49285, differ b80 90/c6).
- T-ring TRANSPOSED (2nd ever) CONFIRM: M6 b42,43,76-79 by COL off&15 16/16;
  Q6 b36,37,72-75 by ROW off>>4 16/16; b42 full 16-distinct; normal frame
  M-rows 0/16 refuted.

## 3. counters + dips: CONFIRM + 2 minor CORRECTIONS, NONE
- Odd-lencode all 83553..83644: 92/92 exact.
- T-ring b4=(0x7b+2off)&FF 256/256; b5=0x8d+(off>=67)+(off>=195) 256/256;
  edges 83711->83712 ff/8d->01/8e + 83839->83840 ff/8e->01/8f.
- Quad b5 carry at off3 CONFIRM (off0-2 0x8c -> off3+ 0x8d, odd-lo: 83583
  FF -> 83584 01).
- b5 const: T-ring base 0x8d NOT const (tiers {0x8d,0x8e,0x8f}, steps @67/195
  as writer); PBA const 0x8c whole block.
- CORRECTION 1: consts are 75/65/70, not 74/65/70 — PBA VPOS is 9 (b4+M8, b5
  const single-tier) so 84-9=75; writer's 74 contradicts their own PBA VPOS.
- CORRECTION 2: PBA-M heads are 16/16 quads (full), not 15/16 per hb30.
- varpos partitioned exact (quad 19=b4+b5+R7+M6+tails; tring 14=b4+b5+M6+Q6),
  0 stragglers. NO D-class dips.

## geometry agrees on all legs modulo 2 PBA counts (75 consts, 16/16 heads)
