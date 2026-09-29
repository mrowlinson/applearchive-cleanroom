# Research summary: AppleArchive Cleanroom Research Report

Source: `AppleArchive Cleanroom Research Report.docx`
Bytes: 3034051. SHA256: 8d7d8142aabbfeedc5cd492a1bd9d0438f61a6d7c4a3a720c64b203f2bce2bdd.
Filed: 2026-09-29. Derived summary only. Zero transcription.

## Derived findings (numbered fragments)

AAR container (all UNVERIFIED vs local `aa` bytes until probed):
1. Magic `AA01` = 41 41 30 31 @0x00. Legacy `YAA1` = 59 41 41 31.
   Backing: file.org page live, text confirms (see links).
2. 2-byte header-size int follows magic. Payload blobs stream after
   header, excluded from that size. Backing: file.org confirms.
3. Metadata keys 3-char ASCII, TLV-style, strict sequence.
   file.org-confirmed: TYP (entry type), PAT (path), UID, GID, MOD
   (permissions), DAT (blob size). Docx-only: SIZ, CMP. Treat SIZ/CMP
   as single-sourced claims until oracle-confirmed.
4. Codecs: LZ4, LZMA, zlib, LZFSE (matches scaffold). NEW name:
   LZBITMAP ("in newer versions", file.org). Single-sourced. UNRESOLVED.
5. LZFSE ~= zlib-5 ratio, faster, lower energy. Targets Apple Silicon.
   BSD ref impl exists (scaffold already cites). Avoid as cross-platform
   default (specialized).
6. Ext behavior: `.aar` = dir container; `.lzfse` = single blob; no-ext
   file -> `.lzfse`, folder -> `.aar`. UNVERIFIED locally.

AEA envelope:
7. Magic `AEA1` = 41 45 41 31. LE ints. Profile int selects alg combo.
   (Matches scaffold FORMAT.md notes.)
8. Primitives: scrypt KDF (pw -> key), AES-CTR payload (parallelism
   linchpin), ECDSA P-256 sig, ANSI X9.62 pubkey format.
9. Decrypted AEA payload ~= embedded AAR. Wrapper, not fs format.
   Single-hypothesis corroboration (archiveteam wiki). Still UNRESOLVED
   until local decrypt-own-key probe (JOBS #4).
10. Verify-before-decrypt flow: ECDSA check vs PEM pubkey, then AES-CTR
    stream into AAR pipeline. Symmetric key binary or scrypt passphrase.

API surface (names only, from public dev docs; no signatures pasted):
11. Classes/protocols: ArchiveHeader, ArchiveStreamProtocol /
    ArchiveStream, ArchiveByteStreamProtocol / ArchiveByteStream,
    ArchiveError enum, APPLE_ARCHIVE_API_VERSION const. Corroborate via
    browser read (JOBS #6). UNRESOLVED.

Prior art:
12. python-aea (kinnay = Yannik Marchand, MIT): Py lib + FORMAT.md.
    Scaffold already cites. Docx adds nothing new.
13. ipsw (blacktop, Go): firmware toolkit, decrypts AEA cross-platform.
    Pure-Go fallback `pkg/aea/decrypt.go` when native `/usr/bin/aea`
    missing/fails. Proves independent AEA decode viable. Behavior-level
    note only; never transcribe/port (wall).
14. Native `aea` failure modes reported: 0xba006800 stream-read error +
    "Decryption failed Authentication failed" on SystemOS DMGs (Apple
    Silicon resource contention alleged); Linux / `/tmp` runs fail
    (no such file / permission denied). Unreproduced locally. UNRESOLVED.
15. ipsw key flows: embedded offline keys, `--fcs-key`, `--pem-db`,
    CDN fetch fallback. UNVERIFIED locally.
16. AEA adoption: AEA-encrypted DMGs in iOS 18 / 18.5 Simulator OTAs.
    "iOS 26.5 beta" citation looks anachronistic; distrust that datum.

XIP predecessor (feeds JOBS #10):
17. XIP = signed XAR container. macOS Sierra+: only Apple-signed XIP
    expands natively. Deprecated path -> AEA.
18. CLI unwrap chain: `xar -xf` -> XML meta + Content (pbzx over LZMA)
    -> pbzx parse -> Content.partNN.cpio.xz -> unxz each -> concat ->
    cpio extract. Multi-tool, single-threaded. Motivates AAR parallelism.
    Corroboration pending (local xar/cpio probes).

## Bearing on goal question (port vs impl vs docs) — NO DECISION

- Report argues: port impossible (no Apple source tree; 404 stands);
  independent impl derived from docs is the viable lane.
- Evidence for impl-viability: ipsw Go fallback exists and ships.
- Decision stays owner-open. JOBS #1 untouched.

## New verified links (fetched 2026-09-29)

200, body-checked where noted:
- <https://file.org/extension/aar> — AAR magic/header/keys/codecs text.
  Backs findings 1-4 (except SIZ/CMP, LZBITMAP single-mention).
- <https://eclecticlight.co/2022/05/10/inside-apple-archive-more-than-a-compression-format/>
  Deep-dive. Unread in full; queued (JOBS).
- <http://fileformats.archiveteam.org/wiki/Apple_Encrypted_Archive>
  AEA wiki. Page live, topic confirmed.
- <https://github.com/blacktop/ipsw> — firmware toolkit. Repo live.
- <http://justsolve.archiveteam.org/wiki/XIP> — XIP wiki. Live.
- <https://en.wikipedia.org/wiki/Xar_(archiver)> — XAR background. Live.
- <https://docs.fileformat.com/compression/xip/> — XIP format doc. Live.

Unfetched (403 bot-wall, NOT cited as sources):
- apple.stackexchange.com/questions/242948 (XIP format Q&A).
- stackoverflow.com/questions/42197588 (xip CLI extract Q&A).

Skipped as low-value: generic magic-byte/RE tutorials (refs 7-13);
SE q&a duplicates of XIP chain already covered.

## Firewall exclusions

None required. Docx contains: prose synthesis, factual names/numbers,
public-doc API identifiers, CLI behavior descriptions, URLs. No pasted
spec text, no SDK header excerpts, no reference code excerpts, no
binaries. Nothing transcribed above.

Caution recorded:
- Docx cites scaffold README.md as its own ref [6]. Circular. Claims
  resting only on [6] get zero weight.
- Magic/key/codec claims are factual-diegetic, filed as UNVERIFIED
  until local `aa`/`aea` oracle probes confirm. Single-source items
  (SIZ, CMP, LZBITMAP, 0xba006800, iOS 26.5) flagged inline.

## Open questions (from this research)

1. SIZ/CMP keys real? No second source found. Oracle probe decides.
2. LZBITMAP: real codec? OS floor? `aa -h` + Compression docs.
3. AEA payload == AAR always? Decrypt-own-key probe (JOBS #4).
4. `aa` ext-bridging behavior (.aar vs .lzfse vs no-ext) as claimed?
5. ipsw Go fallback: which AEA profiles does it cover? Behavior notes
   only; compare vs FORMAT.md profile table (JOBS #5).
6. 0xba006800 failure reproducible on local Apple Silicon?
7. API names accurate vs dev docs? Browser read (JOBS #6).
