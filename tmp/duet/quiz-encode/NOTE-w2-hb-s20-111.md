# NOTE-w2-hb-s20-111 — P256 ANALYZER GREEN
bump-20
- P256 CENSUS: 105825..106172 348 cells missing 0 RC=0
- ANALYZER: GREEN P256 348/348 (M-tails novelty in log)
- sigs: PB0 641a0300 NEW/PB1 e58c3506 NEW/PBA a0802f7c x16/C10-2SIG 3506x4+1503x3+3506x3 sandwich/QUADms 7cx32+3cx32 pair-led 1B-off/T88 06000000 x256(==P252/253T)
- PBA: M10 b14,15,21-23,31,76-79 V11 C73 b5-const 3a
- C10-2SIG 4+3+3: M14 b2,3,22,23,30-35,80-83 V15 C69 b5-const 3a
- QUADms: QM7 b36-38,76-79; R10 b3,15,22,23,30-35 r0==r1 PAIRED (r2/r3 1B-off 04-vs-08); tails 4/4 (r0/r1 sha 299170); b5-carry 3a->3b @105855->105856 (early edge); V23 C61
- T88: STANDARD M7 b39,46,47,80-83 cols / R7 b40-42,76-79 rows 16/16; b5 3b+steps[67,195]; V16 C72
- NEXT: stage p256-patch -> try-p256 -> sweep 348/348 -> Q-320
