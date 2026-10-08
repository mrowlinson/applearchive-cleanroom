# aae C port. Build outputs NEVER in repo: BUILDDIR defaults to NVME.
BUILDDIR ?= /Volumes/NVME/applearchive-cleanroom-ws/build/aae
CC ?= cc
CFLAGS ?= -O2 -Wall -Wextra -std=c11
# Pinned liblzma 5.8.4 per quiz A-20(b): direct link, never unpinned dlopen.
# sha256 1b2e12cc1b920264f3dd15eeba22e85b8afd589595d8945d1d12a52afa694b09
LZMA_PREFIX ?= /opt/homebrew/opt/xz
LZMA_DYLIB ?= /opt/homebrew/Cellar/xz/5.8.4/lib/liblzma.5.dylib
CFLAGS += -I$(LZMA_PREFIX)/include
LDLIBS = -lz $(LZMA_DYLIB)

all: $(BUILDDIR)/aae

$(BUILDDIR)/aae: aae.c
	mkdir -p $(BUILDDIR)
	$(CC) $(CFLAGS) -o $@ $< $(LDLIBS)

clean:
	rm -f $(BUILDDIR)/aae
