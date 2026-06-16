# Relation Signal Graph v1

Automatic relationship mining over the stream/evidence graph. Signals are prioritization, not causal proof.

- Latest run index: **10**
- Nodes: **48**
- Edges: **89**

## Top relation signals
| signal | support | src | relation | dst | strength | lift | confidence | next_control |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.0000 | 153 | pattern:core_high_pt | pattern_supports_hypothesis | hypothesis:AH1 | 0.1738 | 1.9608 | MEDIUM | remove particle0 / keep only particle0 / top-k controls |
| 0.9869 | 120 | pattern:particle0 | pattern_supports_hypothesis | hypothesis:AH1 | 0.2295 | 2.5000 | HIGH | remove particle0 / keep only particle0 / top-k controls |
| 0.8581 | 84 | pattern:particle0 | particle_pattern_associated_with_class | class:label_Hqql | 0.0554 | 1.0244 | MEDIUM | particle0/top-k/random controls |
| 0.8492 | 113 | pattern:core_high_pt | particle_pattern_associated_with_class | class:label_Hqql | 0.0376 | 1.0808 | MEDIUM | particle0/top-k/random controls |
| 0.8390 | 126 | pattern:charged | particle_pattern_associated_with_class | class:label_Hqql | 0.0324 | 1.0418 | MEDIUM | route-neighbor trace and heldout stability |
| 0.7974 | 31 | pattern:particle0 | particle_pattern_associated_with_class | class:label_Tbl | 0.1475 | 1.2302 | HIGH | particle0/top-k/random controls |
| 0.7739 | 34 | pattern:core_high_pt | particle_pattern_associated_with_class | class:label_Tbl | 0.1302 | 1.0582 | MEDIUM | particle0/top-k/random controls |
| 0.7660 | 40 | pattern:charged | particle_pattern_associated_with_class | class:label_Tbl | 0.1047 | 1.0761 | MEDIUM | route-neighbor trace and heldout stability |
| 0.7261 | 30 | pattern:wide | pattern_supports_hypothesis | hypothesis:T6_WIDE_SECONDARY_CONTEXT | 0.2879 | 2.5000 | MEDIUM | route-neighbor trace |
| 0.6643 | 13 | pattern:wide | particle_pattern_associated_with_class | class:label_Tbl | 0.2258 | 2.0635 | MEDIUM | route-neighbor trace and heldout stability |
| 0.6629 | 1 | pattern:particle0 | particle_pattern_associated_with_class | class:label_Wqq | 4.5594 | 2.5000 | LOW | particle0/top-k/random controls |
| 0.6590 | 1 | pattern:core_high_pt | particle_pattern_associated_with_class | class:label_Wqq | 4.5594 | 1.9608 | LOW | particle0/top-k/random controls |
| 0.6548 | 52 | pattern:other_particle | particle_pattern_associated_with_class | class:label_Hqql | 0.0552 | 0.9512 | MEDIUM | route-neighbor trace and heldout stability |
| 0.6159 | 7 | pattern:other_particle | particle_pattern_associated_with_class | class:label_QCD | 0.4098 | 2.3864 | MEDIUM | route-neighbor trace and heldout stability |
| 0.6141 | 2 | pattern:particle0 | particle_pattern_associated_with_class | class:label_Zqq | 2.2542 | 1.2500 | LOW | particle0/top-k/random controls |
| 0.5871 | 2 | pattern:core_high_pt | particle_pattern_associated_with_class | class:label_Zqq | 2.2542 | 0.9804 | LOW | particle0/top-k/random controls |
| 0.5848 | 7 | pattern:other_particle | particle_pattern_associated_with_class | class:label_Hgg | 0.4175 | 1.6406 | MEDIUM | route-neighbor trace and heldout stability |
| 0.5586 | 16 | pattern:wide | particle_pattern_associated_with_class | class:label_Hqql | 0.1845 | 0.7805 | MEDIUM | route-neighbor trace and heldout stability |
| 0.5338 | 13 | pattern:other_particle | particle_pattern_associated_with_class | class:label_Tbl | 0.2191 | 0.7738 | MEDIUM | route-neighbor trace and heldout stability |
| 0.5174 | 8 | pattern:charged | particle_pattern_associated_with_class | class:label_Hgg | 0.3694 | 0.8475 | MEDIUM | route-neighbor trace and heldout stability |
| 0.4999 | 1 | pattern:wide | particle_pattern_associated_with_class | class:label_Zqq | 2.7486 | 2.5000 | LOW | route-neighbor trace and heldout stability |
| 0.4985 | 1 | pattern:particle0 | particle_pattern_associated_with_class | class:label_QCD | 4.7018 | 0.2273 | LOW | particle0/top-k/random controls |
| 0.4936 | 1 | pattern:core_high_pt | particle_pattern_associated_with_class | class:label_QCD | 4.7018 | 0.1783 | LOW | particle0/top-k/random controls |
| 0.4809 | 2 | pattern:core_high_pt | particle_pattern_associated_with_class | class:label_Hgg | 2.0729 | 0.2451 | LOW | particle0/top-k/random controls |
| 0.4771 | 1 | pattern:particle0 | particle_pattern_associated_with_class | class:label_Hgg | 4.5432 | 0.1562 | LOW | particle0/top-k/random controls |

## Alerts / controls
| severity | relation | score | next_control | reason |
| --- | --- | --- | --- | --- |
| HIGH | task:T1_PARTICLE0_SHORTCUT_OR_CORE_ANCHOR->hypothesis:AH1 | 1.0000 | Run particle0 removal / keep-only particle0 / top-k removal / same-count random controls. | Is the all-head system over-dominated by particle0 / leading-core evidence? |
| MEDIUM | task:T3_NEGATIVE_SUPPRESSIVE_GATES->hypothesis:NEGATIVE_GATES | 1.0000 | Add suppressive-head analysis and class-specific negative gate gradients. | Are there heads that suppress the current class logit? |
| MEDIUM | task:T5_PATCH_VS_GRADIENT_DIVERGENCE->hypothesis:AH3 | 1.0000 | Build patch-rank vs gate-rank report and run multi-head patch combinations. | Which heads are patch-important but not gradient-important, or gradient-important but not patch-important? |
| HIGH | pattern:particle0->hypothesis:AH1 | 0.9869 | remove particle0 / keep only particle0 / top-k controls | may be leading-particle shortcut |
| HIGH | task:T4_HQQL_TBL_SIGNATURE->hypothesis:AH2 | 0.9750 | Run class-specific all-head gradients: Hqql, Tbl, Tbqq, Wqq, Zqq. | Is the current stream dominated by Hqql/Tbl high-confidence events? |
| HIGH | task:T2_HEAD_RANK_STABILITY->hypothesis:AH4 | 0.9400 | Keep tracking; if unstable, split by class/sample size and run heldout stability. | Do the same heads stay important across snapshots? |
| HIGH | pattern:particle0->class:label_Tbl | 0.7974 | particle0/top-k/random controls | co-occurrence only; can reflect sorting or class imbalance |
| HIGH | task:T1_PARTICLE0_SHORTCUT_OR_CORE_ANCHOR->hypothesis:AH1 | 0.2426 | Run particle0 removal / keep-only particle0 / top-k removal / same-count random controls. | task score is deterministic weak signal |
| HIGH | task:T3_NEGATIVE_SUPPRESSIVE_GATES->hypothesis:NEGATIVE_GATES | 0.2426 | Add suppressive-head analysis and class-specific negative gate gradients. | task score is deterministic weak signal |
| HIGH | task:T5_PATCH_VS_GRADIENT_DIVERGENCE->hypothesis:AH3 | 0.2426 | Build patch-rank vs gate-rank report and run multi-head patch combinations. | task score is deterministic weak signal |

## Interpretation

- Strong particle0/core relations are currently candidates, not proof. They require particle0/top-k controls.
- Head relations are mostly gradient/support relations until class-specific gradients and causal patches are added.
- Wide/secondary relations need route-neighbor trace.

## Files

- JSON: `manifests/latest/relation_signal_graph_v1.json`
- Edges: `reports/latest/tables/relation_signal_edges.csv`
- Nodes: `reports/latest/tables/relation_signal_nodes.csv`
- Alerts: `reports/latest/tables/relation_signal_alerts.csv`
