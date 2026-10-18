# GATE-12c4bdc (encode-writer2 tip): PASS, matrix 72/72 first-hand

- scope: 3 harness docs + 3 probe scripts + RESULTS.txt (82-cell
  outer matrix). no impl, no pins, no new OSS (PARENT-003 clean).
- docs: 3/3 full-sha MATCH lanes/harness-oracle (e887afb3...,
  8c6d8073..., 269b3d3c...) + A-1/A-8 pins. contam grep 0. no pyc.
- matrix re-run first-hand (sh probe-outer.sh $WS/out): deterministic
  72/72 EXACT (size+magic16+sha16; incl -b16 400459 / -b20 360427 /
  -t4 EQ). probes are clean black-box (execute + observe + byte
  parse only; read all 3 first-hand).
- minor (non-blocking): "fixed seed via openssl" comment FALSE —
  openssl rand = fresh entropy; r-cell shas single-run (proven:
  fresh r1000-raw sha16 2b54d329 != committed e7a3b1c6; sizes stable).
  fix comment or seed via python random. recommend provenance header
  in RESULTS.txt (generator + seed policy).
- verdict: PASS. no FLAG.
