# NOTE-42 writer1s3 (rescan shipped 7f80ea0 488; chunk-start parked)

- COMMIT 7f80ea0: chunk-start tail rescan (miss-only,
  [gpos-8,gpos-5] nearest-first). 488/672 (+1/-0:
  bis/131072 fixed). LZ4-GREEN + UNITS-GREEN.
- CHUNK-START WAR (parked, ~30 calls, net +1): K-pending /
  tailroom / ktail / tail-override ALL lose (-25..-29);
  miss-only stands. OPEN: bis/200000-c3 (MS+8-at-IP0 needed
  (131080) but C1-MS+8 (65544) poisons same-chunk (spurious
  phase-0 hits); pending-MS+8 circular (C2-rescan-vs-65544)).
  smells emergent (window/expiry/density), not rule. Q-32
  candidate later (chunk-index-1v2 split).
- PIVOT (cheaper): LEN 10!=9 x42 (late over-match, likely
  one rule) -> EXT-shorter x8 (C-refine) -> POS-early x13
  (lookup gate) -> POS-late-tablegap (psw/ttail).
- Q-30 (collisions) + Q-31 (mod5 mechanism) still open.
