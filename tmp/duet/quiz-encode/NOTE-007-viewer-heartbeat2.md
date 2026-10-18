# NOTE-007 viewer heartbeat 2: Q/A 8/8, VERIFY 2/2, recon tables landed

- quiz: Q-1..Q-8 answered (A-1..A-8 filed), VERIFY-dc87389 + VERIFY-2d1ec2d PASS, NOTE-006 corrections filed.
- writer1 @2d1ec2d: battery re-run first-hand 8/8 RAWENC-GREEN. carried gaps: UID/GID trunc, FLG=0, LNK bytes, xattr order, B/C/S.
- writer2 (lanes/encode-writer2) up: A-7 provisional turf (outer split vs writer1 NOTE-5 collision; PARENT must confirm), A-8 doc hashes.
- model deltas: CTM=btime AGREED (my min() withdrawn — touch retrodates btime); 15/16 store rule RE-CONFIRMED at exact boundary (796/850 flip); outer parse unified.
- recon: provenance MATCH, nm 226/98, xarch diff = libSystem shims only, dyld exports captured (libAppleArchive 232 = tbd count MATCH; libParallelCompression 930 rows incl re-exports), encode-entry offsets recorded, Ghidra ABSENT (no install; RE via binutils + probes so far).
- next: lane commit (recon record) -> poll -> clause drafts CR-nnn (framing/behavior, MEASURED) -> table inventory from export offsets -> serve new Qs.
