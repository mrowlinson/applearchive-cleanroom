# NOTE-cport-08 attempt#2: C6 COMMITTED e64e2da (band6 T10PL0..T10R20)

- 2dbd144 partial-merge w2@055bb85 (rgram.py +222, PINS +36,
  test N-list 1/1; staged exactly 3 files, clean auto-merge).
  NOTE: merged w2 tip incl UNGATED-at-merge P21+R20; both since
  VERIFY-PASS (5d92e24 92/92, 055bb85 256/256). band self-consistent
  regardless (C vs in-commit py+pins).
- e64e2da band6: rgramc.c --upto 24392 (38396 lines, +729).
  transpiler clean first try (tables 911/915; b32 q3dec OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1484/1484 GREEN +
  RGRAM-GREEN 2968/2968 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN. spot 4/4 SAME (PL0/PLQ/R20/R20-end).
- ee40fd9 Makefile phony aae/rgramc aliases (PV-0f57814 wart fixed:
  `make rgramc` -> BUILDDIR, NO-STRAY proven, C-BUILD 0w + spot SAME).
- read: PARENT-032 (inherited legs OBSERVED, per-tip GATEs unblock;
  920e187 no-action) + PARENT-033 (band1 MERGED 4459536; stop
  same-cause holds; Q-37 2nd prod to viewer).
- sweep: please gate oldest-first (920e187/937c347/2dbd144/e64e2da).
- next: band7 chase w2 f949df5 T10P22 (letter M, n<=24484).
