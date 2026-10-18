# A-22 SCR mechanism: same-SET-different-ORDER PROVEN, fork mechanized, pin-fork narrowed (Q-20)

## N1: order is NOT a function of SET (2750 vs 3000 discriminating pair)
- IDENTICAL 12-key sets {00,7f,be,bf,df,ee,ef,f7,fb,fd,fe,ff}: L2750 -> SCR [ff,00,fe,fd,...],
  L3000 -> ASC [00,7f,be,...,ff]. Slot0 ff-vs-00. KILLS globally: hash-bucket-dump, value-sort,
  every static SET->ORDER rule. (ASC-regime compaction stands as the no-pressure PATH, not global.)
- counts near-identical too (ff 328/358, 00 99/99, rest ≤3): order differs DESPITE set+counts match.

## N2: fork = PRESSURE, mechanistically (not just correlationally)
- 2750: 13 OP-keys (3f CUT!) -> SCR-path. 3000: 12 OP-keys (no cut) -> ASC-path. Same set, split
  EXACTLY on CUT-presence. w2's trigger (nkeys>12 ⟺ SCR) now has same-set mechanistic proof.
- ASC-path rule (CLOSED): (pbc,value)-ASC compaction (fits 39/40 + odd-tails + X80/Y20 + K-tit).

## N3: SCR-path = count-DRIVEN (same-set reorder bed)
- 1-byte flip @pos5200 on B: SAME 12-key set, fb sinks slot3->8 ([00,ff,fe,f7,ef,df,fd,7f,fb,...]).
  Order FOLLOWS counts within SCR (fb's count fell, still selected). So SCR = f(counts),
  ASC = count-blind. The paths use DIFFERENT inputs (counts vs values).
- B = 00-pin + count-DESC-<= EXACT-fit stands (clean tail); 2750 = pure count-DESC + 1 inversion.

## N4: PIN-FORK narrowed to within-SCR (B:00@0 vs 2750:ff@0, both CUT+SCR) — OPEN
- exhausted (each fails one side): all insertion orders (count±/value±/first/last-seen), fixed-hash
  buckets, sorts+ties, run-counts (w2 runs=1 kills), length (unshaken but ASC-incompatible alone),
  ff/00 shares/ratios (no mechanism). REMAINING: (i) PRE-PASS quantities (unknowable directly —
  Q-19#2 as THE question; propose JOINT FIT: one rule (count-DESC-<=?) + latent per-chunk counts
  fitted over all 516 SCR tables — jointly identified or ruled out); (ii) many-tie bed for qsort
  (still undiscriminated: necessary-nowhere (B/2750 deterministic fits exist modulo fork),
  unruled-out globally).
- Q-20#1 (structure?): ASC = value-scanned array/compaction; SCR = count-driven dynamics with
  unknown insertion/pre-pass (array+insertion favored over heap: heap-property ≤32% per w2).
- Q-20#3 (qsort?): NOT NEEDED for any bedded case; many-tie bed (20+ equal counts) still decides.
