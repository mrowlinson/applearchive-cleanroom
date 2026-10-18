# NOTE-6 writer: PBZE-GREEN 4/4, 15/16 rule, lzfse path done

- commit next: src/pbze.py + src/encode.py + tests/test_pbze.sh +
  vectors/pbze-PINS.csv. batteries: RAWENC-GREEN 8/8,
  PBZE-GREEN 4/4 (z1/r1/mb-5fr/mix), roundtrip via oracle extract
  all cells exit 0.
- store-vs-compress: per block, compressed iff comp*16 <= unc*15.
  100/100 fresh probes (60+40, 2 seeds sets). razor exhibit:
  n=600 unc833/oss781: 781*16=12496 > 833*15=12495 -> S by 1.
  exact-tie (==) never observed; <= assumed, flagged micro-gap.
- OSS lzfse == oracle frame bytes everywhere tested (single,
  5-block, mixed, last-frame-full). stored block == raw bytes.
- scope now: raw + lzfse byte-exact. remaining algs: zlib/lzma/
  lz4 (OSS-compare next, own probes) + lzraven/lzbitmap (viewer).
  + impl-backend adapter (BACKEND swap) + C port decision.
- gap: g6 DONE (lzfse). waiting A-6. no PARENT-*, no writer2
  filings in quiz-encode yet (claim only).
