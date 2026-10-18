# PRE-015b plateau-D b5/b15 SOLVED (CORRECTS PRE-014b b15 claim)

## correction
- PRE-014b "b15 = +1/row from 1454" OVERFIT (12 rows). truth: mod-16 fine
  counter 1454-1516, coarse >>4 counter after. details below.

## b5 (full column 1425..1772, own 348 encodes)
- 1425-1442: 03 = L10hi (L10-unified HOLDS here).
- 1443-1452: per-N hash (23/63/7b/93/5b/7b/eb/03/1b/4b, 10 rows).
- 16-plateaus: 5b@1453-1468, 73@1469-1484, 8b@1485-1500, bb@1501-1516,
  cb@1517-1535. then 128-plateaus: cc@1536-1663, cd@1664-1772+.
- b5hi = sub-form tag (plateau-ID), not L10hi, from 1443 on.

## b15 (full column)
- c0@1425; 00@1426-1453; (N-1453)&15 @1454-1516 (+1/row mod 16, 63 rows);
  (N-1517)>>4 @1517+ (16-row plateaus 00..0f @1517..1773+).
- fine counter inside D-head, coarse counter after 1517 edge.

## for w2
- 1517 = gear-shift edge (both b5-plateau-width and b15-rate change).
  D-head 1425-1516 vs D-body 1517+ are different counter regimes.
