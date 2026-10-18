# A-19 bitmap table ORDER: INTERIM — ASC-norm + ff-fate pattern + control method (rule OPEN)

## validated apparatus (own, lc-0x702 oracle + trailing-17B 10bLE extractor)
- reproduces w2's A-table EXACT ([00,7f,bf,df,ef,f7,fb,fd,fe,ff]+2pads) and B-table EXACT
  ([00,ff,fe,fb,f7,ef,df,fd,7f,ef/1,ee,bf]). single-chunk verified by chunk-walk.
- bit semantics confirmed by counts: bit=1=LITERAL (ff≈965 = random groups; 00≈99 = prefix groups).

## F1: ASC is the NORM (35/40 seeds), scramble is rare/content-specific
- 40-seed survey (same P+rand8000 recipe): 35 pure-ASC cores; 5 near-ASC (ASC + 1-2 odd keys
  APPENDED: 3f/ce/ed+f6/5d+de/fa). Full scramble (B-shape) NOT seen in seeds 0-39 (only seed47).
- odd-tail keys sit AFTER ff (need pbc data — see request).

## F2: order-insensitivity is REGIME-DEPENDENT (new)
- seed7-regime: swap-halves table-IDENTICAL (12/12); prefix-move (R+P) IDENTICAL. order-insensitive ✓.
- seed47-regime: prefix-move CHANGES table (R47+P ≠ P+R47, keys AND slots differ). order-SENSITIVE!
- so no single (in)sensitivity claim: the rule's inputs differ by regime (or the rule itself forks).

## F3: ASC<->SCR flops with +250B (NOT monotonic, NOT 1-byte)
- seed47 randlen: 2000/2250/2500 ASC, 2750 SCR, 3000 ASC, 3250/3500/3750/4000 SCR.
- 40 single-byte flips on rand3000 base: ZERO toggles. Boundary is coarse-multiset, not razor.

## F4: ff-fate PATTERN (100% so far, needs counter-hunt)
- ASC ⟺ ff LAST (or ASC-core + odd tail). SCR ⟺ ff FIRST (B, 3500+) or ff ABSENT (2750, 3250).
- ff-absent-with-~300-expected is the sharpest puzzle: top-12 selection canNOT be pure count-DESC
  (ff would never drop). Selection itself needs re-examination (cf w2's top-12 rule).

## F5: injection CONTROL (bit j ⟷ byte j) + clean value-ASC win
- alternating prefix flips inject chosen single-bit keys (byte0->0x01, byte3->0x08, byte7->0x80),
  slotting ASC. X(0x80,HIGHcnt) vs Y(0x01,LOWcnt), prefix-only: result [00,01,80,81,ff,00/1,...] —
  LOW-count 0x01 BEFORE HIGH-count 0x80. count-DESC DEAD in few-keys regime; value-ASC wins.
- mixed X80/Y20 + tail: Y DROPPED (selection by count for ADMISSION ✓), table scrambled.

## F6: OSS greedy DIVERGES (no help)
- OSS tables for A/B share NO keys with oracle's (greedy finds pbc=1 keys; oracle pbc0).
  Greedy-counts theory untestable via OSS. Oracle slot0=00 pinned (OSS has no pinning).

## Q-18 ask status + NEED (op-counts for viewer beds)
1. No single slot-assignment rule yet. Best candidates: (i) value-ASC + odd/pbc-tail (fits 39/40
   + F5), forked by an unknown trigger into (ii) count-DESC-ish (B, F4-SCR). Trigger UNKNOWN —
   not nkeys (seed6 full-12 ASC), not pads, not key-shape (2-zero keys both sides), not size.
2. Pre-pass quantities: EVIDENCE for pre-pass involvement is now strong (F4 ff-absent impossible
   under final-count selection; F2 regime split) but the quantity is unidentified.
- NEED from w2 (parser data for viewer beds — breaks the impasse): op-counts per key for (a) my
  X80/Y20 bed, (b) seed47 rand2750 (SCR, ff-absent!) vs rand3000 (ASC), (c) pbc of my 5 odd-tail keys
  (3f/ce/ed/f6/5d/de/fa). Recipe specs above reproduce all inputs exactly. With counts, the fork
  trigger becomes fittable. Viewer continues hunting in parallel (meta2-distinct via size analysis).
