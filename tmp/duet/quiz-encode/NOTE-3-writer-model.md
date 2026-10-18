# NOTE-3 writer: raw model CLOSED, harness adopted, smoke green

- adopted (A-1 prescription, git-show read-only, hashes MATCH: adapter
  full c8f52713..., smoke full 56d751f9..., 3 docs prefix-match):
  harness/oracle-adapter.sh, tests/smoke.sh, CLI-CONTRACT.md,
  BATTERY.md, README.md. own contamination grep: CLEAN.
- smoke.sh first-hand: SMOKE-GREEN (6 PASS). oracle pins MATCH A-1.
- read: CLI-CONTRACT.md, BATTERY.md, docs/RESEARCH.md (CLEAN per A-3).
- CORRECTION to NOTE-2: @4 u16 = HEADER SIZE (entry start thru last
  field hdr), not kind. field key is PAT (not ATP). TYP'1' value 1B
  (D/F/L). verified exact on 20+ entries.
- closed raw model (own probes, all -a raw):
  hdr = 6 + TYP1(5) + PAT'P'(6+len) + [LNK'P'(6+tlen)] + UID2(6) +
  GID1(5) + MOD2(6) + FLG1(5) + CTM(T16/S12) + MTM(T16/S12) +
  [DAT'A'(6, u16 n<=65535)/DAT'B'(8, u32 n)] + XAT'A'(6).
  payloads after ALL hdrs in field order: DAT content, XAT records
  (u32 reclen self-incl + name NUL + value, chained; provenance
  rec always first: 4+21+11=36B, blob const 8/8 probes).
  times: S iff nsec==0 (both fields same kind); CTM==MTM==mtime
  proven (touch -m: CTM=mtime, atime/ctime=now differ).
  order: entries sorted bytewise, dirs traversed depth-first inline;
  PAT = full rel path. A->B switch at n>65535 (65535=A, 65536=B).
  stored lzfse inner == raw bytes same-input (TRUE).
  -t 1 == default-t on tiny input (cmp-clean).
- A-4 discrepancy: bed1 "CTM/MTM 8B value" contradicts 113B total
  (113 needs 12B T-values: 39+16+16+42=113 exact). my T=12B stands
  first-hand; flagging for viewer re-verify (Q-6a).
- gap list: g0 DONE (adapter adopted+green). g1 DONE (beds exceed A-4).
  g2 DONE (A-3). g3 ongoing (edge probes). g4 NEXT: src/rawenc.py
  prototype + tests/test_rawenc.sh (fixed-mtime pins). g5 pins file.
  g6: impl-backend adapter shape for smoke BACKEND swap.
- open edges -> Q-6 (UID/GID/FLG/S-link/fifo/TYP-set/pbze-rule).
