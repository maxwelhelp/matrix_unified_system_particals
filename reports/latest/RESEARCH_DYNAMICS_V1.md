# Research Dynamics v1

This report compares evidence graph snapshots across runs.

- Graph snapshots: **6**
- Real dynamics available: **True**

## Runs
| run | generated | baseline_acc | n_events | nodes | edges | heads | particles |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2026-06-16T04:05:30.121747+00:00 | 0.7574 | 2560 | 1080 | 1255 | 24 | 959 |
| 1 | 2026-06-16T04:10:17.558878+00:00 | 0.7574 | 2560 | 1080 | 1255 | 24 | 959 |
| 2 | 2026-06-16T04:12:40.863052+00:00 | 0.7719 | 640 | 814 | 966 | 24 | 710 |
| 3 | 2026-06-16T04:24:36.833330+00:00 | 0.7719 | 640 | 814 | 966 | 24 | 710 |
| 4 | 2026-06-16T04:24:47.422420+00:00 | 0.7719 | 640 | 814 | 966 | 24 | 710 |
| 5 | 2026-06-16T04:25:12.140529+00:00 | 0.7719 | 640 | 1076 | 1246 | 24 | 950 |

## Latest top heads
| rank | head | gate_abs | delta_gate | delta_rank | patch_drop | role |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | L1_ch112:128 | 0.8644 | 0.0000 | 0 | 0.0000 | middle learned-neighborhood / route-composition head |
| 2 | L2_ch224:256 | 0.7841 | 0.0000 | 0 | 0.0000 | late aggregation / class-evidence head |
| 3 | L1_ch16:32 | 0.7805 | 0.0000 | 0 | 0.0000 | middle learned-neighborhood / route-composition head |
| 4 | L0_ch40:48 | 0.7150 | 0.0000 | 0 | 0.0000 | early feature/geometry/PID reader |
| 5 | L0_ch8:16 | 0.4293 | 0.0000 | 0 | 0.0000 | early feature/geometry/PID reader |
| 6 | L0_ch48:56 | 0.3819 | 0.0000 | 0 | 0.0000 | early feature/geometry/PID reader |
| 7 | L2_ch64:96 | 0.3301 | 0.0000 | 0 | 0.0000 | late aggregation / class-evidence head |
| 8 | L2_ch128:160 | 0.3290 | 0.0000 | 0 | 0.0000 | late aggregation / class-evidence head |
| 9 | L2_ch0:32 | 0.2666 | 0.0000 | 0 | 0.0000 | late aggregation / class-evidence head |
| 10 | L0_ch0:8 | 0.2581 | 0.0000 | 0 | 0.0000 | early feature/geometry/PID reader |

## Latest class particle patterns
| class | n | mean_score | mean_pt | mean_deltaR | particle0_fraction | charged_fraction |
| --- | --- | --- | --- | --- | --- | --- |
| label_H4q | 36 | 3.1633 | 24.7656 | 0.1738 | 0.0833 | 0.3889 |
| label_Wqq | 60 | 3.0352 | 42.4440 | 0.1617 | 0.0833 | 0.4667 |
| label_Hbb | 12 | 2.9578 | 10.5056 | 0.2611 | 0.0833 | 0.5000 |
| label_Zqq | 72 | 2.9576 | 45.4628 | 0.1705 | 0.0833 | 0.4722 |
| label_Hgg | 24 | 2.9388 | 23.1597 | 0.1917 | 0.0833 | 0.3750 |
| label_Hcc | 12 | 2.8848 | 35.0600 | 0.1944 | 0.0833 | 0.5000 |
| label_QCD | 146 | 2.8790 | 54.0609 | 0.1411 | 0.0890 | 0.4315 |
| label_Tbl | 300 | 2.8519 | 39.7091 | 0.3196 | 0.0833 | 0.3900 |
| label_Hqql | 288 | 2.8415 | 46.8404 | 0.2012 | 0.0833 | 0.4757 |

## Output files

- JSON: `manifests/latest/research_dynamics_v1.json`
- Head dynamics: `reports/latest/tables/dynamics_head_ranks.csv`
- Particle dynamics: `reports/latest/tables/dynamics_particle_patterns.csv`
- Hypothesis dynamics: `reports/latest/tables/dynamics_hypotheses.csv`
