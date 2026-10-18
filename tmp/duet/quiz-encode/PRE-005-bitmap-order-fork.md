# PRE-005 bitmap ORDER: B-rule derived EXACT, A-rule = ASC, fork still open (Q-18 follow-up)

## B-rule: DERIVED, exact-fit (hand-traced 12/12)
- rule: slot0 = 00 PINNED; slots1-11 = insertion-sort by count-DESC with `<=` (later displaces;
  ties resolve value-DESC) over candidates arriving (value,pbc)-ASC.
- trace on B's counts reproduces [00,ff,fe,fb,f7,ef,df,fd,7f,ef/1,ee,bf] EXACTLY (all 12 slots).
- predicts: ties always value-DESC; 00 never moves; ff placement = pure count rank.

## A-rule: value-ASC (fits 100%, count-blind)
- [00,7f,bf,df,ef,f7,fb,fd,fe,ff] + pads; ff(969) LAST. No count-sort emits this (insertion sort
  ALWAYS count-orders regardless of arrival; verified by trace). X80/Y20 bed confirms count-blindness
  in few-keys regime (01-count4 before 80-count80).

## fork trigger: STILL UNKNOWN (two theories DIED)
- fullness/pressure (v1): DEAD — 3000-ASC is FULL 12/12 while 2750-SCR has a pad (inverted!).
  (Unobservable distinct-count version survives only as untestable; needs w2 op-counts.)
- pbc-mixing: DEAD — B's pbc0 subsequence itself is non-ASC (interleaving theory requires ASC core).
- size-neutrality PROVEN: ratios across flop series exactly on-trend (0.740→0.851 smooth, no jumps
  at 2750/3250 flips). Order costs NOTHING → pure construction-process artifact. The process forks;
  economics don't. (Kills any "order optimizes size" theory incl. nibble-cost assignment.)

## standing data for the fork hunt
- A-regime: value-ASC + odd/pbc-tail appended (39/40 survey); order-insensitive (swap/move-invariant).
- B-regime: count-DESC-<= (B + 3500/3750/4000-series?); order-SENSITIVE (R47+P ≠ P+R47).
- ff-fate pattern holds (ASC⟺ff-last; SCR⟺ff-first-or-absent) — now reads as COROLLARY (ff placement
  follows whichever rule is active), not trigger.
- next discriminators queued: (i) w2 op-counts for X80/Y20 + 2750/3000 (A-19 NEED stands);
  (ii) arrival-order probe: SAME multiset, microscopically different GROUP order (rotate by 8B!) —
  ASC-arrival theory predicts IDENTICAL tables (arrival = value scan, order-free); any flip kills it.
