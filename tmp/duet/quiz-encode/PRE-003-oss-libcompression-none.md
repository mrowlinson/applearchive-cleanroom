# PRE-003 OSS libcompression survey: NONE-FOUND — no Apple encoder source exists (closes A-10 follow-up)

- survey (own, this shift): GitHub API search over org apple-oss-distributions for `compression`
  = 0 repos; for `lzfse OR lzma OR lz4` = 0 repos. Apple publishes NO Compression-framework
  encoder source (no libcompression release, no lzma/lz4/raven/bitmap encoder code, no license to record).
- contrast: LZFSE (the one Apple OSS codec) lives at lzlabs/lzfse, already nominated/used per A-10.
  everything else Apple-encoder is closed: bed-war is the ONLY path (consistent with PARENT-007(4)).
- consequence: no nomination will ever come from this direction; w1 lzma/lz4 hunt + w2 raven hunt
  proceed on oracles (ct + libcompression one-shots, beds-OK) + third-party OSS leads only.
- survey item CLOSED. no further Apple-OSS hunting unless a new release appears (re-check on OS bumps).
