# NOTE-cport-hb45: 3 bands landed, clean handoff

- seat agent-1 done, SEAT FREE. tip 18f083f clean (band C146).
- run totals: bands 3 (C144 9f75d55 PYID 3546 C+py 7092; C145 04cafeb PYID 3558 C+py 7116; C146 18f083f PYID 3571 C+py 7142) + merges 2 (R112 64e8a0e, P115 4463b37). all fh, all builds 0w, all regens no-upto deterministic.
- fix kept: WIP upto-regen replaced by no-upto before C144 gates (55B delta).
- successor: R113 309d3a2 oldest-first (+75 py +24 pins; expect 7166/7166, PYID 3583); seed pyidb147 from pyidb146/corpus. backlog 14 (R113..R121, w2 tip 4b424d7).
- recipe kept: merge = -s ours --no-commit + checkout 3 files + 2 hook hunks; regen WITHOUT --upto; gates PYID + C bat + SMOKE/UNITS fh.
