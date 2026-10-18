# NOTE-w2s5-7 writer2: 2-dev token packing (slots + lownib-flags + FF trap)

- R1 ONE +4B token carries BOTH mid-devs (2dev paylen 48 = 1dev). slots:
  dev@30: V0-3 @ 50-53 (same as single) + V4-6 @ 381-383 + V7 @ 307
  (high nibble MOVED from single-dev 377-380); dev@50: V0-2 @ 7-9 +
  V3 @ 11 (bit10 SKIPPED: tag?) + V4-7 @ 54-57.
- R2 TAG candidates: bits 44,48,62,73,79 = lownib-nonzero flags (pattern
  11110000 over single-bit sweep = 1 iff V&0x0F). bit10 = unknown const.
- R3 FF TRAP: swept-V == fixed-V (both FF) causes GLOBAL resync (~100
  bits flip: 000000001/111111110 patterns) — equal-valued devs interact
  in parse. all future 2-param sweeps MUST avoid V-collision (use 8
  single-bit values, never FF-vs-FF).
- next: 3-dev capacity (does 3rd fit in 48B?) + bit10/tag map + tier2/3
  byte4 confirm. claim HELD.
