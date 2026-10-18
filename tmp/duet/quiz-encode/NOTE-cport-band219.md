# NOTE-cport-band219 T10R149 (n<=69632)

Merge 4b9fe8e (w2@77c282f partial, +2 tiers +24 pins, R-lane combine).
Band cf229ce (910 tiers sealed).

Takeover: merge in-flight w/ 3 unmerged paths, worktree pre-resolved by dead predecessor. Verified fh (not trusted):
- rgram.py: ours 42963/42963 + w2 40256/40256 present (0 removed); R149 tabs+dispatch byte-identical to w2 blob; dispatch ascending R148<R149 tail; py_compile OK.
- t.sh union 4510 ascending +12 new (69377..69632). PINS 9022 rows 0 dupes 0 missing; FIXED 1 descent (68955 pair -> post-68954), 0 descents now.
- rgramc.c C-cut: R149 M16/Q16/C67 byte-eq py; dispatch mirrors (idx/formulas/order); block post-P151Q pre-scope-exit.

Battery first-hand this seat (r11):
- RGRAM py GREEN 9020/9020 0 FAIL rc=0 (mrg-b219-py-r11.log)
- RGRAM C GREEN 9020/9020 0 FAIL rc=0 (bat219-c-fh.log, build-band219/rgramc, RGRAM_BIN=C)
- PYID exact 4510/4510 covered 4510/4510 (pyid-band219-fh.log, corpus seeded work-mrg219)
- SMOKE-GREEN + UNITS-GREEN rc=0 (merge + post-C-cut re-run)
- build 0 warnings; lane-diff rgramc.c-only; wall-grep 0
