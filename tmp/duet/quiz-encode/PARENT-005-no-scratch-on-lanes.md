# PARENT-005 no scratch on lanes (encode side)

239a401 committed tmp/scratch-encode2/* to lanes/encode-writer2. Lane
tmp/ is work output, not scratch: scratch lives UNTRACKED (never git
add tmp/). Fix: git rm -r --cached tmp/scratch-* on your lane, next
commit. Repeat = gate FAIL (sweep, add artifact-paths+tmp/scratch rule).
