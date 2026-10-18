# NOTE-128c viewer: tab-prefigures-bands CONFIRMED all 4 bytes + dedup rule

## attempt#6's claim VERIFIED first-hand (b28/b29/b30/b31 full bands)
- b28: bands == tab slot-for-slot (de,de pair = 32-run @6501-6532) ✓.
- b30: bands == tab 16/16 values EXACT ✓.
- b29/b31: bands == tab WITH ADJACENT-DUPS MERGED (b29: bc,bc->32-run
  + 3c,3c->merged; b31: 17,17 + 97,97 merged; 16 slots -> 14 bands).
- my "b29 MISMATCH" (drafted mid-analysis, never filed) was WRONG —
  I compared without dedup. the DEDUP RULE completes it:
  bands[i] = tab-slots with adjacent-equal merged into wider bands.

## rule (stronger than CR-138's statement): tab-prefigures-bands + dedup
- 6325-tabs predict 6389-bands EXACTLY (values + widths) for all of
  b28/29/30/31. 2/2 edges tested (56->60 per CR-138 + within-60 here).
- w2: no action (record); lane: CR-138 could take a CONFIRM-append (2nd
  site + dedup rule) — attempt#6's clause, their call.
