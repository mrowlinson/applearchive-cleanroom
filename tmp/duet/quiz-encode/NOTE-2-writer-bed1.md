# NOTE-2 writer bed1: raw AAR framing derived black-box (own probes)

- oracle: /usr/bin/aa, macOS 27.0.1. probes: probe1 (empty/emptyfile/
  onefile x lzfse+raw), probe2 (0/1/6B content, determinism), probe3
  (mtime sweep). all exit 0, stderr empty.
- sizes: empty-dir=141B, 1-emptyfile=199B, 1x5B-file lzfse=237B /
  raw=362B, 1x0B raw=237B, 1x1B=238B, 1x6B=243B. +1 content B = +1B.
- determinism: same tree twice -> byte-identical (d1a==d1b, sha
  5e00101c...). pins valid.
- outer: -a raw -> no wrapper, starts "AA01". default lzfse ->
  "pbze" wrapper (empty=141B: pbze hdr + AA01M entry inside).
- entry: "AA01" + kind1B + 0x00. kinds seen: M(root dir), X(file),
  P(subdir). then fields.
- field: key3B + kind1B + payload. kinds derived:
  '1' u8 (GID=0x14=20 staff; FLG=0x00), TYP'1' value 2B ("DP" dir,
  "FP" file).
  '2' u16le (UID=0x01f5=501; MOD file 0x01a4=0644, dir 0x01ed=0755).
  'P' u16le len + bytes (PAT path; dir "" len0; file "f.bin" len5).
  'S' u64le seconds (CTM/MTM when nsec=0; e1 field == stat mtime
  978325200 exactly; e2 == 1592238896).
  'T' 12B timespec (CTM/MTM live files: u64 sec + u32 nsec presumed;
  offsets verified, split UNRESOLVED -> Q-5).
  'A' u16le len + OUT-OF-LINE payload (DAT content nB then XAT
  value 36B; hdrs-first payloads-after, 3/3 lengths 0,1,6 + 9B
  case agree; multi-A order rule UNRESOLVED -> Q-5).
- XAT'A' value 36B = u32le 0x24 + "com.apple.provenance\0"(21B) +
  11B blob 01 02 00 66 97 d0 7a bb 10 2c 73, IDENTICAL all 8
  probes (dirs+files, all mtimes). const-candidate -> Q-5.
- mtime: file mtime touches exactly 8B (2x u32/u64 sec slots at
  entry off ~153,165 abs); dir entry untouched by file touch.
- exhibits: own worktree tmp/scratch-encode/out/*.aar (d0,d1a,d1b,
  d6,e1,e2,empty,onefile*). next: xattr/symlink/mode/nest/70KB/pbze.
