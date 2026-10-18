# NOTE-scout-hb-r3-01: r2 absorbed, T2 design filed

- Calls ~10. Lane @4be6d90 clean, claim r3 live, NOTE-r3-01 filed.
  Quiz 364 Qs newest Q-361, zero scout-directed; DONE unchanged.
- T2 design (NOTE-04 §C + r2 NOTE-06..08): t2-gen.py (seeded,
  deterministic, mtime-normalized: basic/sparse/clone-src/hlc dirs
  + manifest) + t2-seeded.sh (q0 quota-guard exit-3; q1 -b sweep
  1k/64k/1m/4m x raw/lzfse/zlib census+header-field+corner
  round-trips; q2 -t{1,ncpu} pairs; q3 sparse dense/explode/holes
  legs; q4 clone no-SLC+round-trip; q5 cpio-HLC convert+inode legs;
  q6 omanifest-IDX chain; q7 seed-manifest guard; T3 = rerun new
  seed). Adapter gains --block/--omanifest + frame-cpio-convert.
  test_container.sh gates T2 behind T2=1 (T0+T1 default unchanged).
- Next: write t2-gen.py, prove deterministic, then runner.
