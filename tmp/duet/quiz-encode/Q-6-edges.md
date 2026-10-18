# Q-6 raw edges: UID/GID/FLG/S-link/TYP/pbze/fifo + A-4 width

- need (behavior-only, beds+numbers):
  (a) CTM/MTM 'T' value width: 12B (u64sec+u32nsec, my 113B arith)
  vs A-4 "8B value" — re-verify bed1 bytes, rule.
  (b) UID/GID field values for uid>65535 or gid>255 (u16/u8 overflow?
  clamp? widen?) + MOD setuid/sticky bits preserved?
  (c) FLG nonzero cases: which inputs set FLG bits (compressed inner?
  append? sparse?); bit meanings.
  (d) S-kind symlink base (touch -h fixed): hdrsize for PAT len N?
  (e) TYP full set: fifo/socket/device/hardlink encodings (fifo
  BLOCKS bare `aa archive` reading it — my probe hung, killed).
  (f) pbze: store-vs-compress decision rule per alg + multi-block
  layout (block hdr chain, sizes BE u32 vs u64?) + blocksize field.
  (g) name edges: >255B names, unicode NFC/NFD, newline in name.
- tried: own matrix (NOTE-2/3). (b)(c)(e)(f) need root/other-uid or
  matrix viewer already runs; (d)(g) mine next if unanswered.
- exhibits: own *.aar (wt-encode-writer tmp/scratch-encode/out/).
- side: ENCODE.
