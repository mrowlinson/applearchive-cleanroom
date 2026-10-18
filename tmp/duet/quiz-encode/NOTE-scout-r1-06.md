# NOTE-scout-r1-06: black-box framing probes (rounds 6-7)

All runs vs /usr/bin/aa (macOS 27.0), -t 1, NVME scratch. Own oracle
outputs only; beds+numbers, zero transcription.

## P1. Header-chain walk (hello-raw.aar, 2445B, 3 entries)
- AA01 magics at 0/118/310; hsizes 82/98/99 (u16le @+4, INCLUDES
  magic — theapplewiki claim CONFIRMED structurally).
- Entry spans: e0 = 118B (82 hdr + 36 XAT blob: u32le len 0x24 +
  com.apple.provenance payload — L3 §8 corroborated); e1 = 192B
  (98 + 94: 58B greet.txt + 36 framing); e2 = 2135B (99 + 2036:
  2000B repeat.txt + 36 framing). Constant 36B overhead/file —
  container lane parses exact DAT framing split.
- Header-only stepping stops at first blob (BAD-MAGIC@82 on naive
  walk) — item step = header + parsed-blob-lengths, as wiki claims.
- e0 keyruns: TYP PAT UID GID MOD FLG CTM MTM XAT (no DAT: dir).
- No YAA1 anywhere in selfgen set (legacy path untestable locally;
  rewrite-behavior claim stays UNVERIFIED).

## P2. pbz* magic census (13 selfgen .aar — FIXTURES §4 CONFIRMED)
- pbz4/pbzb/pbze/pbzx/pbzm/pbzz each + 00000000 for -a
  lz4/lzbitmap/lzfse/lzma/lzraven/zlib. Raw-start set (AA01 52 00
  54 59...): hello-raw, bdev-basic, hlink-basic, hlink-missing,
  mix-fail. empty-lzfse + fifo-mixed = pbze (compressor default).
- Total selfgen .aar bytes: 14794.

## P3. SLC acceptance (RESOLVED: accepted, -h list incomplete)
- `-include-field SLC` rc=0. Distinct-content pair: 0 SLC keys
  emitted (dedup marks clusters only). Identical 100B twins:
  SLC count = 2 (one per twin entry, 585B total).
- Verdict: man EXAMPLE correct; `aa -h` field vocabulary OMITS a
  working field. Container battery MUST include an slc-twins vector
  (dedup-marked) + -enable-dedup extract leg (clone-output check).

## P4. list-json shape (CONFIRMED, golden-ready)
- Top-level JSON array, one object per entry; keys UPPERCASE wire
  form (TYP/PAT/UID/GID/MOD/FLG/CTM/MTM/XAT observed); TYP "D"/"F";
  XAT value = blob size int (36); CTM/MTM = float seconds.
- Case verdict: CLI lowercase (typ/pat/...) are aliases; wire+JSON
  uppercase. (One transient empty-stdout flake on first pipe; two
  subsequent GREEN incl T0 c2 — noted, not filed as behavior.)

## Carry-forward (container-lane probes queued, not scout work)
- TYP 9-vs-11: needs symlink/fifo/device/whiteout archives + byte
  census (decode fixtures hlink/fifo/bdev exist; whiteout/door/port
  creation unknown — probe `aa archive` of such nodes or mark
  UNPROBEABLE-locally).
- -omanifest convert-time shape; HLC/cpio acceptance; YAA1 handling.
