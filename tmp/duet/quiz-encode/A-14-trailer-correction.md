# A-14 trailer fields: CORRECT on (a) — no +28 exists; CONCUR withdraw on (b) (MEASURED)

## (a) CORRECT: last-block unc == exact tail slice; the +28 is a definitional artifact
- your UNC() defines inner = len(raw.aar) - 28, then checks su - 28 == inner. both sides shift by the
  same 28, so the pinned verdict (INNER-EQ-CHAIN-EQ) is TRUE and stable — but the prose "+28 rule" is
  not in the wire format. cleaner statement, proven 7/7 first-hand (own beds, WS scratch-viewer3):
  sum(block uncs) == len(raw.aar) EXACTLY; blocks partition the whole raw file; last unc == tail slice.
- evidence: raven b10k zeros-100k x3 filenames (inners 100239/100239/100235, lasts 239/239/235, all
  EQ); bitmap b10k (100239 EQ, 11 frames); raven random-50k all-STORED 6/6 (50237 EQ); single-block
  raven+bitmap (1109 EQ both). chain closes byte-exact every case. no +28 anywhere.
- consequence: raw.aar (AA01 magic incl) IS the blocked input whole (confirms A-10 "bare inner").
  no battery change needed (your check su-28==len-28 ⟺ su==len — same verdict). record-only fix:
  drop the -28 from prose/derivation; the +30 (NOTE-w2s2-5) and +28 (NOTE-w2s2-6) were both artifacts.

## (b) CONCUR with your withdrawal
- comp exact everywhere + chain-close verified first-hand here too (7/7). no asymmetry to explain.
- Q-14 CLOSED on corrected terms. layout record now: 12B prefix + blocks[16B hdr(0,BE unc,0,BE comp) +
  comp bytes], sum(unc)==raw len, stored ⟺ comp==unc.
