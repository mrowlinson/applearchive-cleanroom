# A-15 AEA -a matrix: 8 accepted (7 + raw-alias), NO plaintext codec field (MEASURED)

## (a) accepted values: 7 documented + undocumented `raw` (= none)
- own beds (WS scratch-viewer3, profile 1, fixed key): none/lzfse/lzma/lz4/zlib/lzraven/lzbitmap ALL
  rc=0 (matches `aea --help` list). PLUS `-a raw` rc=0 — behaves as none (zeros-100k: raw 118784B ==
  none 118784B; both decrypt RT-clean). so the AAR-outer 7 ⟷ AEA 7 correspondence holds, with raw
  as an 8th accepted alias of none.
- YES, same 7 as AAR outer (none/lzma/lz4/zlib/lzfse/raven/bitmap — help order differs, set same).

## (b) codec manifestation: encrypted region ONLY — no stable plaintext field
- header first-12B IDENTICAL across all 8 values (AEA1 01 00000000 00000000, own hex). beyond @12,
  bytes are ciphertext: same-alg rerun agrees only 127/24576 (~chance; 1/256 = 96 expected + 12 hdr).
  every "stable-across-rerun" offset past 12 differs across algs identically = chance collisions, not fields.
- observable codec effect = SIZE on compressible input (zeros-100k: none/raw 118784 vs all 6 codecs
  19456 — codecs collapse equal here since padding quanta dominate; urandom-5k: all-7 24576 equal).
  segment-level codec IDs (PRE-001 OPEN item) therefore live INSIDE the encrypted envelope: unbeddable
  from ciphertext. decrypt-then-inspect is decode-side territory — flag it there, don't chase here.
- pins for your battery: per-alg SIZE on zeros-100k (118784/19456 split) + hdr12 const + RT-clean.

## (c) unaccepted -a: hard error, no fallback
- `-a bogus`: rc=1, stderr `Invalid compression algorithm: bogus` + full usage dump. no fallback.
