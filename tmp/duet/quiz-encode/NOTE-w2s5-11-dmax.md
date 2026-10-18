# NOTE-w2s5-11 writer2: D-MAX = 65535 exact + length frontier + chunk-cap note

- D-MAX CLOSED: matches emitted at D=65280/65408/65500/65520/65530/65535
  (L=256, nl=0, period EXACT = D). format ceiling (u16) IS encoder ceiling.
  D=81536: all-literal (unrepresentable ✓). predecessor TBD closed.
- LENGTH FRONTIER (min-L for match, in-chunk): D=1K:(32,64], D=8K:(64,128],
  D=16K:(128,256], D>=48768: <=256. threshold DOUBLES with D (1K->16K).
- METHOD trap: chunk dlen cap = 32768; repeats crossing into a trailing
  uncompressed chunk read as nl=0 = FALSE "matched". all frontier cells
  re-bedded in-chunk (offset-source K=4096 for deep D). dmax.py kept.
- Q-22 open (ff-slot mechanism). claim HELD.
