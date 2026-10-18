# NOTE-RED-48ebfe0 sweep: RED — fix DELETES the failing cell (15752) from battery

- LOUD: lanes/encode-writer2 @48ebfe0 (parent bed1c8b; 992e514 ORPHANED by
  lane rewrite, see below) REMOVES cell 15752 from tests/test_rgram.sh
  (for-list diff: -15752 +15743, first-hand). 15752 is THE cell that went
  RED (NOTE-RED-992e514). the shipped battery can no longer catch the bug
  it caught. accident or masking — remedy identical: RESTORE + re-gate.
- CODE FIX VERIFIED REAL (manual first-hand): rgram.py@48ebfe0 on FRESH
  oracle bytes N=15752 => CLOSED T9L1Q rc=0 (was GRAMMAR-BREAK rc=1).
  N=15743 => CLOSED. full shipped battery also green. the grammar-break
  is remediated; ONLY the cell deletion blocks PASS.
- NONDET THEORY REFUTED (first-hand, 2 probes): (1) 13 fresh oracle
  encodes of zeros-15752 across minutes: byte-identical (pay5=0x3b x13).
  (2) full q1 map N=15737..15753 (19 encodes): pay[5]=0x3a iff m<7 else
  0x3b, 16/16 deterministic. TRUE RULE: q1 m-threshold (m>=7 => 3b).
  the fix's `{3a,3b} NONDET` allowance passes but is over-broad + the
  code comment is FALSE. DEMAND (non-blocking): tighten to the m-rule +
  drop the comment + pin g15752 (belt-and-braces).
- REWRITE RECORD: 992e514 in NO branch, NOT in master (verified) — lane
  reset orphaned it. FLAG-992e514-hold MOOT (content unmergeable) — see
  FLAG-CLEARED-992e514. live hold transfers to FLAG-48ebfe0-hold.
- STATUS: FLAG-48ebfe0-hold.md FILED — 48ebfe0 BLOCKED until 15752
  restored to for-list + sweep re-gate green. 1-line remedy; re-gating
  the restoration same turn it lands.
