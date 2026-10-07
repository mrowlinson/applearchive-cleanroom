# DPROBE-01 decode black-box probes (writer first-hand, oracle execution only)

Env: os 27.0.1 arm64; aa 527200B 823df81f...; aea 337040B 16bfbb1c...
Bed: tmp/decode-probes + tmp/decode-health (scratch, uncommitted).
All runs via adopted harness/oracle-adapter.sh unless noted direct argv.

## T0 baseline
- `sh tests/smoke.sh <workdir>`: 6/6 PASS, SMOKE-GREEN, exit 0.

## AAR magics (own encode, -t 1, same src tree)
- lzfse=70627a65 pbze, lzma=70627a78 pbzx, lzraven=70627a6d pbzm,
  zlib=70627a7a pbzz, lz4=70627a34 pbz4, lzbitmap=70627a62 pbzb,
  raw=41413031 AA01. All 7 encode exit 0.

## aar-list shape (lzfse, 3 files + 2 dirs)
- stdout: leading blank line, then 1 path/line:
  ``, a.txt, empty-sub, empty.txt, sub, sub/b.txt. exit 0.

## decode tree fidelity
- empty file (0B) + empty dir + nested sub/b.txt all reproduced; 3/3 cmp MATCH.

## determinism
- AAR lzfse re-encode: cmp clean = DETERMINISTIC.
- AEA p5 re-encrypt: cmp -l first diffs at 1-based bytes 13,14,15.

## AEA decrypt
- p5 password: exit 0, cmp-clean. p1 -key file: exit 0, cmp-clean.
- range -offset 4 -size 8 on 32B plain: exit 0, 8 bytes = plain[4:12] exact.
- wrong pw (32ch): exit 1, stderr 4 lines:
  `Failed to unlock container / Error 0xde108400 / HMAC / unlock container`.

## AAR errors
- 100B random: exit 1, stderr 5 lines incl `Error 0xbd035000`,
  `Invalid/non-supported archive stream`, `archive stream read error (header)`.
- trunc-20B of valid: exit 1, stderr 10 lines incl `Error 0xbd009800`,
  `Truncated block header (8/16 bytes read)`.

## extract -o behavior
- `aa extract -i t.aar -o o.bin`: exit 0, o.bin NOT created, tree extracted
  to cwd (-o ignored for extract). Stray home-root files removed same turn.

## fixture health (adopted vectors/selfgen, 13/13 shasum OK)
- 10/10: 7 alg decodes cmp-clean + empty-dir + p1 + p5 decrypts cmp-clean.
