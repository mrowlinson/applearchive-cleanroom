# PV-f563e5f: parent-verify first-hand (band75 T10P66 n<=40356) — PASS

Worktree tmp/wt-pv-f563e5f (fresh, detached @f563e5f), TMPDIR + seat-private
BUILDDIR on NVME pv-f563e5f/ (shared build/aae untouched). Parent-run battery.

- C-BUILD: rc=0, 0 warnings.
- RGRAMC-PYID 2385/2385 covered=2385/2385, RGRAMC-GREEN, 0 FAIL.
- RGRAM-GREEN via C: 4770 PASS / 0 FAIL.
- RGRAM-GREEN via python: 4770 PASS / 0 FAIL.
- SMOKE-GREEN: 6 PASS.
- Wall: lane diff (src/c/rgramc.c only) vendor/disasm grep 0 hits.

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-f563e5f/
Verdict: PASS. GATE-f563e5f PASS-functional + VERIFY-f563e5f PASS + FLAG-free.
