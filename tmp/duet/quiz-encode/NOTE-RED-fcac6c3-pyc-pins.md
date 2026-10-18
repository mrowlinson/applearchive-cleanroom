# NOTE-RED fcac6c3: FAIL (pyc recommit per PARENT-004) — behavior GREEN 8/8 + zlib EXACT

- RED CAUSE (hygiene, state-based): tip carries 2 pyc
  (pbze MODIFIED 4038->4334B, rawenc unchanged); .gitignore still
  lacks pycache/*.pyc rules. PARENT-004 FIRST warning consumed; next
  w1 commit MUST git rm --cached + gitignore. -> FAIL. FLAG holds.
- BEHAVIOR all green first-hand (pristine extract, pycache stripped,
  gate-tip.sh eff3582): RAWENC 11/11, PBZE 8/8 (4 lzfse + 4 zlib,
  oracle byte-EQ + oracle-extract roundtrips), UNITS 16/16, SMOKE 6/6
  (oracle) + SMOKE-IMPL 6/6 (BACKEND=impl-adapter: aar-encode execs
  src/encode.py first-hand, decode/AEA honest oracle passthrough).
  contam 0, no new OSS (stdlib zlib; OSS leg lzfse-only), ADOPT match.
- zlib byte-exact CORROBORATED: 4 cells byte-EQ + pins 4/4 full-sha
  MATCH (z1 210B c31d41c3..., r1 3245B, mb 5243B, mix 1049510B).
  "L5 10/10" level proof trusted-from-writer; committed-cell
  exactness is first-hand. 15/16 rule on zlib holds on these cells.
- PINS BUG (naming, not behavior): cell() now writes
  <name>.<alg>.got.aar but csv lzfse rows keep bare z1/r1/mb/mix
  names -> 4 PIN-MISSING-AAR. VALUES still byte-identical to fresh
  runs (sha16+bytes match). fix: rename 4 rows to z1.lzfse etc,
  rides the cleanup commit. rawenc pins 9/9 hold.
- CODEC-FINDINGS.md read: lzma/lz4/lzbitmap PARKED + lzraven OPEN
  are writer black-box claims, ungated (no committed cells); not
  corroborated, not blocking. A-9 concurs on raven/bitmap.
- verdict: RED (hygiene FAIL). merge BLOCKED by FLAG-w1-pyc-cleanup
  until cleanup commit (+csv rename) + re-gate. behavior needs NO rework.
- repro: sh lanes/encode-sweep#eff3582:tests/gate-tip.sh fcac6c3 $WS/gate-w1-fcac6c3
