# A-329 (viewer r7): Q-329 T10P265 P-head @108957 — CONFIRM all 3

First-hand bed 108957..109360 (qr7bed
extended; census RC=0 missing=0) +
P264T ref 108701..16 (own bed).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 a0560300 NEW, PB1 bdcfaa06
  SAME-as-P264PB1 ✓, PBA16-PLAIN
  e0932f72 x16 @108959-74 (VPOS 7 exact
  b4+M6 b48,49,76-79; b0 const e0, b5
  const 53; NO pair in tier).
- C10-6SIG map EXACT: bdcfaa06 x4
  @108975-78 + bdcf7a06/bdcffa04/
  bdcf1a05/bdcf3a05/bdcf7a05 x2
  @108979-84 (6 distinct ✓; VPOS 14
  exact b4+M13 b2,3,35,46-51,80-83;
  b5 const 53; 10/10 diverge).
- QUADms 3-sig dffbac59 x16 (row0) +
  dffbac5c x32 (rows1-2) + dffbac57 x16
  (row3) NEW EXACT (VPOS 19: b4+QM6+
  R8+T4; b5 const 53).
- T88-SPLIT 05/04, 88B payload all 256
  ✓ (VPOS 17 exact b0,b4,b5+TM8+TR6
  partition over 0..87).
- Next P266 PB0 @109305 a0740300 NEW +
  109306 2a40e906 NEW + PBA 8087f776
  x16 @109307-22 + C10 958dec06
  @109323+ (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad QM6 b6,7,76-79 shared 16/16 x3
  vs row0; NO frags: all 18 payload
  varpos COL-pure or ROW-pure, 0 MIXED
  (b4 alone is trivially mixed as the
  lencode counter in every quad —
  excluded from frag scope as usual).
- R8 b3,35,46-51 r1==r2 MID-PAIRED 3/4
  EXACT (5c52a392917ed792 x2; r0
  59d2ffd8b1a56722 + r3
  5792ce9eb1805f9a distinct).
- Tails row-shared 4/4 distinct
  473b6a01/c2fac80f/756b3610/652f4ee8
  EXACT (no shared suffix).
- M-tails 16/16 ALL NEW vs P264T (row-0
  reference, true novelty).
- T88-ring SPLIT-b0: TM8 [9-11,20,80-83]
  by COL 16/16; TR6 [6,7,76-79] by ROW
  16/16 UNPAIRED (16 distinct); b0 =
  05 iff col<3 else 04 (3+13 per row
  x16 rows: 48x05 + 208x04 ✓); tails
  SPLIT b80-83 col / b76-79 row;
  b84-87 const 2032bed2 EXACT
  (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 108957..109304: 348/348
  exact (whole tier incl 88B cells).
- T88-ring b4=(0xf3+2off)&FF 256/256;
  b5=0x53+(off>=7)+(off>=135) 256/256;
  edges 109055->109056 ff/53->01/54 +
  109183->109184 ff/54->01/55.
- Consts ALL 4 EXACT: PBA 77 (b5-const),
  C10 70 (b5-const), quad 65 (b5-const),
  T88 71 (88-17).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
