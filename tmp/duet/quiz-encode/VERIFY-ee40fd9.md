# VERIFY-ee40fd9 cport Makefile phony aliases: PASS

## first-hand (at-commit tree ver-ee40fd9, seat-local build)
- delta: Makefile only (+6: .PHONY aae/rgramc aliases).
- `make BUILDDIR=seat rgramc` (bare alias, the old footgun):
  rc=0, 0 warnings, binary lands in BUILDDIR, NO stray
  ./rgramc in tree (the PV-0f57814 defect fixed; I hit the
  old behavior first-hand on bands 1-4 pre-fix).
- C source byte-identical to band6 (cmp SAME); alias-built
  binary parity own run: RGRAMC-PYID 1484/1484 =>
  RGRAMC-GREEN (behavior unchanged by build fix).
- wall-grep/hygiene: no source touched, carries band6.

## verdict: PASS (build fix works, C behavior intact)
