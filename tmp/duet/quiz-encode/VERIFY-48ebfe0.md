# VERIFY-48ebfe0: PASS + FLAG (w2 T9L1+L1Q re-land, 15752 fixed)

- commit: lanes/encode-writer2 @48ebfe0
  (child of 992e514; re-lands T9L1+L1Q;
  rgram.py +138, PINS +40 rows).
- at-commit tree: RGRAM-GREEN + SMOKE-GREEN.
- 15752 fix REAL (direct probe, not battery
  inference): rgram.py @48ebfe0 returns
  `CLOSED T9L1Q N=15752 off=31` rc=0 (was
  `GRAMMAR-BREAK T9L1Q blk` rc=1 @992e514).
- independent vendor sha: 15693 9924e9d1…
  == pin; 15784 a1101227… == pin. MATCH.
- FLAG (coverage, not correctness): GCELL
  loop swapped 15752 -> 15743 (`15736 15737
  15743 15753`); the fixed cell has NO pin
  rows and is untested by the battery.
  recommend re-adding 15752 as regression
  pin. vendor sha for the record: 15752 =
  bed9ad929f8448e9… (full .rav, ct-lzraven).
- verdict: PASS. VERIFY 52/53 (992e514 FAIL
  superseded by fix).
