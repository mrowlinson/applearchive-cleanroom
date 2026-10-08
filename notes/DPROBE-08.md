# DPROBE-08 outer u64 framing + chown-before-chmod (writer1, first-hand)

## Outer framing (revised; kills the zeros-field model)
- Prefix = magic `pbzX`(4) + bsize u64be (bytes 4..11). Bytes 4..7 are the
  bsize HIGH half, not a zeros field (P1: byte4=0xFF -> `invalid block size`).
- bsize valid iff 0 < bsize <= 0x8000000 (128MB; 0x8000000 ok / 0x8000001 bad
  first-hand). Else exit 1 + 4-line cascade, byte-IDENT:
  `Failed to create decompression stream / Error creating input stream /
  extract failedError 0x9404c000 / invalid block size`. Outdir stays empty.
- Block header = raw u64be + pay u64be (NO zero fields; P2/P3: z1/z2 high
  bytes feed the u64 values, named in the message). Invalid iff raw > bsize
  OR pay > bsize -> exit 1 + 12-line cascade incl blank line, byte-IDENT:
  `Extraction failed / extract failedError 0xbd009800 / istream read error /
  refill buffer / archive stream read error (header) / flushing shared
  buffer / Invalid block header payload=0x%llx raw=0x%llx block=0x%llx /
  <blank> / NOP received / processStream / decoder failed / stream cancelled`
  (lowercase bare hex; e.g. payload=0x125 raw=0x98d block=0x3e8).
- Check order: bsize-prefix first (beats prefix corruption, ord-A), then per
  block at header-read time (multi-block: block1 decodes, block2 header can
  still fail, mb-bad2), validation BEFORE data-availability (ord-T:
  pay-huge + truncated -> header cascade, not EOF error).
- Multi-block chains: inner = concat of decoded blocks; inner parse walks
  the whole concat (mb21: second archive's headers still extracted;
  TREE-MATCH both orders). C+proto chain walk already correct, now pinned.
- Removed: C `memcmp(d+4,"\0\0\0\0")` checks (also UB: NUL literal has no
  length) + proto zeros asserts. Both over-rejected; oracle has no such rule.

## Attr order: chown BEFORE chmod (seed-987654 case191)
- MOD=0xd6a4 (&07777=03244): oracle keeps 103244, old code left 101244.
- Root cause: chown(501,20) SUCCEEDS (own uid/gid) and successful chown
  strips SUID/SGID. Old order chmod->chown lost setgid; oracle orders
  chown->chmod (mode sticks). Proven by in-process stat bisection:
  3244 right after chmod, 1244 right after chown.
- New order everywhere (C apply_rest + proto apply_rest): XAT -> chown ->
  chmod -> times. XAT-first kept (mk566 probe); times last (no mode effect).
- Cell mode-suid pins stat 103244 oracle==mine + content match.
