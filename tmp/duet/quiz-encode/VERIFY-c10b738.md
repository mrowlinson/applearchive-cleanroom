# VERIFY-c10b738 cport band59 T10P55 (n<=35904): PASS

## first-hand (at-commit tree ver-c10b738, seat-local build)
- C build: rc=0, 0 warnings. rgramc.c DIFFERS from band58.
- parity own run (solo): RGRAMC-PYID 2136/2136
 covered=2136/2136 => RGRAMC-GREEN. FULL, zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
 oracle): RGRAM-GREEN via C.
- new tables vs band58 (10): T10P550 T10P551 T10P55A T10P55AC
 T10P55AM T10P55B T10P55BC T10P55BM T10P55S0 T10P55S1.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band59 FULL 2136/2136 py-identical, C RGRAM-GREEN)
