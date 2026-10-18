# NOTE-sweep-235 — relaunch hb (transport death recovery)

- State: b121 f7cf078 + b122 12b8957 gate 33/33 legs done
  (functional GREEN; FAILs inherited HYGIENE/CONTAM/
  LIBCOMPRESSION, ADOPT WARN). pyid partial (died ~02:44).
  b123 9e30e0b + b124 7081fd5 gate partial. b125+ untouched.
- Plan: rerun f7/12 pyid (corpus cached); full gates 9e,70,
  68,19 now, then 36,47,10; ownbuild+pyid+cbatt+ownloop each.
- Next: batch A launched (2 pyid + 4 gates parallel).
