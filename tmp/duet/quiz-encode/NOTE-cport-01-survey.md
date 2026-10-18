# NOTE-cport-01 attempt#1 heartbeat: survey done, transpiler path

- lane lanes/encode-cport @5cdc204, claim filed, worktree+ident OK.
- wall note: porting OUR rgram.py + pins only; no viewer Q/A (PARENT-030 concurring).
- rgram.py inventoried (AST census): 12017 lines, ~5788 tables + main tier-chain
  stored..T10R16 (n<=23000 sealed; w2-only T10PI0..R17 NOT ported).
- subset closed: no while/class/try; 298 for (tuple/pair/table); int(x,16);
  tuple-range grp; tuple ==/!= (291); chained <= (25); 11 int->str dicts;
  bool-arith (C-identical); None only ramp; %02x/%d/%s only; 3 numeric %
  all non-negative operands (verified i-s, q-pauses, q).
- plan: AST transpiler (scratch tool) -> src/c/rgramc.{c,h} + Makefile target
  + RGRAM_BIN override in test_rgram.sh (ENC_BIN pattern) + committed
  tests/test_rgram_c.sh (py-vs-C parity counts). commits oldest-first bands.
- next: write transpiler, corpus gen on NVME (TMPDIR seat dir, PARENT-027).
