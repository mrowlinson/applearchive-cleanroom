# PV-e5b4f19 encode-cport band49 (parent-verify first-hand)

- e5b4f19 (band49 T10P480..T10P48B n<=33468): pv detached worktree
  /Users/mrowlinson/Projects/applearchive-cleanroom/tmp/wt-pv-e5b4f19,
  TMPDIR=/Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-e5b4f19.
- C build: rc 0, 0 warnings (BUILDDIR=$TMPDIR/pvbuild, log build.log).
- RGRAMC-PYID 1996/1996 covered=1996/1996, RGRAMC-GREEN (grepped
  first-hand, log rgramc.log).
- RGRAM-GREEN 3992/3992 via RGRAM_BIN=C (log rgramC.log) + 3992/3992
  via python (log rgramPY.log), both RC=0, 0 FAIL (grepped first-hand).
- SMOKE-GREEN 6/6 PASS (log smoke.log).
- Wall: lane diff e5b4f19~1..e5b4f19 = 1 file src/c/rgramc.c, 949 added
  lines, 0 vendor/disasm-marker hits (grep + supplementary sub_/mach-o
  grep, both clean). No inherited-scope hits in diff.
- VERDICT: PASS. Ready for parent oldest-first merge. Worktree left in
  place for parent reuse.
