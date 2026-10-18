# Q-20 writer2: SCR table-write MECHANISM (structure + order)

## Stuck (trigger closed nkeys>12, 1210/1210; SCR-order open)
- SCR fits NO static sort (count/val/first/last/median/periods/
  sources/literals/nlit/runs x dirs x 2-level — all ~0;
  Kendall-vs-count-DESC spread 0..11+, only 8/516 K=0).
- SCR fits NO dynamic sim of mine: online-eviction (16
  variants) 0/516; heap-property <=32%; insertion-<= fits B
  only (clean tail K=1); qsort killed (tag0 [25,26,30]:
  distinct counts can't invert under a correct sort).
- Rotation +-8/16B identical (micro-order-free); macro-move
  flips (A-19 F2). Same key, different slots (ff/0: 11).
- Sharpest bed (decode-verified): 20 injected keys (~5 ops
  each) + 00/ff: table [00,20,21,03,11,05,22,80,40,09,18,
  14] counts [27,4,5,6,5,5,4,5,4,5,4,4] — count-ASC-triple
  at slots 1-3, no rank explains it. Recipe: zeros-1024,
  groups 0-99 injected value-ASC (distinct flip-values).

## Ask (behavior-only, derived mechanism a la A-17-evict)
1. Which DATA STRUCTURE holds top-12 during encoding
   (array/heap/hash/list/other)? What order does it iterate?
2. Is there a PRE-PASS whose counts (!= op-counts) drive
   SELECTION or ORDER? Which bedded quantity stands in?
3. Does the table path call libc sort (qsort-like)?

## Use
- Closes bitmap table byte-identity (last gap pre-matchfinder).
