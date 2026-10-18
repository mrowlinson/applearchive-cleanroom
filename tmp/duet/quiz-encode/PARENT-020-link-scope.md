# PARENT-020 encode: PARENT-008 gate-3 DECISION + PARENT-010 XZ scope ruling

## Gate 3 (C-link decision): APPROVED direct-link explicitly.

- C port (aae.c) direct-links PINNED liblzma 5.8.4
  (Makefile LZMA_DYLIB, surveyed license 0BSD + pin).
- Gate 1 DONE (docs/OSS-SURVEY.md §1 in master) + gate 2
  DONE (sweep holdout 12/12 x2 + m4m re-confirm PASS
  + LZMA 6/6 both backends). No silent default: this
  NOTE is the explicit record.

## PARENT-010 scope: own-XZ-framing = CONTAINER (in scope).

- Packets are STOCK liblzma preset-6 output (codec =
  LINKED per PARENT-010; byte-verified). Hand-written
  part is XZ/pbzx FRAMING (vint/header/index/footer/
  chunk walk) = container work. No codec rewrite => no
  divergence-proof/sign needed. (If a future lane
  re-implements packet compression itself, that DOES
  need proof + sign.)
