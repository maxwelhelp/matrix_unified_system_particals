# PART_WEAVER_OUTPUT_ANALYZER_V1

- glob: `reports/latest/part_weaver_predict_smoke_v3_*.root`
- files: **10**

## Summary
| file | n | accuracy | labels | scores | prefix | error |
| --- | --- | --- | --- | --- | --- | --- |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | 100000 | 0.00039 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | 100000 | 0.03708 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | 100000 | 0.0 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | 100000 | 0.25694 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | 100000 | 0.00012 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | 100000 | 0.0 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_TTBarLep.root | 100000 | 0.14533 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_WToQQ.root | 100000 | 0.00011 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_ZJetsToNuNu.root | 100000 | 0.71085 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_ZToQQ.root | 100000 | 0.07936 | 10 | 10 | score_ |  |

## Top confusion pairs
| file | true | pred | n |
| --- | --- | --- | --- |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Zqq | 49394 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_QCD | 36929 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Hcc | 5413 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Hqql | 4400 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Tbl | 3788 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Hbb | 39 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Wqq | 14 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_H4q | 13 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Hgg | 10 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Zqq | 45779 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Hqql | 18860 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_QCD | 17033 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Tbl | 14345 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Hcc | 3708 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Hbb | 170 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_H4q | 96 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Wqq | 8 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Hgg | 1 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Zqq | 60725 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_QCD | 28441 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Hqql | 6077 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Tbl | 2415 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Hcc | 2251 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Hbb | 74 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_H4q | 14 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Wqq | 3 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_QCD | 37564 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Hqql | 25694 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Hcc | 22311 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Zqq | 9195 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Tbl | 4577 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_H4q | 641 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Wqq | 12 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Hgg | 3 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Hbb | 3 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Zqq | 59219 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_QCD | 22298 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Hqql | 13149 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Hcc | 3396 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Tbl | 1902 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Hbb | 21 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_H4q | 12 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Wqq | 2 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Hgg | 1 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Zqq | 88894 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_QCD | 4421 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Tbl | 3460 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Hqql | 3027 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Hcc | 103 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Hbb | 64 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Wqq | 31 |
| reports/latest/part_weaver_predict_smoke_v3_TTBarLep.root | label_Tbl | label_QCD | 35511 |
| reports/latest/part_weaver_predict_smoke_v3_TTBarLep.root | label_Tbl | label_Zqq | 22264 |
| reports/latest/part_weaver_predict_smoke_v3_TTBarLep.root | label_Tbl | label_Hcc | 20825 |
| reports/latest/part_weaver_predict_smoke_v3_TTBarLep.root | label_Tbl | label_Tbl | 14533 |
| reports/latest/part_weaver_predict_smoke_v3_TTBarLep.root | label_Tbl | label_Hqql | 6443 |
| reports/latest/part_weaver_predict_smoke_v3_TTBarLep.root | label_Tbl | label_H4q | 235 |
| reports/latest/part_weaver_predict_smoke_v3_TTBarLep.root | label_Tbl | label_Hgg | 108 |
| reports/latest/part_weaver_predict_smoke_v3_TTBarLep.root | label_Tbl | label_Wqq | 41 |
| reports/latest/part_weaver_predict_smoke_v3_TTBarLep.root | label_Tbl | label_Hbb | 39 |
