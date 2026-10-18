# A-33 eviction = ~2K buckets x ~5 slots, distinct-keyed LRU-ish (Q-28 verdict)

## structure (black-box fit, fixed-T survival curve, 280 encodes)
- N(bytes)=6K..12K fires: 32/26/26/21/18/12/10 per 40. best Poisson
  P(Pois(N/B)<S): B=1920 S=5 (sse 13.7); band B=1600-2560 S=4-6.
  capacity ~10K grams; 50% @~9K distinct. gradual + seed variance at
  fixed N KILLS sharp-global-cap (H3); steep cliff KILLS 1-slot-uniform
  (w1's 4K-uniform mismatch CONFIRMED from structure side).
- slots are DISTINCT-keyed with refresh: repeats don't consume (PH-C).

## discriminating pair (same 12K total bytes, opposite fate)
- X (12K distinct once): 2/12 fires (EVICTS). Y (3K-set x4, 3K distinct):
  12/12 fires (SURVIVES). DISTINCT-count rules, total-insert-count moot.
- bed-shape for w1: Y-vs-X at 12K total. any model predicting Y<=X is out;
  any model keyed on total inserts is out.

## supporting (v4q28 PH1)
- 0/9200 single-gram evictors (nosig 0, baseline fires ✓): lone inserts
  never evict — multi-slot, not 1-slot. hash width NOT measurable this
  way (rate ~0); width comes from the curve fit instead (B~2K).

## model guidance (behavioral, w1 maps to code)
- replace "4K last-write" with: hash-partition ~2K buckets x ~5 slots,
  last-write + per-bucket LRU (re-insert refreshes, no double-count),
  keep 4B-validate + mstart/+1/ends + continuous + K-gate.
- residual span>7K first-divs: score as same-bucket-distinct-overflow
  (>=5 distinct bucket-mates after T), not global age.
- caveat: B non-power-of-2 (1920 fit; 2048 within band) — hash fold or
  segmentation inside is OPEN; exact hash function unprobed (black-box
  fit only). S=4-6 band, 5 best.

## apparatus
- v4q28b.py + PH-C inline (bed3/lz4probe shapes, T=pre[100:108], seeds
  200-239 + 300-311), oracle compression_tool -a lz4. Q-28 CLOSED.
