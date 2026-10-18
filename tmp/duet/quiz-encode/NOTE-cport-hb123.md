# NOTE-cport-hb123: mrg-b188 landed, PYID running

- mrg-b188-py-r10 GREEN 8180/8180 0 FAIL rc=0 fh (~40 min, oracle-paced).
- merge be21af9 landed (w2b@8fb7560 partial, T10P136 n<=64156 +2 tiers +28 pins).
- regen no-upto fh rc=0 tables 2298/2302, 0 stderr; b187-regen==committed confirms copy-over; rgramc.h untouched since band1.
- seat build rc=0, 0 warnings (build-band188/rgramc).
- PYID full running (corpus seeded from pyidb187-fh, 4642 files); expect 4090/4090. Then C GREEN + SMOKE/UNITS + band188 cut.
- no joint DONE. never push.
