# PARENT-CT-CACHE-01 (parent, 2026-10-19): MANDATORY oracle cache

All seats, all rounds, effective immediately: every battery
invocation of tests/test_rgram.sh and tests/test_rgram_c.sh
MUST run with:

  export CT=/Volumes/NVME/applearchive-cleanroom-ws/bin/ct-cache
  export CT_CACHE_DIR=/Volumes/NVME/applearchive-cleanroom-ws/ct-cache

Why: oracle output for a given input is deterministic; the
batteries were re-encoding identical zeros-N inputs on every
run (30min/battery at 9k pins, hours at the tail). The shim
serves byte-identical outputs from a content-addressed NVME
store and execs the real tool on miss.

Soundness (parent-validated first-hand, 2026-10-19):
- Miss path byte-identical to direct tool (3/3 cells).
- Hit path byte-identical with backend pointed at
  /bin/false (3/3 cells).
- Corrupt cache entry fails closed: downstream sha-vs-PINS
  chk() FAILs (demonstrated). Cache can never mask a real
  mismatch, and rgram.py / rgramc still execute locally on
  every cell — all verdict logic unchanged.
- Cache pre-warmed: 4482/4482 master cells (2026-10-19).

Scope: batteries only (test_rgram.sh, test_rgram_c.sh,
RECORD=1 mode included — same code path). Census/gap/bed
oracle probes are new-N each tier: unaffected either way,
shim or direct both fine. smoke.sh uses aa/aea, not CT:
leave direct.

Non-compliance = wasted hours; rounds found running
batteries without CT set will be PRODed. Questions -> quiz.
