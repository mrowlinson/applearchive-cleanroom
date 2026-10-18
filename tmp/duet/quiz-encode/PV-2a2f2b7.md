# PV-2a2f2b7: parent-verify first-hand (band74 T10R65 n<=40052) — PASS

Worktree tmp/wt-pv-2a2f2b7 (fresh, detached @2a2f2b7), TMPDIR + seat-private
BUILDDIR on NVME pv-2a2f2b7/ (shared build/aae untouched). Parent-run battery.

- C-BUILD: rc=0, 0 warnings.
- RGRAMC-PYID 2362/2362 covered=2362/2362, RGRAMC-GREEN, 0 FAIL.
- RGRAM-GREEN via C: 4724 PASS / 0 FAIL.
- RGRAM-GREEN via python: 4724 PASS / 0 FAIL.
- SMOKE-GREEN: 6 PASS.
- Wall: lane diff (src/c/rgramc.c only) vendor/disasm grep 0 hits.

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-2a2f2b7/
Verdict: PASS. GATE-2a2f2b7 PASS-functional + VERIFY-2a2f2b7 PASS + FLAG-free.
