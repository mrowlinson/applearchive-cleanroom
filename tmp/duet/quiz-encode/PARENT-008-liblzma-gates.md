# PARENT-008 liblzma merge gates (encode-writer1@9433954)

Commit links pinned liblzma 5.8.4 + own XZ rewrite. Nomination
exists (A-10/A-20). Merge requires ALL PARENT-003 gates:

1. liblzma named in docs/OSS-SURVEY.md with license + source +
   pinned hash (viewer: CLAUSES mention is not the survey entry).
2. Sweep first-hand byte-exactness on every liblzma-loaded path.
3. C-link decision recorded (direct-link approved explicitly or
   own-XZ-only for ship; no silent default).

Plus usual GATE + VERIFY. Own-XZ code unaffected. No merge
until all 3 + pair land.
