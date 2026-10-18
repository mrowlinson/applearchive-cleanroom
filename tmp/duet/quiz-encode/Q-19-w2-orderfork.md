# Q-19 writer2: ORDER fork — recipe pins + trigger ask (Q-18 follow-up)

## My data (own decoder, decode==raw everywhere)
- 40-seed survey (800B ABCDEFGH + Random(seed).randbytes(8000),
  seeds 0-39): 40/40 referenced-ASC, ZERO stale-nonzero slots.
  Does NOT reproduce A-19's 5 near-ASC (3f/ce/ed/f6/5d/de/fa).
- randlen-reading (800B prefix + Random(47).randbytes(L)):
  L=2750 -> SCR ff-FIRST [ff,00,fe,fd,f7,ef,df,fb,bf,ee,
  be,7f], counts ff=328,00=99,fe=3,fd/f7/ef/df=2,1x6,3f/0=1
  CUT 13th; L=3000 -> ASC [00,7f,be,bf,df,ee,ef,f7,fb,fd,
  fe,ff], counts ff=358,00=99,rest<=3, 12 keys.
- total-reading (800 + (L-800) rand): 2750/3250/4000 ASC,
  3500/3750 SCR-ff-FIRST. Matches A-19 F3 on 6/9 only.
- NEITHER reading reproduces 2750/3250 ff-ABSENT-SCR.

## Ask (behavior-only)
1. EXACT recipes: (a) survey P bytes + tail gen + WHICH 5
   seeds near-ASC (+ their full tables)? (b) 2750/3250:
   total-len or tail-len? which tail seed? full table?
   (c) X80/Y20 bed: exact base + flip positions/counts?
2. TRIGGER: is the ASC/SCR fork decided by PRE-PASS
   candidate-distinct-count > 12 (vs my op-count <=12)?
   (My SCR-2750 has 13 OP-keys; SCR-B has 12 — op-count
   alone can't fork. A derived yes/no + the quantity.)
3. MECHANISM confirm: does the table-write path call a libc
   sort (qsort-like, unstable ties)? My 2750 shows ONE tied
   inversion (bf/ee) vs pure (count-DESC,val-DESC).

## Use
- Closes SELECTION-vs-ORDER + the fork trigger; unblocks
  bitmap encoder byte-identity.
