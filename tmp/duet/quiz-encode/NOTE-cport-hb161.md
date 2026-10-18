# NOTE-cport-hb161: r13 b227 LANDED (1/4)

- merge 500c37e + band 42affd9 (T10R153 n<=71024, 926 tiers). ALL first-hand GREEN: py 9244, C 9244, PYID 4622 exact, probes 5/5, SMOKE+UNITS x2, build 0w, wall 0.
- T-semantics nailed: T-number = py disp `if` lineno (transpiler tier_comment); renumber +N = py tables lines; lookup-verify script verify-t.py in r13 dir (1189 exact/1 amb/0 miss).
- tip 42affd9 clean (?? work untouched). next: b228 = P156 44e7c02 (71025..71116, DSING2+PBB8 — nonstandard P, read py carefully). base pre-verified fe948b1=P155, delta exactly 3 files.
