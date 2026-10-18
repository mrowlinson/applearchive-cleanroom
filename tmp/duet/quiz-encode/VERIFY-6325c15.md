# VERIFY-6325c15 cport band26 T10PY0..T10PYQ (n<=28660, 404 tiers): PASS

## first-hand (at-commit tree ver-6325c15, seat-local build)
- C build via phony alias: rc=0, 0 warnings.
- parity own run: RGRAMC-PYID 1716/1716 covered=1716/1716 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C.
- code-read: 949 static tables (+10 vs band25), growth
  consistent with T10PY0..PYQ band range; scope gate above
  band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band26 FULL 1716/1716 py-identical, C RGRAM-GREEN)
