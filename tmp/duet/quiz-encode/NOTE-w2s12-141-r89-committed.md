# NOTE-w2s12-141: T10R89 COMMITTED @0022950

- tier: 48149..48404 (256 cells, single 16x16, no quad/B split).
  m-tab 7B b29-31,72-75 16/16 NEW; q-tab 7B b14,22,23,68-71
  16/16, tail-4 = P90M tails 16/16 (30th); b4=(0x2b+2off),
  b5=0x78+(off>=107)+(off>=235); 64 consts.
- gates: probe 256/256 CLOSED, storm 8/8 (dbl-carry edges),
  pins +26 pure, bat91 rc=0 RGRAM-GREEN 0 FAIL, SMOKE-GREEN.
- Q-54 open (A pending). PRE-1265b/1266b on file (P91/R90).
- frontier n=48404. next: T10P91 (gen validated 164L, census
  on disk, matches PRE-1265b).
