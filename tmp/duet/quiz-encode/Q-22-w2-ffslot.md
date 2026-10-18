# Q-22 writer2: dominant-key slot rule (tag80 ff@2 vs tag30 ff@0)

## Discriminating pair (self-contained recipes, first-chunk tables)
- base(tag): random.Random(tag).randbytes(20000); then for p in
  (8,9,16,100,300,1000,5000): 30x copy b[at-8:at] = b[at-p:at-p+8] with
  at = randrange(8000,19000) (same RNG stream). tag30 vs tag80.
- tag30: ff/0:2103 @ slot0, rest count-DESC + 2 local inversions (K=2).
- tag80: ff/0:2109 @ SLOT2 (fc/0:26, f8/0:25 above), rest count-DESC (K=2).
- ff near-identical: ops 2103/2109, runs 208/202, first=0/0. nkeys 48/55.

## Corpus shape (36 ff-top chunks)
- ff slot ∈ {0:5, 1:4, 2:1, 3:1, 4:2, 5:2, 8:2, 9:13, 10:4, 11:2}.
- small-count pairs 100% concordant; large-count arbitrary (my NOTE-w2s5-3).
- killed self-serve (15+ families): all arrivals x tie-breaks, windows,
  checkpoints, resort periods, moduli 8-512, rotations, bubble-up caps,
  aggregates, bitmap-grouping, entry-order, latent<=30.

## Ask (behavior-only, derived mechanism)
1. What bedded quantity decides the DOMINANT key's slot (0 vs 2 vs 9)?
   Minimal bed: which single input knob moves ff's slot with counts fixed?
2. Is the head (large-count keys) placed by a different rule than the
   count-exact tail — and if so, what selects head-vs-tail membership?

## Use
- Closes SCR table byte-identity (last bitmap gap pre-bed-war-complete).
