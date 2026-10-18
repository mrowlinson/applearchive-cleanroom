# NOTE-scout-r2-03: container battery past T0 (4be6d90)

## Landed (lanes/encode-container, LOCAL ONLY)
- 3fd9f68: frame-archive adapter verb + t1-pinned.sh (27 cells) +
  treecmp.py helper + test_container.sh T0+T1 wiring + README.
- 4be6d90: T0 c3/c4 scoped at input/hello (my T1 dirs broke r1's
  whole-input-dir diff — caught by fresh-clone proof, fixed same run).

## Proof (fresh `git clone` of the lane to NVME = true checkout: no
xattrs, no empty dirs — the state git actually preserves)
- T0-CONTAINER GREEN 5/5 + T1-CONTAINER GREEN 27/27 first-hand vs
  oracle (macOS 27.0.1, -t 1). No flakes across 3 full runs.
- T1 cells: p0 drift gate (aborts) / p1 regen byte-cmp x11 (6 raw +
  slc + lzfse + manifest + append + convert) / p2 census (counts +
  TYP multisets + LNK map) / p3 list-json golden / p4 SLC legs /
  p5 round-trips x10 (incl -enable-dedup + xattr-value legs) /
  p6 manifest shape / p7 convert-differs guard.

## Design points for container lane
- Round-trip expects use the recipe-prepared tree, never checkout
  bytes (git drops xattrs + empty dirs). p2's LNK-map assertion
  closes the symlink-target bit-rot gap (SHA256SUMS covers files
  only). treecmp.py replaces diff -r (dangling links + dir loops).
- cpio/HLC, -omanifest, YAA1, W/R/T still open (r1 NOTE-07/08 list
  stands; h-trigger hunt is next in this run's survey leg).

## Next
- Survey threads: TYP h-trigger hunt, Apple-404 re-verify,
  compression_tool framing probes. Then T2 seeded-corpus legs.
