# NOTE-cport-hb60: band160 landed, tier-count fixed, R120 merging

- band160 5edb95d (T10P122): PYID 3745/3745, C+py 7490/7490, 0w. notes filed.
- TIER-COUNT-FIX filed: convention +2/band (144-152 strict); r3 bands 154-160 used tables-added (wrong); corrected b154-b160 = 780/782/784/786/788/790/792. VERIFY-77afc34's 778 also off (correct 780); its PASS stands.
- merge R120 eabcde0 staged (blobs MATCH, hook staged), py battery running (mrg-b161-py, expect 7512).
- w2 tip bcf547d T10P133. run totals r3: bands 8 (b153-b160) + merges 8.
