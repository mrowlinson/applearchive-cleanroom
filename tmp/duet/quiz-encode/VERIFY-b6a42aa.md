# VERIFY-b6a42aa cport band8 T10R21 (n<=24740, 333 tiers): PASS

## first-hand (at-commit tree ver-b6a42aa, seat-local build)
- C build via phony alias: rc=0, 0 warnings.
- parity own run: RGRAMC-PYID 1502/1502 covered=1502/1502 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C (tail PASS g-z24740-closed,
  PASS g-z24740).
- code-read: 804 static tables (+3 vs band7: single R21 tier
  with q=PMM reuse => small delta, consistent), scope gate
  above band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band8 FULL 1502/1502 py-identical, C RGRAM-GREEN)
