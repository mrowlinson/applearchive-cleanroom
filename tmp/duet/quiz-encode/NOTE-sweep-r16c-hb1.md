# NOTE-sweep-r16c-hb1: b199 battery running

- r16c (retry 2): CLAIM-sweep-9d9b10d refreshed. Tree verified
  byte-identical to 9d9b10d (rgramc.c + rgram.py).
- Lane-diff vs writer-merge parent 643d5cd: src/c/rgramc.c
  only +1253/-1094. Wall-grep 0 first-hand.
- Fixed inherit-scan.sh sed leftovers (was self-comparing
  sc197 vs sc197; now f11a1ca/197 vs 9d9b10d/199).
- Full first-hand battery launched (run-battery.sh): ownbuild
  fresh warnings=0; gate-tip running. PYID/C-batt/own-loop
  65897..66152/tables/audits/inherit to follow.
- Quiz diff 0 (Q364/A368, counts match brief baseline; 13-15
  dup + A362-367 renumber are pre-existing naming quirks).
- cport poll: tip ff0c9c2 band200 (even, sweep2 turf); no
  b201+ yet.
