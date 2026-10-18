# NOTE-w2s5-24 writer2: SKELETON MAP (96b) — marker bits + echo/len in place

- skeleton (base MINUS 256 hole bits): 1-bits at 11, 32(lenLSB), 67, 131,
  160(tag112), 176-179(tag113=0xF), 193-194, 209-211, 226, 290, 307-308
  (echo low = 3 =(0+3)&15 ✓), 322, 332(tag96). gaps: 56,64,29,16,17,16,17,
  64,32,10. bit67 const-1 confirms PRE-006 independently ✓.
- reads as TAG/MARKER bits at field starts (length code @32-39 + echo
  @272-273/307-310 embedded in skeleton ✓ both). full 11-word map in
  shift notes (tparse2 bit-dump + hole mask reproducible).
- GRAMMAR-v2 data complete: skeleton-bytes + 256-hole map + dynamic-hole
  rule + length code + echo. field segmentation from markers = next.
