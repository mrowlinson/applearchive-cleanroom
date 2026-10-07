# APROBE-01 AEA black-box probes (decode-writer2, oracle `aea`, macOS 27.0.1)

All own-measured via execution. Outputs in WS writer2/probes/ (scratch, uncommitted).
Notation: P# = probe id. Passwords/keys: `testpw32....` (38ch), `test-password-fixture`
(fixtures), key32.bin (32 rnd), ec-priv/pub.pem (P-256 openssl).

## Credential matrix (decrypt, all roundtrips cmp-clean own)

| prof | encrypt creds | decrypt creds | size@16B/-a none |
|---|---|---|---|
| 0 signed | -sign-priv PEM | -sign-pub PEM (nokey: `-sign-pub is required`) | 18796 |
| 1 symmetric | -key file | -key file / -key-value `hex:`/`base64:` (bare/0x REJECT `Error parsing key`) | 18636 |
| 2 sym+sign | -key + -sign-priv (else `Invalid options for profile`) | -key + -sign-pub | 18796 |
| 3 ecdhe | -recipient-pub PEM (else `-recipient-pub is required`) | -recipient-priv PEM | 18701 |
| 4 ecdhe+sign | -recipient-pub + -sign-priv | -recipient-priv + -sign-pub | 18861 |
| 5 scrypt | -password-value/-password-file | same | 18636 |

- -key-gen file = ASCII `hex:<64hex>\n` (69B). bare64hex/0x/base64-bare all rejected.
- pwfile: exact bytes CLEAN; trailing `\n` also CLEAN (NL-tolerant).
- Magic: `AEA1` + u24LE profile @4 + u8 scrypt @7 (always 0 own) + u32LE auth-size @8.

## Size rules (own, -a none unless noted)

- OUT = IN + 18620 for all IN in 1B..2MB, p5/sha256 (9 points, no 64K/256K/1M steps).
- 18620 = 156 prologue + 18464 fixed segment area (256-entry table, checksum-mode sized).
- empty IN -> 156B total (prologue only); decrypts to 0B exit 0.
- checksum mode sizes @16B/p5: none=10444, murmur64=12492, sha256=18636 (default=sha256).
- prologue = 156B PROVEN 3 ways: empty size; corrupt flip boundary 155/156; trunc boundary 155/156.
  Holds p1+sha256, p5+sha256, p5+none.
- -b {64k,1m} no size effect @300KB. -a {zlib,lzma,lzfse} on 100B rnd: IN+18620 (stored).
- padding @16B: none 18636 / adaptive 19456 (=default) / 16->18640 / 4096->20480 / 65536->65536.
- append: +N bytes for N appended (19B->+19, 1MB->+1000000, 0 table growth); decrypt = concat.
- `aea sign` on p5: `This archive profile can't be signed`.

## Determinism / id

- Nondet from byte 13 (1-based) own, all modes/threads (salt/nonce region).
- `aea id`: deterministic 64-hex/file; auth-data changes it.

## Errors (own chains, exit 1 unless noted)

- wrong-pw / prologue-corrupt(8..155): `Failed to unlock container / Error 0xde108400 / HMAC / unlock container`.
- seg-corrupt(>=156): `Decryption failed / Authentication failed / Error 0xde108400 / HMAC / decrypting cluster / unlocking next cluster / Segment load / byte stream read error / Stream processing cancelled`.
- magic-corrupt: `Context creation failed / Error 0xcf00d800 / Invalid magic bytes / Invalid magic`.
- trunc keep<12: `Context creation failed / 0xb9041c00 / reading magic`; keep 12..155: `0xb9045000 / reading prologue`. Boundary EXACT @12.
- trunc keep>=156: `Decryption failed / Authentication failed / Error 0x9e015800 / loading cluster header / unlocking next cluster / Segment load / byte stream read error / Stream processing cancelled`.
- profile-corrupt (0x51): `Context creation failed / 0xcf00e400 / Invalid profile: 81 / Invalid magic`.
- scrypt-strength=3 (valid, wrong N): unlock-fail HMAC class. strength=9: `Failed to unlock container / 0xde0d0000 / Invalid hardness parameter / Main key derivation failed (-5) / Main key derivation / unlock container`.
- authsize-huge: prologue class (0xb9045000) exit 1. Missing creds: `-sign-pub is required` etc, exit 1.
- stderr text beyond exit-class = POLISH, out of CLI-CONTRACT (per writer1 NOTE-011; bytes+exits gated). Proto v1 emits own `aead:` lines.
- `-o -` writes literal file `-` (exit 0); omit -i = stdin CLEAN; omit -o = stdout (A-001; own stdin confirmed).
- range clamps, never errors: 0/17->16B, 16/1->0B, 100/10->0B, exit 0.

## Verbose manifest (-v decrypt)

`Operation/input/output/profile-string/worker threads/auth data: N B/compression: <alg> 1 MB/checksum/archive identifier/raw data size/container size/MB/s/total time`.
Encrypt adds `padding:` line. Encrypt to /dev/null fails (temp+rename).

## Gaps (Q or v2)

- murmur64a vectors (Q-010 open). lzraven seg codec id `m` (Q-011 bed open; compression_tool cross-check MATCH, proto fail-closed by design).
- auth-data>0 MAPPED own: prologue = 156+authsize (2-blob auth12B flips unlock/decrypt @167/168); kv-form = u32LE pair + key\0+value (own-confirm FORMAT.md); both MATCH in proto.
- `-keychain` flows (OUT of scope, touches system store). lzvn `f` (no oracle -a flag; skip).

## Wide corpus (tests/aea-wide.sh v1)

- FULL-equiv seed 7: 8 sizes (1B..3MB) x p{1,5} x {none,zlib} x {none,sha256} = 64 MATCH.
- Holdout seed 99: 4 sizes x {p1/lzma/sha, p5/lz4/none} = 8 MATCH. 72/72 WIDE-GREEN.
