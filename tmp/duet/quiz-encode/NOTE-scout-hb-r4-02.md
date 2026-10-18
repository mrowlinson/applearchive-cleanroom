# NOTE-scout-hb-r4-02: heartbeat (codec map pinned, q8/q9 scoping)

- Codec->pbz* map MEASURED on own bytes (compressible input,
  payload magics agree with r2-06): lzma->pbzx (XZ FD377A),
  lz4->pbz4 (bv41), lzraven->pbzm (2B00CAEC), lzbitmap->pbzb
  (ZBM), lzfse->pbze, zlib->pbzz. Mnemonic is NOT
  codec-initial (lzma->x, lzraven->m) — naive guess would flip
  two cells. lz4_raw reconfirmed rc=1 usage error.
- Bycatch: random-corpus chunks store RAW (u==c, payload = stream
  bytes) on ALL four codecs — the r3-06 ZBM-or-raw rule
  generalizes: every codec raw-stores incompressible chunks.
  Same u across codecs (stream is codec-independent).
- Next: q8 sweep measurement (-b x 4 codecs, framing+monotonicity)
  then q9 verify/fix rc probes. Quiz unchanged (no scout Qs).
