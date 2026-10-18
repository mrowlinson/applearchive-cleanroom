# PARENT-003 OSS dylib rule (encode side)

src/pbze.py loads OSS liblzfse via ctypes. NOT a wall violation (OSS, used
black-box), but gated from here:

1. Viewer: name lzfse in the OSS survey with license + source + pinned hash.
   Unnamed OSS in src = inadmissible at merge.
2. Sweep: first-hand byte-exactness verify before any merge (already
   FLAG-required for pbze; applies to every OSS-loaded path).
3. No new OSS deps (dylib, submodule, vendored code) without viewer
   nomination in quiz first. Absolute NVME default path: portability wart,
   env-override required (present) + documented.
4. Prototype-only note: Python is reference-only per skill; the C port
   carries any final OSS-link decision with the same 3 gates.
