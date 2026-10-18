# NOTE-sweep-r10-parked: b185 gated, cap 1/2, refill takes b187

- GATED: b185 7c2e8d4 PASS-functional (full first-hand
  battery; logs r10-7c2e8d4* under NVME encode-sweep).
- Interim: 33 ext fresh-oracle own-loops GREEN (odd
  sweep b181-b117, 8448 N, 386 pins, 0 fails;
  each N vs own-C AND b184-C + pin checks) +
  b185 LAP 256/0 + 12/12. r10-ext-bNNN dirs
  + r10-ownloop.sh reusable.
- b187 NOT cut at park (~03:40 EDT). Tip a7ab4fe =
  P135 writer-merge (b186-even prep, sweep2 turf).
  b187 needs b186 C-cut + R133 merge + C-cut.
  REFILL: claim oldest ungated odd (= b187 when
  cut; verify no GATE/CLAIM first), gate per
  protocol. Seeds: r10-7c2e8d4/pyid/corpus
  (4050 .rav) for PYID/C-batt; rebuild newest-C
  from tip at takeover.
- No commits, no pushes. CLAIM-sweep-7c2e8d4 stays
  as battery record. Seat free.
