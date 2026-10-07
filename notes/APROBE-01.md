# APROBE-01 AEA black-box probes (decode-writer2, oracle `aea`, macOS 27.0.1)

All own-measured via execution. Outputs in WS writer2/probes/ (scratch, uncommitted).
Notation: P# = probe id. Passwords/keys: `testpw32....` (38ch), `test-password-fixture`
(fixtures), key32.bin (32 rnd), ec-priv/pub.pem (P-256 openssl).

## Credential matrix (decrypt, all roundtrips cmp-clean own)

| prof | encrypt creds | decrypt creds | size@16B/-a none |
|---|---|---|---|
| 0 signed | -sign-priv PEM (sealed) or -sign-pub only (UNSIGNED, null sig) | -sign-pub PEM (nokey: `-sign-pub is required`; unsigned: `0xde13d800 Invalid signature` exit 1; `aea sign` seals -> MATCH) | 18796 |
| 1 symmetric | -key file | -key file / -key-value `hex:`/`base64:` (bare/0x REJECT `Error parsing key`) | 18636 |
| 2 sym+sign | -key + -sign-priv (else `Invalid options for profile`) | -key + -sign-pub | 18796 |
| 3 ecdhe | -recipient-pub PEM (else `-recipient-pub is required`) | -recipient-priv PEM | 18701 |
| 4 ecdhe+sign | -recipient-pub + -sign-priv | -recipient-priv + -sign-pub | 18861 |
| 5 scrypt | -password-value/-password-file | same | 18636 |

- -key-gen file = ASCII `hex:<64hex>\n` (69B). bare64hex/0x/base64-bare all rejected.
- pwfile rule EXACT own: bytes verbatim + chomp trailing [\r\n]+ only (exact/NL/CRLF/2NL CLEAN; spaces significant — stripped variant REJECTED; sweep NOTE-006 observation confirmed + fixed in proto).
- keyfile rule EXACT own: `hex:`/`base64:` text (trailing NL ok) parsed; else RAW byte-exact (32B+\n=33B REJECTED 0xcf058400; 31/33B same class).
- Magic: `AEA1` + u24LE profile @4 + u8 scrypt @7 (always 0 own) + u32LE auth-size @8.
- EC P-256-ONLY own: secp384r1/secp521r1 recipient-pub REJECTED (`Error parsing public key file`); secp384r1 sign-priv REJECTED (`Error parsing PEM blob 'EC PRIVATE KEY'`, p0+p2). No non-P256 oracle output exists -> proto P-256 path sufficient.

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
- raw cat(a.aea+b.aea): decrypt = FIRST archive only (trailing bytes ignored); proto agrees. Raw cat != append.
- `aea sign` on p5: `This archive profile can't be signed`.

## Determinism / id

- Nondet from byte 13 (1-based) own, all modes/threads (salt/nonce region).
- `aea id`: deterministic 64-hex/file; auth-data changes it.
- `aea id` requires FULL prologue: trunc keep<156 FAIL (`0xb9045000`); keep>=156 prints full id (auth12B: 167 FAIL / 168 OK). Proto enforces len<n (cells err-id-trunc100/155, id-trunc156).

## Errors (own chains, exit 1 unless noted)

- wrong-pw / prologue-corrupt(8..155): `Failed to unlock container / Error 0xde108400 / HMAC / unlock container`.
- seg-corrupt(>=156): `Decryption failed / Authentication failed / Error 0xde108400 / HMAC / decrypting cluster / unlocking next cluster / Segment load / byte stream read error / Stream processing cancelled`.
- PAD-AUTH own (padded files): flips in [18620+IN, EOF) -> `0x9e041c00 / authenticating padding / Padding authentication` exit 1. padstart EXACT = 18620+IN (16B->18636, 18B->18638, 3MB->3018620). Proto GAP: accepts (exit 0) — Q-016 open for rule bed.
- SEG-N own (multi-seg): segment-data flips -> `0x9e05cc00 / Multi-thread read / HMAC / decrypting segment / decrypting segment N` (N = 1MB-seg index from file off 18620). Proto parity OK (exit 1).
- magic-corrupt: `Context creation failed / Error 0xcf00d800 / Invalid magic bytes / Invalid magic`.
- trunc keep<12: `Context creation failed / 0xb9041c00 / reading magic`; keep 12..155: `0xb9045000 / reading prologue`. Boundary EXACT @12.
- trunc keep>=156: `Decryption failed / Authentication failed / Error 0x9e015800 / loading cluster header / unlocking next cluster / Segment load / byte stream read error / Stream processing cancelled`.
- profile-corrupt (0x51): `Context creation failed / 0xcf00e400 / Invalid profile: 81 / Invalid magic`.
- scrypt-strength=3 (valid, wrong N): unlock-fail HMAC class. strength=9: `Failed to unlock container / 0xde0d0000 / Invalid hardness parameter / Main key derivation failed (-5) / Main key derivation / unlock container`.
- authsize-huge: prologue class (0xb9045000) exit 1. Missing creds: `-sign-pub is required` etc, exit 1.
- stderr text beyond exit-class = POLISH, out of CLI-CONTRACT (per writer1 NOTE-011; bytes+exits gated). Proto v1 emits own `aead:` lines.
- `-o -` writes literal file `-` (exit 0); omit -i = stdin CLEAN; omit -o = stdout (A-001; own stdin confirmed).
- `-i -` = LITERAL path (missing -> `Error creating I/O streams / 0x9106b002`, exit 1), NOT stdin. Proto parity: absent -i/-o = stdio, `-` = literal (cells stdin/stdout/dash-o-literal).
- range clamps, never errors: 0/17->16B, 16/1->0B, 100/10->0B, exit 0.
  offset-without-size reads to end (off6->tail, off0->full, exit 0); explicit size 0 -> empty, exit 0.

## Verbose manifest (-v decrypt)

`Operation/input/output/profile-string/worker threads/auth data: N B/compression: <alg> 1 MB/checksum/archive identifier/raw data size/container size/MB/s/total time`.
Encrypt adds `padding:` line. Encrypt to /dev/null fails (temp+rename).

## Gaps (Q or v2)

- murmur64a DONE (A-010 path-line; own routine, cksum-murmur + big MATCH).
- lzraven DONE (A-011 bed + liblzraven @700b88c nomination; own-built lzraven_dec via LZR_BIN).
  Framing own-confirmed on AEA seg: 244B = 8hdr + [4+148] + [4+76] + term, end-exact;
  nblocks 2 == ceil(900000/512K); params i=15 size 917504 smallest>=900000 (resolves A-011 §4 CHECK: 2 blocks, not 1).
  BCJ flags=0x002 fired own (own-built Mach-O input) -> proto MATCH.
  In-stream raw (bit0) FIRED own, both paths (bit0sweep.py, WS probes/bit0/):
  raw compression_tool 10/10 end-exact + 10/10 lzraven_dec TOOL-MATCH; bit0 on
  incompressible 512K blocks (random 3/3, rand-then-text blk1, text-then-rand
  blk3, half-text blk3). AEA segs 10/10 proto cmp OK; bit0 fired 1 block
  (rand-then-text seg1 0x1) -> MATCH via tool. Rule: bit0 = raw block for
  incompressible content, per-block; fully-random AEA input stores at segment
  level (decomp uncalled). Q-014 self-closed for AEA turf; battery 4b cells.
- auth-data>0 MAPPED own: prologue = 156+authsize (2-blob auth12B flips unlock/decrypt @167/168); kv-form = u32LE pair + key\0+value (own-confirm FORMAT.md); both MATCH in proto.
- auth edges own: 3-blob MATCH (cell auth-raw3); EMPTY auth-data-value REJECTED at encrypt (`Invalid auth-data-value`, raw + kv). Empty password REJECTED at encrypt (`Invalid password / Error loading credentials`).
- `-keychain` flows (OUT of scope, touches system store). lzvn `f` (no oracle -a flag; skip).

## Wide corpus (tests/aea-wide.sh v3, 168/168 WIDE-GREEN)

- FULL-equiv seed 7: 8 sizes (1B..3MB) x p{1,5} x {none,zlib,lzraven} x {none,sha256} = 96 MATCH.
- FULL lzraven-text (compressible): 8 sizes x p{1,5} x {none,sha256} = 32 MATCH.
- Holdout seed 99: 4 sizes x {p1/lzma/sha, p5/lz4/none, p1/lzraven/murmur64} = 12 MATCH.
- Fresh seed 1234: 4 sizes x {p1/lzfse/sha, p5/lzbitmap/none, p5/lzraven/murmur64} = 12 MATCH.
- v2 adds LZR_BIN export (v1 lacked it: lzraven never ran in wide) + first murmur64 wide cells.
- v3 adds padded leg: 4 sizes x p{1,5} x {zlib,lzraven} x sha256, default pad = 16 MATCH.
- 2-cluster: 269MB p5/none/sha256 OVH 37084 = 18620+18464 (2nd cluster hdr); proto MATCH 0.8s.
- SPLIT RULE EXACT own (checksum-none, -a none): 1 cluster iff IN <= 268435456 (256MiB); 268435457 -> 2 clusters. Points: 200/255/256MB OVH 10428 (1 cl); 256MiB+1/257/260MB OVH 20700 (2 cl). Fits segcount>256 @1MB segs. (Q-015 Q1 self-closed; Q2 header-walk still open for viewer.)
- SPLIT RULE GENERAL own (p5/-a none/cksum-none, zeros): clusters = ceil(IN/256MiB); 512MiB OVH 20700 (2 cl), 512MiB+1 OVH 30972 (3 cl). Per-extra-cluster delta 10272 (OVH = 10428 + (N-1)*10272 this shape; sha-shape differs: 18620+18464/cluster). Proto decrypts 3-cluster MATCH 1.1s (chaining blind, works). Q-015-Q1 scope now fully closed own (1->2->3 splits); Q2 walk still viewer-open.
