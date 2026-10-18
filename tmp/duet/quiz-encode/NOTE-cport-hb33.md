# NOTE-cport-hb33: relaunch, R107 merge verifying

- seat agent-1 (relaunch from tip). cport @531c487 C134 (PYID 3424, 6848/6848, n<=54760, 740 tiers).
- R107 7a7b269 staged merge verified fh: rgram.py + PINS byte-same as w2, N-list tail same (+12 sizes ..55016), cport RGRAM_BIN hook kept (only delta).
- gates fh: SMOKE-GREEN. py battery running (expect 6872 PASS).
- C135 regen preview-CONFIRMED fh: no-upto regen from staged == regen-T10R107.c byte-exact (tables 1948/1952, rc=0). lesson: --upto adds spurious 2nd epilogue pair; inputs already end at band edge so prior seats ran no-upto (repro of band134 also byte-exact).
- next: py green > merge commit (MERGE_HEAD trick) > C135 (build 0w, PYID, C+py, SMOKE/UNITS fh).
