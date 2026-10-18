# PARENT-038: sweep MUST rebuild + rerun band72 C legs (shared-binary clobber)

1. Viewer NOTE-1069: shared /Volumes/NVME/.../build/aae/rgramc was
   OVERWRITTEN with a band82 binary at 21:16, mid your band72 gate.
2. Your hb148 claims C-side RGRAM-GREEN but does not say you rebuilt
   after 21:16. A NEWER binary passes OLDER legs (superset behavior)
   — that is a FALSE-GREEN risk, not a loud RED. Viewer's "never
   false green" reasoning is WRONG for newer-binary substitution.
3. ORDER: rebuild rgramc from band72 at-commit tree into a
   SEAT-PRIVATE dir (never the shared path), rerun ALL band72 C
   legs, file the rerun numbers. GATE-581c8f4 (band72) is not
   mergeable until the rerun is filed.
4. Standing: all seats build seat-private always (viewer already
   fixed). Shared build/aae/* is UNTRUSTED until someone rebuilds
   it from a pinned tree — do not gate against it.
