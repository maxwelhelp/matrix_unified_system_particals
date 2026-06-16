# Research Dynamics v1

This report compares evidence graph snapshots across runs.

- Graph snapshots: **11**
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
| 10 | 2026-06-16T05:11:25.686042+00:00 | 0.7602 | 5120 | 2056 | 2269 | 24 | 1893 |

## Latest top heads
| rank | head | gate_abs | delta_gate | delta_rank | patch_drop | role |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | L1_ch112:128 | 0.8424 | 0.0418 | 0 | 0.0000 | middle learned-neighborhood / route-composition head |
| 2 | L1_ch16:32 | 0.7223 | 0.0578 | -2 | 0.0000 | middle learned-neighborhood / route-composition head |
| 3 | L0_ch40:48 | 0.7015 | 0.0281 | 1 | 0.0000 | early feature/geometry/PID reader |
| 4 | L2_ch224:256 | 0.7009 | 0.0293 | 1 | 0.0000 | late aggregation / class-evidence head |
| 5 | L0_ch48:56 | 0.3678 | 0.0058 | 0 | 0.0000 | early feature/geometry/PID reader |
| 6 | L0_ch8:16 | 0.3511 | 0.0161 | -1 | 0.0000 | early feature/geometry/PID reader |
| 7 | L2_ch128:160 | 0.3357 | -0.0154 | 1 | 0.0000 | late aggregation / class-evidence head |
| 8 | L2_ch64:96 | 0.3033 | 0.0063 | 0 | 0.0000 | late aggregation / class-evidence head |
| 9 | L2_ch0:32 | 0.2646 | 3.847e-04 | 0 | 0.0000 | late aggregation / class-evidence head |
| 10 | L0_ch0:8 | 0.2323 | -3.275e-04 | 0 | 0.0000 | early feature/geometry/PID reader |

## Latest class particle patterns
| class | n | mean_score | mean_pt | mean_deltaR | particle0_fraction | charged_fraction |
| --- | --- | --- | --- | --- | --- | --- |
| label_Hgg | 16 | 3.0404 | 23.5073 | 0.1336 | 0.0625 | 0.5000 |
| label_QCD | 16 | 2.9434 | 21.2429 | 0.0465 | 0.0625 | 0.3750 |
| label_Zqq | 32 | 2.6212 | 24.4876 | 0.1733 | 0.0625 | 0.3438 |
| label_Tbl | 489 | 2.5385 | 36.9509 | 0.3147 | 0.0634 | 0.3926 |
| label_Hqql | 1324 | 2.5213 | 36.7218 | 0.2071 | 0.0634 | 0.4569 |
| label_Wqq | 16 | 2.2540 | 44.4436 | 0.2169 | 0.0625 | 0.2500 |

## Output files

- JSON: `manifests/latest/research_dynamics_v1.json`
- Head dynamics: `reports/latest/tables/dynamics_head_ranks.csv`
- Particle dynamics: `reports/latest/tables/dynamics_particle_patterns.csv`
- Hypothesis dynamics: `reports/latest/tables/dynamics_hypotheses.csv`
