# PART_WEAVER_OUTPUT_ANALYZER_V1

- glob: `reports/latest/part_weaver_predict_smoke_v3_*.root`
- files: **10**

## Summary
| file | n | accuracy | labels | scores | prefix | error |
| --- | --- | --- | --- | --- | --- | --- |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | 100000 | 0.00287 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | 100000 | 0.00869 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | 100000 | 6e-05 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | 100000 | 0.00441 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | 100000 | 0.04035 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | 100000 | 0.0 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_TTBarLep.root | 100000 | 0.03339 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_WToQQ.root | 100000 | 0.00467 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_ZJetsToNuNu.root | 100000 | 0.3756 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_ZToQQ.root | 100000 | 0.55071 | 10 | 10 | score_ |  |

## Top confusion pairs
| file | true | pred | n |
| --- | --- | --- | --- |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_QCD | 80867 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Zqq | 13304 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Wqq | 2756 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_H4q | 1112 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Hcc | 900 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Tbl | 543 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Hbb | 287 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Hgg | 125 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Hqql | 88 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Tbqq | 18 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_QCD | 76687 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Zqq | 17418 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Wqq | 3753 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Hcc | 869 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_H4q | 793 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Hbb | 278 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Tbl | 111 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Hgg | 58 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Hqql | 22 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Tbqq | 11 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_QCD | 81378 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Zqq | 11577 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_H4q | 3664 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Hcc | 2931 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Wqq | 390 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Tbqq | 24 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Hbb | 24 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Tbl | 6 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Hgg | 6 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Zqq | 45355 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_QCD | 39728 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Hcc | 7887 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Hbb | 3433 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Wqq | 1081 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_H4q | 1026 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Tbl | 725 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Hqql | 441 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Hgg | 271 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Tbqq | 53 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_QCD | 81525 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Zqq | 10705 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_H4q | 4035 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Hcc | 3104 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Wqq | 532 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Hbb | 44 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Hgg | 44 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Tbl | 7 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Tbqq | 4 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_QCD | 98090 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Zqq | 1104 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Wqq | 408 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_H4q | 317 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Hcc | 63 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Hbb | 9 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Tbl | 6 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Hgg | 2 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Hqql | 1 |
| reports/latest/part_weaver_predict_smoke_v3_TTBarLep.root | label_Tbl | label_QCD | 51497 |
| reports/latest/part_weaver_predict_smoke_v3_TTBarLep.root | label_Tbl | label_Zqq | 20671 |
| reports/latest/part_weaver_predict_smoke_v3_TTBarLep.root | label_Tbl | label_Hbb | 9667 |
