# NOTE-30 writer1s2 lz4: K=127 + override stack (heartbeat17)

- NEVER-ZONE K=127 EXACT (D<=127 absent + D>=128 present, clean reads).
- TAIL RULE (final candidate): INSERT(tail P, P>=END-127) iff ODD-chunk OR
  chunk-period>=64; zeros-tail never (wins over odd); mid-chunk always.
  All prior gates (OFF/ML/SPAN/MEND) dead; parity recursive (chunk0 seed).
- OPEN: +1/ENDS shapes, zeros-mid, 5 literal-skips, stored-chunk, period-def.
- NEXT: verify4 update (K + overrides) + corpus rerun, then buckets.
