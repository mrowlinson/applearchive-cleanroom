# NOTE-scout-hb-r2-06: T2 measured, entering stay-alive poll loop

- NOTE-r2-07 filed (threads deterministic, sparse mapped). All three
  r2 work items done: T1 set + battery (4be6d90, GREEN from fresh
  clone), survey threads (HLC/h/links/omanifest/pbz*-spec), T2
  measurements (-b/-t/sparse).
- Lane clean, nothing pushed, master untouched, no map reads.
- Entering sleep-60/poll loop: checking scout Qs + joint DONE +
  parent PROD each poll. Claim HELD until joint DONE.
