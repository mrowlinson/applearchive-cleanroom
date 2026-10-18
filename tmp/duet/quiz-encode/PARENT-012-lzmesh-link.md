# PARENT-012 lzmesh link spec (encode; from lzmesh parent, verified)

- Deliverable: PUBLIC mrowlinson/lzmesh (0BSD). API =
  include/lzmesh.h over src/lzmesh_enc.c + src/lzmesh_dec.c
  (C). Perf build = `make pgo`.
- PIN: tag duet-land3 = f56d181aaa3e8aa2274005833431431d09b57da4
  (pushed, clone-verified). Link ONLY this until they announce
  newer; re-pin = event + full re-gate, never silent.
- Their lane-4 has no remote: link the PUBLIC tag, never
  their branches. Stay out of lzmesh-cleanroom/ scratch.
- Viewers: lzmesh-in-AppleArchive callsite is UNKNOWN to
  them — it is OUR finding to make. Confirm whether/where
  AppleArchive invokes lzmesh; file finding + link plan.
  No integration until the callsite is proven.
- Sweep: when lzmesh link lands: pin check + byte-verify vs
  APPLE oracle (never vs lzmesh port alone).
