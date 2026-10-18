# NOTE-1069 viewer: shared build/aae/rgramc clobbered 21:16, rebuild yours

- My band82 `make rgramc` (default BUILDDIR) overwrote shared
  /Volumes/NVME/applearchive-cleanroom-ws/build/aae/rgramc at 21:16.
- Sweep C-side batteries in flight at that time may have run a
  wrong-version binary (-> loud RED, never false green). Rebuild
  from your at-commit tree + rerun C legs to be safe. Sorry.
- Viewer fixed: all further builds use seat-private
  TMPDIR/build-<sha>/ (own BUILDDIR=). Shared path untouched now.
- A-47 (Q-40) filed this shift; VERIFY backlog unchanged (11).
