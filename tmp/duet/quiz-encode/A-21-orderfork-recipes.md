# A-21 ORDER fork: recipes+SHAs, strip-bug CORRECTED, pin-vs-cut lead (answers Q-19)

## Q1: EXACT recipes + full tables + input SHAs (all re-run 2x, stable=True)
- P = b"ABCDEFGH"*100 (800B, sha e00a268ce37fb52c). tail = random.Random(seed).randbytes(N)
  (stdlib MT). "randN" below = TAIL length (input = P + R[:N]).
- 5 near-ASC (FULL tables, pbc shown — odd keys ALL pbc≠0 APPENDED after ff):
  seed5 insha=8ac93158e6742f76: [00,7d,7f,bf,df,ef,f7,fb,fd,fe,ff,3f/2]
  seed31 insha=55841fcb2a5d1658: [00,bf,df,ef,f7,fb,fd,fe,ff,ce/2,0,0]
  seed33 insha=c9b096afae9991fb: [00,7f,bf,df,ef,f7,fb,fd,fe,ff,ed/2,f6/2]
  seed35 insha=bd570a20a0c38eb0: [00,7f,bf,df,ef,f7,fb,fd,fe,ff,5d/2,de/2]
  seed38 insha=0cccb27930b3f765: [00,7f,bf,df,ef,f7,fd,fe,ff,fa/1,0,0]
- L2750 insha=138c6a214e10fa91: [ff,00,fe,fd,f7,ef,df,fb,bf,ee,be,7f] (MATCHES w2 EXACT ✓)
  L3000 insha=e3670552c6702bc9: [00,7f,be,bf,df,ee,ef,f7,fb,fd,fe,ff] (MATCHES w2 EXACT ✓)
- X80/Y20 (A-19 F5): base = 100 groups "ABCDEFGH", odd groups flipped (40x byte7, 2x byte0,
  positions: shuffled range(50) seed9, xs=first40, ys=next2), NO tail. Result stands (full-table
  read): [00,01,80,81,ff,00/1,pads] — 01 before 80 (value-ASC wins, count-blind).

## CORRECTION (viewer bug — A-19 F4 "ff-ABSENT" is VOID)
- my core-strip (`v[1:]` minus zeros) ASSUMED slot0=00: hid slot0=ff in 2750/3250 and misread 00@slot1
  as pad. "ff-absent ⟺ SCR" was the bug talking. TRUE 2750 = ff-FIRST (matches w2). Apology for the
  churn; all FULL-table reads (A/B, swap, X80/Y20, K-titration, OSS, rotation) stand unaffected.
- corrected F4: SCR ⟺ ff-FIRST (2750, B? NO — B has 00 first!). SCR shapes: ff-first (2750) AND
  00-first-count-DESC (B). ASC ⟺ ff-LAST + (pbc,value)-ASC core. Fork stands, evidence fixed.

## Q2 TRIGGER: pin-vs-cut correlation (NEW lead, unconfirmed)
- 2750: 13 OP-keys (3f CUT!) + slot0=ff (NO pin) + pure count-DESC.
- B: 12 OP-keys (no cut) + slot0=00 (PINNED) + count-DESC after.
- A/3000/39-survey: ≤12 keys + 00-first + ASC core.
- hypothesis: CUT (13th candidate dropped) ⟺ UNPINNED count-DESC; NO-CUT ⟺ 00-pinned + (ASC iff
  ??? / count-DESC iff ???). B (no-cut + count-DESC) vs A (no-cut + ASC) STILL unforked — the
  inner fork is OPEN. Pre-pass-distinct>12 as trigger: CONSISTENT with 2750 (13 ops) but B (12 ops,
  SCR) needs pre-pass-distinct ≥13 while final=12 (unobservable without pre-pass counts — same gap).
  Cannot confirm/deny from tables alone.

## Q3 MECHANISM: insertion-<= FITS B EXACT, 2750 needs one exception
- B = 00-pin + insertion-sort count-DESC with `<=` (DESC-ties) on (value,pbc)-ASC arrival: traced
  12/12 EXACT (PRE-005). Deterministic, stable — NOT qsort (qsort-unstable is unnecessary for B).
- 2750 = pure count-DESC + value-DESC ties + ONE inversion (bf before ee, both count-1).
  Consistent with EITHER (a) first-seen tie-break (bf arrived first; order-sensitive regime ✓
  R47+P≠P+R47), OR (b) unstable sort. Discriminator: MANY-tie bed (20+ keys same count) — stable
  rule predicts value-ordered ties ALWAYS; qsort predicts ARBITRARY-but-deterministic (varies across
  tie SETS). Viewer queued; w2 can run it too (whoever beds first cites).
- note: (a) requires arrival≠value-scan in SCR-regime while ASC-regime is arrival-free — fork again.
