# PV-c12ddb1d b280 T10R181 n<=80768 (992 tiers): PASS

Parent-first-hand, fresh detached WT tmp/wt-pv-c12ddb1d @c12ddb1d,
seat-private build ws/tmp/pv-c12ddb1d/build, CT shim in env.
Log: ws/tmp/PV-b279-b282-parent.log.

- Build: cc -O2 -Wall -Wextra -std=c11, rc=0, 0 warnings.
- RGRAM py 10716/10716 0 FAIL RGRAM-GREEN (test_rgram_fast.py).
- RGRAM C 10716/10716 0 FAIL RGRAM-GREEN (RGRAM_BIN=C).
- RGRAMC-PYID 5358/5358 covered=5358/5358 RGRAMC-GREEN.
- SMOKE-GREEN (aea-decrypt + aea-bytes PASS).
- G+V+PV GREEN -> merge.
