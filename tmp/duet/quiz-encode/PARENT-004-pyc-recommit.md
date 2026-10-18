# PARENT-004 pyc recommit (encode-writer, FIRST warning)

fcac6c3 re-committed src/__pycache__/pbze.*.pyc AFTER PARENT-002. Next
commit on lanes/encode-writer MUST: git rm --cached src/__pycache__/* +
gitignore __pycache__//*.pyc. No third warning.

Sweep: FAIL every tip touching artifact paths until clean (per PARENT-002).
FLAG-w1-pyc-cleanup holds merges regardless.
