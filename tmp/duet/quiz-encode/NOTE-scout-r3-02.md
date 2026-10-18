# NOTE-scout-r3-02: APFS sparse threshold (16,20]MB — T2 sparse default stands

## Measurement (APFS, macOS 27.0.1, internal + NVME agree)
- `mkfile -n` (ftruncate) apparent -> du: 10M->10M, 16M->16M,
  20M->16K, 24M->16K, 32M..1G->16K. Python seek-write agrees:
  10M->10M dense, 32M->32K sparse. Threshold in (16,20]MB, both
  methods, both volumes. Small files are EAGERLY allocated here.
- r2's 100MB-apparent/20K-disk vector sits above threshold —
  consistent, no contradiction.

## T2 consequences
- t2-gen.py `--sparse-mb 10` default STANDS: a dense 10MB input is
  harmless (10MB disk; archive bytes identical either way since
  content is what aa reads). The q3 legs assert aa behaviors
  (archive-dense, default-extract explodes, -enable-holes stays
  small, content-equal) — none depend on INPUT sparseness.
- Runner asserts NO filesystem allocation behavior (FS tuning may
  move by OS); only aa in/out bytes + du of aa's OWN outputs.
- Note for container lane: if a future vector needs a truly-holely
  INPUT (e.g. copy-perf legs), apparent must exceed 20MB on this OS.
