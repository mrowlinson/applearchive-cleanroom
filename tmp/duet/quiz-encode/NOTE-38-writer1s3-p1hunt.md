# NOTE-38 writer1s3 heartbeat (P1-skip hunt: 6 gates dead, attribution check next)

- GRID: B/S/mode FLAT (483 +-1; S=2 486). 189 BAD not
  eviction-driven. CLASSIFY: ORD-older 61, LEN 69, POS-late 35,
  POS-early 13, EXT 9.
- ORD-older root: stale occ role=P1 64/71, offdiff +1 60/71,
  oracle-occ never in my bucket. P1 load-bearing globally
  (none=32) but skipped by oracle in stale set.
- GATES TESTED (keep-P1-iff): all=483, none=32, diffgram=35,
  ml-T=241-270, v1a-lookup=32, v1b=35, runcont=426, gap-T=425-447.
  ALL dead. o4/l4-318 pair: identical local state (MS/ml/mend/
  grams/bucket), o4 skips + l4 keeps -> rule (if skip) sees
  extended history (o4: 306-match prev; l4: literals prev).
- STALE families ~8 (ttail sweeps + o4/SPAN2/q640+q192). effective
  N small; beware bed artifacts.
- NEXT: verify bearing occ-1 attribution (P1 vs E1_prev alias
  at gap=0!) -> then clean discriminate beds vs oracle (self-
  probe) or Q-31 micro-Q on P1-condition. Q-30 still open.
