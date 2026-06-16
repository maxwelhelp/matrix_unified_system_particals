# Research Stream Index v1

This is the first thing to read before deep logs. It converts evidence graphs into queryable stream events.

- Snapshots: **11**
- Stream events: **4871**
- Latest run index: **10**

## Main cards
| priority | title | value | drilldown |
| --- | --- | --- | --- |
| P0 | Stream state | 11 snapshots, 4871 events | manifests/latest/research_stream_index_v1.json |
| P0 | Top current all-head gate | L1_ch112:128 rank 1 gate_abs=0.8424 | python tools/query_research_stream_v1.py --event-type HEAD_GATE --top 10 |
| P0 | Top current particle evidence | event 1810 particle 0 label_Hqql score=5.0100 | python tools/query_research_stream_v1.py --event-type PARTICLE_TOP --top 20 |
| P0 | particle0/core dominance in top particle stream | run particle0 removal / top-k controls | reports/latest/tables/research_stream_alerts.csv |
| P1 | negative/suppressive head gates exist | compare positive vs negative gates; add suppressive-head analysis | reports/latest/tables/research_stream_alerts.csv |

## Alerts
| severity | title | score | next_action |
| --- | --- | --- | --- |
| HIGH | particle0/core dominance in top particle stream | 1.0000 | run particle0 removal / top-k controls |
| MEDIUM | negative/suppressive head gates exist | 5.0000 | compare positive vs negative gates; add suppressive-head analysis |

## Top current heads
| rank | title | score | summary |
| --- | --- | --- | --- |
| 1 | L1_ch112:128 rank 1 gate_abs=0.8424 | 0.8424 | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? |
| 2 | L1_ch16:32 rank 2 gate_abs=0.7223 | 0.7223 | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? |
| 3 | L0_ch40:48 rank 3 gate_abs=0.7015 | 0.7015 | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? |
| 4 | L2_ch224:256 rank 4 gate_abs=0.7009 | 0.7009 | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? |
| 5 | L0_ch48:56 rank 5 gate_abs=0.3678 | 0.3678 | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? |
| 6 | L0_ch8:16 rank 6 gate_abs=0.3511 | 0.3511 | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? |
| 7 | L2_ch128:160 rank 7 gate_abs=0.3357 | 0.3357 | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? |
| 8 | L2_ch64:96 rank 8 gate_abs=0.3033 | 0.3033 | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? |
| 9 | L2_ch0:32 rank 9 gate_abs=0.2646 | 0.2646 | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? |
| 10 | L0_ch0:8 rank 10 gate_abs=0.2323 | 0.2323 | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? |

## Top current particles
| rank | title | score | summary | tags |
| --- | --- | --- | --- | --- |
| 1 | event 1810 particle 0 label_Hqql score=5.0100 | 5.0100 | pt=288.1587 dR=0.0467 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 2 | event 1746 particle 0 label_Hqql score=4.9855 | 4.9855 | pt=379.5849 dR=0.0690 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 3 | event 1922 particle 0 label_Hqql score=4.9746 | 4.9746 | pt=493.3960 dR=0.0331 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 4 | event 1941 particle 0 label_Hqql score=4.9659 | 4.9659 | pt=596.0616 dR=0.0393 charge=1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 5 | event 1989 particle 0 label_Hqql score=4.9449 | 4.9449 | pt=437.4170 dR=0.0272 charge=1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 6 | event 1839 particle 0 label_Hqql score=4.9108 | 4.9108 | pt=444.0590 dR=0.0185 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 7 | event 1656 particle 0 label_Hqql score=4.8996 | 4.8996 | pt=427.5177 dR=0.0538 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 8 | event 1793 particle 0 label_Hqql score=4.8928 | 4.8928 | pt=557.3921 dR=0.0414 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 9 | event 1794 particle 0 label_Hqql score=4.8573 | 4.8573 | pt=441.8409 dR=0.0349 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 10 | event 1950 particle 0 label_Hqql score=4.8449 | 4.8449 | pt=377.5678 dR=0.0388 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 11 | event 1673 particle 0 label_Hqql score=4.8401 | 4.8401 | pt=309.6795 dR=0.0841 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 12 | event 1653 particle 0 label_Hqql score=4.8398 | 4.8398 | pt=426.3585 dR=0.0282 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 13 | event 1561 particle 0 label_Hqql score=4.8382 | 4.8382 | pt=372.7248 dR=0.0116 charge=1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 14 | event 2561 particle 0 label_Tbl score=4.7971 | 4.7971 | pt=498.7116 dR=0.1038 charge=1.0000 | particle,label_Tbl,particle_0,particle0,core_high_pt,charged |
| 15 | event 1734 particle 0 label_Hqql score=4.7918 | 4.7918 | pt=526.2284 dR=0.0404 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |

## Next actions
- Run particle0/top-k controls and rebuild stream index.
- Run class-specific all-head gradients for Hqql/Tbl/Tbqq/Wqq/Zqq.
- Run route-neighbor trace for top all-head particles.
- Create more distinct snapshots with HISTORY_COPY=1 for real dynamics.
- Move large stream history to SQLite/DuckDB when Git files get too large.

## Drilldown examples

```bash
python tools/query_research_stream_v1.py --query particle0 --top 20
python tools/query_research_stream_v1.py --head L1_ch112:128
python tools/query_research_stream_v1.py --class-label label_Hqql
python tools/query_research_stream_v1.py --hypothesis AH1
python tools/query_research_stream_v1.py --event-type HEAD_GATE --top 20
```
