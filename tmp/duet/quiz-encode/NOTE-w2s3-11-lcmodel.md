# NOTE-w2s3-11 writer2: lc = optimal-parse + tie-to-set (4+2 cells)

- decoder (own zbm-dec.py) EXACT on all beds (lc+OSS) —
  format understanding proven; op traces authoritative.
- matchfinder core (lc-0x702 one-shot, DETERMINISTIC 2/2):
  B0@file-offset-0 INVISIBLE to new-period search (diffs-0
  matches rejected; D=8 works via current-period path);
  visible search = min-diffs, ties->earliest-source.
- economics = OPTIMAL-PARSE (global, future-dependent):
  C1/C2 future-swap PROVES future matters; zeros+R cells:
  strict-wins keep (L>=16 repeat, C1, C2, inv), exact-ties
  SET early (zeros-128, aa-ocean TIE2: ff/1/D-8). tie-break
  = toward-SET (2 instances). poison windows (B0-copy kills
  period-8 for g17) force the switch timing.
- open: tie-break exact shape, top-12 rule, rep scheme,
  uncomp fallback threshold, chunking, initial bitmap.
- next: g0-forced? + fallback threshold + top-12 beds.
