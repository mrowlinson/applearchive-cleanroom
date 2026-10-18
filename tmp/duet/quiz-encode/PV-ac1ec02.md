# PV-ac1ec02 encode-cport band50 (parent-verify first-hand)

- ac1ec02 (band50 T10R47+T10P490..T10P49B n<=33816): pv detached worktree
  /Users/mrowlinson/Projects/applearchive-cleanroom/tmp/wt-pv-ac1ec02,
  TMPDIR=/Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-ac1ec02.
- C build: rc 0, 0 warnings (BUILDDIR=$TMPDIR/pvbuild, log build.log).
- RGRAMC-PYID 2016/2016 covered=2016/2016, RGRAMC-GREEN (grepped
  first-hand, log parity.log; re-run after NVME case-insensitive
  rgramC.log/rgramc.log collision clobbered first parity log — corpus
  cached, identical result both runs, rc=0, 0 FAIL).
- RGRAM-GREEN 4032/4032 via RGRAM_BIN=C (log rgram-viaC.log) + 4032/4032
  via python (log rgramPY.log), both rc=0, 0 FAIL (grepped first-hand).
- SMOKE-GREEN 6/6 PASS (log smoke.log).
- Wall: lane diff ac1ec02~1..ac1ec02 = 1 file src/c/rgramc.c, 1234
  added lines, 0 vendor/disasm-marker hits in added lines (grep +
  supplementary sub_/mach-o/dylib grep, both clean). No inherited-scope
  hits in diff (PARENT-032 lane-diff scope).
- Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-ac1ec02/
  {build,parity,rgram-viaC,rgramPY,smoke}.log.
- VERDICT: PASS. Ready for parent oldest-first merge. Worktree left in
  place for parent reuse.
