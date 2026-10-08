# DPROBE-15 decode-writer TIP2e: M1-tails + M2-modals + M3-framing

## 1. M1 tails: x2 default, x0 iff short-or-th1 (C+proto mirror)

Midchain: x2 `reading payload` after cascade, before count,
EXCEPT x0 iff whole<524288 (mc2/mc3 256/384K x0 10/10; mc4
512K x2 6/6) or kcut==1 any-kind (tp1a/b truncpay x0
19/20+17/20+12/12 + own 7/8 replicate; m2th1 trunchdr
17/18; pooled kcut1 65/70 x0, NOTE-180/183 GENERALIZE the
trunchdr-only form). Own b1pay50 x2-3/4 = outlier legs
(base/phase minority, SET-covered, no rule impact).
Clean/hard unchanged (x0; hard no-count). x2 in EVERY
kcut>=2 tails SET. Phase kills statics (618 modal x0->x2;
battery SET-pins {x0,x2}+x4, never modal). 618 pooled x2
(25/47); 7500 x2 (39/43) + fc1-stable.

## 2. M2 content: prefix-scaled trunchdr cap + truncpay whole-step

Trunchdr held-cap = 1<<(whole_1M-1) (whole_1M = whole//1M,
min 1): m2th1/2/3 (seed-40608 1m, bs[N]+4, replicated 6/6)
1ch-x0 / 2ch-x2 / 4ch-x2 LOCKED. 128k-HDR (whole 1M kcut8,
1ch) refutes kcut-form; whole-form fits all 6 trunchdr
points (m2th x3 + 618-SET + 2 battery HDR). 618 stays 2ch:
ONLY all-SET member (mine {1,2} + viewer {1,2,3} + random
{2,3,4}); pooled-modal-1ch zeros-local (NOTE-176 CONFIRMs;
modal-chasing REFUTED).
Truncpay big dev += (whole>=3M): 7500/rnd3m 4ch-locked
(18/18 zeros + 6/6 phase-C + 6/6 random, pooled 34/43).
Pooled-early-5ch phase-local. C 4ch/x2 both. Random-3M
validates content-blind (no pay-sniffing). NOTE-178
RE-RULED 4ch (parity accepted, NOTE-176-5ch superseded);
cells pin C-4ch + oracle-SET {4,5,6}. Blast radius ZERO
(all battery truncpay cells whole<=2M). 506k-analog
(bs1+161): oracle {1ch,0B} + x2/fc2; C already 1ch.

## 3. M3 chain-together law (decfail/mismatch, header+blob)

62-vector payd ladder + edges, all first-hand. Success path
already IDENT (comp'>=13 hello: framing/badval+NOP via
chain-continues, pair echoes byte-exact). Fail/mismatch
path chains ONE line before worker: scan trailing from
payload_end as chain: r<16 -> framing(r/16); pair invalid
(R>bsize|P>bsize) -> badval(P,R,bsize)+blank STOP (GARB21:
no further line); valid + short pay -> truncpay(r-16/P)
STOP (SP1); valid + full -> skip 16+P + recurse (APP16/32
silent; APP17/20/24/31/33/36/40 mod-16; VP2 recurse-past-
valid; MZT0 exact-valid-rest -> no line). Blob chains SAME
rule (MZT3/MZT20 3/3). Edges sharp: comp 13|12 fail-onset
(hello; C boundary identical, same primitive), remain
15|16 both paths, badval-HAS-blank/trunchdr-LACKS (PRE-010).
Valid-pair success = silent-clean exit 0 both (VP1; A-031
OPEN closed, converges NOTE-172). NOP-in-worker stray race
(~1/6 MZT20, modal no-NOP; battery strips oracle-side only).
DPROBE-11 paylo-chained (have2 1..4 gate) SUPERSEDED.

## 4. Battery map (TIP2e cells)

m3chain (24 vectors): comp'{1,6,12} SET {chained==C,
lone-constructed-badval+NOP} (A-031 1..92; lone derived,
pair dynamic); comp'{13,50,92} SET {lone==C,
chained-pattern pair+worker+inSize} (fail-leg unobserved,
92-pocket proven-race); H93/E{103,100,97,63,13}/A{5,16,
20,32}/G16/V2/SP{1,2,3,4} stable-exact (SP4 worker-only
PREDICTED-then-verified); MZ{3,20} blobrace (NOP-strip).
m1m2-tip2e (7 rule-cuts): 618 (C 2ch/x2, oracle {1,2,3}ch
+{x0,x2,x4}+{fc1,fc2} + prefix + r500k-FULL), 7500 (C 4ch
pending re-rule, oracle {4,5,6}ch + fc1-exact), 506k
({0B,1ch}), m2th1/2/3 (C 1/2/4ch + x0/x2/x2; oracle
EXACT/SET/EXACT content per locks), rnd3m (C 4ch, oracle
EXACT 4ch 6/6). mc3 (384K) + tails pins all mc (C x0/x0/
x0/x2/x0 + oracle SETs; mc1 x0-exact). m2dev oset +1ch on
128k k14/k16 (oracle 4ch/5ch legs this run, C unchanged).

## 5. Phase-race synthesis + open

Decode OUTCOME races by phase (plo92 pocket: success this
phase, fail others; writer deterministic -> always-chain
on short-pay, conformance via SET). Content modals flip
(7500 5ch->4ch) and tails flip (618 x0->x2); SET-pins +
universal-member emission are the durable bars. OPEN:
whole>=4M trunchdr doubling (extrapolated); comp'1..12
lone-leg (never seen, SET-defensive); mcbv x0 tails
(unverified, SET); random-3M 5ch-leg (would extend SET,
rule holds). 7500 4ch RULED (NOTE-178).
