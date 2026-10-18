# PRE-061b 60-regime 6389..6644: 16-tabs + 16-bands + b5-128s (T7C stage)

## census (v5ak first-hand, 256 rows all 60B, 12 var)
- 14 edges>=8 @6405..6629 (16-step + 32-gap 6501-6533). quiet
  head 6389..6404. dip 6645 ahead (bookend).
- 16-tabs full-span (period16 ✓): b36=(4e 14 dc f2 a8 6e 84
  9a ff c5 98 91 59 88 4e 2e), b37=(fcx4 bfx4 fcfc bfbf
  fc bf bf fc), b38=(ef db 77 7f ff eb f3 fb 53 3f df c7
  63 13 ff 3f), b39=(7e a9 ae ae b3 de de de ef 1a 1e 1f
  24 25 4f 50), b40=9/7-duty (b5/d5).
- b4 ramp. b5: 128-plateaus 51/52/53 @6389/6400/6528.
- bands from 6405: b28/b29/b30/b31 16-bands (+32s over gap);
  b32: single edge b6->d6 @6597.
- one commit 6389..6644 (or split at 6501/6533 gap).
