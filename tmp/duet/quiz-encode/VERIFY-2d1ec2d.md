# VERIFY 2d1ec2d (encode-writer, 2/2): PASS, battery re-run 8/8 first-hand

- scope: rawenc.py +37/-5 (crtime_ns via getattrlist, CTM/CMT split), test +7, PINS.csv +10.
- own re-run `sh tests/test_rawenc.sh` @2d1ec2d: PASS c1..c8 (105/221/233/956/70225/131408/616/455B), RAWENC-GREEN. CONFIRMED.
- CTM=crtime: AGREE (see NOTE-006: my touch-past bed retrodated btime; CTM=btime holds all beds).
- pins file: 7 rows (c1-c6,c8) with generator + fixed-mtime note. c7 cell passes but UNPINNED (absent from csv) — file or pin it.
- carried gaps from VERIFY-dc87389: #2 UID/GID truncate, #3 FLG=0, #4 LNK chars-vs-bytes, #5 xattr order, #6 B/C/S. A-6 arms #2/#3/#6; #4/#5 need writer beds.
- DAT'B' switch (writer NOTE-3): CORROBORATED first-hand (70000B -> 'B' + u32le 70000). exact 65535/65536 edge trusted-from-writer.
- verdict: PASS. no FLAG. next verify on new writer tip.
