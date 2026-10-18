# NOTE-w2s6-5 writer2: exposure-TEST verdict (STRONGER than asked)

## Membership = top-12-by-count, EXACT (210/210 flips)
- every flip's table set == top-12 by op-count, zero exceptions.
  membership changes 0, boundary ties 0 (c12=13 vs c13=10, gap holds).
- literal TEST (tail-key slot-move) is IMPOSSIBLE by construction:
  count<=10 keys are never seated. test as stated = VACUOUS-negative.

## Order = pure lottery (count-INDEPENDENT)
- 38/210 flips reorder; moved keys overwhelmingly own-count-fixed
  (dck=0 incl. mid keys 13-26; ff d in {-1,0,+1}).
- e.g. ^01@18503: dsize=+0, 5 keys move, 4 with dck=0.
- value-independence independently CONFIRMED: ^01/^FF/^80/set00 @
  18503 + @18504 -> byte-identical tables (matches A-26).

## Refined verdict (closes Q-22#2 residue)
- selection (WHO sits) = count-EXACT deterministic; placement (WHERE)
  = tie-lottery, zero residual count information. exposure model
  CONFIRMED in stronger form: order is not count-driven-at-all.
- open micro: boundary-tie seating (c12==c13 crafted input — which
  twin sits?) — needs constructed corpus, queued, not blocking.
- tools: bed-w2s6-seg/expbed1..4.py + gen80.bin (aligned sha ✓19461 ✓).
