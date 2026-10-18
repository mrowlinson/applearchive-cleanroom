# A-42 Q-35: cross-eviction matrix (101x696) + 4 T-collisions + partition

## protocol (v6q35d first-hand; v1/v2 lessons folded in)
- neutral-transplant: neutralize o1 (verified fires) +
  plant V at validated neutral offset n1 (R2-plant
  evicts), confirm at n2. posctrl (home1 at n1 +
  neutral o1 evicts): 100/101 beds (T[682] only fail —
  its 7 v1 prefix-22 hits REJECTED as overlapping-FPs).
- why neutral: destruction-transplants have BOTH FPs
  (~1/585 overlapping-gram, v1 o1-screen) and FNs
  (duplicate-key collapse — writer NOTE-55 confirmed —
  kills v1-o2 confirm; v1 screen missed 4/11 @T[501]).
- matrix: 101 beds x 696 cands (495 grams + 101 T-grams
  + 100 randoms), 70,180 encodes, r2-CONF2 required.

## T-COLLISIONS (multi-witness, P(chance)<<1e-5 each)
- H(99244451)==H(1714a27e): T[614]==T[687] (3 wit:
  017c50a8@614, 9625532f@687, T687@614).
- H(e1c9770a)==H(b875c22e)==H(a3abc27e): T[642]==T[671]
  ==T[694] (2+3 wit: c24e055b+T671@642, b1394027+
  T694+e00e15bd@671/694).
- H(50d77649)==H(a9451707): T[634]==T[676] (2 wit:
  50d77649+df13b332@676).
- components: {614,687} + {642,671,694} + {634,676};
  rest singleton (incl T[501]: 6/6 pinned CONF2, ZERO
  foreign edges).

## chance singles (value-collisions, ~14.7 expected)
- 654x0c983c04(630), 662x62b7f5be(672), 708x4910ff66
  (649), 634x75136748(642), 655x5641af46(N),
  693x64e2f1b4(N). unconfirmed-as-T-links; usable as
  single equalities only.

## puzzle (fit clue, not blocker)
- shared pairs hit 2-3/12 cross-tests, not 12/12.
  candidates: (i) correlated differences (mult-class:
  small+small=carry-kill ~75%?); (ii) canonical-gram
  offset errors; (iii) slot-order. follow-up on
  demand: offset sweep +-3 on pair grams.
- crosstalk 0/3 (mixed 3+2 fillers never evict):
  buckets INDEPENDENT. timing (a) declined (spawn
  noise >> slot signal); N-scan (c) subsumed.
- verdict: Q-35 CLOSED. multi-bit signal DELIVERED:
  partition + 4 T-collisions (6 T-equalities) + 21
  CONF2 edges. matrix logs: v6q35Ad.log/v6q35Bd.log.
