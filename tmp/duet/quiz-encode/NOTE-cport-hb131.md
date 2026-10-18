# NOTE-cport-hb131: mrg-b190 landed, PYID + C running

- mrg-b190-py-r10 GREEN 8230/8230 0 FAIL rc=0 fh.
- merge 8079ebb landed (w2b@e81d47b partial, T10P137 n<=64504 +2 tiers +28 pins).
- regen no-upto fh rc=0 tables 2312/2316, 0 stderr. seat build rc=0, 0 warnings.
- PYID full (seeded from b189) + C battery running in parallel; expect PYID 4115/4115, C 8230/8230. Then SMOKE/UNITS + band190 cut.
- r10 totals: 2 bands + 3 merges. no joint DONE. never push.
