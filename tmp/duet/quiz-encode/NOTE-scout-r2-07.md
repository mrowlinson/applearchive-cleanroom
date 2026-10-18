# NOTE-scout-r2-07: T2 measurements — threads deterministic, sparse mapped

## -t determinism: PARALLEL DETERMINISTIC (measured, 2 cells)
- t1-big (900KB, -a lzfse -b 1k, 880 chunks): -t 18 == -t 1
  byte-identical. t1-twins -a raw: -t 18 == -t 1 identical.
- Pins stay -t 1 (CLI-CONTRACT conservative; determinism proven only
  for these cells, not all codecs/shapes), but relaxation is now an
  option the container lane can take with a full-matrix re-measure.
  T2 -t {1,ncpu} pairs (NOTE-04 §C) start from this positive result.

## Sparse files (100MB-apparent/20K-disk holey.bin, NVME only)
- Archive side is DENSE: -a raw = 104,857,966B (full + 262 framing);
  -a lzfse = 65,844B. Holes are not preserved in the stream.
- Extract default (-no-enable-holes): EXPLODES to ~100MB on disk.
- Extract -enable-holes: 8K on disk, content cmp-identical.
- T2 battery rules: sparse fixtures stay SMALL-apparent (10MB, quota
  guard); assert content-equal on both legs + du-small on holes leg
  + du-big on default leg (the explode is specified behavior, and
  the DoS-shape note from r1 NOTE-02 §B stands: tiny archive -> GBs
  out — impl extract needs the same disk-quota guard as the runner).

## T2 status vs NOTE-04 §C
- DONE measured: -b sweep (b1k..b4m, NOTE-r2-06) + -t pairs + sparse
  (this note). Seeded-corpus GENERATORS (scripts) + clone-dir cells
  + T3 holdout matrix remain for container kickoff (T2/T3 are
  NVME-linked corpora, not pins — no lane commit until then).
