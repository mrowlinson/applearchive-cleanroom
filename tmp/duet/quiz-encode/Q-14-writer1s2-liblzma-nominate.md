# Q-14-writer1s2-liblzma-nominate

## OSS nomination: liblzma (XZ Utils) for lzma codec bytes (PARENT-003 gate 1+3)

Finding (own beds, first-hand): oracle lzma = stock liblzma preset-6 check-none
LZMA bytes, byte-identical 12/12 beds (single/multi-chunk/multistream/stored-mix).
Only the XZ block header/index packaging differs (oracle b0 rule + pad-excluded
sizes — my own framing code, no OSS). Verified identical on system 5.4.3 AND
brew 5.8.4 (stdlib lzma + xz CLI 4-way match).

Request:
1. Survey entry: liblzma / XZ Utils, public-domain, source https://xz.tukaani.org/xz-utils/.
2. Pin strategy: BOTH 5.4.3 (system) and 5.8.4 (brew) verified byte-identical LZMA
   bytes on all beds — pin "preset 6, either version" or name one?
3. C-port: link system liblzma (same gates per PARENT-003.4) — concur?
