# Research Stream Index v1

This is the first thing to read before deep logs. It converts evidence graphs into queryable stream events.

- Snapshots: **4**
- Stream events: **1724**
- Latest run index: **3**

## Main cards
| priority | title | value | drilldown |
| --- | --- | --- | --- |
| P0 | Stream state | 4 snapshots, 1724 events | manifests/latest/research_stream_index_v1.json |
| P0 | Top current all-head gate | L1_ch112:128 rank 1 gate_abs=0.8644 | python tools/query_research_stream_v1.py --event-type HEAD_GATE --top 10 |
| P0 | Top current particle evidence | event 321 particle 0 label_Tbl score=5.0656 | python tools/query_research_stream_v1.py --event-type PARTICLE_TOP --top 20 |
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
| 1 | L1_ch112:128 rank 1 gate_abs=0.8644 | 0.8644 | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? |
| 2 | L2_ch224:256 rank 2 gate_abs=0.7841 | 0.7841 | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? |
| 3 | L1_ch16:32 rank 3 gate_abs=0.7805 | 0.7805 | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? |
| 4 | L0_ch40:48 rank 4 gate_abs=0.7150 | 0.7150 | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? |
| 5 | L0_ch8:16 rank 5 gate_abs=0.4293 | 0.4293 | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? |
| 6 | L0_ch48:56 rank 6 gate_abs=0.3819 | 0.3819 | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? |
| 7 | L2_ch64:96 rank 7 gate_abs=0.3301 | 0.3301 | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? |
| 8 | L2_ch128:160 rank 8 gate_abs=0.3290 | 0.3290 | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? |
| 9 | L2_ch0:32 rank 9 gate_abs=0.2666 | 0.2666 | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? |
| 10 | L0_ch0:8 rank 10 gate_abs=0.2581 | 0.2581 | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? |

## Top current particles
| rank | title | score | summary | tags |
| --- | --- | --- | --- | --- |
| 1 | event 321 particle 0 label_Tbl score=5.0656 | 5.0656 | pt=498.7116 dR=0.1038 charge=1.0000 | particle,label_Tbl,particle_0,particle0,core_high_pt,charged |
| 2 | event 221 particle 0 label_Hqql score=4.9950 | 4.9950 | pt=423.7215 dR=0.0287 charge=1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 3 | event 217 particle 0 label_Hqql score=4.9811 | 4.9811 | pt=372.7248 dR=0.0116 charge=1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 4 | event 219 particle 0 label_Hqql score=4.9777 | 4.9777 | pt=378.6483 dR=0.0171 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 5 | event 208 particle 0 label_Hqql score=4.9504 | 4.9504 | pt=526.1700 dR=0.0220 charge=1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 6 | event 198 particle 0 label_Hqql score=4.9108 | 4.9108 | pt=445.1894 dR=0.0349 charge=1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 7 | event 331 particle 0 label_Tbl score=4.9094 | 4.9094 | pt=564.8672 dR=0.1102 charge=-1.0000 | particle,label_Tbl,particle_0,particle0,core_high_pt,charged |
| 8 | event 364 particle 0 label_Tbl score=4.8889 | 4.8889 | pt=422.0057 dR=0.1213 charge=-1.0000 | particle,label_Tbl,particle_0,particle0,core_high_pt,charged |
| 9 | event 242 particle 0 label_Hqql score=4.8622 | 4.8622 | pt=468.0427 dR=0.0323 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 10 | event 233 particle 0 label_Hqql score=4.8617 | 4.8617 | pt=345.6596 dR=0.0425 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 11 | event 214 particle 0 label_Hqql score=4.8590 | 4.8590 | pt=524.3685 dR=0.0461 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 12 | event 234 particle 0 label_Hqql score=4.8586 | 4.8586 | pt=382.8791 dR=0.0572 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 13 | event 213 particle 0 label_Hqql score=4.8546 | 4.8546 | pt=326.9661 dR=0.0638 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 14 | event 334 particle 0 label_Tbl score=4.7818 | 4.7818 | pt=482.8271 dR=0.1353 charge=1.0000 | particle,label_Tbl,particle_0,particle0,core_high_pt,charged |
| 15 | event 244 particle 0 label_Hqql score=4.7671 | 4.7671 | pt=467.6960 dR=0.0313 charge=1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |

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
