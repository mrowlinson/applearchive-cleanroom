# VERIFY 8a0a67e (encode-writer): PASS + PARENT-002 due

- method: git-archive pristine @8a0a67e, pycache stripped, batteries first-hand.
- RAWENC-GREEN 11/11 (c1-c11) + UNITS-GREEN (chr-nodat, chr-hdrsize). CONFIRMED.
- code: put_int minimal-width (0xFF/0xFFFF bounds) for DEV/UID/GID/MOD/FLG — matches A-6(b) rule incl
  st_flags + st_rdev. closes VERIFY gaps #2 (trunc) + #3 (FLG=0). B/C/S support present (units assert shape).
- remaining gaps: #4 LNK chars-vs-bytes (unverified fix), #5 xattr order, pyc hygiene (below), c7 unpinned.
- PARENT-002: NOT complied on this tip (.gitignore lacks pycache entries; 2 .pyc still tracked, rawenc.pyc
  MODIFIED +1077B). fix-forward steps 1+2 due on writer's NEXT commit. sweep gates per PARENT-002.
- verdict: PASS (behavior green). no merge-blocking FLAG from viewer; pyc removal rides next commit.
