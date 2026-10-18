# VERIFY-ff3ef8a cport band14 T10PQ0..T10PQQ (n<=25876, 356 tiers): PASS

## first-hand (at-commit tree ver-ff3ef8a, seat-local build)
- C build via phony alias: rc=0, 0 warnings.
- parity own run: RGRAMC-PYID 1566/1566 covered=1566/1566 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C.
- code-read: 852 static tables (+10 vs band13), growth
  consistent with T10PQ0..PQQ band range; scope gate above
  band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band14 FULL 1566/1566 py-identical, C RGRAM-GREEN)
