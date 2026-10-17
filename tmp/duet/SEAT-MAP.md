# SEAT-MAP — append one line per launch (seat, run#, work id, live)
# occupancy signal 1 (§8): map + run list. Keep current every turn.
# 2026-10-13 reload: wonder-model runs stopped, all seats relaunched pinned model muse-spark-1.3.
viewer | run spark-r1 | work.v1.workflow.sha256.9e360d1e98c7052836336504e8753254cdbd704430e5309309783fa961d28299 | DEAD 429 ~22:05 | lanes/encode-viewer@4495498
writer2 | run spark-r1 | work.v1.workflow.sha256.3e60ada6459f2f0b37ae314034839a0482da13e6e80316830ab611bf7a1ffd6d | DEAD 429 ~22:05 | lanes/encode-writer2@4b424d7
cport | run spark-r1 | work.v1.workflow.sha256.0294dfda406ec9c91e2688945c47f8a675b1faf993f6e819cbca72fd930f85cb | completed bands 144-146, freed | lanes/encode-cport@6e9422a
sweep | run spark-r1 | work.v1.workflow.sha256.f944d1d0685fcc97a5b3b741d3f5987399bf11f78886447822600def1bc07538 | DEAD 429 ~22:05 | lanes/encode-sweep@d56ce19
cport | run r2 | work.v1.workflow.sha256.9afcd1442bd62960c2eb6c702a4dced8236f33419461bd928376eddb9f10b6d9 | DEAD 429 ~22:05 (landed bands 147-152) | lanes/encode-cport@18f083f
sweep2 | run r1 | work.v1.workflow.sha256.c4bc0afc748afd569deaa574c7a9358ea975a0c857de9632906a8a2753d076b7 | DEAD 429 ~22:05 | lanes/encode-sweep2@d56ce19
# 2026-10-13 22:37 quota reset: all seats relaunched Spark (PARENT-063 outage).
viewer | run r2 | work.v1.workflow.sha256.b150436ace8e47495967585cf8321aad508cb9fe2724229c09bcab1264d8b06f | live | lanes/encode-viewer@4495498 | wt tmp/wt-encode-viewer
writer2 | run r2 | work.v1.workflow.sha256.3745b77721833c129fbe28417fe0a37f95b7279942554d635bdc3d4cc8e1ac00 | live | lanes/encode-writer2@26b73ca | wt tmp/wt-encode-writer2
cport | run r3 | work.v1.workflow.sha256.7f1f09a559a0d0d0c541caa05e443e6884f0ac213dd71bd3370118dc43259938 | live | lanes/encode-cport@bfa3762 | wt tmp/wt-encode-cport
sweep | run r2 | work.v1.workflow.sha256.7da2f9028f5c484c9418519a96daa99afbdb2e6928deb5f1379dcd8686212193 | live | lanes/encode-sweep@d56ce19 | wt tmp/wt-encode-sweep
sweep2 | run r2 | work.v1.workflow.sha256.243e2db6e234e8ac39007bd582bd50dbc1754112fc84629b418e156fb238a656 | live | lanes/encode-sweep2@d56ce19 | wt tmp/wt-encode-sweep2
# 2026-10-13 ~23:35 watch: viewer r2 (b150436a) exited active list; viewer r3 heartbeats fresh (hb-r3-05 23:29, VERIFY batteries 149+150 running); PV-149 legs running. Unknown active work IDs {1037306e,65999f35} = viewer-r3 + PV-149 (map by elimination on PV-149 completion).
viewer | run r2 | work.v1.workflow.sha256.b150436ace8e47495967585cf8321aad508cb9fe2724229c09bcab1264d8b06f | EXITED ~23:2x, r3 live | lanes/encode-viewer@4495498
viewer | run r3 | work.v1.workflow.sha256.1037306e-or-65999f35-TBD | live | lanes/encode-viewer@4495498 | wt tmp/wt-encode-viewer
pv-149 | run 1 | work.v1.workflow.sha256.65999f35-or-1037306e-TBD | live (legs 23:31) | tmp/wt-pv-49f108c
# 2026-10-13 ~23:47 watch: sweep2 r2 (243e2db6) COMPLETED (gated b150+b152); r3 + pv-152 launched same-turn. b154 cut 77afc34. V-150 PASS filed; PV-150 PASS filed; V-149 pending; PV-149 2/4.
sweep2 | run r2 | work.v1.workflow.sha256.243e2db6e234e8ac39007bd582bd50dbc1754112fc84629b418e156fb238a656 | COMPLETED ~23:38 (GATE-150+152) | lanes/encode-sweep2@d56ce19
sweep2 | run r3 | work.v1.workflow.sha256.cbf4b0f036dae62f6bd2c036bd5529b8477bd2278ca707cbfa7c9998b0b31c8e | live (hb1 23:44) | lanes/encode-sweep2@d56ce19 | wt tmp/wt-encode-sweep2
pv-152 | run 1 | work.v1.workflow.sha256.121128c3dc5c551777b29361790a736b2e9c778a137d5b0aca22bd353bd55f4c | live (C+smoke GREEN 23:46) | tmp/wt-pv-dae6b48
# 2026-10-13 ~23:52 watch: PV-149 4/4 GREEN first-hand, PV-49f108c.md filed (V-149 pending); PV-152 2/4+; sweep2-r3 CLAIM-77afc34 (b154); no lane movement; no exits.
# 2026-10-13 ~23:56 watch: ID map RESOLVED by elimination (1037306e gone after pv-149 completion): pv-149=1037306e COMPLETED PASS; viewer-r3=65999f35 live. V-149 PASS 23:50 -> MERGED 149 (277108a) + 150 (9596693) oldest-first, cmp IDENTICAL x2, local-only. Quiz drained thru Q-250/A-256.
pv-149 | run 1 | work.v1.workflow.sha256.1037306ee7c39e9ed0ac744fa9930eabfc8fd32ac6035ad92992ccff8a7807a8 | COMPLETED PASS ~23:53 (PYID 3607/3607) | tmp/wt-pv-49f108c
viewer | run r3 | work.v1.workflow.sha256.65999f35b6a132a34111862c111e1811c9d788f61760c63f838271d81da4297f | live (V-149 + A-256 23:54) | lanes/encode-viewer@4495498 | wt tmp/wt-encode-viewer
# 2026-10-14 00:02 watch: PV-152 4/4 GREEN first-hand (PYID 3644/3644, 0 warn), PV-dae6b48.md filed (V-152 pending, 151 ahead). Quiz drained thru Q-251/A-257. No lane movement, no exits. sweep2-r3/cport quiet 17/22min (batteries/cutting, inside line).
pv-152 | run 1 | work.v1.workflow.sha256.121128c3dc5c551777b29361790a736b2e9c778a137d5b0aca22bd353bd55f4c | COMPLETED PASS ~00:03 (PYID 3644/3644, matches parent PV filing) | tmp/wt-pv-dae6b48
# PV slot open: no successor target (GATE-151 + GATE-154 unfiled). Refills when either GATE lands.
# 2026-10-14 00:07 watch: cport pulled w2 T10R117 py-side (91763c1, wall 0). Quiz Q-253/254 fresh-open. sweep2-r3 quiet 23min (b154 battery, inside line). No GATEs/VERIFYs, no exits, PV slot open.
# 2026-10-14 00:13 watch: cport cut band155 c9dd7f8 (T10R117, PYID 3681/3681, wall 0). sweep2-r3 hb2 broke quiet streak. Quiz Q-254/255 fresh-open. No GATEs/VERIFYs, no exits, PV slot open.
pv-151 | run 1 | work.v1.workflow.sha256.30923fc85f8480770b22ea573b30aff168952fc24b6e3bc9e5fdef54bfa84f60 | live (C+smoke GREEN 00:27) | tmp/wt-pv-885fc37
# 2026-10-14 00:27 watch: GATE-151 PASS (wall 0, no FLAG) -> PV-151 launched same-turn. Quiz drained thru Q-257/A-263. No VERIFYs/new GATEs, no lane movement, no exits.
pv-154 | run 1 | work.v1.workflow.sha256.02b162c789dde7b7ea022a503b20dc8f509633869a4a18793b5750c47b545de4 | live (legs started 00:35) | tmp/wt-pv-77afc34
# 2026-10-14 00:35 watch: GATE-154 PASS (wall 0, no FLAG) -> PV-154 launched same-turn (2nd concurrent PV). cport cut band156 e53abca (T10P120, PYID 3694/3694, wall 0). Q-258 fresh-open. No VERIFYs, no exits.
# 2026-10-14 00:41 watch: all 7 live, filings <9min. sweep2-r3 CLAIM-e53abca (b156). Q-259 fresh-open. PV-151 py ~70%, PV-154 C+smoke green/py early. No VERIFYs, no lane movement, no exits.
pv-151 | run 1 | work.v1.workflow.sha256.30923fc85f8480770b22ea573b30aff168952fc24b6e3bc9e5fdef54bfa84f60 | COMPLETED PASS ~00:44 (PYID 3631/3631, matches parent PV filing) | tmp/wt-pv-885fc37
# 2026-10-14 00:45 watch: PV-151 4/4 GREEN first-hand (PYID 3631/3631, 0 warn), PV-885fc37.md filed (V-151 pending, oldest-first head). w2 T10P131 wall 0. Q-259 fresh-open. No successor PV target (GATE-155/156 unfiled). No seat exits.
# 2026-10-14 00:52 watch: all 6 live, filings <13min. Quiz drained thru Q-259/A-265. PV-154 pyid GREEN + py ~77%. No VERIFYs, no lane movement, no exits.
pv-154 | run 1 | work.v1.workflow.sha256.02b162c789dde7b7ea022a503b20dc8f509633869a4a18793b5750c47b545de4 | COMPLETED PASS ~00:53 (PYID 3669/3669, matches parent PV filing) | tmp/wt-pv-77afc34
# 2026-10-14 00:54 watch: PV-154 4/4 GREEN first-hand (PYID 3669/3669, 0 warn), PV-77afc34.md filed. Back to 5 seats live, filings <14min. Quiz drained thru Q-259/A-265. No VERIFYs/new GATEs, no lane movement, no seat exits. PV slot open (GATE-155/156 unfiled).
# 2026-10-14 01:01 watch: cport pulled w2 T10R118 py-side (b0e6ca5, wall 0). Q-261 fresh-open. sweep2-r3 quiet 21min (b156 battery, inside line). No VERIFYs/GATEs, no exits, PV slot open.
pv-153 | run 1 | work.v1.workflow.sha256.4f9287ed699e61b11418239d1c857911adcaa6281217b056bcefda464aa93acf | live (C+smoke GREEN 01:07) | tmp/wt-pv-c1cd305
# 2026-10-14 01:07 watch: GATE-153 PASS (wall 0, no FLAG) -> PV-153 launched same-turn. cport cut band157 8ed30d1 (T10R118, PYID 3706/3706, wall 0). Q-263 fresh-open. sweep2-r3 quiet 28min (b156 battery; prod if silent next turn). No VERIFYs, no exits.
# 2026-10-14 01:13 watch: V-151 PASS 01:11 -> MERGED 151 (3c4652d), cmp IDENTICAL, local-only. w2 T10R129 wall 0. Q-264 fresh-open. PARENT-PROD-sweep2-r3-01 filed (32min silent, b156 battery). Next head: 152 (V-152 pending).
# 2026-10-14 01:17 watch: HEAD 3c4652d (151). All 6 live. sweep2-r3 37min silent post-prod (drop line 45; successor next turn if dark). Q-264 fresh-open. PV-153 py ~62%. No VERIFYs/GATEs, no lane movement, no exits.
sweep2 | run r3 | work.v1.workflow.sha256.cbf4b0f036dae62f6bd2c036bd5529b8477bd2278ca707cbfa7c9998b0b31c8e | COMPLETED quota 2/2 ~01:28 (GATE-154+156 PASS; hold vindicated) | lanes/encode-sweep2@d56ce19
pv-153 | run 1 | work.v1.workflow.sha256.4f9287ed699e61b11418239d1c857911adcaa6281217b056bcefda464aa93acf | COMPLETED PASS ~01:27 (PYID 3656/3656, matches parent PV filing) | tmp/wt-pv-c1cd305
sweep2 | run r4 | work.v1.workflow.sha256.d25103b3e360d3e03e4a6accca0383369243128a41f120bda0eb87de77db0ca7 | live (hb1 01:28) | lanes/encode-sweep2@d56ce19 | wt tmp/wt-encode-sweep2
pv-156 | run 1 | work.v1.workflow.sha256.80d7e41acf15b709ae99321318eb19f16ee68b620b48bdaacdf1e4f29f668b75 | live (smoke GREEN 01:32) | tmp/wt-pv-e53abca
# 2026-10-14 01:33 watch: r3 done -> r4 + PV-156 launched same-turn. GATE-156 PASS (wall 0, no FLAG). Q-266/267/268 fresh-open (1-8min). cport cutting (commit ~01:27). No VERIFYs, no exits.
# 2026-10-14 01:43 watch: V-152 PASS 01:40 -> MERGED 152 (216b6c6), cmp IDENTICAL, local-only. cport cut band158 5b9cc83 (T10P121, PYID 3719/3719, wall 0; sweep2-r4 CLAIMED). w2 T10P132 wall 0. Q-266..269 open (6-18min, viewer on VERIFYs). Next head: 153 (V-153 pending).
# 2026-10-14 01:47 watch: HEAD 216b6c6 (152). All 6 live, filings <9min. Quiz 5-open Q-266..270 (oldest 23min; prod if 30+ next turns). PV-156 py ~72%. No VERIFYs/GATEs, no lane movement, no exits.
sweep2 | run r4 | work.v1.workflow.sha256.d25103b3e360d3e03e4a6accca0383369243128a41f120bda0eb87de77db0ca7 | COMPLETED quota 2/2 ~03:5x (GATE-158+160 PASS) | lanes/encode-sweep2@d56ce19
pv-156 | run 1 | work.v1.workflow.sha256.80d7e41acf15b709ae99321318eb19f16ee68b620b48bdaacdf1e4f29f668b75 | COMPLETED PASS (PYID 3694/3694, matches parent PV filing) | tmp/wt-pv-e53abca
sweep2 | run r5 | work.v1.workflow.sha256.e12e67dadc17bb10d67da68b02069bfff6cb9a8a25af302726aea850246e0f43 | live | lanes/encode-sweep2@d56ce19 | wt tmp/wt-encode-sweep2
pv-155 | run 1 | work.v1.workflow.sha256.a75781edc04acaf90ef23824605e4115c319b86e9775854debd82ca7bceea2a2 | live | tmp/wt-pv-c9dd7f8
pv-158 | run 1 | work.v1.workflow.sha256.ec976ca72f465c8702f1a1e3f6246fdfba6439aa1d767d03a6487f9a2ed9aba8 | live | tmp/wt-pv-5b9cc83
pv-160 | run 1 | work.v1.workflow.sha256.801c6d10f52a684ec493c1ebb9a3630dce357676919f362de359101355834f34 | live | tmp/wt-pv-5edb95d
# 2026-10-14 04:05 watch: V-153+154 PASS -> MERGED 153 (a6e18c4, 778t) + 154 (1ad47e7, 780t), cmp IDENTICAL x2, local-only. r5 + PV-155/158/160 launched. PV-156 filed (PYID 3694/3694). Walls 0 (155/158/160 + full ranges). Q-291/292 fresh-open. MONITOR installed (persistent 60s lanes/quiz/PV watcher, immediate wake) — cron now backstop. Next head: 155 (PV running).
# 2026-10-17 ~16:05 RESUME (new parent session 01a14b70): old session 01a13733 dead ~14:20. All seats DROPPED (dark past 45min, no orphans). 10 seats relaunched 1 workflow each:
sweep2 | run r25 | work.v1.workflow.sha256.82dce879... | live | lanes/encode-sweep2@d56ce19 | wt tmp/wt-encode-sweep2
sweep | run r16e | work.v1.workflow.sha256.fa57b756... | live | lanes/encode-sweep@d56ce19 | wt tmp/wt-encode-sweep
viewer2 | run r13 | work.v1.workflow.sha256.5ccbedf1... | live | lanes/encode-viewer@4495498 | wt tmp/wt-encode-viewer
writer2b | run r7 | work.v1.workflow.sha256.bdf3ed21... | live | lanes/encode-writer2b@93f4162 | wt tmp/wt-encode-writer2b
cport | run r11 | work.v1.workflow.sha256.0b2f1d1a... | live | lanes/encode-cport@1a423eb | wt tmp/wt-encode-cport
writer2 | run r15 | work.v1.workflow.sha256.9077d199... | live | lanes/encode-writer2@7a913e0 | wt tmp/wt-encode-writer2
viewer | run r22 | work.v1.workflow.sha256.f7cd86d0... | live | lanes/encode-viewer@4495498 | wt tmp/wt-encode-viewer
viewer3 | run r11 | work.v1.workflow.sha256.49e15d19... | live | lanes/encode-viewer@4495498 | wt tmp/wt-encode-viewer
viewer4 | run r12 | work.v1.workflow.sha256.58d941f7... | live | lanes/encode-viewer@4495498 | wt tmp/wt-encode-viewer
scout | run r35 | work.v1.workflow.sha256.671d8560... | live | lanes/encode-container@142e8d4 | wt tmp/wt-encode-container
# PV-b201 (c74c56b) launched parent-shell ~16:08 via bin/pv-band.sh. Merge backlog b201-b218 oldest-first. PARENT-072 filed.
# 2026-10-17 16:41 watch: root pool 8/8 (7 live + parent). viewer3-r11, viewer4-r12, scout-r35 workflows PENDING 0 agents (queued, last-launched). PROD-01 vacated for them (PARENT-073). Rotation via run-cap exits + completion-wake refills. Live 7 all filing healthy.
