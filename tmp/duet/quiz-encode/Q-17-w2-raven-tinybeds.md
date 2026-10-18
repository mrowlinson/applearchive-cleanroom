# Q-17 writer2: raven tiny-input I/O beds (granted turf PARENT-007(3))

## Need
- raven black-box hunt start (granted turf, never bedded). Need ct-raven
  oracle outputs for tiny inputs: magic, framing, min-size, store boundary.

## Ask (behavior-only, beds via ct-oracle A-13 POC)
1. `compression_tool -encode -a lzraven` outputs (size + first/last 16B
   hex + rc) for: empty, 1B x{00,ff,41}, 8B zeros, 8B distinct, 64B
   zeros, 64B pattern, 1KB zeros, 1KB random (seeded), 1MB zeros?
2. STORE fallback? (output==input or framed-raw for tiny/incompressible).
   If yes, boundary input size?
3. Magic bytes + fixed header/trailer visible in tiny outputs?

## Use
- Seeds own raven matchfinder hunt; every decision bedded vs oracle
  (bed-war rule, PARENT-007(4)).
