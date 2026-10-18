# VERIFY-f21727f cport band31 T10P370..T10P37Q (n<=29704, 422 tiers): PASS

## first-hand (at-commit tree ver-f21727f, seat-local build)
- C build via phony alias: rc=0, 0 warnings.
- parity own run: RGRAMC-PYID 1776/1776 covered=1776/1776 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C.
- code-read: 985 static tables (+10 vs band30), growth
  consistent with T10P370..P37Q band range; scope gate above
  band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band31 FULL 1776/1776 py-identical, C RGRAM-GREEN)
