# NOTE-w2s3-10 writer2: OSS read done, bitmap hunt plan

- OSS contact log (A-16 condition; pin 574abeae MATCHED
  first-hand): README.rst (14 lines) + libzbitmap.h (75) +
  libzbitmap.c (1184, full) READ. decisions-only; zero OSS
  bytes will enter src (hand-written impl only).
- format (own understanding): ZBM\\x09 magic; chunks u24
  len+decmp (final 6B zero-chunk); uncompressed iff len==
  decmp+6; compressed = 15B hdr + data + meta1(periods) +
  meta2(non-top bitmaps) + meta3(nibble bmap-nums + f-led
  repcounts) + trailing 17B (12x10b top table); bitmap op
  = 8B literal/backref-at-period; nums 0-2 meta2 / 3-14
  top / f repeat; initial period 8.
- OSS encode choices (hunt targets): 0x8000 chunking;
  greedy 8B matchfinder (cur-period + 1B-window + 2B-window
  same-first-byte, diff+digits cost, early exits); forced
  initial 0xff; top-12 by usecnt (ties first-seen); rep<=3
  trivial else f-scheme; overflow->uncompressed fallback.
- plan: build OSS in WS (never repo) -> differential bed
  (OSS vs lc-oracle, structural diff via own parser) ->
  hand-written prototype converges to oracle bytes; every
  decision bedded vs ORACLE (bed-war rule). raven parallel.
- next: OSS build + diff bed.
