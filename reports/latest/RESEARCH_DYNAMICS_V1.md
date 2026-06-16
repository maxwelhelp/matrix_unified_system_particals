# Research Dynamics v1

This report compares evidence graph snapshots across runs.

- Graph snapshots: **10**
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
| 6 | 2026-06-16T04:26:01.675182+00:00 | 0.7574 | 2560 | 1080 | 1255 | 24 | 959 |
| 7 | 2026-06-16T04:29:01.473693+00:00 | 0.7574 | 2560 | 1080 | 1255 | 24 | 959 |
| 8 | 2026-06-16T04:30:31.493657+00:00 | 0.7574 | 2560 | 1080 | 1255 | 24 | 959 |
| 9 | 2026-06-16T05:06:52.665592+00:00 | 0.7574 | 2560 | 2027 | 2241 | 24 | 1865 |

## Latest top heads
| rank | head | gate_abs | delta_gate | delta_rank | patch_drop | role |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | L1_ch112:128 | 0.8006 | 0.0000 | 0 | 0.0000 | middle learned-neighborhood / route-composition head |
| 2 | L0_ch40:48 | 0.6735 | 0.0000 | 0 | 0.0000 | early feature/geometry/PID reader |
| 3 | L2_ch224:256 | 0.6716 | 0.0000 | 0 | 0.0000 | late aggregation / class-evidence head |
| 4 | L1_ch16:32 | 0.6645 | 0.0000 | 0 | 0.0000 | middle learned-neighborhood / route-composition head |
| 5 | L0_ch48:56 | 0.3620 | 0.0000 | 0 | 0.0000 | early feature/geometry/PID reader |
| 6 | L2_ch128:160 | 0.3511 | 0.0000 | 0 | 0.0000 | late aggregation / class-evidence head |
| 7 | L0_ch8:16 | 0.3350 | 0.0000 | 0 | 0.0000 | early feature/geometry/PID reader |
| 8 | L2_ch64:96 | 0.2970 | 0.0000 | 0 | 0.0000 | late aggregation / class-evidence head |
| 9 | L2_ch0:32 | 0.2642 | 0.0000 | 0 | 0.0000 | late aggregation / class-evidence head |
| 10 | L0_ch0:8 | 0.2327 | 0.0000 | 0 | 0.0000 | early feature/geometry/PID reader |

## Latest class particle patterns
| class | n | mean_score | mean_pt | mean_deltaR | particle0_fraction | charged_fraction |
| --- | --- | --- | --- | --- | --- | --- |
| label_Zqq | 29 | 2.5199 | 34.9848 | 0.2194 | 0.0690 | 0.5172 |
| label_Tbl | 765 | 2.4363 | 34.6515 | 0.3272 | 0.0641 | 0.4026 |
| label_Hqql | 972 | 2.3994 | 36.4722 | 0.1991 | 0.0638 | 0.4465 |
| label_QCD | 19 | 2.3756 | 70.2321 | 0.1566 | 0.1053 | 0.3684 |
| label_Wqq | 80 | 2.3566 | 37.5050 | 0.1724 | 0.0625 | 0.4875 |

## Output files

- JSON: `manifests/latest/research_dynamics_v1.json`
- Head dynamics: `reports/latest/tables/dynamics_head_ranks.csv`
- Particle dynamics: `reports/latest/tables/dynamics_particle_patterns.csv`
- Hypothesis dynamics: `reports/latest/tables/dynamics_hypotheses.csv`
