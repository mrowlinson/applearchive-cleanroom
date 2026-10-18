# PRE-006 raven tail fields: word1 SOLVED (0x01 + 3xRAW8), TAG-bit offsets ASKED (Q-21 Q2)

## word1 = TAG-BYTE 0x01 + 3 RAW FIELDS (CLOSED, exact)
- bits 32-39 = `10000000` (0x01) CONSTANT across dev-counts (0-3) AND values (00/01/7f/80/ff).
- pos100 -> bits 40-47 (= V LSB-first EXACT, 5/5 values), pos101 -> 48-55, pos102 -> 56-63.
- 8 + 8x3 = 32 EXACT (full word, no slack). Multi-dev does NOT change the tag (1-3 devs same 0x01).
- prediction: pos103+ live in later words (their fields NOT in word1 — verify by diff).

## value-linearity: ALL 32 tail pos = EXACTLY 8 diff bits (0x00->0xFF)
- contiguous for pos100/101/102/104/105/106 (+96/112/120!); scattered (split-nibble) for others.
- neighborhoods all-zero (NO adjacent tag!) => tags are NON-ADJACENT (word-level or distant).

## TAG-01/0000 BIT-OFFSET PUZZLE (need w2's exact offsets — ASK)
- word8 (pos120, TAG-0000?): all-zero baseline; LSB-first-4b-prefix "0000" CONSISTENT (weak: zeros).
- word10 (pos96, TAG-01?): (1,0) found ONLY at bits 322-323 (2b value-1 LSB-first ✓) — offset +2
  from word start; word-start bits 320-321 = (0,0). INCONSISTENT-PLACEMENT vs word5 (pos112,
  TAG-01?): (1,0) at word start (bits 160-161), field at 166-173 (gap 4); pos96 field at 334-341
  (gap 10 after 322-tag). Same tag-type, different geometry — my guesses don't cohere.
- ASK (30-second answer from tparse2, saves hours): publish the EXACT payload bit offsets of the
  TAG bits for pos96/112 (01) and pos120 (0000) + the READ ORDER (LSB-first? MSB-first?).
  With offsets, viewer beds width-selection (which knob flips which tag) AT field level.

## Q-21 status
- Q1 (selection): position-tier CONFIRMED live (A-23); (len,off,value) eliminated (0..128).
- Q2 (payload bits): mid-dev value packing CONFIRMED exact (V0-3@50-53 LSB-first + bit66/67 const-1
  (bit67 NEW)); tail TAG-bit offsets ASKED above; word1 structure CLOSED.
