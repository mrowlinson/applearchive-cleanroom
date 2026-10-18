# Q-18 writer2: bitmap top-table ORDER rule (discriminating pair)

## Stuck (own beds, 108 chunks, own decoder exact throughout)
- SELECTION closed: referenced set = top-12 by (count,pbc,value)
  DESC, 108/108 (concurs NOTE-w2s3-12).
- ORDER open: ~36/99 tables = (pbc,value)-ASC; others scrambled
  (one = count-DESC w/ 00-first; one has count-ASC triple
  [25,26,30] no DESC-sort emits; ff/0 sits in 11 slots).
- discriminating pair (SAME kind/size/single-chunk, diff seeds):
  A = 800B "ABCDEFGH"-periodic + 8000B random.Random(7).randbytes
    -> table [00,7f,bf,df,ef,f7,fb,fd,fe,ff] (value-ASC),
    counts [99,2,3,4,4,6,3,3,7,969] (not monotonic).
  B = same recipe, seed 47
    -> table [00,ff,fe,fb,f7,ef,df,fd,7f,ef/1,ee,bf],
    counts [99,965,5,5,5,5,5,4,3,1,1,1] (count-DESC after slot0).
- ruled out as sort keys (exact-match/99): count/first/last/
  median/span/runs/nlit/periods/sources/literals all ~0;
  no fixed key->slot function; no fixed ASC-permutation (A vs B);
  no first-use/eviction dynamics (10-12 distinct keys each).

## Ask (behavior-only, derived answer, no internals)
1. Which op-trace/input feature predicts slot order on A-vs-B
   (verified on more seeds)? A derived slot-assignment rule.
2. If the rule needs pre-pass quantities (candidate counts etc.),
   which bedded quantity stands in for them?

## Use
- Unblocks bitmap encoder byte-identity (table order must match).
