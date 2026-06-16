# ParticleNet Hypothesis Atlas v3

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

## Global causal map: all inputs, particles, EdgeConv and FC layers
| rank | patch | layer | group | delta_logit | KL | top1 | acc->patch_acc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | edge_conv_zero | 1 | edge_conv | 247.2862 | 91.9487 | 0.1008 | 0.7688->0.1000 |
| 2 | edge_conv_zero | 0 | edge_conv | 237.3249 | 19.2966 | 0.0992 | 0.7688->0.1000 |
| 3 | features_zero | input | all_features | 107.7624 | 47.7066 | 0.1000 | 0.7688->0.0984 |
| 4 | feature_group_zero | input | coords_last2 | 34.9960 | 7.2883 | 0.1430 | 0.7688->0.1414 |
| 5 | edge_conv_zero | 2 | edge_conv | 21.8102 | 4.6428 | 0.0961 | 0.7688->0.1000 |
| 6 | feature_group_zero | input | kin_logs_0_4 | 13.7333 | 4.4670 | 0.1727 | 0.7688->0.1516 |
| 7 | mask_all_true | input | mask | 8.1562 | 2.3263 | 0.2531 | 0.7688->0.2398 |
| 8 | feature_group_zero | input | pid_charge_5_10 | 6.5118 | 3.5461 | 0.1078 | 0.7688->0.1078 |
| 9 | feature_channel_zero | input | part_deta | 6.3333 | 1.3511 | 0.5828 | 0.7688->0.5281 |
| 10 | feature_channel_zero | input | part_logptrel | 5.9791 | 1.6570 | 0.4164 | 0.7688->0.3867 |
| 11 | particle_topk_mask_zero | particles | top_pt | 5.6078 | 2.2219 | 0.5227 | 0.7688->0.4617 |
| 12 | particle_topk_mask_zero | particles | top_energy | 5.6078 | 2.2219 | 0.5227 | 0.7688->0.4617 |
| 13 | particle_topk_mask_zero | particles | high_deltaR | 5.6078 | 2.2219 | 0.5227 | 0.7688->0.4617 |
| 14 | feature_channel_zero | input | part_pt_log | 4.7550 | 2.2472 | 0.1742 | 0.7688->0.1680 |
| 15 | feature_channel_zero | input | part_logerel | 4.5308 | 1.0534 | 0.5992 | 0.7688->0.5461 |
| 16 | feature_channel_zero | input | part_dphi | 4.2514 | 0.7558 | 0.5977 | 0.7688->0.5344 |
| 17 | feature_channel_zero | input | part_deltaR | 3.9011 | 0.9497 | 0.5938 | 0.7688->0.5398 |
| 18 | points_zero | input | all_points | 1.2792 | 0.3142 | 0.7641 | 0.7688->0.6719 |
| 19 | feature_channel_zero | input | part_isChargedHadron | 1.2063 | 0.4817 | 0.6625 | 0.7688->0.5953 |
| 20 | feature_channel_zero | input | part_isPhoton | 1.0246 | 0.4568 | 0.6883 | 0.7688->0.6141 |
| 21 | fc_zero | 0 | fc | 0.9013 | 1.7715 | 0.1078 | 0.7688->0.1000 |
| 22 | feature_channel_zero | input | part_isMuon | 0.8819 | 0.5665 | 0.8820 | 0.7688->0.6648 |
| 23 | fc_zero | 1 | fc | 0.8772 | 1.6504 | 0.0961 | 0.7688->0.1000 |
| 24 | feature_channel_zero | input | part_isElectron | 0.8535 | 0.5882 | 0.8789 | 0.7688->0.6719 |
| 25 | feature_channel_zero | input | part_charge | 0.8067 | 0.4572 | 0.6883 | 0.7688->0.6133 |
| 26 | feature_channel_zero | input | part_isNeutralHadron | 0.5894 | 0.2590 | 0.7984 | 0.7688->0.6906 |
| 27 | feature_channel_zero | input | part_e_log | 0.3380 | 0.0558 | 0.8859 | 0.7688->0.7430 |

## Per-class strongest causal patch
| class | patch | layer | group | acc_drop | logit_drop | base->patch_acc |
| --- | --- | --- | --- | --- | --- | --- |
| label_QCD | edge_conv_zero | 1 | edge_conv | 0.7109 | 254.7318 | 0.7109->0.0000 |
| label_Hbb | edge_conv_zero | 1 | edge_conv | 0.6797 | 277.2245 | 0.6797->0.0000 |
| label_Hcc | edge_conv_zero | 1 | edge_conv | 0.5625 | 277.1858 | 0.5625->0.0000 |
| label_Hgg | edge_conv_zero | 1 | edge_conv | 0.7578 | 321.1304 | 0.7578->0.0000 |
| label_H4q | edge_conv_zero | 1 | edge_conv | 0.8125 | 296.8640 | 0.8125->0.0000 |
| label_Hqql | edge_conv_zero | 1 | edge_conv | 0.9531 | 168.4021 | 0.9531->0.0000 |
| label_Zqq | edge_conv_zero | 1 | edge_conv | 0.6250 | 262.0989 | 0.6250->0.0000 |
| label_Wqq | edge_conv_zero | 0 | edge_conv | 0.7188 | 239.4601 | 0.7188->0.0000 |
| label_Tbqq | edge_conv_zero | 1 | edge_conv | 0.8906 | 243.0281 | 0.8906->0.0000 |
| label_Tbl | edge_conv_zero | 0 | edge_conv | 0.9766 | 255.6412 | 0.9766->0.0000 |

## Candidate hypotheses

- label_H4q: class decision is strongly dependent on `edge_conv_zero:1:edge_conv`; patch acc drop=0.812.
- label_Hbb: class decision is strongly dependent on `edge_conv_zero:1:edge_conv`; patch acc drop=0.680.
- label_Hcc: class decision is strongly dependent on `edge_conv_zero:1:edge_conv`; patch acc drop=0.562.
- label_Hgg: class decision is strongly dependent on `edge_conv_zero:1:edge_conv`; patch acc drop=0.758.
- label_Hqql: class decision is strongly dependent on `edge_conv_zero:1:edge_conv`; patch acc drop=0.953.
- label_QCD: class decision is strongly dependent on `edge_conv_zero:1:edge_conv`; patch acc drop=0.711.
- label_Tbl: class decision is strongly dependent on `edge_conv_zero:0:edge_conv`; patch acc drop=0.977.
- label_Tbqq: class decision is strongly dependent on `edge_conv_zero:1:edge_conv`; patch acc drop=0.891.
- label_Wqq: class decision is strongly dependent on `edge_conv_zero:0:edge_conv`; patch acc drop=0.719.
- label_Zqq: class decision is strongly dependent on `edge_conv_zero:1:edge_conv`; patch acc drop=0.625.
- Global mechanism: strongest causal components are edge_conv_zero[1:edge_conv], edge_conv_zero[0:edge_conv], features_zero[input:all_features].

## Example-level signed drops
| idx | pred | pred_label | true | true_label | conf | pred_logit | true_logit | drop_features_zero_input_all_features | drop_feature_group_zero_input_coords_last2 | drop_feature_group_zero_input_kin_logs_0_4 | drop_mask_all_true_input_mask | drop_feature_group_zero_input_pid_charge_5_10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1093 | 0 | label_QCD | 0 | label_QCD | 0.9999281167984009 | -16.417905807495117 | -16.417905807495117 | 5.238534927368164 | 8.732532501220703 | -1.190047264099121 | 20.129968643188477 | 0.7359466552734375 |
| 1089 | 0 | label_QCD | 0 | label_QCD | 0.9993353486061096 | -1.7375850677490234 | -1.7375850677490234 | 10.493647575378418 | 30.535337448120117 | 16.479225158691406 | 15.930545806884766 | 0.42104363441467285 |
| 52 | 1 | label_Hbb | 1 | label_Hbb | 0.9963611960411072 | -1.8153471946716309 | -1.8153471946716309 | 84.90340423583984 | 22.41611671447754 | 14.289587020874023 | 10.176950454711914 | 4.043421745300293 |
| 59 | 1 | label_Hbb | 1 | label_Hbb | 0.994642972946167 | -0.9287437796592712 | -0.9287437796592712 | 85.7900161743164 | 7.005889892578125 | 11.750694274902344 | -0.1739301085472107 | 6.088247776031494 |
| 205 | 2 | label_Hcc | 2 | label_Hcc | 0.9881271719932556 | 2.373568058013916 | 2.373568058013916 | 111.58928680419922 | 76.23107147216797 | 17.15643310546875 | 17.258224487304688 | 6.23907470703125 |
| 240 | 2 | label_Hcc | 2 | label_Hcc | 0.9831521511077881 | 2.0879294872283936 | 2.0879294872283936 | 111.30364990234375 | 22.071563720703125 | 15.097912788391113 | 15.987311363220215 | 14.222725868225098 |
| 299 | 3 | label_Hgg | 3 | label_Hgg | 0.9755978584289551 | 0.7866596579551697 | 0.7866596579551697 | 114.31578063964844 | 16.46820068359375 | 6.202691555023193 | 4.548703670501709 | 5.148252010345459 |
| 359 | 3 | label_Hgg | 3 | label_Hgg | 0.9594886898994446 | 0.3844149112701416 | 0.3844149112701416 | 113.91353607177734 | 19.564712524414062 | 5.871368408203125 | 1.9891340732574463 | 5.700177192687988 |
| 522 | 4 | label_H4q | 4 | label_H4q | 0.9965152740478516 | 3.253621816635132 | 3.253621816635132 | 165.09584045410156 | 39.3082275390625 | 9.566410064697266 | 20.66577911376953 | 9.976166725158691 |
| 538 | 4 | label_H4q | 4 | label_H4q | 0.9941601753234863 | 2.821122407913208 | 2.821122407913208 | 164.66334533691406 | 15.750763893127441 | 7.991540908813477 | 11.861734390258789 | 13.58144760131836 |
| 411 | 5 | label_Hqql | 5 | label_Hqql | 0.9999996423721313 | 4.907090663909912 | 4.907090663909912 | 65.86481475830078 | 18.91716957092285 | 34.25741195678711 | 18.98136329650879 | 6.477044582366943 |
| 471 | 5 | label_Hqql | 5 | label_Hqql | 0.9999951124191284 | 3.175077199935913 | 3.175077199935913 | 112.98324584960938 | 39.022647857666016 | 27.083248138427734 | 12.060062408447266 | 5.919833183288574 |
| 1262 | 6 | label_Zqq | 6 | label_Zqq | 0.9536870121955872 | 1.5763447284698486 | 1.5763447284698486 | 118.14971923828125 | 50.90066146850586 | 18.10921859741211 | 7.155026435852051 | 6.36085319519043 |
| 1233 | 6 | label_Zqq | 6 | label_Zqq | 0.9466081857681274 | 1.33008873462677 | 1.33008873462677 | 117.90345764160156 | 9.358807563781738 | 20.757638931274414 | 16.45711898803711 | 6.845595359802246 |
| 916 | 7 | label_Wqq | 7 | label_Wqq | 0.9740322232246399 | 0.7448228597640991 | 0.7448228597640991 | 105.91805267333984 | 43.71139144897461 | 13.980262756347656 | 6.621339321136475 | 6.198444366455078 |
| 909 | 7 | label_Wqq | 7 | label_Wqq | 0.9713129997253418 | 1.0450942516326904 | 1.0450942516326904 | 65.07803344726562 | 23.257265090942383 | 16.330537796020508 | 23.166959762573242 | 3.7617342472076416 |
| 844 | 8 | label_Tbqq | 8 | label_Tbqq | 0.9999363422393799 | 1.2317509651184082 | 1.2317509651184082 | 134.69786071777344 | 27.123443603515625 | 22.40577507019043 | 13.796672821044922 | 2.673454761505127 |
| 840 | 8 | label_Tbqq | 8 | label_Tbqq | 0.9998780488967896 | 2.966946601867676 | 2.966946601867676 | 136.43304443359375 | 13.243598937988281 | 26.692691802978516 | 13.47038745880127 | 10.064638137817383 |
| 669 | 9 | label_Tbl | 9 | label_Tbl | 1.0 | 0.5695033073425293 | 0.5695033073425293 | 47.32085037231445 | 31.75030517578125 | 24.240272521972656 | 7.061765193939209 | 11.600107192993164 |
| 647 | 9 | label_Tbl | 9 | label_Tbl | 1.0 | 1.405466079711914 | 1.405466079711914 | 60.02690124511719 | 19.069049835205078 | 25.797693252563477 | 9.62353801727295 | 9.297764778137207 |

Full CSV tables:
- `reports/latest/tables/hypothesis_global_patches.csv`
- `reports/latest/tables/hypothesis_per_class.csv`
- `reports/latest/tables/hypothesis_examples.csv`
