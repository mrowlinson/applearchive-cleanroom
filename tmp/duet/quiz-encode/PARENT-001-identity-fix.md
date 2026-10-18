# PARENT-001 identity fix (all encode seats)

Worktree identity missing -> commits blocked. Fix (parent-provided values, not invented):

git -C <own-worktree> config --worktree user.name "Michael Rowlinson"
git -C <own-worktree> config --worktree user.email "mrowlinson@gmail.com"

Verify: git -C <own-worktree> config --worktree --list | grep user

Rules: exact --worktree command only. Never bare git config (pollutes shared).
Shared identity is the ONLY permitted value. Sweep successor: apply FIRST, then
gate ungated writer tips 2d1ec2d + 9c955a2 before steady-state.
