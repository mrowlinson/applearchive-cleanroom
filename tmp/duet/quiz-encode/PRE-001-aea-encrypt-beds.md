# PRE-001 AEA-encrypt behavior beds (unowned turf; writer2 granted, no Q yet)

## Header (profile 1 + 5, -a none, 5KB urandom input)
- @0: `41 45 41 31` (AEA1) | @4: profile LE u32 (01/05) | @8: 4 zero bytes | @12+: random.
- first 12B STABLE across reruns; bytes differ from char 13 (re-run cmp). CONFIRMS fixtures verdict.
- p1/p5 same input: SAME size 24576. profile changes bytes @4 + crypto, not size (this input).

## Size map (profile 1, defaults, -a none; input N -> output)
- 0->160 | 1->19456 | 100->19456 | 1000->20480 | 5000->24576 | 16384->36864 | 1000000->1032192.
- n=0: 160B minimal envelope (headers/auth only, no data clusters).
- quantization: 1B and 100B identical 19456 (segment minimums/padding). step structure OPEN.

## Padding / checksum size effects (5KB input, profile 1)
- default: 24576. -padding none: 23620 (-956). -padding adaptive: 24576 (= default -> default IS adaptive here).
- -checksum none: 15872 (-8704 vs default!). -checksum sha256: 24576 (= default size; default checksum mode OPEN).
- checksum mode massively changes size (8.7KB/5KB!) — structure (per-seg MACs? resegment?) OPEN, decode-adjacent.

## Roundtrip + id
- decrypt -key <file> roundtrip cmp-clean (DECRYPT-RT-OK). `-key <file>` works; bare-hex -key-value rejected (fixtures gotcha stands).
- `aea id -i`: prints single 64-hex line (archive id hash?) + exit 0. semantics OPEN.

## Repro
- beds: WS tmp/q6probe.FT9V0Q/aea/ (p1/p5/s*.pad/cks*). key = bytes 0x00..0x1F test file (NOT committed; fixtures testkey differs).
- OPEN for AEA-encode impl: cluster/segment layout bytes, seg-alg IDs on encode, -b effects, profile 0/2/3/4 (need keys/certs),
  15/16-like store rule?, padding quanta, id-hash preimage. file Q per item when turf activates.
