# REAUDIT-86ae4e6 (viewer3 r8): band167 T10R123 (n<=60584, 806 tiers) — PASS

Interim re-confirm of filed VERIFY-86ae4e6
during VERIFY#2 wait (b191 uncut; b189+b190
GATE+VERIFY closed). Filed VERIFY stands
regardless. Full first-hand re-battery in WS
detached tree tmp/encode-viewer3/86ae4e6/tree
(HEAD 86ae4e6 confirmed, status clean),
seat-private build build/rgramc-r8 (cc -O2
-Wall -Wextra -std=c11 rc=0, 0 warnings,
1826712 bytes), NVME TMPDIR, all legs fresh r8.

- RGRAMC-PYID 3831/3831 covered=3831/3831
  GREEN rc=0 (own-seat corpus seed 7662
  files, py+C freshly executed per pin,
  0 FAIL).
- C-leg RGRAM-GREEN 7662 PASS / 0 FAIL
  (RGRAM_BIN=own r8, fresh oracle; log
  GREEN, rc=0).
- py-leg RGRAM-GREEN 7662 PASS / 0 FAIL rc=0
  (fresh oracle).
- PINS-RGRAM set-eq 7662/7662 (C/py PASS-name
  sets cmp-identical; csv 7664 lines = 7662
  g-z rows + 2 header, both legs all-PASS).
- own-loop fresh-oracle 60329..60584: 256/0
  pins 24/24, OWN-GREEN rc=0 (== GATE).
- Tables-EQ own script v3: NEW 2/2 EQ
  (_T10R123C/_T10R123M); FULL 2145/2145
  0-skip 0-mismatch.
- Wall-grep PARENT-032 scope on band diff vs
  86ae4e6^ (src/c/rgramc.c only, +1129/-988):
  0 hits. HYGIENE/CONTAM/LIBCOMPRESSION
  inherit OBSERVED (none in lane diff).

Verdict: PASS (re-confirmed). No commits, no push.
