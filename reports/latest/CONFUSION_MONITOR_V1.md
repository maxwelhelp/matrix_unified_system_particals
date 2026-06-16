# Confusion Monitor v1

Automatic stream monitor for class-pair confusion shifts. No LLM is used.

- events: **10240**
- accuracy: **0.7662**
- signals: **49**
- baseline: `manifests/latest/confusion_monitor_v1_baseline.json`
- update_baseline: `True`

## Signal board
| status | class_pair | score | reason | next |
| --- | --- | --- | --- | --- |
| ALERT | label_Zqq->label_Wqq | 3.4525 | confusion_rate=0.2236, delta=0.2236, count=229 | run feature ranker for this class pair |
| ALERT | label_Wqq->label_Zqq | 2.1998 | confusion_rate=0.1465, delta=0.1465, count=150 | run feature ranker for this class pair |
| ALERT | label_Hbb->label_Hcc | 1.8420 | confusion_rate=0.1240, delta=0.1240, count=127 | run feature ranker for this class pair |
| ALERT | label_Hcc->label_Hbb | 1.7185 | confusion_rate=0.1162, delta=0.1162, count=119 | run feature ranker for this class pair |
| ALERT | label_Hgg->label_H4q | 1.5801 | confusion_rate=0.1074, delta=0.1074, count=110 | run feature ranker for this class pair |
| ALERT | label_H4q->label_Hgg | 1.3968 | confusion_rate=0.0957, delta=0.0957, count=98 | run feature ranker for this class pair |
| ALERT | label_Hbb->label_Hgg | 1.2451 | confusion_rate=0.0859, delta=0.0859, count=88 | run feature ranker for this class pair |
| ALERT | label_Hcc->label_Hgg | 1.1697 | confusion_rate=0.0811, delta=0.0811, count=83 | run feature ranker for this class pair |
| ALERT | label_Hcc->label_H4q | 1.1096 | confusion_rate=0.0771, delta=0.0771, count=79 | run feature ranker for this class pair |
| ALERT | label_QCD->label_Hgg | 0.9452 | confusion_rate=0.0664, delta=0.0664, count=68 | run feature ranker for this class pair |
| ALERT | label_Hgg->label_Hcc | 0.9155 | confusion_rate=0.0645, delta=0.0645, count=66 | run feature ranker for this class pair |
| ALERT | label_Wqq->label_QCD | 0.8563 | confusion_rate=0.0605, delta=0.0605, count=62 | run feature ranker for this class pair |
| ALERT | label_Hgg->label_Hbb | 0.8268 | confusion_rate=0.0586, delta=0.0586, count=60 | run feature ranker for this class pair |
| ALERT | label_QCD->label_Wqq | 0.7094 | confusion_rate=0.0508, delta=0.0508, count=52 | run feature ranker for this class pair |
| ALERT | label_QCD->label_Zqq | 0.6803 | confusion_rate=0.0488, delta=0.0488, count=50 | run feature ranker for this class pair |
| ALERT | label_Zqq->label_QCD | 0.6803 | confusion_rate=0.0488, delta=0.0488, count=50 | run feature ranker for this class pair |
| ALERT | label_Hcc->label_Zqq | 0.6657 | confusion_rate=0.0479, delta=0.0479, count=49 | run feature ranker for this class pair |
| ALERT | label_Hbb->label_Zqq | 0.6077 | confusion_rate=0.0439, delta=0.0439, count=45 | run feature ranker for this class pair |
| ALERT | label_Tbl->label_Hqql | 0.5788 | confusion_rate=0.0420, delta=0.0420, count=43 | run feature ranker for this class pair |
| ALERT | label_QCD->label_Hcc | 0.4785 | confusion_rate=0.0352, delta=0.0352, count=36 | run feature ranker for this class pair |

## Top confusion pairs
| status | pair | count | rate | baseline | delta | conf | score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ALERT | label_Zqq->label_Wqq | 229 | 0.2236 | 0.0000 | 0.2236 | 0.6347 | 3.4525 |
| ALERT | label_Wqq->label_Zqq | 150 | 0.1465 | 0.0000 | 0.1465 | 0.5884 | 2.1998 |
| ALERT | label_Hbb->label_Hcc | 127 | 0.1240 | 0.0000 | 0.1240 | 0.5764 | 1.8420 |
| ALERT | label_Hcc->label_Hbb | 119 | 0.1162 | 0.0000 | 0.1162 | 0.6196 | 1.7185 |
| ALERT | label_Hgg->label_H4q | 110 | 0.1074 | 0.0000 | 0.1074 | 0.6259 | 1.5801 |
| ALERT | label_H4q->label_Hgg | 98 | 0.0957 | 0.0000 | 0.0957 | 0.5552 | 1.3968 |
| ALERT | label_Hbb->label_Hgg | 88 | 0.0859 | 0.0000 | 0.0859 | 0.5810 | 1.2451 |
| ALERT | label_Hcc->label_Hgg | 83 | 0.0811 | 0.0000 | 0.0811 | 0.5399 | 1.1697 |
| ALERT | label_Hcc->label_H4q | 79 | 0.0771 | 0.0000 | 0.0771 | 0.5772 | 1.1096 |
| ALERT | label_QCD->label_Hgg | 68 | 0.0664 | 0.0000 | 0.0664 | 0.5456 | 0.9452 |
| ALERT | label_Hgg->label_Hcc | 66 | 0.0645 | 0.0000 | 0.0645 | 0.5316 | 0.9155 |
| ALERT | label_Wqq->label_QCD | 62 | 0.0605 | 0.0000 | 0.0605 | 0.6126 | 0.8563 |
| ALERT | label_Hgg->label_Hbb | 60 | 0.0586 | 0.0000 | 0.0586 | 0.5388 | 0.8268 |
| ALERT | label_QCD->label_Wqq | 52 | 0.0508 | 0.0000 | 0.0508 | 0.5218 | 0.7094 |
| ALERT | label_QCD->label_Zqq | 50 | 0.0488 | 0.0000 | 0.0488 | 0.4944 | 0.6803 |
| ALERT | label_Zqq->label_QCD | 50 | 0.0488 | 0.0000 | 0.0488 | 0.5756 | 0.6803 |
| ALERT | label_Hcc->label_Zqq | 49 | 0.0479 | 0.0000 | 0.0479 | 0.5659 | 0.6657 |
| ALERT | label_Hbb->label_Zqq | 45 | 0.0439 | 0.0000 | 0.0439 | 0.5748 | 0.6077 |
| ALERT | label_Tbl->label_Hqql | 43 | 0.0420 | 0.0000 | 0.0420 | 0.7683 | 0.5788 |
| ALERT | label_QCD->label_Hcc | 36 | 0.0352 | 0.0000 | 0.0352 | 0.5420 | 0.4785 |
| ALERT | label_QCD->label_Tbqq | 36 | 0.0352 | 0.0000 | 0.0352 | 0.5678 | 0.4785 |
| ALERT | label_H4q->label_Hcc | 36 | 0.0352 | 0.0000 | 0.0352 | 0.5120 | 0.4785 |
| ALERT | label_Hqql->label_Tbl | 35 | 0.0342 | 0.0000 | 0.0342 | 0.7615 | 0.4643 |
| ALERT | label_Hcc->label_Tbqq | 33 | 0.0322 | 0.0000 | 0.0322 | 0.6401 | 0.4359 |
| ALERT | label_Hgg->label_QCD | 32 | 0.0312 | 0.0000 | 0.0312 | 0.5548 | 0.4218 |
| ALERT | label_Zqq->label_Hcc | 31 | 0.0303 | 0.0000 | 0.0303 | 0.5705 | 0.4077 |
| WATCH | label_Hbb->label_H4q | 30 | 0.0293 | 0.0000 | 0.0293 | 0.5759 | 0.3936 |
| WATCH | label_QCD->label_H4q | 29 | 0.0283 | 0.0000 | 0.0283 | 0.5636 | 0.3795 |
| WATCH | label_H4q->label_Tbqq | 27 | 0.0264 | 0.0000 | 0.0264 | 0.5757 | 0.3515 |
| WATCH | label_Zqq->label_Hbb | 27 | 0.0264 | 0.0000 | 0.0264 | 0.5810 | 0.3515 |

## Interpretation

WATCH/ALERT rows should be passed to the Feature Ranker. Deep probes should run only after a feature candidate passes contrastive/monotonic filters.
