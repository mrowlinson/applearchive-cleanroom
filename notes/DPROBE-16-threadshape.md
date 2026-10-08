# DPROBE-16 decode-writer thread-shape TIP: -t-1-only mirror (PARENT-024 (a))

## 1. Mirror target + limitation (SPEC NOTE)

Deliverable mirrors `aa extract -t 1` (default -wt) EXACTLY on
block-layer paths. Default-threading (-t>=2) block-layer
ERROR-PATH cosmetics (bd009800 worker stanzas: flushing/NOP
tails, Truncated/Invalid counts, invalid-output-size lines,
Threads-reported footers; extracted-prefix races) are NOT
mirrored — machine-dependent races, unpinnable. Success-path
bytes identical across threadings (NOTE-60 78/78 + this TIP:
all success cells green unchanged). Revisit trigger per
PARENT-024 (fresh-corpus -t-dependent SUCCESS bytes, or
parent call). Viewer folds to CR-027/028 (NOTE-60 next;
A-032 folding to CR-028 in progress).

## 2. -t-1 stanza map (first-hand NOTE-193, battery IDENT)

Header flavor (7 lines, rc=1, no tails, tree empty): bcode =
trunchdr 0x94034400 `truncated stream header` / truncpay
0x94036c00 `truncated stream payload` / badval 0x94036800
`corrupted stream header` (NO value echo) / decfail
0x94039800 `block decompression failed`; tail `istream read
error / refill buffer / archive stream read error (header) /
stream cancelled`. Blob flavor (whole>=256K at fail): middle
`Refill buffer failed / read error / ... (blob)` + `N
entries failed to extract` (+ `reading payload` x2 rule
unchanged: whole>=512K && kcut!=1; all tails/counts green
unchanged). No chain line, no worker stanza anywhere under
-t 1 (trailing garbage -> 94036800 header, trail probe).

## 3. Unclo rule change (got>unc now hard decfail)

compression_decode_buffer SILENTLY TRUNCATES over-decode
(dst=unc). Default-t tolerated unclo (extract + worker
stanza + count); -t-1 hard-fails short 94039800, 0 files, 0
tails (m3 uc10/25/36/37/100 first-hand 12/12). Fix (C +
proto _lib_dec): +1 dst (unc+1 returns unc+1 iff true output
exceeds unc) -> decfail. Other proto paths (ctool/zlib/lzma)
already exact-size-checked; zbm unclo unprobed (no shape).
Midchain unclo (unc-1 blk idx1, whole=1M): blob 94039800 +
`1 entries` + holdback-1 prefix, C IDENTICAL (stderr+bytes);
A-032 mc-uc header+0files reconciled as block0 shape
(1-indexed blk1), uc10-family. Battery: runm3 collapsed
(IDENT + t1pin, uc/x retired); uc content checks -> empty3.

## 4. Holdback-1 prefix rule (retires M2-dev + trunchdr-cap)

Midchain DAT-short content = whole 256K chunks of dav minus
the final chunk, floor 0 (wlen = floor((dav-256K)/256K)*256K,
min 0); A-028 presence gate UNCHANGED. Dataset: 7-point cut
series (whole 1/2/3M -> big2 1/5/9ch x3, kind-independent) +
9-shape x10 survey + exact shortend/dav via proto parser +
r2 actuals (O=C+1ch uniform on 13 differing shapes; 20+
equal-shapes traced same). C+proto: replaced dev + cap
branches. C modals now equal -t-1 oracle modals on all 13.

## 5. Residual -wt race + SET policy + -wt-1 proposal

Stanza/exit/counts pin under -t 1; midchain prefix sizes race
-1ch minority on some shapes (t27500 {9ch x9, 8ch x1} +
battery 8ch; rnd3m battery 8ch + x10 9ch; viewer cut@1.5M
{1ch,2ch}). Cause = -wt flush timing: -wt 1 pins fully
(t27500-wt1 x10; viewer x6). rp-coupling CONFIRMED both
sides: rp=2 ⟺ min-SET leg, rp=0 ⟺ modal (r3 rnd3m minority
had rp=2). Policy: oshape SETs = {modal, modal-1ch} on all
re-pinned midchain shapes (cx-cell precedent); C pins modal
(= race-SET MAX, formula). PROPOSAL (needs PARENT): run
oracle -t 1 -wt 1 + pin singletons (viewer A-032
prescription; -wt-1 value = race MAX here, stanza
byte-ident) — NOT adopted unilaterally (mirror-target
change).

## 6. Battery pins (-t shape in every outer cell)

Adapter aar-decode forces -t 1 (all oracle decode flows via
it: battery + flip-fuzz; sweep already -t 1). t1pin helper
(grep 0x9403 on oracle stderr) in oh/r64/ladder-9403/mc/dv/
m3/ch/t2 cells. runchain race modes (setlone/setchain/
blobrace) retired -> IDENT + pin (25 shapes). New totals:
1069/1069 + cvp 150/150 + flip 200/200 + asan 13/0 + raw
130/0 + units green (r4, first-hand).
