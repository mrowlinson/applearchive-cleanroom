# NOTE-scout-r1-04: fixture inventory for the container battery

Rule honored: hashes-not-bytes; zero vendor bytes committed (this note
carries no archive bytes, only pins already in repo + generation plan).

## A. In-repo pinned set (vectors/selfgen, L5 wave-1 + decode adds)
- `shasum -c SHA256SUMS` re-verified PASS this round (all rows OK).
- 13 .aar: hello-{lzfse,lzma,lzraven,zlib,lz4,lzbitmap,raw} (same
  2-file input, one per -a) + empty-lzfse (141B empty-dir edge) +
  fifo-mixed + hlink-basic + hlink-missing + bdev-basic + mix-fail
  (decode-lane edge adds; generators in decode notes, not reaped
  here — container lane re-derives or cites at kickoff).
- 2 .aea + testkey.bin (32B TEST KEY, intentionally committed):
  hello-p1-nopad + hello-p5 over hello-raw.aar plaintext.
- Determinism law (FIXTURES.md §3, restated for container battery):
  AAR regen MUST be byte-identical (cmp-clean) or it is an EVENT;
  AEA regen NEVER byte-compared (nondeterministic from byte 13) —
  decrypt-compare vs pinned plaintext only.
- Container-relevant oracle facts already on record (FIXTURES.md §4):
  compressed AARs start pbz4/pbzb/pbze/pbzx/pbzm/pbzz + 4 zero bytes
  (only -a raw starts AA01); AEA1 @0 + LE u32 profile @4.

## B. WS scratch corpus (regenerable, UNPINNED — not fixtures)
- 70 cbattery.* dirs + 13501 .aar + 2172 .aea at WS top two levels
  (counts 2026-10-15). Decode-battery scratch: May be harvested for
  breadth AFTER provenance triage (generator unknown per file —
  treat as fuzz inputs, never pins). Do NOT link as fixtures without
  regenerating from recorded commands.

## C. Container-battery fixture gaps (generation plan, no bytes yet)
Needs beyond L5 set, keyed to T0/T1/T2 tiers (harness/BATTERY.md):
- T1 (pinned, <1MB each, generator+OS recorded, SHA256SUMS rows):
  multi-entry dirs (nested 3-deep, 50-file flat, symlink farm,
  xattr-bearing, empty-file, 0-byte + 1-byte edges); one -a raw
  multi-entry archive (exercises AA01 header-chain iteration incl
  headerSize+blobSize stepping per NOTE-02 §A); manifest pair
  (archive + -manifest output); append pair (base + appended);
  convert pair (lzfse->raw); list-json golden (aa list
  -list-format json, exact-pin once stable).
- T2 (seeded corpus, NVME-resident, linked not committed): sparse
  file dir + clone-file dir (APFS; explode-on-extract edge per
  NOTE-02 §B — sizes recorded per cell, disk-quota guard in runner);
  -b sweep {1k,64k,1m,4m} x -a {raw,lzfse,zlib} (framing/stepping
  coverage); -t {1,ncpu} determinism pairs (byte-compare runs pin
  -t 1 per CLI-CONTRACT until parallel determinism measured).
- T3 holdout: disjoint seeds, same matrix shape. G1/G2/G3 (real-world
  .aar/.aea/Apple-sample) stay owner-acquire per FIXTURES.md §7.
- AEA container-adjacent: profile-0 signed + profile-1 symmetric
  vectors already exist (hello-p1/p5); profiles 2-4 need key flows
  (owner-gated: ECDHE/ECDSA keygen) — file as blocked, not dropped.

## D. Commit discipline (restated)
- New vectors append bytes + SHA256SUMS rows in ONE lane commit;
  >1MB stays out (link + hash). DRIFT-FAIL binds: harness shasum -c
  before every battery; mismatch = HARD FAIL + incident, never
  silent re-baseline.

## Carry-forward
- Next: NOTE-05 harness skeleton (CLI stub + battery dirs) committed
  LOCAL ONLY on lanes/encode-container.
