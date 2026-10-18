# GATE-34df169 sweep: PASS (C lz4 port; LZ4 4/4 py+C identical SHAs)

- tip: lanes/encode-writer @34df169 (parent 9895a19 gated PASS). src/c only
  (+435/-3: lz4c.h/c NEW + aae.c --alg lz4 hook + Makefile). py untouched.
- code read (ALL): lz4c.h (LZ4_BKT=(v*K)>>20>>1 swap-ready, 2048x5 table,
  64KB chunk, NEVER_K 127) + lz4c.c 381 lines (table lookup/put, emit_seq,
  chunk loop, pbz4 regroup bv41/bv4-/bv4$ + 16/15 store rule, empty-inner
  path) + aae.c hook (usage + pbz4 magic + wrap call) + Makefile (mechanical).
  mirrors lz4enc.py V0+K+A33; no OSS/disasm/vendor markers in new code.
- battery: GATE-PASS (outdir gate-w1-34df169-s4). C-BUILD w=0, RAWENC 13/13 +
  PBZE 10/10 + LZMA 6/6 + SMOKE 6/6 + UNITS 22 (py AND C), SMOKE-IMPL 6/6,
  PINS-RAWENC(-C) 11/11, PINS-PBZE(-C) 10/10, HYGIENE/GITIGNORE clean,
  LIBCOMP zero, ADOPT match.
- LZ4 manual (no framework leg yet — GAP): test_lz4.sh py 4/4 GREEN +
  C 4/4 GREEN, PASS lines diff-IDENTICAL (z1/r1/empty1/rzs oracle-identical
  both backends). finding-harness 672-cell claim NOT re-runnable (uncommitted
  scratch); VERIFY-34df169 PASS concurring cited, not relied on.
- CONTAM/OSS PASS first-hand re-verified: rawenc.py CDLL=/usr/lib/libc.dylib
  x2 (system-libc clean), pbze.py/aae.c lzfse nominated (PARENT-003),
  Makefile pinned liblzma 5.8.4 + A-20 cite. CPAT 0-hits, Mach-O 0-hits.
- FRAMEWORK BUG (verdict stands, fix to land): gate-tip.sh `echo "$DHITRAW"`
  interprets \n in match text (aae.c:328 %s\n) -> phantom F-fragments + grep
  stderr noise. fail-open fragments can't mask (real file always also
  checked); literal \c in match text WOULD truncate (real FN vector). fix =
  printf '%s\n'. noted for sweep-lane commit.
- coverage: 78/78 writer tips gated (78 battery-PASS, ZERO holds).
- viewer: VERIFY-34df169 PASS concur (build 0w, LZ4-GREEN C, 672/672, 488/184).
