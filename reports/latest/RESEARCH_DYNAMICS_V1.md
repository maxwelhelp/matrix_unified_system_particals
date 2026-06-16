# Research Dynamics v1

This report compares evidence graph snapshots across runs.

- Graph snapshots: **4**
- Real dynamics available: **True**

## Runs
| run | generated | baseline_acc | n_events | nodes | edges | heads | particles |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2026-06-16T04:05:30.121747+00:00 | 0.7574 | 2560 | 1080 | 1255 | 24 | 959 |
| 1 | 2026-06-16T04:10:17.558878+00:00 | 0.7574 | 2560 | 1080 | 1255 | 24 | 959 |
| 2 | 2026-06-16T04:12:40.863052+00:00 | 0.7719 | 640 | 814 | 966 | 24 | 710 |
| 3 | 2026-06-16T04:24:36.833330+00:00 | 0.7719 | 640 | 814 | 966 | 24 | 710 |

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
| label_Wqq | 36 | 3.1290 | 42.4871 | 0.1323 | 0.0833 | 0.4444 |
| label_H4q | 12 | 2.9607 | 19.0285 | 0.2021 | 0.0833 | 0.3333 |
| label_Hcc | 12 | 2.8848 | 35.0600 | 0.1944 | 0.0833 | 0.5000 |
| label_Zqq | 36 | 2.8564 | 43.2638 | 0.2172 | 0.0833 | 0.5000 |
| label_Tbl | 276 | 2.8474 | 40.9462 | 0.3176 | 0.0833 | 0.3877 |
| label_QCD | 98 | 2.8450 | 58.5640 | 0.1699 | 0.0918 | 0.4388 |
| label_Hqql | 240 | 2.8183 | 46.1975 | 0.1996 | 0.0833 | 0.4708 |

## Output files

- JSON: `manifests/latest/research_dynamics_v1.json`
- Head dynamics: `reports/latest/tables/dynamics_head_ranks.csv`
- Particle dynamics: `reports/latest/tables/dynamics_particle_patterns.csv`
- Hypothesis dynamics: `reports/latest/tables/dynamics_hypotheses.csv`
