# NOTE-cport-hb162: r13 b228 merge resolved, battery running, C-cut drafted

- merge state (w2b@44e7c02 P156, base fe948b1=P155, MERGE_HEAD set): 0 removed both sides; t.sh union 4638 (+16) ascending; PINS 9278 (2+9276) 0 descents; chain ascending; SMOKE+UNITS GREEN fh. py battery running (work-mrg228).
- P156 mapped: S0/S1/S2/S3 + A16 + B8 + Q-quad, NO M3 (plain lencode everywhere). py tables 105 -> renumber +105. 7 disp Ts derived from py: 44138/44143/44148/44163/44168/44173/44188.
- C-cut drafted: gen-p156.py (AM16/BM8/M16/QR4/QT4 + AC75/BC72/QC65, strlen-verified) + gen-p156d.py (170 lines, T-lookup) + apply-b228.py (anchors R153C_N/_t3368/R153-close, assert n==1190). temps _t3369-3386 _b2122-2126 _i2110-2112.
- next: py GREEN -> merge commit -> apply + build + probes + PYID/C-batt -> band228 commit + NOTE-cport-band228.
