# DPROBE-03 metadata fidelity (writer black-box, attr tree)

Tree: f.txt (0640, xattr tag=TAGBYTES, fractional mtime) + rel/abs symlinks
+ sub/g.txt (empty-value xattr) + sub dir. All 7 algs.

## Pinned layouts (own bytes)
- XAT record: u32le size (incl 4B) + NUL-term name + value. f.txt 64B =
  36B provenance + 28B tag; g.txt 58B = 36B + 22B (0B value OK).
- timespec: S/8B = sec u64le; T/12B = sec u64le + nsec u32le
  (1577952245.123456789 verified).
- oracle restores: mode, uid/gid, mtime+atime ns, birthtime, xattrs
  (incl symlink xattrs, incl empty values).

## Proto behavior (aad.py v2-meta)
- applies MOD/chmod, UID/GID/chown (EPERM-tolerant), MTM/utime ns,
  XAT/setxattr (nofollow for links), dir metadata deferred post-children.
- 7/7 algs FULL-MATCH vs oracle (mode/uid/gid/mtime-ns/bytes/links/xattrs).
- GAP: birthtime (CTM) not restored (needs setattrlist; deliverable item).
