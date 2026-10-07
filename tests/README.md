# tests

Harness notes live here. Black-box oracles: local `aa` / `aea`.

Batteries (all: exit 0 green / 1 FAIL / 2 harness error; work in WS):
- c-battery.sh — C deliverable vs oracle, 53 cells (fixtures,
  attrtree, wide, multiblock, hardlink, specials, hlink-path,
  device-fail, errors, trunc-sweep, no-typ, xattr-order, adler).
- smoke.sh — T0 encode/decode roundtrip smoke.
- flip-fuzz.sh — oracle-vs-C, 200 seeded flips (seed 49420).
- c-vs-proto.sh — C-vs-proto, 150 seeded flips (seed 40608).
- raw-trunc.sh — truncation sweep, 130 pts, no crash/signal.
- asan.sh — ASan/UBSan build, 13 fixtures, exit parity.
- fuzz.py — seeded driver behind flip-fuzz/c-vs-proto (see its
  docstring for the bar + DIVERGENCE class; DPROBE-05).
