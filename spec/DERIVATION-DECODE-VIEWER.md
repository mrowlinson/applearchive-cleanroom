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

## 2026-10-07 decode-viewer lanes/decode-viewer (entry 1: CR-006..008 + OPEN-3 + VERIFY x4 + A-006/PRE-001)
inputs:
- lanes/fixtures@eeedef2 vectors/selfgen 8 AAR (xxd first-hand, 10 samples w/ own-gen)
- own-gen probes: WS tmp/decode-viewer-probes/hello-b1m.aar + tiny.aar + tiny-z.aar + rnd.aar (aa archive -t 1, macOS 27.0.1)
- quiz-decode Q-006 + writer DPROBE-01 (db0de34) + writer/sweep NOTEs (read first-hand)
- writer tips verified: 8fd3a8d + 1beb58d + db0de34 + 8c6740a (diffs + wall greps first-hand)
- dyld_info -arch arm64e -fixups /usr/bin/aa (uniq -d pass for OPEN-3)
- OSS allow-list URLs: 7x curl -I 200 re-verified this session
not-consulted: SDK header contents, decompiler output (still none), patent contents,
  reference/port sources, encode-side lanes, vendor bytes beyond hashes+metadata
outputs: +3 clauses (CR-006 MEASURED, CR-007 MEASURED, CR-008 INFERRED:STRONG),
  tag mix total MEASURED 4 / SYMBOL 2 / INFERRED 2; VERIFY x4 PASS; A-006 + PRE-001 + NOTE-04/05
findings:
- outer 28B layout + blocksize@8 CONFIRMED (-b 1m probe); fileSize = 28+comp 10/10
- stored positive (empty 113==113) + 2 negatives (tiny/random framed); trigger predicate OPEN
- inner TLV STRONG (uid501/gid20/mode755 triple corroboration)
- OPEN-3 settled (chkstk x4); writer DPROBE-01 cross-checks 8/8 MATCH
pre-edit: docs/RECON-DECODE.md sha256:77ea0d30e3a3954ed7fe8046a7afae84f00cb98c479543d0a421a3283e2d1b45 bytes:4182
pre-edit: spec/CLAUSES-DECODE-VIEWER.md sha256:9dd6426fe02f033f7401bd4547aa4cd4c2aead8137f130985f8008f4dc02b483 bytes:4639
pre-edit: spec/DERIVATION-DECODE-VIEWER.md sha256:a963ca81ab48a8ab1c0ba1275bfdbf0778f7301535e73c37a0f8076794b6d6d0 bytes:2688
post-edit: (recorded at commit; see commit 2nd line stats)

## 2026-10-07 decode-viewer lanes/decode-viewer (entry 2: CR-009/010 + A-007/PRE-002 + VERIFY-7bb7b2b)
inputs:
- own-gen big/ probes @ -b 1m/-b 256k/-b 4m + -a raw (inner 3500382B) + extract cmp-clean (WS tmp/decode-viewer-probes)
- own-gen lzraven tiny/rnd payloads (3-sample bed) + compression_tool decode matrix (lz4 x4, lzraven x7, lzfse x1, lzbitmap x1)
- quiz-decode Q-007 (read first-hand) + writer 7bb7b2b proto/aad.py (read full 167 ln via git show + ran 5 cases first-hand)
- https://github.com/lz4/lz4 (curl -I 200) + lib/LICENSE (BSD redistribution text verified)
not-consulted: SDK header contents, decompiler output (still none), patent contents,
  reference/port sources, encode-side lanes, writer worktree files (git-show only + black-box runs)
outputs: +2 clauses (CR-009/010 MEASURED), tag mix total MEASURED 6 / SYMBOL 2 / INFERRED 2;
  A-007 + PRE-002 + NOTE-06 + VERIFY-7bb7b2b PASS
findings:
- multi-block chain EOF-exact x3, unc sums 3500382 exact; stored mixes per-block
- codec-frame rule: whole-payload oracle decode MATCH (lz4/lzraven/lzfse); lzma raw-XZ
- proto v1 wall-clean + 3/3 MATCH re-run own; lzraven size fields still unlocated
pre-edit: spec/CLAUSES-DECODE-VIEWER.md sha256:dc82ac4077c1ab7162c6b9382cc369726e3c26908e524ca0c04715431aac67ae bytes:7292
pre-edit: spec/DERIVATION-DECODE-VIEWER.md sha256:0b7458b886191e2446a3ee9854d71601a2c662dad564ef82354e11e3da46dcc4 bytes:4419
post-edit: (recorded at commit; see commit 2nd line stats)

## 2026-10-07 decode-viewer lanes/decode-viewer (entry 3: CR-011 + A-008/A-009 + NOTE-07)
inputs:
- own-gen magic sweep: 20 archives (zeros 1K-600K, text 20K, random 100B-600K; -a lzfse/lz4, -b 4m) + bvx walks (WS tmp/decode-viewer-probes)
- quiz-decode Q-008 + Q-009 + writer2 NOTE-001 (read first-hand)
- writer1 lanes/decode-writer@7bb7b2b (turf inventory for A-009 split: proto/aad.py + notes/DPROBE-01 + adopted copies)
not-consulted: SDK header contents, decompiler output (still none), patent contents,
  reference/port sources, encode-side lanes, lzfse OSS stream internals (writer-side read)
outputs: +1 clause (CR-011 MEASURED), tag mix total MEASURED 7 / SYMBOL 2 / INFERRED 2;
  A-008 + A-009 + NOTE-07
findings:
- 4096 magic rule (100B bracket) + lz4 64KB frames (EOF/usum exact x2) + stored ~= comp>=unc
- writer2 seated on AEA turf; Q/A 9/9; VERIFY current; joint DONE not reached (claim HELD)
pre-edit: spec/CLAUSES-DECODE-VIEWER.md sha256:2c0cec815a47474f471d252ff9de75aa1e81979234fd4b8c6783c6b606d16d7f bytes:9184
pre-edit: spec/DERIVATION-DECODE-VIEWER.md sha256:2324515c85d840e2a94cac95e07802b5cdd1fd779bdfbc1a7ecdcb54b3330011 bytes:5892
post-edit: (recorded at commit; see commit 2nd line stats)

## 2026-10-07 decode-viewer lanes/decode-viewer (entry 4: CR-012/013/014 + A-010/011/012 + VERIFY x20)
inputs:
- quiz-decode Q-010/Q-011/Q-012 + all A/NOTE/VERIFY/FLAG/GATE/PARENT filings (read first-hand; 12/12 Q answered)
- own-gen lrv-ladder: 18 aa-emitted -a lzraven (unc 337..1048815) + 3 compression_tool -encode + surgery/sweep/leniency/range probes (WS tmp/decode-viewer-probes/lrv-ladder; macOS 27.0.1)
- anat0m1a/liblzraven@700b88c4b2e1b1d96e499d172dfa0b8e5d9134ab (pin verified ls-remote+clone+tree): SPEC.md (65160B) + README + LICENSE (0BSD) + Makefile + tests/c/lzraven_dec.c usage read; built clean (-Werror) + 16/16 xcheck MATCH + 2/2 correct-reject own
- kinnay/AEA@d22f4fd aea/murmur.py (200, 508B, stock M64A) + w2 murmur xcheck 21/21 own (WS murx/)
- own-gen kindbed: 9-entry TLV + feeder-guarded fifo + crafted-cpio device convert + extract matrix (WS tmp/decode-viewer-probes/kindbed); root mknods x3 via helper (chowned back, no strays)
- SDK MacOSX27.0 AADefs.h (130 ln) + AAFieldKeys.h (191 ln) read first-hand (vendor-published); dgelessus README (links-only, no format detail)
- oss-survey@6056a80 §3 (murmur reusable) + vendor-docs L2 types/fields (corrected 8->11) + fixtures pins (reused, not re-pinned)
- writer commits verified first-hand (full diffs + A-004 wall greps 0/20): w1 1d073b9 848bada c332c96 4a3c8ce 59fb30f 88b1e3d 16d9a8b; w2 5daf51c d59d825 64af2c4 1ecfb3f 9ca2a1e 650e0c5 35a1f7a 2d58522 6f4bea5 2ace77e 8ff280a 3bcdcb6 716dfb4
not-consulted: decompiler output (still none), patent contents, reference/port sources,
  encode-side lanes, writer worktree files (git-show only + black-box runs), liblzraven src/*.c internals (framing verdict needed only SPEC+build+xcheck)
outputs: +3 clauses (CR-012/013/014 MEASURED), tag mix total MEASURED 10 / SYMBOL 2 / INFERRED 2;
  A-010 + A-011 + A-012 + NOTE-09..13 + VERIFY x20 PASS (0 new FLAGs; sweep FLAG-59fb30f ACKed)
findings:
- lzraven framing fully cracked first-principles (block-hdr halves, params size(i) 24/24, terminator, unc-absent, no-checksum) + third-party SPEC mutual-CONFIRM; survey §10 OPEN settled by nomination
- murmur path-line granted (A-010) + proven 21/21 in writer2 code; entry census 11 TYPs (A-012) + HLC exact-agreement
- w1 848bada..59fb30f unbuildable-as-committed (Makefile lineage; fixed @88b1e3d, sweep-gated); c-battery xattr overclaim flagged to writer; w2 printf-octal 4-byte note
- joint DONE not reached (writers mid-turf: w1 kinds/HLC-era, w2 lzraven-implementing; claim HELD)
pre-edit: spec/CLAUSES-DECODE-VIEWER.md sha256:02e806f0b12bf4b2ede23137c0e51867cd98db64a3ce1a0698bf0450c76634a0 bytes:10363
pre-edit: spec/DERIVATION-DECODE-VIEWER.md sha256:c97e3504e726db17c3e3cfa4936e5864be19d855afbfc3baa6698100a39c0483 bytes:7110
post-edit: (recorded at commit; see commit 2nd line stats)

## 2026-10-07 decode-viewer lanes/decode-viewer (entry 5: CR-015/016 + A-013/014 + VERIFY x8)
inputs:
- quiz-decode Q-013/Q-014 (read first-hand) + writer1 DPROBE-04 (03aec9c) + writer2 NOTE-034 (e78e38e era)
- own-gen bit0/ probes: zr/rz/r600k/r2m (aa) + ct2-r/ct2-zr/ct2-r10k (pure-stream, seeded; first ct- rows discarded: reseed-per-draw bug -> 0xB0 const) + root B/C extract (WS tmp/decode-viewer-probes/bit0 + kindbed)
- writer1 fixtures hlink-basic/missing + fifo-mixed (bytes + pins verified own) + `aa list` TYP-H parse own
- writer commits verified first-hand (full diffs + A-004 wall greps 0/8): w1 e87ec65 ffcb297 99db53e 03aec9c; w2 7205bf9 e7a9249 80577a2 e78e38e
not-consulted: decompiler output (still none), patent contents, reference/port sources,
  encode-side lanes, writer worktree files (git-show only + black-box runs), liblzraven src/*.c internals
outputs: +2 clauses (CR-015/016 MEASURED), tag mix total MEASURED 12 / SYMBOL 2 / INFERRED 2;
  A-013 + A-014 + NOTE-14 (H correction) + VERIFY x8 PASS (0 new FLAGs)
findings:
- TYP H real (12th kind): writer-crafted + oracle-parsed; own census CORRECTED (11->12); CLI 'h' = H filter
- bit0 rule: incompressible block -> raw verbatim (6/6 size-exact, 5/5 roundtrips); pure-random aa inners outer-stored
- B/C extract always-fails incl root (capability, not privilege); unknown-TYP silent-skip accepted (writer-measured); W/R/T loud-vs-skip UNRESOLVED
- joint DONE not reached (writers mid-turf; claim HELD)
pre-edit: spec/CLAUSES-DECODE-VIEWER.md sha256:135db0a2ee5fd0697e917abb4137dada756aac6b3f2f0a3e5f6c3298cb7bed35 bytes:14269
pre-edit: spec/DERIVATION-DECODE-VIEWER.md sha256:7926c122762e351d6677f879815ed21ce0abc108e1f2b3c2c436186a53220651 bytes:9930
post-edit: (recorded at commit; see commit 2nd line stats)

## 2026-10-07 decode-viewer lanes/decode-viewer (entry 6: CR-017/018/019 + A-015/016/017/018 + VERIFY x37)
inputs:
- quiz-decode Q-015/Q-016/Q-017/Q-018 + PARENT-001..008 + writer2 NOTE-051..063 + writer1 NOTE-024 + sweep NOTE-009/010/014 (read first-hand; answered A-015..A-018)
- own-gen cluster2/: in-256M1.bin + c2-sha.aea (268472541B) + c1-18.aea + c2p-sha.aea (276824064B) + walk.py + flip matrices (WS tmp/decode-viewer-probes/cluster2; macOS 27.0.1)
- own-gen padauth/: p-18/p-18b/p16-18.aea + padsearch.py (MAC-search v1, 0 hits) + segdump TEXT dump + xref/capstone reads (WS tmp/decode-viewer-probes/padauth)
- own-gen q018/: raw single-file archive + 8 TYP-flip extracts (WS tmp/decode-viewer-probes/q018)
- /usr/bin/aea sha256:16bfbb1c09b092ef0996191ba5e152485fad40be8b28736bf40f68f1628e6c10 MATCH
- /usr/bin/aa sha256:823df81f1c4331d1e36eee38b20b71a76f016835a01c68d863ce5d8fcb280ef4 MATCH
- libAppleArchive.dylib __TEXT self-dump (630836B, own-session addrs): pad-auth routine + caller window read via capstone (behavior extraction: streaming digest, "AEA_PAK" functional label, const-time compare; procedures/addresses stay in WS probe records, never in quiz/spec) [scrubbed entry-8: code addrs + internal names removed]
- writer2 proto/aead.py (read full decrypt path + ran for walks/searches/parity: viewer privilege) + notes/APROBE-01.md (read first-hand)
- writer1 notes/DPROBE-04.md (read first-hand) + fixtures bdev-basic/mix-fail.aea (pins re-verified own + oracle extract first-hand)
- kinnay/AEA + ipsw-aea OSS (read for pad-auth; DRY, no container-pad coverage)
- writer commits verified first-hand (full diffs + wall greps 0/37): w2 d6df55e 5bf50fd 158d434 8818e05 1528d04 327831f e253e4d 9d45117 9ad63af 196d115 0f41f20 b13df0f a59c9cd 96f0ea8 944cc08 2f960ae 01170b2 7446cc2 c617d73 2d300d7 24a8d56 d445282 ce4315f b8abeb2 87313db 454d5c2 3661b43 8ec8dab 0365e18 163a1e3 ad33592 d79a170 5535467 9fd0936 2a59c5c 33cc27b; w1 2ad1b1e
not-consulted: patent contents, encode-side lanes, reference/port sources,
  Ghidra/IDA-class decompilers (none installed; capstone-on-own-dump used instead),
  writer worktree files (git-show only + black-box runs), liblzraven src/*.c internals
outputs: +3 clauses (CR-017/018/019 MEASURED), tag mix total MEASURED 15 / SYMBOL 2 / INFERRED 2;
  A-015 + A-016 (partial: ranges closed, construction open) + A-017 + A-018 + NOTE-16..22 + VERIFY x37 PASS (0 FLAG)
findings:
- cluster walk closed (offsets/repeat/continue/N-global/equations) + 2-cluster MT flip matrix; -o-target head-code dependence found+resolved (NOTE-22: /dev/null 0x9e05cc00 vs file 0xba006800)
- pad ranges closed ([padstart,arc), arc-ignored, read-vs-auth classes); tag outside pad (2B proof); construction still open (MAC-search v1 0 hits; setup-callee reads queued) [scrubbed entry-8]
- Q-017 premise refuted (proto verifies via explicit HMAC 8/8); W/R/T/M dispute closed (silent-skip stands, A-013 corrected)
- joint DONE not reached (Q-016 construction + sweep-v3 + writer DONEs pending; claim HELD)
pre-edit: spec/CLAUSES-DECODE-VIEWER.md sha256:4bd81b4599c1e6e2f500044ba17f6e88d51d8dfda502cf2259dfc4a5b348d724 bytes:16402
pre-edit: spec/DERIVATION-DECODE-VIEWER.md sha256:4c1b7baff5dbd183d84150d2a2aa9dc046598b9614c7e8cf0e944c337af73b5e bytes:11719
post-edit: (recorded at commit c9ffd27; 2 files, +57)

## 2026-10-07 decode-viewer lanes/decode-viewer (entry 7: CR-020 pad-tag rule + A-016B + PRE-003/004)
inputs:
- quiz-decode writer2 NOTE-072 (HOLD on A-016(3)) + writer1 NOTE-029 (fuzz adler hole) + sweep GATEs 9fd0936/2a59c5c/33cc27b (read first-hand)
- own-gen padauth v2: padsearch2.py (1848 combos x3 files, HIT 3/3) + padconfirm.py (c2p last-nmac + fresh p1-3m + p5none-3m, ALL-CONFIRMED) + unpadded negatives c1-18/c2-sha (WS tmp/decode-viewer-probes/padauth)
- own-gen adler/: hello-zlib.aar + 7 wrapper/trailer/stream flips vs oracle (WS tmp/decode-viewer-probes/adler)
- own TEXT-dump reads: setup-callee crypto-dispatcher arms + caller-xref survey (auth routine invoked via pointer, 0 direct xrefs; frame-shared split pair) [scrubbed entry-8: code addrs + internal names removed]
- fixtures hello-zlib.aar + hello-raw.aar (wt-fixtures copies, read-only)
not-consulted: patent contents, encode-side lanes, reference/port sources,
  writer worktree files (git-show only + black-box runs), liblzraven src/*.c internals
outputs: +1 clause (CR-020 MEASURED), tag mix total MEASURED 16 / SYMBOL 2 / INFERRED 2;
  A-016B + PRE-003 + PRE-004 + NOTE-23/24
findings:
- pad-tag construction CLOSED: last-nmac = HMAC-SHA256(HKDF(main,"AEA_PAK"), [padstart,arc)); 6/6 + 2/2 negatives; Q-016 fully closed, writer2 unblocked
- zlib wrapper-ignored rule replicated (CMF/FLG/adler unchecked, raw inflate; deflate-data corruption -> header-parse abort); pre-answered writer1 case188 via PRE-004
- joint DONE not reached (writer2 verify-or-reject + sweep-v3 + DONEs pending; claim HELD)
pre-edit: spec/CLAUSES-DECODE-VIEWER.md sha256:98aeea34c2dd6df8d8437d03659fbb0bba06f3c6025987fc34f5d8bcee467a4f bytes:19806
pre-edit: spec/DERIVATION-DECODE-VIEWER.md sha256:a37f52800bed89378f08898f83167e16d7291828d8319ba2f4fa02fb707ddfcd bytes:14990
post-edit: (recorded at commit 625dc1b; 2 files, +29)

## 2026-10-07 decode-viewer lanes/decode-viewer (entry 8: wall-hygiene scrub, no behavior change)
inputs:
- quiz-decode writer2 NOTE-074 (quarantine handling of NOTE-19/PRE-003 internals) + NOTE-030/031 + PV-006 (read first-hand)
- own filings re-read: NOTE-19/PRE-003/NOTE-20 (scrubbed of code addrs + internal names, behavior kept) + this log entries 6/7 (same scrub)
- writer commits verified first-hand (full diffs + wall greps 0/2): w2 a5f53e3; w1 4ef6d9e (fuzz legs + 3 fixes, proto central len-guard confirmed covering zlib fallback)
not-consulted: patent contents, encode-side lanes, reference/port sources,
  writer worktree files (git-show only + black-box runs), liblzraven src/*.c internals
outputs: 0 clauses (mix unchanged MEASURED 16 / SYMBOL 2 / INFERRED 2);
  NOTE-25 (incident record) + NOTE-26 + VERIFY-a5f53e3 + VERIFY-4ef6d9e (PASS, 0 FLAG)
findings:
- symbol internals crossed into shared quiz via NOTE-19/PRE-003 (code addrs + internal names); writer2 self-quarantined with zero-hit proof; scrubbed own filings + log entries; mechanism fix (behavior-only quiz filings) in NOTE-25
- VERIFY current thru both tips (39 PASS total, 0 FLAG); PV-006 merged viewer@c9ffd27 + writer2@33cc27b
- joint DONE not reached (writer2 pad-verify + sweep-v3 + DONEs pending; claim HELD)
pre-edit: spec/CLAUSES-DECODE-VIEWER.md sha256:ef4a24537a0562cc6b7cd9f1647ec5c761f7967c6050da50791ad94521c8e6e6 bytes:20738 (unchanged this entry)
pre-edit: spec/DERIVATION-DECODE-VIEWER.md sha256:e281984805ac98a4338436d0eb254a29139804055a2a0ceeb99b0cdfeb9cc6bf bytes:16834 (at 625dc1b; entry covers scrub + this entry)
post-edit: (recorded at commit 1f6b710; 1 file, +20/-3)

## 2026-10-07 decode-viewer lanes/decode-viewer (entry 9: CR-021 export inventory)
inputs:
- dyld_info -all_dyld_cache -exports (macOS 27.0.1, arm64e) first-hand -> WS aa-exports.txt + aa-block.txt (409MB full dump deleted post-extract)
- lanes/vendor-docs docs/API-SYMBOLS-L2.txt (232 names, read first-hand; setdiff EMPTY both ways own)
- own lane docs/RECON-DECODE.md CR-002/003 import enumerations (re-confirmed resolving)
not-consulted: patent contents, encode-side lanes, reference/port sources,
  decompiler output (none), writer worktree files, liblzraven src/*.c internals
outputs: +1 clause (CR-021 SYMBOL), tag mix total MEASURED 16 / SYMBOL 3 / INFERRED 2; NOTE-27
findings:
- dylib public surface fully enumerated (232 = 185 AA + 47 AEA); three-way cross-check exact; full public decode surface listed (CLIs bind a subset)
- joint DONE not reached (writers/sweep active, no DONEs; claim HELD)
pre-edit: spec/CLAUSES-DECODE-VIEWER.md sha256:ef4a24537a0562cc6b7cd9f1647ec5c761f7967c6050da50791ad94521c8e6e6 bytes:20738
pre-edit: spec/DERIVATION-DECODE-VIEWER.md sha256:7117916cf132579ab38308d905d3d82873e5247ceb8fe865e0d1dac1d3ffd31c bytes:18613
post-edit: (recorded at commit; see commit 2nd line stats)
