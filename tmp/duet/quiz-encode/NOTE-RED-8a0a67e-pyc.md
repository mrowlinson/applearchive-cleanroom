# NOTE-RED 8a0a67e: FAIL per PARENT-002 (pyc bytes modified in tip) — behavior GREEN

- RED CAUSE (hygiene, state-based): tip modifies
  src/__pycache__/rawenc.cpython-314.pyc (10268->11345B); 2 pyc in
  tip; .gitignore lacks pycache/*.pyc rules. PARENT-002: "gate FAIL
  any tip adding artifact paths until clean." -> FAIL. TIMING: tip
  17:07:12 predates PARENT-002 (17:07:36) by 24s — NO writer fault;
  fix-forward per PARENT-002 steps 1-3, then re-gate (fast: see below).
- BEHAVIOR all green first-hand (pristine, pycache stripped):
  RAWENC-GREEN 11/11 (c1-c8 same shas, c9 563B sha MATCHES pin
  edcc9c0c..., c10 505B MATCHES 32004f4b..., c11 186B live-socket
  compare-only). UNITS-GREEN 16/16, 0 FAIL. PBZE-GREEN 4/4, pins
  hold. contam grep 0. no new OSS (PARENT-003 gate 3 clean).
- code claims corroborated: put_int min-width (units exact incl
  u32 99999/u32bnd); FLG=st_flags; DEV-after-PAT B/C + no DAT/XAT
  (units vs A-6 0x01000001/0x03000002 + hdrsize==len); socket no-DEV
  (c11 byte-green proves); LNK-bytes: NOTE-7's correction ACCEPTED
  (readlink(bytes)->bytes; c10 unicode len 9 green) — viewer gap #4
  was a misread, never a bug. pins header documents c7/c11
  compare-only. fifo skip w/ hang note correct per A-6e.
- verdict: RED (hygiene FAIL). merge BLOCKED by FLAG-w1-pyc-cleanup
  until cleanup commit + re-gate. behavior needs NO rework.
