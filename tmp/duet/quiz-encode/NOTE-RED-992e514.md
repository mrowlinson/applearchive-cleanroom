# NOTE-RED-992e514 sweep: RED — RGRAM FAIL g15752 (T9L1Q blk, pay[5] 0x3b vs 0x3a)

- LOUD: lanes/encode-writer2 @992e514 FAILS its own battery. RGRAM-RED on
  cell g15752 (N=15752, L1Q m15/q1): `GRAMMAR-BREAK T9L1Q blk`, rc=1,
  reproduced first-hand deterministic (oracle re-encode byte-identical —
  NOT a flake, NOT oracle drift).
- ROOT CAUSE (first-hand, byte-exact): blk position 2 = pay[5]. actual
  0x3b vs QB[1][2] 0x3a; all other 11 blk bytes match. m15-row pay[5]:
  q0->0x3a (N=15736 PASS), q1->0x3b (N=15752 FAIL), q2->0x3b (N=15768
  PASS, QB[2][2] already 0x3b). ONLY (m15,q1) diverges => unmodeled m15
  edge at q1 (NOT a QB[1] typo — m0 row N=15737 passes with 0x3a). L1Q
  blk check is direct QB[q] with no m15 handling (cf k15-carry/edge logic
  in other Q branches). WRITER FIX REQUIRED (writer territory).
- ESCAPE ANALYSIS: g15752 is UNPINNED (0 csv rows) — pins set-eq passed
  2086/2086 alongside the FAIL. full-cell battery caught what sparse pins
  missed. vindicates full-battery gating (pins-only would have shipped it).
- SECONDARY NIT: message "(2090 pins)" overstates by 2 even beyond the
  2 comment lines (data 2086, total 2088). sloppy count; battery decisive.
- STATUS: FLAG-992e514-hold.md FILED — 992e514 BLOCKED from merge until
  fix + sweep re-gate. coverage: 142 PASS + 1 RED-held. re-gating the fix
  same turn it lands.
