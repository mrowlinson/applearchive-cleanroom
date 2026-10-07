# Derivation log: decode-viewer lane

Append-only. 1 entry per session. Updated IN THE SAME COMMIT as anything
it describes. Commit without log touch = rejected.

## 2026-10-07 decode-viewer lanes/decode-viewer (entry 0: adoption + gated recon + CR-001..005)
inputs:
- lanes/target-research@8a5e83e docs/TARGET-L1.md (read first-hand, 182 ln)
- lanes/vendor-docs@67527c5 docs/VENDOR-DOCS-L2.md + VENDOR-DOCS.md + API-SYMBOLS-L2.txt sha256:18a4a95c4638f0b6caab5a2d1f65e57f817be12eeabff8ff4fcd069a60ccb363 values:232-symbols
- lanes/oss-survey@6056a80 docs/OSS-SURVEY.md (read first-hand, 192 ln)
- lanes/vendor-binaries@111024a docs/VENDOR-BINARIES.md (hashes re-verified own)
- lanes/fixtures@eeedef2 vectors/FIXTURES.md + selfgen/SHA256SUMS sha256:d9ab0f8c0214ec79e9723661f06e898661235ddc87a24efaea420374ccad4894 values:shasum-c-13/13-OK-own
- lanes/harness-oracle@543bb13 harness/oracle-adapter.sh sha256:c8f5271318d9395f0ded55c432468b90d1d8b6ac96c2bef6bd32ce7ed5ef49de tests/smoke.sh sha256:56d751f9a1b2ca27e3e2cd2c98382b4af454cfb33e3b3cd65b8f96468eff86a2 values:probe-run-ok
- lanes/spec-acquire@ebff5cf spec/CLAUSES.md + OPEN.md + DERIVATION-LOG.md + ACQUISITION-DRAFT.md + VENUE-QUESTIONNAIRE-DRAFT.md (read first-hand)
- lanes/setup-scaffold@3519129 docs/HOST-CAPS.md + src/README.md + tests/oracle-adapter.sh (read first-hand)
- /usr/bin/aa sha256:823df81f1c4331d1e36eee38b20b71a76f016835a01c68d863ce5d8fcb280ef4 MATCH
- /usr/bin/aea sha256:16bfbb1c09b092ef0996191ba5e152485fad40be8b28736bf40f68f1628e6c10 MATCH
- master@0999654 docs/RESEARCH.md + docs/FIREWALL.md + README.md + tmp/queries/JOBS.md (read first-hand)
- quiz-decode Q-001..Q-005 + writer/sweep NOTEs (read first-hand, answered A-001..A-005)
not-consulted: SDK header contents, decompiler output (none installed), patent contents,
  reference/port sources, encode-side lanes, other-track files, vendor bytes beyond hashes+nm/otool/strings metadata
outputs: 3 new files (docs/RECON-DECODE.md, spec/CLAUSES-DECODE-VIEWER.md, this log),
  5 clauses (CR-001..005), tag mix MEASURED 2 / SYMBOL 2 / INFERRED 1, quiz A-001..A-005 + NOTE-01..03
findings:
- gated recon PASS both builds: provenance MATCH, 225/97 undef enumerated, tbd cover 0-missing, binds reconcile EXACT
- 9/9 decode probes green; CORRECTED CLI-CONTRACT stdio claim (dash = literal, omit-flag = stdio)
- decode entries enumerated client-side (11 aa + 4 aea families); logic lib-side (CR-005 MODERATE)
- decompiler absent; dylib tables OPEN (OPEN-1/OPEN-2)
pre-edit: (new files, no pre-edit hashes)
post-edit: docs/RECON-DECODE.md bytes:4182 / spec/CLAUSES-DECODE-VIEWER.md bytes:4639 / spec/DERIVATION-DECODE-VIEWER.md bytes:this-file
base commit 0999654
