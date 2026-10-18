# PARENT-035: OWNER ORDER — post-compat CPU optimization round

After encode hits 100% (joint DONE, all gates green): run a CPU
optimization round over the C deliverables for x86-64 (SSE2/AVX/AVX2
where the venue has them) + ARM (NEON/SVE) via intrinsics or
auto-vectorization. Runtime-detected fast paths, scalar fallback.
Per-kernel bar: bit-identical output vs scalar on FULL battery +
timing gate proving in-matrix speedup. Standard CPU features only;
no GPU/DSP. Skill §15 governs. NOT before 100% — no early start.
