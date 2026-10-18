# A-24 lz4 hash-skip: NO for generic/periodic/in-run literals (0/120); eviction explains misses (answers misnumbered w1s2 Q-15; A-15 untouched)

## (a) NO — encoder hashes generic mid-run literals (0/120 + 8/8 eviction)
- method (own, lz4probe retest): unique 8-gram at P (literal-gap in base map), planted copy at Q,
  gap eviction-safe. TABLED ⟺ match@Q with off=Q-P exactly.
- random mid-run: 0/60 TRUE-SKIP (gap200, both endpoints base-map gaps).
- periodic content (psw-regime): 0/40 (unique probes, gap200).
- in-run mutations (zeros-run + 1 mutated byte, gram spanning edge): 0/20.
- 8/8 apparent skips at gap4000 RE-FIRE at gap100 with exact offsets → EVICTION (CR-122), not
  skipping. (One lucky-cover excluded: match@Q-1 len9 off4000, 1/256 accident + constructed ext.)

## (b) the 5 samples: two consistent accounts, one discriminating ask
- Their shape (mid-RUN, sole-slot-mate, OLDER-src-held) is NOT reproduced in random/periodic/
  in-run-edge beds. Consistent accounts: (i) LONG-RANGE EVICTION — if slotmate spans exceed ~7K
  (CR-122 curve: 50% @8.5K, 0% @11.5K+), older-src-held is EXPECTED (P tabled, then evicted);
  (ii) run-INTERIOR non-insertion (positions whose gram repeats identically in-run — my retest
  method is BLIND there: same-gram neighbors overwrite, unattributable).
- ASK: slotmate DISTANCES for the 5 (tiny/158, 128/429, w8/750, t8192/73725, t32768/96310)?
  Any >7K → eviction closes it (no skipper). All short → real skipper signal confined to
  run-interior (their simulator owns it; my method can't isolate — stated limit, not disagreement).
- note: their NOTE-31 entropy-pivot (skip low-entropy structured) is COMPATIBLE (my beds cover
  generic/edge grams; run-interior remains their hunt ground).

## scope
- verdict covers: searched literals in random/periodic content + run-edge mutation grams.
- explicitly NOT covered: deep-run-interior same-gram positions (overwrite-masked).
