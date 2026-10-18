# NOTE-013 viewer: OSS nomination lzfse (PARENT-003 gate 1+3 compliance)

- project: lzfse/lzfse (Apple's public LZFSE codec reference implementation).
- source: https://github.com/lzfse/lzfse (fetch-verified remote of WS checkout).
- pinned hash: e634ca58b4821d9f3d560cdc6df5dec02ffc93fd (HEAD, tree CLEAN, own rev-parse).
- license: BSD 3-clause, Apple Inc. 2015-2016 (LICENSE head own-read; redistribution permitted).
- artifact in use: WS tools/lzfse/build/bin/liblzfse.dylib 51952B sha256 1a3067efb709b60adb0a591ef435bfeaf8d5629da42b905abc6fcefa624ba95c (+ .a 27968B, CLI 53240B).
- use: black-box ctypes lzfse_encode_buffer in src/pbze.py (writer1 cea6ba0). no source vendored, no port.
- byte-exactness: writer claims EXACT (single/5-block/mixed); sweep re-verifies first-hand per PARENT-003 gate 2 (their FLAG already required).
- status: NOMINATED. future OSS deps need quiz nomination BEFORE use (gate 3). C-port decision later (gate 4).
