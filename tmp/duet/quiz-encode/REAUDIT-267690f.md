# REAUDIT-267690f (viewer3 r8): band170 T10P127 (n<=61024, 812 tiers) — PASS

Interim re-confirm of filed VERIFY-267690f
(viewer3 r1) during turf-starved wait (b189
yielded to viewer2; b190 claimed r8, battery
next). Filed VERIFY stands regardless. Full
first-hand re-battery in WS detached tree
tmp/encode-viewer3/267690f/tree (HEAD 267690f
confirmed, status clean), seat-private build
build/rgramc-r8 (cc -O2 -Wall -Wextra -std=c11
rc=0, 0 warnings, 1843848 bytes), NVME TMPDIR,
all legs fresh r8.

- RGRAMC-PYID 3865/3865 covered=3865/3865
  GREEN rc=0 (own-seat corpus seed 7730
  files, py+C freshly executed per pin,
  0 FAIL).
- C-leg RGRAM-GREEN 7730 PASS / 0 FAIL
  (RGRAM_BIN=own r8, fresh oracle; log
  GREEN, rc=0).
- py-leg RGRAM-GREEN 7730 PASS / 0 FAIL rc=0
  (fresh oracle).
- PINS-RGRAM set-eq 7730/7730 (C/py PASS-name
  sets cmp-identical; csv 7732 lines = 7730
  g-z rows + 2 header, both legs all-PASS).
- own-loop fresh-oracle 60933..61024: 92/0
  pins 24/24, OWN-GREEN rc=0 (== GATE).
- Tables-EQ own script v3: NEW 10/10 EQ
  (AC/BC/QC/AM/BM/M/QR/QT/S0/S1); FULL
  2167/2167 0-skip 0-mismatch.
- Wall-grep PARENT-032 scope on band diff vs
  267690f^ (src/c/rgramc.c only, +1446/-995):
  0 hits. HYGIENE/CONTAM/LIBCOMPRESSION
  inherit OBSERVED (none in lane diff).

Verdict: PASS (re-confirmed). No commits, no push.
