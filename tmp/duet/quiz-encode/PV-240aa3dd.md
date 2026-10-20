# PV-240aa3dd b279 T10R180 n<=80420 (990 tiers): PASS

Parent-first-hand, fresh detached WT tmp/wt-pv-240aa3dd @240aa3dd,
seat-private build ws/tmp/pv-240aa3dd/build, CT shim in env.
Log: ws/tmp/PV-b279-b282-parent.log.

- Build: cc -O2 -Wall -Wextra -std=c11, rc=0, 0 warnings.
- RGRAM py 10692/10692 0 FAIL RGRAM-GREEN (test_rgram_fast.py).
- RGRAM C 10692/10692 0 FAIL RGRAM-GREEN (RGRAM_BIN=C).
- RGRAMC-PYID 5346/5346 covered=5346/5346 RGRAMC-GREEN.
- SMOKE-GREEN (aea-decrypt + aea-bytes PASS).
- G+V+PV GREEN -> merge.
