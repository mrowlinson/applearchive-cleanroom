# NOTE-w2s5-10 writer2: dominant-key slot ARBITRARY + rotation/modulus dead

- tag80 micro-case: ff (2109 ops, max) @ slot2, rest count-DESC (K=2). tag30
  (ff 2103, near-identical stats): ff @ slot0. group-counts: ff=202 runs
  still max — RUNS dead as sort key. first/last-seen dead.
- corpus-wide (ff top-count, 36 chunks): ff slot ∈ {0:5, 1:4, 2:1, 3:1, 4:2,
  5:2, 8:2, 9:13, 10:4, 11:2} — dominant key lands ANYWHERE (mode slot9!).
  head scrambled + tail count-exact = standing shape.
- killed: lossy moduli 8..512 (monotone to plain-count, med 33->11, no knee);
  exact rotation of count-DESC (0/63 despite med-11 ≈ rot1 signature).
- next: Q to viewer (distinct-count inversion mechanism is now the SOLE
  blocker; self-serve exhausted 15+ families) + D-max probe meanwhile.
