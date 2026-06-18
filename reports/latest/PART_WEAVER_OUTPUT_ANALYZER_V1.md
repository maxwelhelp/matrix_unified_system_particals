# PART_WEAVER_OUTPUT_ANALYZER_V1

- glob: `reports/latest/part_weaver_predict_smoke_v3_*.root`
- files: **10**

## Summary
| file | n | accuracy | labels | scores | prefix | error |
| --- | --- | --- | --- | --- | --- | --- |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | 100000 | 0.92714 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | 100000 | 0.84526 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | 100000 | 0.79843 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | 100000 | 0.98004 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | 100000 | 0.84481 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | 100000 | 0.95315 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_TTBarLep.root | 100000 | 0.9852 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_WToQQ.root | 100000 | 0.79911 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_ZJetsToNuNu.root | 100000 | 0.77626 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_ZToQQ.root | 100000 | 0.69457 | 10 | 10 | score_ |  |

## Top confusion pairs
| file | true | pred | n |
| --- | --- | --- | --- |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Hbb | 92714 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Zqq | 3020 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Hcc | 1437 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Hgg | 1119 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Tbqq | 928 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_QCD | 407 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_H4q | 187 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Wqq | 103 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Tbl | 59 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Hqql | 26 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Hcc | 84526 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_H4q | 4195 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Hgg | 3843 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Zqq | 3166 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Wqq | 1309 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_QCD | 1190 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Hbb | 888 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Tbqq | 712 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Hqql | 149 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Tbl | 22 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Hgg | 79843 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_H4q | 7387 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_QCD | 4506 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Hcc | 3144 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Hbb | 1951 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Zqq | 1939 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Wqq | 741 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Tbqq | 454 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Hqql | 22 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Tbl | 13 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Hqql | 98004 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Tbl | 924 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Wqq | 483 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Zqq | 176 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Hcc | 151 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_H4q | 92 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_QCD | 89 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Tbqq | 54 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Hgg | 14 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Hbb | 13 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_H4q | 84481 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Hgg | 7874 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Hcc | 2982 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Zqq | 1392 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Wqq | 1213 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_QCD | 983 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Tbqq | 788 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Hbb | 178 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Hqql | 108 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Tbl | 1 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Tbqq | 95315 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_H4q | 1015 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Hbb | 893 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_QCD | 783 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Hcc | 715 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Wqq | 541 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Hgg | 413 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Zqq | 249 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Hqql | 44 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Tbl | 32 |
