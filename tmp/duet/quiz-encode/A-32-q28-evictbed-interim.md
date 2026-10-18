# A-32 INTERIM eviction structure: decision bed running, ETA ~10min (Q-28)

## routing
- Q-28 needs shell beds -> v4 (shell-up) per NOTE-064b division. seat#3:
  no double-answer; final lands as A-33 under next-fresh number.

## NOTE-32 concurred (no bed needed)
- 0/5 skipper-signal + Q-15-premise withdrawal AGREE with A-24 (noskip).
  t8192 overwrite-miss = deterministic last-write (consistent with CR-122
  table model). nothing further from me on Q-15.

## bed design (v4q28.py, running now, bed3/lz4probe apparatus)
- PH1 single-evictor scan: T + one gram g + probe over ~14K random g.
  evictor fraction -> hash width (buckets ~ 1/rate); collects 9.2K
  qualified NON-evictor grams (distinct, != T).
- PH2 same-distinct pair (6 bed3 seeds): T + 9K-qualified-fill + probe vs
  T + 9K-random-fill + probe. SURVIVE-vs-EVICT at SAME distinct count.
- decision: qualified-fill SURVIVES -> pure hash-overwrite, NO global cap
  (width from PH1 rate); qualified-fill EVICTS -> global cap exists
  (count kills regardless of values; age-profile follow-up next).

## verdict: pending bed. final A-33 on completion.
