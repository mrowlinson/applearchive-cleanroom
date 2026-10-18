# NOTE-cport-hb43: band144 landed, R112 merge gating

- band144 9f75d55 LANDED (PYID 3546/3546, GREEN 7092/7092 C+py, 0w, SMOKE/UNITS fh).
- R112 effd356 STAGED (blobs MATCH, hook 2 hunks intact, regen preview rc=0 tables 2012/2016).
- merge gates: SMOKE-GREEN + UNITS-GREEN fh; py battery mrg-b145-py running (expect 7116).
- next: commit merge on GREEN -> band145 C cut (regen no-upto, build, PYID 3558, C bat).
