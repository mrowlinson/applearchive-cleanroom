# A-23 raven TAG-width: position-tier CONFIRMED live, (len,off,value) ELIMINATED (INTERIM)

## size-signature maps (own, ct-oracle, zeros128 base = 44B payload)
- T1 run-len (AA-run@8, L=0..40): 44,44,48,48... — L=1 FREE, L=2 +4B (ONE tag), flat to 40
  (length fully in-field; RLE-ish ✓ w2s4-8). Single knob L=1->2 flips tag COUNT (not width).
- T2 len/off: length 1..120 FLAT (no tiers — length always in-field); offset 8..128 FLAT except
  +4B blip D=56..96 then BACK DOWN at 112/128 (structural token-count, non-monotonic — late-absorb
  ✓ "late always free"). (len,off) do NOT select width (0..128).
- T3 position (single-AA all 128 pos): THREE TIERS — early 0..18 FREE (44B), mid 19..76 +4B (48B),
  late 77..127 FREE (44B). SHARP boundaries (18/19, 76/77). CONFIRMS+SHARPENS w2s4-8 early/mid/late
  (their early-PAIR +4B + my early-SINGLE free + L=2 +4B = one consistent rule: early token carries
  ONE patch; first rides free).
- T4 value (13 values @mid + 6 @early): FLAT (48/44). Value costs NOTHING — width can't be
  value-driven (but value must still be STORED somewhere — see Q2).

## Q-21#1: position-tier is the LIVE candidate (of their 3)
- ELIMINATED (0..128 range): run-len (beyond 1-vs-2+), (len,off)-joint, value.
- PREDICTION for tparse2 (falsifiable): the single-mid-deviation +4B token IS the TAG-01/0000 field
  (measure WHICH width!); early/late singles ride in-field (no new tag). If mid->TAG always and
  early/late->in-field/RAW-8 -> Q-21#1 CLOSED as position-tier-selected. If mid-token width VARIES
  with (pos within 19..76, value, neighbors) -> report the sub-rule, viewer re-beds.
- caveat: 4B quantization hides sub-4B width flips in size data — FIELD attribution needs tparse2
  (theirs). Boundaries 18/19 + 76/77 are the exact re-bed points.

## Q-21#2 (payload bits): DEFERRED to tparse2 (honest)
- size data cannot resolve bit contents. Constraint from T4: value costs nothing -> all 256 values
  share ONE width (no value tiers); payload MUST carry value + position in fixed width (mid token).
- ask: publish the tparse2 FIELD GRAMMAR (tag discrimination + slot/bit layout rules) in quiz when stable —
  lets viewer bed AT field level (width-flip knobs per field) instead of size level.
