# A-35 dip selection: offset-pure fragile form + d==1-mod-4 class split (Q-29)

## confirmed first-hand (v4q29, ravbed)
- PH1 dips EXACT: 1077:44B amid 48B; 2469+2470:48B amid 52B (double-dip);
  2817:48B amid 52B; 4209:52B amid 56B. short=tierlen-4 ✓.
- PH2 distinct forms: dip-vs-prev byte-diffs 30/48/17/42/49 (2470-vs-2469
  also differ: 17 — the two dip frames aren't identical either).

## mask rule (the discriminator asked)
- pos 0..N-33: ALL mask, continuous (step4 zones cover everything; no holes).
  outcome by position: +4 (full-tier restore) or +8 (tier jump) — sample 5/5
  mixed at every dip. short form is FRAGILE: any non-tail content destroys it.
- tail d=1..32: transparent at 1077/2469/4209 (0/32 deviate ✓ concurs w2) —
  BUT d≡1 mod 4 (1,5,9,13,17,21,25,29) CLEAN-MASK at 2470+2817 (8/8 -> +4B
  full restore, no jumps). dip class splits on d≡1 response.
- recipe: dev@(N-1) ff masks 2470/2817, transparent at 1077/2469/4209;
  dev@0 ff masks everywhere (mask-or-jump).

## selecting field (constrained, not closed)
- L10-alias ((N<<1|1)&0x3FF, w2s7-11) explains 1077 (L10=107, post-wrap
  small code) but NOT 2469 (843)/2470 (845)/2817 (515)/4209 (227) — no
  common small-code value there. selector below L10 still OPEN.
- constraints from my side: offset-pure (tail-blind except d≡1 class) +
  fragile (content masks, never moves — same shape as A-28 edge) +
  class split (2469 vs its neighbor 2470 differ in d≡1 response: the
  selector couples to 4-periodic tail structure at 2470/2817 only).
- Q-29 CLOSED on discriminator; field-identity stays OPEN for T4 grammar.
