# NOTE-w2s4-3 writer2: decoder exact, selection 108/108, ORDER paradox

- own zbmparse.py EXACT: decode==raw 24/24 + 108/108 corpus
  chunks (fixed 2 own bugs: cross-chunk backrefs, per-rep
  meta2 consume). oracle deterministic 3/3 same input.
- SELECTION reproduced 108/108: top-12 by (count,pbc,value)
  DESC (concurs pred). padding always (0,0); pads at END
  usually, but tag4 has (0,0) at SLOT0 unused — padding or
  pin? slot0 = 00/0 in 95/108.
- ORDER paradox: value-ASC ⟺ all-pbc0 (18/18 ASC all /0;
  6/6 mixed nonASC) — but tag7 (kind7, single-chunk) rest =
  pure value-ASC (counts 2,3,4,4,6,3,3,7,969 arbitrary) while
  tag47 (SAME kind/size, other seed) = count-DESC-exact
  (ties val-DESC) except 00/0 pinned slot0. tag0: two local
  inversions vs selection ([30,26,25]->[25,26,30] reversed
  triple!). ff/0 sits in 11 different slots across chunks.
- ruled out (exact-match/108): sel 9, count 9, value 18,
  first 0, last 0, op0 5, opN 14, fixed-permutation (7v47).
- next: REFERENCED-vs-table split (nums 3-14 actually used;
  kill padding confusion) -> big-corpus pairwise tie-break
  consistency -> controlled micro-beds.
- SIDE-DISCOVERY (queued): oracle chunking NOT 0x8000-fixed
  (tag26 chunk dlen~15000 of 40000B input) — chunk rule OPEN.
- Q-17 still open (no A-18). claim HELD.
