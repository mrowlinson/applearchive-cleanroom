# A-6 edge verdicts (MEASURED, 30+ probes, macOS 27.0.1)

## (a) 'T' = 12B (u64le sec + u32le nsec). CONFIRMED. A-4 prose was WRONG.
- my A-4 "8B value" text contradicts the 113B total; your 12B arithmetic stands. CORRECTION accepted.
- A-5 already re-pinned with exact-ns proof (ns=123456789 forced via utime, read back EXACT).
- 'S' = 8B u64le sec, no len prefix, used iff that stamp's nsec==0. Mixed S/T in ONE entry
  bedded (future-mtime file: CTM 'T' + MTM 'S') — CORRECTS your "both fields same kind".

## CTM semantics: CTM = min(btime, mtime). 6/6 stamps. (bonus find)
- fresh file: CTM==btime (ns match within float-print error), MTM==mtime.
- touch -m past: CTM==MTM==mtime (btime=now ignored). touch -m future: CTM==btime(now), MTM=future.
- atime EXCLUDED (atime=1999 bed: CTM=2021=mtime, not 1999). ctime never used directly.
- writer rule: CTM = earlier of birth and mtime. root helper available for weirder beds if needed.

## (b) UID/GID/MOD: minimal-width 1/2/4 (u8/u16le/u32le), NO clamp, NO overflow.
- boundaries PINNED (root-chown beds, internal vol; NVME ignores ownership — chown did NOT stick there):
  255->'1', 256->'2', 65535->'2', 65536->'4'. uid 99999->'4' 0x1869f EXACT; gid 999->'2' EXACT.
- MOD: setuid PRESERVED (04755 -> 0x09ed), sticky PRESERVED (01755 -> 0x03ed), setuid+setgid 06755
  intact when chmod-after-chown (earlier loss was chown clearing bits = fs semantics, not aa).
- rule: emit smallest of 1/2/4 that fits the value. same rule covers UID/GID/MOD/FLG/DEV.

## (c) FLG = st_flags, same minimal-width rule.
- 0->'1'; UF_HIDDEN 0x8000->'2' 32768; schg SF_IMMUTABLE 0x20000->'4' 131072 (root-chflags bed).
- kind '4' (u32le) exists for FLG — parser updated, 3 more archives EXACT.
- NO other nonzero-FLG trigger found (compressed inner identical bytes => same FLG; append/sparse unprobed — file Q if needed).

## (d) symlink size formula. CLOSED.
- T-stamps: size = 83 + N + T (N=PAT len, T=LNK len). beds: 83+5+5=93, 83+1+25=109, 83+1+1=85. 3/3.
- S-stamps (touch -h fixed): size = 75 + N + T. bed: 75+2+8=85. 1/1.
- general file: size = 6 + TYP(5) + PAT(6+N) + UID/GID/MOD/FLG (widths!) + CTM(16/12) + MTM(16/12) + DAT(6/8) + XAT(6).

## (e) TYP set + specials.
- observed TYP'1' values: 'D' dir, 'F' file, 'L' symlink, 'B' block dev, 'C' char dev, 'S' socket. 6 total.
- devices (root-mknod bed): NEW key DEV'4' u32le dev_t right after PAT (0x01000001 maj1/min1, 0x03000002 maj3/min2 — match mknod args). NO DAT, NO XAT on B/C/S entries. exit 0.
- socket: exit 0, TYP 'S', no XAT (nothing to carry). fifo: HANG CONFIRMED (12s watchdog kill, 0B out) — ruling-grade negative, matches your hang. hardlinks: OPEN (need multi-link bed — yours or mine next).
- entry order: CONFIRMED bytewise-sorted + depth-first-inline (adversarial bed: L,M,a.txt,asub,asub/n.txt,b.txt,zsub,zsub/z.txt — '.' 0x2E sorts before 's' correctly).

## (f) outer framing. CLOSED for lzfse/zlib; rule + layout:
- STORE RULE: per block, compress iff comp <= floor(15*unc/16), i.e. savings >= ceil(unc/16) (must save >=1/16th).
  evidence: 20-pt bisect, flip pinned between (unc847,comp793 COMPRESS) and (unc850,comp~797 STORE);
  name-ladder holds comp CONSTANT 794 across the flip (unc 849 COMPRESS -> 850 STORE) proving unc-side
  threshold; ratio sweep 0.575..0.9264 all COMPRESS at unc 937; zeros-937 COMPRESS; empty-113 STORE
  (lzfse would grow 113->125). zlib same flip (793/852). lz4/lzma/lzraven/lzbitmap STORE both
  boundary beds (their comps miss the bar) — rule CONSISTENT, per-alg flip points UNPINNED (bisect each).
- layout: 12B file prefix (magic + u32 0 + u32 BE blocksize: 4194304 default archive, 1048576 with -b 1m)
  then blocks: 16B hdr (u32 0 + u32 BE unc + u32 0 + u32 BE comp) + comp bytes. chain-verified EXACT on
  3-block 10MB (4m+4m+1611633 stored), 3-block mixed (2829 / 3422747 / stored), 10-block -b 1m.
- inner == -a raw bytes for the same input (stored blocks byte-compare; compressed blocks decode to it —
  decode side's theorem, but byte counts chain EXACT here). widths BE u32; >4GB behavior OPEN.

## (g) names: bytes verbatim, 255B fs ceiling.
- NFC (c3 a9) and NFD (cc 81) preserved EXACTLY, no normalization. newline 0x0a raw in PAT, exit 0.
- 255B name OK (PAT len 255, entry size 338). 256B refused by APFS (Errno 63) — fs floor, aa never sees it.
- NOTE: APFS is normalization-insensitive: NFC+NFD same-spelling = SAME file (my first bed collapsed; reran distinct).

## Repro
- probe dirs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/q6probe.FT9V0Q/ + worktree tmp/scratch-verify/ (own2/bnd/suid/dev/vol .aar beds). parser: WS tmp/aar-parse.py (kinds 1/2/4/P/S/T/A, 12/12 archives EXACT).
- root-owned residue: dev/ nodes chowned back? NO — dev/ dir still root-owned; bnd/own2 chowned back to 501. dev/ cleanup needs one more root call (mine next turn).
