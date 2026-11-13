# src/c objects linked into the unified aae-cli (see root Makefile) plus the
# test-only rgramc verifier. Standalone aae/aeadc targets are dropped: the
# batteries drive the unified binary's subcommands now (aar-encode --alg X,
# aeadc ...); only rgramc keeps a target (test_rgram_c.sh, NOT shipped).
BUILDDIR ?= build
CC ?= cc
CFLAGS ?= -O2 -Wall -Wextra -std=c11

all: rgramc

# Phony short name (PV-0f57814): bare `make rgramc` must NOT fall
# through to the implicit rule (which drops ./rgramc in the repo).
.PHONY: all rgramc verify-tables
rgramc: $(BUILDDIR)/rgramc

# verify-tables (NOT in all, NOT shipped): regen + verify the generated
# table artifacts, keyed on their inputs. lzraventab.h regenerates from
# ../rgram.py via gen_lzraventab.py (byte-exact diff or fail). rgramc.c
# comes from the NVME scratch generator (see its header); here the table
# literals it shares with lzraventab.h are pinned against the same
# ../rgram.py inputs, with full parity covered by tests/test_rgram_c.sh
# (which should invoke this target). Never slows the default build.
verify-tables: ../rgram.py gen_lzraventab.py lzraventab.h rgramc.c rgram_gen.py
	tmp=$$(mktemp -d); \
	regen=$$(mktemp -d); \
	python3 gen_lzraventab.py > "$$tmp/lzraventab.h" || \
	    { echo "verify-tables: generator failed" >&2; rm -rf "$$tmp" "$$regen"; exit 1; }; \
	diff -u lzraventab.h "$$tmp/lzraventab.h" || \
	    { echo "verify-tables: lzraventab.h stale; run python3 src/c/gen_lzraventab.py > src/c/lzraventab.h" >&2; rm -rf "$$tmp" "$$regen"; exit 1; }; \
	rm -rf "$$tmp"; \
	echo "verify-tables: lzraventab.h in sync with ../rgram.py"; \
	python3 rgram_gen.py ../rgram.py "$$regen/rgramc.c" || \
	    { echo "verify-tables: rgram_gen failed" >&2; rm -rf "$$regen"; exit 1; }; \
	python3 -c 'import sys; a,b=[open(p).read() for p in sys.argv[1:3]]; s=lambda t: t.split("*/",1)[1] if t.startswith("/*") else t; x,y=s(a),s(b); assert x==y, "rgramc.c drift: %d body bytes differ" % abs(len(x)-len(y)); print("verify-tables: rgramc.c body matches regen (%d bytes)" % len(y))' "$$regen/rgramc.c" rgramc.c || \
	    { echo "verify-tables: rgramc.c stale; run python3 src/c/rgram_gen.py src/rgram.py src/c/rgramc.c" >&2; rm -rf "$$regen"; exit 1; }; \
	rm -rf "$$regen"; \
	echo "verify-tables: rgramc.c in sync with ../rgram.py"; \
	python3 -c 'import ast,sys; py,cc=sys.argv[1],sys.argv[2]; t=ast.parse(open(py).read()); want=("_T2SCRAM","_T2W32","_T2W240","_T3CASC","_T3P245"); got={n.targets[0].id: ast.literal_eval(n.value) for n in t.body if type(n).__name__=="Assign" and len(n.targets)==1 and type(n.targets[0]).__name__=="Name" and n.targets[0].id in want}; assert set(got)==set(want), "tables missing"; x=open(cc).read(); need=[str(v) for v in got["_T2SCRAM"]]+[str(v) for v in got["_T2W32"]]+["{%d, %d}"%(a,b) for a,b in got["_T2W240"]]+["\""+r+"\"" for r in got["_T3CASC"]+got["_T3P245"]]; bad=[s for s in need if s not in x]; assert not bad, "rgramc.c missing literals"; print("verify-tables: rgramc.c literals match ../rgram.py")' ../rgram.py rgramc.c

$(BUILDDIR)/rgramc: rgramc.c rgramc.h
	mkdir -p $(BUILDDIR)
	$(CC) $(CFLAGS) -o $@ rgramc.c

clean:
	rm -f $(BUILDDIR)/rgramc
