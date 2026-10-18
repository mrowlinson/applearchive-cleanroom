# NOTE-w2s4-18: collision self-fix + predecessor-absorb corrections + VERIFY-15ef0e5 PASS ack

## Collision (my fault, fixed)
- Post-compaction I polled NOTEs via `tail -5` (alpha-sort hid 10-14) and reused
  10/11/12. Pre-existing 10-ravcommit/11-ordertrigger/12-ravenmatch/13-q20/14-rav165
  are my OWN pre-compaction notes (same attempt #4). No second agent; claim HELD, no yield.
- Fix (no shell for mv): title-lines renumbered -> my 10-tailfields=NOTE-15,
  11-modeedge=NOTE-16, 12-shelldown=NOTE-17. Filenames stale; titles rule. Next NOTE=19+.

## Predecessor-absorb corrections to NOTE-17 queue
- MIN-MATCH: already CLOSED <=2 (NOTE-12: L=2..32 repeats free, 2B-period=zero-cost).
  DROP queued min-match bed (redundant).
- X80/Y20 NEED (a): already ANSWERED (NOTE-13: counts 00=84,80=13,00/1=3,01=2,ff=1,81=1).
- MANY-TIE: predecessor bed had UNEQUAL counts (4-6, killed count-primary but not a true
  tie bed). A-21 Q3 discriminator needs 20+ EQUAL counts. Redesign queued (see below).
- Offsets matched D=32..64000 (NOTE-12); D-max beyond 64K still TBD (queue stands).
- Pair-token (0,1,2,3)->48 miss + global-resync (NOTE-12) -> my NOTE-15 tail-field work is
  the direct continuation (bit-level tools as prescribed).

## Acks
- VERIFY-15ef0e5 PASS (additive, wall-clean). 165/165 gated.
- quiz-decode/DONE-writer2 seen: decode-side AEA-decrypt, NOT mine; joint DONE still open.

## Corrected queue (on shell return)
1. clean /tmp/tparse.py; 2. tparse2 run (z64/z128/z821); 3. jointfit run; 4. EQUAL-count
   many-tie bed (design: 20+ keys exactly equal counts via constructed input; stable-rule
   predicts value-ordered ties always, qsort arbitrary-but-deterministic across tie sets);
5. stored-pins (N=1,16,256,4096); 6. D-max probe; 7. L2750 re-bed (A-21 recipe, insha check).
