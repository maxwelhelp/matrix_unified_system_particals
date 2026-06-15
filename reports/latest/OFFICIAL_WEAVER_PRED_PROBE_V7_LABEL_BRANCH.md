# Official Weaver prediction probe v7 label branch

pred_dir=runs/official_weaver_predict_v5_kinpid
n_files=10

## Accuracy by filename mapping

acc=0.101503 label_perm_upper_greedy=0.151806

true_counts=`[100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]`

## Accuracy by one-hot label_* branches

acc=0.101503 label_perm_upper_greedy=0.151806

true_counts=`[100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]`

## Accuracy by _label_ branch

acc=0.101503 label_perm_upper_greedy=0.151806

true_counts=`[100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]`

| file | sample | file-label | entries | acc_file | acc_label_* | acc__label_ | pred_counts | _label_counts | label*_counts |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| `pred_HToBB.root` | HToBB | label_Hbb | 100000 | 0.00276 | 0.00276 | 0.00276 | `[80713, 276, 981, 113, 1134, 80, 13399, 2760, 20, 524]` | `[0, 100000, 0, 0, 0, 0, 0, 0, 0, 0]` | `[0, 100000, 0, 0, 0, 0, 0, 0, 0, 0]` |
| `pred_HToCC.root` | HToCC | label_Hcc | 100000 | 0.00886 | 0.00886 | 0.00886 | `[76651, 281, 886, 65, 805, 19, 17414, 3740, 9, 130]` | `[0, 0, 100000, 0, 0, 0, 0, 0, 0, 0]` | `[0, 0, 100000, 0, 0, 0, 0, 0, 0, 0]` |
| `pred_HToGG.root` | HToGG | label_Hgg | 100000 | 0.00011 | 0.00011 | 0.00011 | `[81099, 35, 2952, 11, 3825, 2, 11637, 399, 30, 10]` | `[0, 0, 0, 100000, 0, 0, 0, 0, 0, 0]` | `[0, 0, 0, 100000, 0, 0, 0, 0, 0, 0]` |
| `pred_HToWW2Q1L.root` | HToWW2Q1L | label_Hqql | 100000 | 0.00421 | 0.00421 | 0.00421 | `[39761, 3318, 8025, 258, 1013, 421, 45343, 1132, 48, 681]` | `[0, 0, 0, 0, 0, 100000, 0, 0, 0, 0]` | `[0, 0, 0, 0, 0, 100000, 0, 0, 0, 0]` |
| `pred_HToWW4Q.root` | HToWW4Q | label_H4q | 100000 | 0.039 | 0.039 | 0.039 | `[81814, 40, 3047, 46, 3900, 1, 10629, 505, 6, 12]` | `[0, 0, 0, 0, 100000, 0, 0, 0, 0, 0]` | `[0, 0, 0, 0, 100000, 0, 0, 0, 0, 0]` |
| `pred_TTBar.root` | TTBar | label_Tbqq | 100000 | 1e-05 | 1e-05 | 1e-05 | `[97969, 12, 65, 5, 350, 4, 1147, 439, 1, 8]` | `[0, 0, 0, 0, 0, 0, 0, 0, 100000, 0]` | `[0, 0, 0, 0, 0, 0, 0, 0, 100000, 0]` |
| `pred_TTBarLep.root` | TTBarLep | label_Tbl | 100000 | 0.03241 | 0.03241 | 0.03241 | `[51609, 9487, 8832, 252, 245, 1827, 20837, 3623, 47, 3241]` | `[0, 0, 0, 0, 0, 0, 0, 0, 0, 100000]` | `[0, 0, 0, 0, 0, 0, 0, 0, 0, 100000]` |
| `pred_WToQQ.root` | WToQQ | label_Wqq | 100000 | 0.00421 | 0.00421 | 0.00421 | `[29388, 1120, 7370, 167, 490, 5, 60806, 421, 66, 167]` | `[0, 0, 0, 0, 0, 0, 0, 100000, 0, 0]` | `[0, 0, 0, 0, 0, 0, 0, 100000, 0, 0]` |
| `pred_ZJetsToNuNu.root` | ZJetsToNuNu | label_QCD | 100000 | 0.37151 | 0.37151 | 0.37151 | `[37151, 261, 2947, 267, 1457, 20, 56511, 810, 458, 118]` | `[100000, 0, 0, 0, 0, 0, 0, 0, 0, 0]` | `[100000, 0, 0, 0, 0, 0, 0, 0, 0, 0]` |
| `pred_ZToQQ.root` | ZToQQ | label_Zqq | 100000 | 0.55195 | 0.55195 | 0.55195 | `[36769, 714, 5254, 103, 537, 26, 55195, 922, 46, 434]` | `[0, 0, 0, 0, 0, 0, 100000, 0, 0, 0]` | `[0, 0, 0, 0, 0, 0, 100000, 0, 0, 0]` |

## First output branches

```json
[
  "label_QCD",
  "score_label_QCD",
  "label_Hbb",
  "score_label_Hbb",
  "label_Hcc",
  "score_label_Hcc",
  "label_Hgg",
  "score_label_Hgg",
  "label_H4q",
  "score_label_H4q",
  "label_Hqql",
  "score_label_Hqql",
  "label_Zqq",
  "score_label_Zqq",
  "label_Wqq",
  "score_label_Wqq",
  "label_Tbqq",
  "score_label_Tbqq",
  "label_Tbl",
  "score_label_Tbl",
  "_label_",
  "jet_pt",
  "jet_eta",
  "jet_phi",
  "jet_energy",
  "jet_nparticles",
  "jet_sdmass",
  "jet_tau1",
  "jet_tau2",
  "jet_tau3",
  "jet_tau4"
]
```
