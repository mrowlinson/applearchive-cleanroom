# NOTE-w2s7-8 writer2: -t EQ matrix + -b echo + big blocks (5ada55e, 284 pins)

## -t byte effects: NONE (10/10 EQ, closes A-7 OPEN item)
- 5MB z/r x raw/zlib/lzma t1-vs-t18 EQ (6) + 10MB z/r lzfse EQ (2) +
  prior 5MB lzfse EQ (2). thread count never changes bytes.
- cells: TCMP cmp+sha (m-tt-*). all EQ pinned.

## -b values: all accepted, BE echo exact (4 cells m-bb-*)
- 1m->1048576:5, 64k->65536:77, 4096->4096:1221, 16m->16777216:1
  (nb @5MB zeros lzfse). echo+nb str + sha pinned.

## big multi-block (4 cells m-bg-*, CHAIN-EQ all)
- 10MB def: NB3 SU10000223 (z+r); -b 1m: NB10 SU10000223 (z+r). sha pinned.

## flake found + fixed (5a83dc4, pre-existing AEA cells)
- 1/14 runs RED: a-p0/p2/p4 rc + a-rt-p3 RT-DIFF. root: aea REJECTS EC
  privkeys whose DER OCTET is 31B (LibreSSL strips leading zero when
  priv<2^248, ~1/256 keys). proof: same key value hand-padded 31->32B
  => ENC-OK + RT-OK; `openssl ec` re-output does NOT pad (still fails).
- fix: keygen loop until der[6]==0x20 (max 10). validated REJECT/ACCEPT
  on bad/good keys + 3x GREEN. pins untouched (append-only +32, 0 churn).
