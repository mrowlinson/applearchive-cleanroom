# NOTE-w2s12-145: T10B91 COMMITTED @5ff15f1

- tier: 48845..49100 (256 cells, 1st BLOCK regime). template 6B
  b18,19,72-75 = f(m) identical 16 blocks 256/256; per-block
  sig 14 distinct (k1=k2, k6=k7 share); q68 = P92M-tail4
  16/16 (32nd); b4=(0x9b+2off) global, b5=0x7d+(off>=51)+
  (off>=179); 64 consts.
- gates: probe 256/256 CLOSED, storm 8/8 (wrap edges),
  pins +28 pure, bat95 rc=0 RGRAM-GREEN 0 FAIL, SMOKE-GREEN.
- Q-56 open (A pending). frontier n=49100.
- next: T10P93 (gen validated 175L, census on disk, matches
  PRE-1269b).
