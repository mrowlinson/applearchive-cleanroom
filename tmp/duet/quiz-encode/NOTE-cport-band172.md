# NOTE-cport-band172: T10P128 sealed (n<=61372, 816 tiers)

- merge 4c26837 (w2 740e5af, +203 py +26 pins, blobs MATCH, hook 2 hunks): py 7780/7780 0 FAIL rc=0 + SMOKE fh.
- TOOL: rgram_gen.py extended (own seat tool, bak-b172): int(STRS[idx],16) -> hexval(TAB[i],strlen) (P128 m38tab row-xor; first abort in 20 rounds). Proven by PYID below.
- band ae7c8dd (rgramc.c +1481/-1001, regen no-upto fh rc=0 tables 2192/2196, 0 stderr): PYID 3890/3890 (13 new ok), C bat 7780/7780 GREEN fh 0 FAIL, build 0w, SMOKE/UNITS fh post-C-cut.
- next: R126 26b73ca oldest-first.
