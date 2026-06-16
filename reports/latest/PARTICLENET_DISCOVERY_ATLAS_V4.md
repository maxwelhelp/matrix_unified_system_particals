# ParticleNet Discovery Atlas v4

Purpose: convert causal patches and dynamic graph routes into candidate physics/mechanistic hypotheses. These are not discovery claims yet; they are candidates requiring heldout validation and physics review.

checkpoint=local_checkpoints/part/ParticleNet_kinpid.pt
mode=kinpid
n=1280
missing=[] unexpected=[]

## Baseline

```json
{
  "n": 1280,
  "acc": 0.768750011920929,
  "pred_counts": [
    123,
    127,
    103,
    147,
    131,
    127,
    126,
    129,
    138,
    129
  ],
  "true_counts": [
    128,
    128,
    128,
    128,
    128,
    128,
    128,
    128,
    128,
    128
  ]
}
```

## Candidate discovery hypotheses

- Global: strongest causal components are edge_conv_zero[1:edge_conv], edge_conv_zero[0:edge_conv], features_zero[input:all_features], feature_group_zero[input:coords_last2], edge_conv_zero[2:edge_conv].
- Feature hypothesis: most influential explicit channels/groups are coords_last2, kin_logs_0_4, pid_charge_5_10, part_deta, part_logptrel.
- Particle-subset hypothesis: removing top_pt particles produces strongest top-8 particle control effect; compare against random_control before claiming physics.
- Route layer 0: neighbor ΔR differs by class; lowest mean label_Wqq=0.1331, highest mean label_Tbqq=0.2521.
- Route layer 1: neighbor ΔR differs by class; lowest mean label_Wqq=0.1586, highest mean label_Tbqq=0.2775.
- Route layer 2: neighbor ΔR differs by class; lowest mean label_Wqq=0.1614, highest mean label_Tbqq=0.2863.

## Corrected particle-subset controls
| group | delta_logit | KL | top1 | acc->patch_acc | jaccard_top_pt |
| --- | --- | --- | --- | --- | --- |
| top_pt | 5.6079 | 2.2219 | 0.5227 | 0.7688->0.4617 | 1.0000 |
| top_energy | 5.5833 | 2.2063 | 0.5234 | 0.7688->0.4625 | 0.9381 |
| wide_angle_high_dr | 0.6705 | 0.2792 | 0.8555 | 0.7688->0.7047 | 0.0072 |
| core_low_dr | 1.2667 | 0.5364 | 0.8484 | 0.7688->0.6992 | 0.0769 |
| random_control | 0.4536 | 0.2265 | 0.9023 | 0.7688->0.7398 | 0.0382 |

## Dynamic KNN / EdgeConv route stats by class
| layer | class | k | neighbor_dr_mean | neighbor_dr_p90 | neighbor_pt_mean | neighbor_energy_mean |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | label_QCD | 16 | 0.1677 | 0.4240 | 19.2666 | 28.3312 |
| 0 | label_Hbb | 16 | 0.1900 | 0.3893 | 16.6722 | 23.5044 |
| 0 | label_Hcc | 16 | 0.1982 | 0.3896 | 17.5731 | 25.3255 |
| 0 | label_Hgg | 16 | 0.1735 | 0.3277 | 13.1024 | 19.8329 |
| 0 | label_H4q | 16 | 0.1761 | 0.3349 | 14.1800 | 21.0894 |
| 0 | label_Hqql | 16 | 0.1633 | 0.3270 | 23.3292 | 32.8237 |
| 0 | label_Zqq | 16 | 0.1567 | 0.3199 | 20.0157 | 29.5247 |
| 0 | label_Wqq | 16 | 0.1331 | 0.2565 | 21.9382 | 36.4646 |
| 0 | label_Tbqq | 16 | 0.2521 | 0.4747 | 13.6300 | 19.7081 |
| 0 | label_Tbl | 16 | 0.2146 | 0.4588 | 19.6287 | 27.1564 |
| 1 | label_QCD | 16 | 0.1977 | 0.4672 | 13.9999 | 20.2639 |
| 1 | label_Hbb | 16 | 0.2099 | 0.4274 | 13.4466 | 18.7812 |
| 1 | label_Hcc | 16 | 0.2174 | 0.4149 | 13.8027 | 20.0881 |
| 1 | label_Hgg | 16 | 0.1919 | 0.3660 | 9.5830 | 14.3840 |
| 1 | label_H4q | 16 | 0.2028 | 0.3836 | 10.3692 | 15.3164 |
| 1 | label_Hqql | 16 | 0.1912 | 0.3826 | 14.5299 | 20.3548 |
| 1 | label_Zqq | 16 | 0.1873 | 0.3759 | 14.3500 | 20.9484 |
| 1 | label_Wqq | 16 | 0.1586 | 0.3072 | 16.4282 | 26.7201 |
| 1 | label_Tbqq | 16 | 0.2775 | 0.5042 | 11.0446 | 15.8140 |
| 1 | label_Tbl | 16 | 0.2357 | 0.4988 | 15.5409 | 21.2267 |
| 2 | label_QCD | 16 | 0.2046 | 0.4911 | 13.7327 | 19.8864 |
| 2 | label_Hbb | 16 | 0.2155 | 0.4386 | 13.5020 | 18.8979 |
| 2 | label_Hcc | 16 | 0.2236 | 0.4280 | 13.8889 | 20.1892 |
| 2 | label_Hgg | 16 | 0.1960 | 0.3733 | 9.6962 | 14.5569 |
| 2 | label_H4q | 16 | 0.2108 | 0.3997 | 10.3143 | 15.2705 |
| 2 | label_Hqql | 16 | 0.1999 | 0.4085 | 14.3939 | 20.1763 |
| 2 | label_Zqq | 16 | 0.1909 | 0.3893 | 14.7959 | 21.5194 |
| 2 | label_Wqq | 16 | 0.1614 | 0.3125 | 17.0187 | 27.7559 |
| 2 | label_Tbqq | 16 | 0.2863 | 0.5207 | 10.8102 | 15.6088 |
| 2 | label_Tbl | 16 | 0.2419 | 0.5176 | 14.8988 | 20.3350 |

## Existing v3 causal tables used as context

- `reports/latest/tables/hypothesis_global_patches.csv`
- `reports/latest/tables/hypothesis_per_class.csv`
- `reports/latest/tables/hypothesis_examples.csv`

## New v4 tables

- `reports/latest/tables/discovery_route_knn_stats.csv`
- `reports/latest/tables/discovery_particle_controls.csv`
