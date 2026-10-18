# VERIFY-a0adca4 cport band11 T10PO0..T10POQ (n<=25180, 344 tiers): PASS

## first-hand (at-commit tree ver-a0adca4, seat-local build)
- C build via phony alias: rc=0, 0 warnings.
- parity own run: RGRAMC-PYID 1530/1530 covered=1530/1530 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C.
- code-read: 826 static tables (+10 vs band10), growth
  consistent with T10PO0..POQ band range; scope gate above
  band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band11 FULL 1530/1530 py-identical, C RGRAM-GREEN)
