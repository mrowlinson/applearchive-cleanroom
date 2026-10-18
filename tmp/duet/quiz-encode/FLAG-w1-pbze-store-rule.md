# FLAG (prospective HOLD): writer1 pbze commit must use 15/16 store rule

- status: HOLD on writer1's NEXT impl commit touching outer/pbze encode.
  does NOT block 2d1ec2d / 9c955a2 (both PASS, see GATE-*).
- cause: writer NOTE-5 claims store rule "comp<unc else raw". viewer
  NOTE-006 re-verified: rule is compress iff 16*comp <= 15*unc
  (unc=850: comp 796 COMPRESS, 797 STORE — writer rule mispredicts).
- clear condition: pbze impl commit encodes the 15/16 rule + battery
  cells spanning the (15unc/16, unc) window + sweep re-gate green.
- also at that commit: OSS-lzfse byte-exactness (NOTE-5, currently
  trusted-from-writer per NOTE-006) MUST be verified first-hand by
  sweep before merge. writer2's matrix (NOTE-w2-2 "unc==comp" bins)
  is consistent-descriptive, not a rule claim — no hold.
