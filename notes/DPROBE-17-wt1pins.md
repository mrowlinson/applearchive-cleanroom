# DPROBE-17: -wt-1 oracle + determinism (PARENT-025 follow-up)

Date: 2026-10-08. Seat: decode-writer attempt#14. Oracle: /usr/bin/aa
extract -t 1 -wt 1 (adapter aar-decode; feeds battery + flip-fuzz).

## Verdict: PARENT-025 premise FALSIFIED — zero singletons ship

-wt-1 REDUCES the midchain {modal,modal-1ch} race but does NOT pin
it. Residual minority legs (~1-3/16/shape) strike even on FIXED
bytes: cxC failed after 34 consecutive clean legs (16+16 survey +
r3 + r4), edge800big1 after 32+, t27500 13/16 fixed after 26/26
across two prior instances. 16-leg surveys cannot bar a ~5% race
(P(16 clean | 5%) = 44%). ALL race SETs stay; no pin changes ship.

## Determinism fix (battery-only — SHIPS)

Self-generated crafts differed run to run (t2mb.aar block0 payload
505783-vs-505781; cuts shift): fresh mtimes embed in the compressed
stream + 4 /dev/urandom inputs. Fix: freeze() fixed mtimes before
every aar-encode (line-38 touch precedent) + seeded
Random(777001..777005) for wsrc/po6src/mcsrc/cx/corrupt. Verified:
r3-vs-r4 all 242 .aar crafts byte-identical. Reproducible inputs
for all future surveys.

## Surveys (first-hand, 50 shapes x16 legs x2 instances = 1600 legs)

wt1x16 (r1 pre-freeze crafts) + wt1x16fixed (r3 fixed crafts); per
leg exit/size/rp/fc/stderr-md5. Race observed under -wt-1 in: t2
618/7500/m2th2/m2th3/rnd3m sizes+tails, dv128k10/12/14,
m2128k-10 (9/7 SPLIT)/12/14, m2512k-1 tails/count, edge600big1,
mc4 tails, edge big2 tails, cxC + edge800big1 (battery legs).
- rp=2 <=> minority-size holds on EVERY minority leg observed.
- chSP3/MZ3/MZ20 stderr byte-stable 32/32 (IDENT-collapse stands;
  MZ md5 4abd2f69 = viewer NOTE-204 mutual-confirm). Empty-output
  shapes: no flush race mechanism applies.
- fc=2 legs under wt1: edge800big1 (PART+rp3), m2512k-1 (ABS+rp2).
  t2-family fc2 never observed (~300 wt1 legs) but same shape
  family as m2512k-1 — counts stay SETs too.

## Rules derived

- Singleton bar that WOULD satisfy: 16/16 fixed AND zero race legs
  on any instance AND no race mechanism in the shape family. No
  midchain content cell meets it. Do not re-attempt singletons
  without a mechanism fix (e.g. oracle-side determinism beyond
  -wt 1) or a much larger bar (64+/64 + multi-instance).
- Singletons attempted and REVERTED this TIP (all restored to
  31735c3-era SETs): cx sizes, cxG, mc/mz exists+tails, t2
  osizes/otails/ocounts, dv osizes, m2 SOSET/OSET, edge800 big1.

## Spec limitation (carried from DPROBE-16)

-t-1-wt-1 oracle is the mirror target (PARENT-024 (a) + PARENT-025).
-t>=2 error-path cosmetics + residual -wt-1 races (cells above)
not mirrored.
