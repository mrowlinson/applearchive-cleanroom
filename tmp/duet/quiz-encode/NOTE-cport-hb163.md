# NOTE-cport-hb163: r13 b228 LANDED (2/4)

- merge f9ad84f + band 8289f49 (T10P156 n<=71116, 928 tiers). ALL first-hand GREEN: py 9276, C 9276, PYID 4638 exact, probes 11/11, SMOKE+UNITS x2, build 0w, wall 0.
- fix carried: my R-disp files end `}`+blank (r12 P-anchors had no blank) -> apply anchor3 for post-R153 cuts needs `}\n\n    fprintf`. apply-b228 fixed + applied clean.
- tip 8289f49 clean (?? work untouched). next: b229 = R154 a987522 (71117..71372, 8B m-tab verbatim). base pre-verified a0517cd=R153, delta exactly 3 files.
