# Research Stream Index v1

This is the first thing to read before deep logs. It converts evidence graphs into queryable stream events.

- Snapshots: **8**
- Stream events: **3468**
- Latest run index: **7**

## Main cards
| priority | title | value | drilldown |
| --- | --- | --- | --- |
| P0 | Stream state | 8 snapshots, 3468 events | manifests/latest/research_stream_index_v1.json |
| P0 | Top current all-head gate | L1_ch112:128 rank 1 gate_abs=0.8006 | python tools/query_research_stream_v1.py --event-type HEAD_GATE --top 10 |
| P0 | Top current particle evidence | event 978 particle 0 label_Hqql score=4.7626 | python tools/query_research_stream_v1.py --event-type PARTICLE_TOP --top 20 |
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
| 1 | L1_ch112:128 rank 1 gate_abs=0.8006 | 0.8006 | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? |
| 2 | L0_ch40:48 rank 2 gate_abs=0.6735 | 0.6735 | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? |
| 3 | L2_ch224:256 rank 3 gate_abs=0.6716 | 0.6716 | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? |
| 4 | L1_ch16:32 rank 4 gate_abs=0.6645 | 0.6645 | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? |
| 5 | L0_ch48:56 rank 5 gate_abs=0.3620 | 0.3620 | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? |
| 6 | L2_ch128:160 rank 6 gate_abs=0.3511 | 0.3511 | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? |
| 7 | L0_ch8:16 rank 7 gate_abs=0.3350 | 0.3350 | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? |
| 8 | L2_ch64:96 rank 8 gate_abs=0.2970 | 0.2970 | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? |
| 9 | L2_ch0:32 rank 9 gate_abs=0.2642 | 0.2642 | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? |
| 10 | L0_ch0:8 rank 10 gate_abs=0.2327 | 0.2327 | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? |

## Top current particles
| rank | title | score | summary | tags |
| --- | --- | --- | --- | --- |
| 1 | event 978 particle 0 label_Hqql score=4.7626 | 4.7626 | pt=379.5849 dR=0.0690 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 2 | event 888 particle 0 label_Hqql score=4.6690 | 4.6690 | pt=427.5177 dR=0.0538 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 3 | event 885 particle 0 label_Hqql score=4.6264 | 4.6264 | pt=426.3585 dR=0.0282 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 4 | event 1281 particle 0 label_Tbl score=4.5839 | 4.5839 | pt=498.7116 dR=0.1038 charge=1.0000 | particle,label_Tbl,particle_0,particle0,core_high_pt,charged |
| 5 | event 1455 particle 0 label_Tbl score=4.5528 | 4.5528 | pt=348.6307 dR=0.1924 charge=-1.0000 | particle,label_Tbl,particle_0,particle0,core_high_pt,charged |
| 6 | event 863 particle 0 label_Hqql score=4.5438 | 4.5438 | pt=380.1771 dR=0.0604 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 7 | event 953 particle 0 label_Hqql score=4.5358 | 4.5358 | pt=513.1412 dR=0.0628 charge=1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 8 | event 909 particle 0 label_Hqql score=4.5189 | 4.5189 | pt=776.4829 dR=0.0371 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 9 | event 797 particle 0 label_Hqql score=4.5062 | 4.5062 | pt=423.7215 dR=0.0287 charge=1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 10 | event 937 particle 0 label_Hqql score=4.5032 | 4.5032 | pt=471.4841 dR=0.0337 charge=1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 11 | event 921 particle 0 label_Hqql score=4.5005 | 4.5005 | pt=394.9027 dR=0.0040 charge=1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 12 | event 954 particle 0 label_Hqql score=4.4891 | 4.4891 | pt=435.9897 dR=0.0599 charge=1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 13 | event 905 particle 0 label_Hqql score=4.4872 | 4.4872 | pt=309.6795 dR=0.0841 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 14 | event 793 particle 0 label_Hqql score=4.4812 | 4.4812 | pt=372.7248 dR=0.0116 charge=1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 15 | event 892 particle 0 label_Hqql score=4.4811 | 4.4811 | pt=351.2416 dR=0.0689 charge=1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |

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
