# NOTE-cport-hb164: r13 b229 merge resolved, battery running, C-cut drafted

- merge state (w2@a987522 R154, base a0517cd=R153, MERGE_HEAD set): 0 removed both sides; t.sh union 4650 (+12) ascending; PINS 9302 (2+9300) 0 descents; chain ascending; SMOKE+UNITS GREEN fh. py battery running (work-mrg229).
- R154 mapped: standard R (b45 155/43 thr 51/179, mtab b20-23,76-79, qtab b13-15,72-75). py tables 53 -> renumber +53. new T44265 = py disp line.
- C-cut drafted: gen-r154.py (M16/Q16/C67) + r154-disp.c + apply-b229.py (anchors P156QC_N/_t3386/P156Q-close-no-blank, assert n==1197). temps _t3387-3390 _b2127-2128 _i2113.
- next: py GREEN -> merge commit -> apply + build + probes + PYID/C-batt -> band229 commit + NOTE-cport-band229.
