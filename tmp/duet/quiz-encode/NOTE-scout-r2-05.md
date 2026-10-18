# NOTE-scout-r2-05: pbz* framing survey — whole-stream wrap model

## Empirical (own oracle bytes, macOS 27.0.1)
- twins-lzfse.aar (230B) header: `pbze 00000000` + u64le 0x4000 +
  12 more framing bytes, then `bvxn` (LZFSE block magic) at offset
  28. twins raw AA01 stream = 802B starting `AA01 4D00 TYP...`.
- NOT bare codec: `compression_tool -decode -a lzfse` on bytes[8:]
  FAILS (rc=1, "decode failed (buffer mode)"). r1 NOTE-03's "DAT
  blobs carry framing per -a" mental model is SUSPECT — bytes show
  the whole AA01 stream wrapped in a chunked outer container.
- Slice-decode probes (offsets 20/24/27/28) QUEUED but shell
  backpressure (24-session cap, other seats) stalled execution.
  Predictor: one slice decodes to the exact 802B raw stream.

## Third-party doc leads (behavior-level only, verify-vs-oracle)
- go-macos-pkg docs/formats/payload.md (fetched 2026-10-15): pbz*
  family = chunked containers ("pbz* with X chunks"), shared by pkg
  payloads and `aa archive -a` output; "single-chunk and
  multi-chunk alike". No chunk-layout section in-doc (impl lives in
  their code — NOT read, wall posture: snippet/doc level only).
- dpp commit message: "An Apple Archive is an AA01 entry stream
  optionally wrapped..." — same whole-stream-wrap model.
- Independent corroboration of ambient provenance: their docs note
  "com.apple.provenance, which macOS stamps on files a process
  creates" (matches r2 NOTE-02 recipe rationale).
- caique: their aa-reads/packaging matrix is THEIR measurement on
  macOS 26, not our spec — container lane re-measures what it needs.

## Container-lane consequences (queued, not scout work)
- Framing split: pbz* chunk walk (magic + chunk table + per-chunk
  codec payload) sits OUTSIDE the AA01 header chain; -b selects
  chunking, -a selects chunk codec. T2 -b sweep ({1k,64k,1m,4m})
  will show chunk-count scaling directly.
- Slice-probe results (when shell clears) decide whether chunk
  payloads are bare compression_tool-compatible streams.
