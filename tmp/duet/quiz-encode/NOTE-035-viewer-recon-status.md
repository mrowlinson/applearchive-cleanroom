# NOTE-035 viewer recon: Ghidra properly confirmed absent; hash-hunt support ready

- tool check (proper, per skill — not PATH-only): /Applications no RE tools, /opt = homebrew only,
  no ~/Tools, Caskroom EMPTY, Cellar has no ghidra/radare2/capstone. disassembly stage stays BLOCKED.
- consequence: recon continues via nm/otool/dyld_info/strings + running-binary probes (carried CR-101..121
  so far; no stall). Ghidra install = parent call (heavy download + JDK); value mostly for w1 hash
  internals, which must bed behaviorally anyway.
- w1 hash-hunt (NOTE-17 open: hash fn + resume + collider + tail limit): viewer ready with independent
  derived beds on Q (equivalence-class mapping, resume-shape grid). not poaching live hunt — file Q anytime.
- open: table-inventory refresh on OS bumps only. recon queue otherwise drained; polling.
