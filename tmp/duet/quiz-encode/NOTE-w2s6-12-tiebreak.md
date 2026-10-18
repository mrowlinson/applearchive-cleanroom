# NOTE-w2s6-12 writer2: boundary-tie VERDICT (11 hypotheses killed, lottery extends)

## Hunt (first-hand + corpus mine)
- gen(80) flips: 11 tied cases (2 positions x values + dense). twins
  {3f/1,7f/0,fb/0}@12 -> 3f/1 always (10/10); {3f/1,df/0,fb/0}@13 ->
  {3f/1,fb/0}. winner value/position-independent within cluster.
- corpus mine: 201 unique tied chunks, diverse twin-sets (free data).

## 11 hypotheses TESTED on 201 (seated-set exact match)
- latest-first 80, earliest-first 77, latest-last 67, narrow-span 79,
  pbc 85, min-bitmap 52, MAX-bitmap 106, min-pop 56, max-pop 108,
  min-str 52, max-str 106. ALL ~coin-flip. NO static rule decides.
- (my early latest-first lead from 2 cases: killed by the corpus.)

## Verdict (closes Q-22#2 residue fully)
- UNTIED membership = count-exact (top ranks seat deterministically).
- AT-TIE seating + ALL order = lottery-class (deterministic per input,
  unpredictable from any summary stat — same class as slot order).
- exposure model COMPLETE: counts decide only clear-cut membership;
  everything contested is tie-outcome. no further micro open here.
