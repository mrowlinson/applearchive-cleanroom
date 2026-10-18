# PARENT-002 pyc hygiene (encode writers)

cea6ba0 committed src/__pycache__/*.pyc. Fix forward (no history rewrite):

1. Add to .gitignore: __pycache__/ + *.pyc (both writers, next commit).
2. git rm --cached src/__pycache__/* on your lane, commit.
3. Never commit build artifacts again (pyc, .o, binaries, traces).

Sweep: gate FAIL any tip adding artifact paths until clean.
