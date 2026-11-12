# aae C port. Build outputs NEVER in repo: BUILDDIR defaults to NVME.
BUILDDIR ?= /Volumes/NVME/applearchive-cleanroom-ws/build/aae
# aeadc C port (proto/aead.py). OUTDIR selects its own build dir; defaults to
# the cport-aead NVME workspace. Respects OUTDIR env (task) or BUILDDIR.
OUTDIR ?= /Volumes/NVME/applearchive-cleanroom-ws/build/cport-aead
AEADC_OUT ?= $(OUTDIR)
CC ?= cc
CFLAGS ?= -O2 -Wall -Wextra -std=c11
# Pinned liblzma 5.8.4 per quiz A-20(b): direct link, never unpinned dlopen.
# sha256 1b2e12cc1b920264f3dd15eeba22e85b8afd589595d8945d1d12a52afa694b09
LZMA_PREFIX ?= /opt/homebrew/opt/xz
LZMA_DYLIB ?= /opt/homebrew/Cellar/xz/5.8.4/lib/liblzma.5.dylib
CFLAGS += -I$(LZMA_PREFIX)/include
LDLIBS = -lz $(LZMA_DYLIB)
AEADC_LDLIBS = -lz -lcompression $(LZMA_DYLIB)

all: $(BUILDDIR)/aae $(BUILDDIR)/rgramc $(AEADC_OUT)/aeadc

# Phony short names (PV-0f57814): bare `make rgramc` must NOT fall
# through to the implicit rule (which drops ./rgramc in the repo).
.PHONY: aae rgramc aeadc
aae: $(BUILDDIR)/aae
rgramc: $(BUILDDIR)/rgramc
aeadc: $(AEADC_OUT)/aeadc

$(BUILDDIR)/aae: aae.c lz4c.c lz4c.h lzravenc.c lzravenc.h lzraventab.h lzbitmapc.c lzbitmapc.h
	mkdir -p $(BUILDDIR)
	$(CC) $(CFLAGS) -o $@ aae.c lz4c.c lzravenc.c lzbitmapc.c $(LDLIBS)

$(BUILDDIR)/rgramc: rgramc.c rgramc.h
	mkdir -p $(BUILDDIR)
	$(CC) $(CFLAGS) -o $@ rgramc.c

$(AEADC_OUT)/aeadc: aeadc.c aeadc.h
	mkdir -p $(AEADC_OUT)
	$(CC) $(CFLAGS) -o $@ aeadc.c $(AEADC_LDLIBS)

clean:
	rm -f $(BUILDDIR)/aae $(BUILDDIR)/rgramc $(AEADC_OUT)/aeadc
