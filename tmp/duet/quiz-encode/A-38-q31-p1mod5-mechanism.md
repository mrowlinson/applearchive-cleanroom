# A-38 Q-31: gap%5 is pure phase (stride-5 from mend_prev), ml/content-free

## filename note (their NOTE-41 referee rule)
- this file answers Q-31-writer1s3-p1mod5-mechanism.md (slug has
  q31+mod5+mechanism ✓). Q-30-buckets answers (no A-30-buckets
  slug; sequential convention): A-37-q30-bucket-mates-final.md
  (4x5 4-grams + repro) + A-37-q30-pairs5-final.md + NOTE-134b
  pointer. "A-30-tooth64192" is the OLD w2-line file — unrelated.

## verdicts (all first-hand, v4q31.py + k4 follow-up, 100+ encodes)
- PURE GAP EFFECT CONFIRMED: sweep g=0..14 -> ABSENT iff g%5==4
  (15/15: absent 4/9/14, present else). content control: g=4/9
  30/30 ABSENT, g=3/8 30/30 PRESENT across random gap bytes.
  NO table/content covariate (their B0/M1 identical-tables
  corroborated from oracle side).
- ANCHOR = mend_prev (relative): A=200/211/233 -> same pattern
  15/15 (absolute position moot).
- ML-INDEPENDENT: k1=4/8/16/32 all skip at g=4 (k1=4: NOPROBE
  5/5 = skip + unique gram; g=3 PRESENT 5/5 control).
- STRIDE REFRAME (exact): skip iff (P1 - mend_prev) % 5 == 0
  (P1 on 5-stride from last match end; == gap%5==4).

## mechanism candidacy (their 3 options)
- stride-5 scan vs phase counter: behaviorally EQUIVALENT here
  (relative phase + content-free + ml-free fits both; no probe
  separates a counter from a stride scan — internal detail).
- token/literal-coding interaction: NEITHER ruled in NOR out
  (no coding-shape probe run; pattern needs no coder to state).
- class verdict: phase-counter/stride-5 anchored at match end,
  phase-0 = skip. exact implementation OPEN (below behavior).

## bed recipe (theirs B0/M1 equivalent, self-built)
- R0(A) + C0(=R0[10:18], M0@A, mend=A+8) + GAP(g) + C1(=R0[50:
  50+k1], M@MS) + PROBE(=inner[P1:P1+8]) + 2000 zeros; query
  probe occ == P1 (PRESENT) vs 51 (ABSENT). k1=4 needs
  self-consistent probe[0]=C1[1]. apparatus: lz4probe.decisions,
  oracle compression_tool -a lz4. Q-31 CLOSED.
