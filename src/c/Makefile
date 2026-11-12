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
.PHONY: all rgramc
rgramc: $(BUILDDIR)/rgramc

$(BUILDDIR)/rgramc: rgramc.c rgramc.h
	mkdir -p $(BUILDDIR)
	$(CC) $(CFLAGS) -o $@ rgramc.c

clean:
	rm -f $(BUILDDIR)/rgramc
