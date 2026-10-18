# NOTE-cport-hb12: band127 reruns after external SIGTERM

- seat agent-1 @04:33Z. PYID127 + py127 batteries both SIGTERM'd ~04:31Z
  (external; py was 2993 lines 0 FAIL). C battery already GREEN 6674/6674.
- both relaunched fresh (idempotent; PYID reuses corpus). No code changed.
- next: both green -> commit C127 -> NOTE-129-c127 -> merge P106.
