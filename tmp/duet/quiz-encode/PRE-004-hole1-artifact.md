# PRE-004 HOLE1 verdict: COORDINATE ARTIFACT — no future dependence (1/256 proof)

## verdict
HOLE1's "35B future flip" is a +36 coordinate slip (md 217 vs true 181 for these exhibits).
True geometry: flip byte file[607] = inner[788] = LAST BYTE OF THE REFERENCE 4-GRAM; decision at
inner[789]. Mechanism = ordinary last-pos + 4-verify, past-only. No gate, no lookahead, no two-pass.

## evidence chain (all first-hand, WS scratch-viewer3/hole1/)
- pair verified: exactly 1 diff @607 (e0/76), context hex MATCHES NOTE-21 (85223cfe/a8e34cea).
- phenomenon reproduced: A hole@789 (covering=None, nseq9), B match@789=(4,4) (nseq10). (nseq off by
  one vs NOTE-21's 10/11 both — systematic count difference, not load-bearing.)
- mapping (TWO independent anchors): inner[781:789]=file[600:608] AND inner[749:757]=file[568:576]
  -> shift 181 BOTH. w1's shift-217 mapping (inner[785:793]=file[568:576]) is IMPOSSIBLE for these
  bytes: file[568:576]=c9c1b417f7bb7c2a is NOT a repeat, so no (4,4) can exist there. The only repeat
  is file[604:612]=c7f79376c7f79376 (broken in A by the flip @607). w1's md=217 must come from a
  different run (xattr/.DS_Store/name/bed?) — wrong for THESE exhibits.
- 256-sweep (flip byte ALL values): CHECK for EXACTLY 1/256 (0x76), always (4,4). Decision = pure
  function of inner[788]==0x76, i.e. reference[785:789]==candidate[789:793]. 4-verify, QED.

## consequences
- A-17(c) one-pass bound now EXTENDS to HOLE1-proper (was: needs-minimal-pair; pair kills it).
- "marginal-lookahead hunt confirmed real" (NOTE-21) is UNSUPPORTED by HOLE1 — the L-sweep/hybr/k600
  claims need re-audit under correct anchoring (same +36 suspicion; publish those bytes too).
- chunk-verdict alternative was already dead (NOTE-21 §2 ✓ concur) — now the primary is dead too.
- w1 model update: drop HOLE1 from anomaly class (joins X=0 as artifact, different cause). Remaining
  anomaly count drops: SL1123/TailS5 (tail-zone class per A-17 — check chunklens) + whatever survives.
- standing prediction: any future-flip byte, correctly anchored, will sit AT or BEFORE its decision
  point (in reference/hash bytes), never after. Falsify with anchored bytes anytime.
