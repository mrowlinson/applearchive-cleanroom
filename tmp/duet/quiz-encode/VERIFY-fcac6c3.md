# VERIFY fcac6c3 (encode-writer): PASS behavior + PARENT-004 FLAG noted

- method: git-archive pristine, pycache stripped. PBZE-GREEN 8/8 first-hand (lzfse 4 same-sha + zlib 4 new).
  smoke BACKEND=impl-adapter: SMOKE-GREEN first-hand (adapter race entry runs).
- zlib L5: CONFIRMED first-hand 4/4 discriminating trials (L4!=L5, oracle==L5 only). writer 10/10 stands.
- scorecard (CODEC-FINDINGS.md, own read): raw/lzfse/zlib DONE; lzma PARKED (355 combos fail, Apple beats liblzma
  236v240); lz4 PARKED (Apple worse/faster matchfinder, no OSS knob); lzbitmap PARKED (OSS differs — matches my
  3268v3228 bed, different input sizes); lzraven OPEN. trusted-from-writer except zlib-L5 (mine) + bitmap (mine).
- impl-adapter.sh (own read): clean contract shape; aar-encode routes raw/lzfse/zlib impl, rest passthrough oracle (honest).
- PARENT-004: pyc RE-COMMITTED on this tip (pbze .pyc 4038->4334B) AFTER PARENT-002. FLAG-w1-pyc-cleanup HOLDS MERGES
  (parent/sweep owned). next writer commit MUST rm --cached + gitignore. viewer notes, does not duplicate-enforce.
- verdict: behavior PASS; merge HELD by parent FLAG until pyc cleanup lands.
