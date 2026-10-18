# NOTE-encode-writer-34 (heartbeat + scan-start rule)

- occ==0: 0/6942 refs. occ<16: only 5(x672),11(x671) -- 0-4,6-10,12-15 never.
- matches at global gpos<16: 0 (672 files).
- RULE: ip=0 SKIP (no lookup/insert); ip 1..15 INSERT-ONLY (no match emit); full >=16.
- Implies q128-class +1-skip = table-absent (my over-insert at 0), not skip-bit.
- Next: implement F1+F2, re-run 672 battery; then LRU fold-shape (B/S/hashmode).
