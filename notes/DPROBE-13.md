# DPROBE-13 TIP2c: PRE-007 unified short rule + M2-clean regimes (C+proto)

## Unification (PRE-007)

- Clean-path short-F DAT-short now runs the presence+content rule with
  (whole, kcut) = (innerlen, nblocks) [nblocks new out-param; raw/empty
  single-piece = 1]. Midchain path unchanged values (mf.whole/kcut).
  Shared block: absent unless present||datcomplete; nch/held/end-gate;
  FULL DAT if complete else min(want, dav) 256K chunks.
- Clean DAT-missing (fsts, C) + clean non-F short (skip, proto) preserved
  with DIVERGENCE-RISK flags (unprobed, pre-existing).

## M2-clean oracle map (own cuts first-hand, WS probe/ + ck* adopted)

- Content modal = held formula on all 11 cuts (M1c/M5c 5ch, M1sc 1ch,
  n12c 3ch, n14c 4ch, n8c/n9c 1ch, n10c 2ch, v512b1 ABS, v512b2 1ch, n1
  ABS). *c cuts (clean outer + short inner) are the PRE-007 shape.
- Multiblock: modal (k ch, 0 tails, count 1) + race legs (k-1 ch + 2
  tails + count 1; phase-dependent). Reduced content = byte-prefix of
  modal (verified 2/2). Tails-2 ⟺ reduced (26 runs, no exception).
- Single-block (nblocks==1): fixed 2 tails + count 2 WITH content
  (M1sc 1ch 4/4 — C pins this, modal 5/6); absent legs race
  {(0t,c1), (2t,c2)} (v512b1 vs m2512k1). Count-bonus model: on
  single-block, tails2 ⟹ count2 (mechanism unknown, bytes pinned).
- want-0: clean → ABSENT (no file, v512b1); midchain → EMPTY file kept
  (cxA/E/F pinned). Path-dependent, data-backed both sides.

## Race hardening (battery)

- runcx (midchain): race-SET (C pinned k; oracle k or k-1/prefix; want-0
  oracle may be ABSENT). cxC flake was oracle-side (262144 tails-leg).
- m2clean cell (self-gen, 8 cuts × 7 = 56 asserts): deterministic src
  (seeded), C modal pinned + mirror + tree-lock + big1 + numeric oshape
  SET (single count-bonus legs + multiblock correlated legs).
- g9/g9P: 5th outcome both-succeed (rc0 silent, full tree) — FIRST
  sighting this battery (pooled was 0/65; closes viewer quadrant hunt).
- Harness: bare `$(grep -c)` with 0 matches kills sh -eu (silent death);
  hardened with `|| true` (matches existing idiom).

## Stack (TIP2c): 528/528 GREEN x3 + smoke + asan13 + trunc130 + flip200
## + cvp150, 0 warnings.
