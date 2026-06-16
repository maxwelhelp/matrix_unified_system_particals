# ParticleNet Research Compass v5

Purpose: richer research layer for particle-interaction hypotheses. It adds EdgeConv channel-head groups, per-class feature channels, known observables, and class contrasts.

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

## Priority hypotheses / research notes

- EdgeConv pseudo-head hypothesis: strongest channel-head groups are L1:ch16:32, L2:ch224:256, L0:ch40:48, L1:ch112:128, L0:ch24:32. These groups should be traced as internal model heads.
- Route-width hypothesis L0: label_Wqq has compact neighbor routing (0.1317), label_Tbqq has wide routing (0.2550).
- Route-width hypothesis L1: label_Wqq has compact neighbor routing (0.1572), label_Tbqq has wide routing (0.2793).
- Route-width hypothesis L2: label_Wqq has compact neighbor routing (0.1599), label_Tbqq has wide routing (0.2873).
- Route-width hypothesis L0: label_Wqq has compact neighbor routing (0.1317), label_Tbqq has wide routing (0.2550).
- Route-width hypothesis L1: label_Wqq has compact neighbor routing (0.1572), label_Tbqq has wide routing (0.2793).
- Route-width hypothesis L2: label_Wqq has compact neighbor routing (0.1599), label_Tbqq has wide routing (0.2873).
- label_Hbb: strongest explicit feature-channel candidate is part_deta with logit_drop=6.20.
- label_Hcc: strongest explicit feature-channel candidate is part_logerel with logit_drop=7.02.
- label_Hgg: strongest explicit feature-channel candidate is part_deta with logit_drop=6.11.
- label_Hqql: strongest explicit feature-channel candidate is part_pt_log with logit_drop=10.30.
- label_QCD: strongest explicit feature-channel candidate is part_deta with logit_drop=7.62.
- label_Tbl: strongest explicit feature-channel candidate is part_deta with logit_drop=12.21.
- label_Tbqq: strongest explicit feature-channel candidate is part_deltaR with logit_drop=6.62.
- label_Wqq: strongest explicit feature-channel candidate is part_logptrel with logit_drop=10.45.
- label_Zqq: strongest explicit feature-channel candidate is part_logptrel with logit_drop=9.00.
- Leading-particle control: top_pt ablation accuracy=0.449 vs random=0.725; leading particles are not interchangeable with random particles.

## EdgeConv pseudo-head groups: strongest causal channel groups
| rank | layer | channel_head | channels | delta_logit | KL | top1 | acc->patch_acc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 16:32 | 9.1083 | 1.2719 | 0.5336 | 0.7688->0.5016 |
| 2 | 2 | 7 | 224:256 | 4.7347 | 0.3052 | 0.7945 | 0.7688->0.7180 |
| 3 | 0 | 5 | 40:48 | 3.7969 | 0.4860 | 0.7023 | 0.7688->0.6305 |
| 4 | 1 | 7 | 112:128 | 3.2104 | 0.3737 | 0.7453 | 0.7688->0.6641 |
| 5 | 0 | 3 | 24:32 | 2.3206 | 0.7236 | 0.6266 | 0.7688->0.5711 |
| 6 | 0 | 1 | 8:16 | 1.6796 | 0.3614 | 0.7172 | 0.7688->0.6328 |
| 7 | 2 | 2 | 64:96 | 1.5928 | 0.0313 | 0.9258 | 0.7688->0.7594 |
| 8 | 0 | 6 | 48:56 | 1.4113 | 0.4231 | 0.6984 | 0.7688->0.6203 |
| 9 | 0 | 2 | 16:24 | 1.1317 | 0.3715 | 0.7195 | 0.7688->0.6367 |
| 10 | 2 | 0 | 0:32 | 0.8849 | 0.1905 | 0.8133 | 0.7688->0.6852 |
| 11 | 1 | 6 | 96:112 | 0.8437 | 0.1867 | 0.7867 | 0.7688->0.6891 |
| 12 | 0 | 0 | 0:8 | 0.8413 | 0.4907 | 0.6531 | 0.7688->0.6125 |
| 13 | 2 | 4 | 128:160 | 0.7935 | 0.0480 | 0.9000 | 0.7688->0.7555 |
| 14 | 0 | 7 | 56:64 | 0.5990 | 0.2166 | 0.7781 | 0.7688->0.6852 |
| 15 | 1 | 2 | 32:48 | 0.5084 | 0.1197 | 0.8328 | 0.7688->0.7227 |
| 16 | 0 | 4 | 32:40 | 0.4977 | 0.1155 | 0.8727 | 0.7688->0.7289 |
| 17 | 2 | 5 | 160:192 | 0.4199 | 0.0395 | 0.9383 | 0.7688->0.7641 |
| 18 | 1 | 3 | 48:64 | 0.4195 | 0.0569 | 0.8992 | 0.7688->0.7508 |
| 19 | 1 | 5 | 80:96 | 0.3851 | 0.0905 | 0.9094 | 0.7688->0.7594 |
| 20 | 2 | 6 | 192:224 | 0.3161 | 0.0339 | 0.9469 | 0.7688->0.7570 |
| 21 | 1 | 0 | 0:16 | 0.2519 | 0.1042 | 0.8617 | 0.7688->0.7531 |
| 22 | 2 | 1 | 32:64 | 0.1887 | 0.0493 | 0.9164 | 0.7688->0.7484 |
| 23 | 2 | 3 | 96:128 | 0.1729 | 0.0227 | 0.9398 | 0.7688->0.7672 |
| 24 | 1 | 4 | 64:80 | 0.1584 | 0.0624 | 0.9023 | 0.7688->0.7516 |

## Per-class strongest explicit feature channel
| class | feature | logit_drop | acc_drop | base->patch_acc |
| --- | --- | --- | --- | --- |
| label_H4q | part_dphi | 4.6150 | 0.2656 | 0.8125->0.5469 |
| label_Hbb | part_deta | 6.2005 | 0.1328 | 0.6797->0.5469 |
| label_Hcc | part_logerel | 7.0182 | 0.5000 | 0.5625->0.0625 |
| label_Hgg | part_deta | 6.1087 | 0.6953 | 0.7578->0.0625 |
| label_Hqql | part_pt_log | 10.2994 | 0.9062 | 0.9531->0.0469 |
| label_QCD | part_deta | 7.6218 | 0.1172 | 0.7109->0.5938 |
| label_Tbl | part_deta | 12.2108 | 0.2266 | 0.9766->0.7500 |
| label_Tbqq | part_deltaR | 6.6220 | 0.7812 | 0.8906->0.1094 |
| label_Wqq | part_logptrel | 10.4490 | 0.7031 | 0.7188->0.0156 |
| label_Zqq | part_logptrel | 8.9969 | 0.6250 | 0.6250->0.0000 |

## Known observables by class
| class | n | jet_nparticles_mean | jet_sdmass_mean | jet_tau1_mean | jet_tau2_mean | jet_tau3_mean | jet_tau4_mean |
| --- | --- | --- | --- | --- | --- | --- | --- |
| label_Hbb | 128 | 41.6328 | 101.6025 | 0.1669 | 0.0569 | 0.0402 | 0.0331 |
| label_Hcc | 128 | 38.1562 | 115.6885 | 0.1871 | 0.0576 | 0.0388 | 0.0313 |
| label_Hgg | 128 | 57.5469 | 105.8130 | 0.1820 | 0.0818 | 0.0603 | 0.0500 |
| label_Hqql | 128 | 28.2188 | 76.5480 | 0.1369 | 0.0612 | 0.0329 | 0.0229 |
| label_H4q | 128 | 49.5547 | 107.3009 | 0.2007 | 0.1078 | 0.0680 | 0.0490 |
| label_Tbl | 128 | 28.0859 | 112.1443 | 0.1819 | 0.0474 | 0.0278 | 0.0212 |
| label_Tbqq | 128 | 50.3906 | 159.0246 | 0.2677 | 0.1267 | 0.0623 | 0.0470 |
| label_Wqq | 128 | 30.8438 | 74.9476 | 0.1268 | 0.0442 | 0.0296 | 0.0236 |
| label_QCD | 128 | 39.0312 | 71.4539 | 0.1179 | 0.0550 | 0.0391 | 0.0314 |
| label_Zqq | 128 | 34.9688 | 79.9648 | 0.1315 | 0.0499 | 0.0340 | 0.0277 |

## Class contrast table
| contrast | L0_dr_delta | L1_dr_delta | L2_dr_delta | sdmass_delta | nparticles_delta |
| --- | --- | --- | --- | --- | --- |
| label_Wqq_vs_label_Zqq | -0.0222 | -0.0265 | -0.0272 | -5.0172 | -4.1250 |
| label_Tbqq_vs_label_Tbl | 0.0517 | 0.0539 | 0.0568 | 46.8804 | 22.3047 |
| label_Hbb_vs_label_Hcc | -0.0072 | -0.0091 | -0.0108 | -14.0860 | 3.4766 |
| label_Hbb_vs_label_Hgg | 0.0097 | 0.0113 | 0.0114 | -4.2105 | -15.9141 |
| label_H4q_vs_label_Hqql | 0.0063 | 0.0062 | 0.0061 | 30.7529 | 21.3359 |
| label_QCD_vs_label_Wqq | 0.0259 | 0.0324 | 0.0363 | -3.4937 | 8.1875 |
| label_QCD_vs_label_Tbqq | -0.0973 | -0.0896 | -0.0911 | -87.5707 | -11.3594 |

## Tables written

- `reports/latest/tables/research_edge_channel_heads.csv`
- `reports/latest/tables/research_edge_channel_heads_per_class.csv`
- `reports/latest/tables/research_feature_channels_per_class.csv`
- `reports/latest/tables/research_known_observables_by_class.csv`
- `reports/latest/tables/research_class_contrasts.csv`
