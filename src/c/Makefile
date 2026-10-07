# aae C port. Build outputs NEVER in repo: BUILDDIR defaults to NVME.
BUILDDIR ?= /Volumes/NVME/applearchive-cleanroom-ws/build/aae
CC ?= cc
CFLAGS ?= -O2 -Wall -Wextra -std=c11
LDLIBS = -lz

all: $(BUILDDIR)/aae

$(BUILDDIR)/aae: aae.c
	mkdir -p $(BUILDDIR)
	$(CC) $(CFLAGS) -o $@ $< $(LDLIBS)

clean:
	rm -f $(BUILDDIR)/aae
