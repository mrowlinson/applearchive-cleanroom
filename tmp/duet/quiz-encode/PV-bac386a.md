# PV-bac386a cport band58 T10P54+T10R53 (n<=35876, 522 tiers sealed): PASS

## first-hand (detached worktree wt-pv-bac386a @ bac386a, seat-private build)
- C build: rc=0, 0 warnings.
- parity own run:
  RGRAMC-PYID 2126/2126 covered=2126/2126
  RGRAMC-GREEN
  FULL coverage: zero uncovered N (2126 sealed closed-pins, all py-identical rc+stdout+stderr).
- RGRAM-GREEN via C (RGRAM_BIN=seat rgramc, own run): 4252/4252 pins, 0 FAIL.
- RGRAM-GREEN via python (own run): 4252/4252 pins, 0 FAIL.
- SMOKE-GREEN (own run): all cells PASS.
- wall-grep lane diff bac386a^..bac386a (1 file: src/c/rgramc.c): 0 hits.

## logs
- /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-bac386a/build.log
- /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-bac386a/rgramc.tail
- /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-bac386a/rgram-c.tail
- /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-bac386a/rgram-py.tail
- /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-bac386a/smoke.log
- build: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-bac386a/build/ (rgramc, aae)
- worktree: /Users/mrowlinson/Projects/applearchive-cleanroom/tmp/wt-pv-bac386a (kept for parent merge)

## verdict: PASS (band58 FULL 2126/2126 py-identical, C+py RGRAM-GREEN, SMOKE-GREEN, wall clean)
