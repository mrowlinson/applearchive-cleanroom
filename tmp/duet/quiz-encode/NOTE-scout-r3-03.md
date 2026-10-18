# NOTE-scout-r3-03: T2 generator + runner LANDED (@b006ad4)

## Committed (lanes/encode-container@b006ad4, LOCAL ONLY, 6 files)
- `tests/container/t2-gen.py` (new): seeded deterministic corpus
  (basic/sparse/clone-src/hlc + MANIFEST.json); same-seed diff -r
  identical proven (seeds 7, 8).
- `tests/container/t2-seeded.sh` (new): 27 cells q0..q7 (quota
  exit-3; -b sweep 12-arch + chunk-walk + corners; -t pairs;
  sparse dense/explode/holes; clone no-SLC; HLC+inode+ignore;
  omanifest-IDX chain; seed guard). T2-SEED7 GREEN + T3-SEED8
  GREEN first-hand (no seed overfit; T3 hook proven by shape).
- Adapter: frame-archive --block/--omanifest + frame-cpio-convert
  (oracle-verified; own positional bug caught pre-test).
- Wiring: test_container.sh T2=1 gate (default T0+T1 unchanged);
  README + FIXTURES §9 (closes G4 -b sweep; G4 corruption pairs
  stay open). T0 5/5 + T1 27/27 regression GREEN post-refactor.
- Hashes-not-bytes honored: zero archive bytes committed (code
  only; corpus NVME-linked). Nothing pushed; master untouched.

## Handoff queue update
- (1) T2 code DONE. Next: (2) m/YAF hunt (aa -h verb sweep +
  corrupt-input check-and-fix probes); (3) W/R/T+YAA1; (4)
  lzbitmap chunk-oracle.
