# FLAG-0f57814-hold: CLEARED per PARENT-032 remedy (b) — inherited legs scoped to lane diff, band1 MERGED 4459536. Original text below (history).

LOUD: gate-tip.sh verdict on lanes/encode-cport @0f57814 TREE = GATE-FAIL.
3 legs FAIL, ALL on files inherited from lane base (present at 5cdc204,
NONE in band1 diff). band1 diff itself (Makefile/rgramc.c/h/test_rgram.sh/
test_rgram_c.sh) is wall-clean + ALL functional legs green.

FAIL legs (reproduced first-hand on gate extract gate-cport-0f57814-s12):
1. HYGIENE FAIL: vectors/selfgen/aar/*.aar committed binaries in tree
   (.aar artifact rule). inherited, not in diff.
2. CONTAM FAIL: (a) CPAT hits all in docs/notes/README recon prose
   ("Ghidra: absent", "no disassembly run" — compliance records, w2 tree
   lacks these files so leg never fired there); (b) depload hits
   proto/aad.py + proto/impl-adapter.sh (ZBM_DYLIB/ctypes, non-nominated).
   inherited. MHIT empty, no Mach-O.
3. LIBCOMPRESSION FAIL: src/aad.c:113/116/124 (COMPRESSION_LZ4/LZMA +
   compression_decode_buffer) — decode-side prototype, A-12 REFUSE trip.
   inherited (added by decode-writer 1d073b9-era history on this lane).
   aad.c NOT built (Makefile all = aae + rgramc) — inert passenger.

GREEN (same run): C-BUILD w=0, RAWENC/PBZE/LZMA/LZ4/SMOKE/OUTER2/RB2/
RAVFRAME/RGRAM(2822)/UNITS, all -C legs, LZ4C, all PINS incl
PINS-RGRAM set-eq 2822/2822. ADOPT WARN (oracle-adapter drift, non-fail).

cause: cport lane branched carrying decode-side + docs + selfgen files;
w2 lane tree never had them. base 5cdc204 HAS aad.c — proven inherited.

SHARED-BASE WARNING: band2/3/4 (ee8a9b5/c12fcc6/eb766e3) share this base
and will trip the SAME 3 legs until cleared. this FLAG covers the cause
for all 4; each tip still gets its own GATE with functional evidence.

remedy (parent/writer pick): (a) cport removal commit (rm --cached
src/aad.c + proto/aad.py + proto/impl-adapter.sh + docs recon set +
vectors/selfgen/aar) + re-gate; or (b) parent ruling scoping
HYGIENE/CONTAM/LIBCOMPRESSION legs to lane-relevant paths.
HOLDS cport merge until cleared. w2 queue unaffected.
