# Relation Signal Graph v1

Automatic relationship mining over the stream/evidence graph. Signals are prioritization, not causal proof.

- Latest run index: **8**
- Nodes: **46**
- Edges: **83**

## Top relation signals
| signal | support | src | relation | dst | strength | lift | confidence | next_control |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.9494 | 115 | pattern:core_high_pt | pattern_supports_hypothesis | hypothesis:AH1 | 0.1355 | 2.6087 | MEDIUM | remove particle0 / keep only particle0 / top-k controls |
| 0.9282 | 80 | pattern:particle0 | pattern_supports_hypothesis | hypothesis:AH1 | 0.2158 | 3.7500 | MEDIUM | remove particle0 / keep only particle0 / top-k controls |
| 0.7939 | 50 | pattern:particle0 | particle_pattern_associated_with_class | class:label_Hqql | 0.0878 | 1.0081 | MEDIUM | particle0/top-k/random controls |
| 0.7817 | 76 | pattern:core_high_pt | particle_pattern_associated_with_class | class:label_Hqql | 0.0505 | 1.0659 | MEDIUM | particle0/top-k/random controls |
| 0.7676 | 100 | pattern:charged | particle_pattern_associated_with_class | class:label_Hqql | 0.0351 | 1.0144 | MEDIUM | route-neighbor trace and heldout stability |
| 0.7423 | 28 | pattern:particle0 | particle_pattern_associated_with_class | class:label_Tbl | 0.1543 | 0.9813 | MEDIUM | particle0/top-k/random controls |
| 0.7190 | 36 | pattern:core_high_pt | particle_pattern_associated_with_class | class:label_Tbl | 0.1103 | 0.8777 | MEDIUM | particle0/top-k/random controls |
| 0.7155 | 55 | pattern:charged | particle_pattern_associated_with_class | class:label_Tbl | 0.0633 | 0.9698 | MEDIUM | route-neighbor trace and heldout stability |
| 0.6967 | 46 | pattern:wide | pattern_supports_hypothesis | hypothesis:T6_WIDE_SECONDARY_CONTEXT | 0.1729 | 1.6457 | HIGH | route-neighbor trace |
| 0.6574 | 27 | pattern:wide | particle_pattern_associated_with_class | class:label_Tbl | 0.0988 | 1.6457 | HIGH | route-neighbor trace and heldout stability |
| 0.6569 | 62 | pattern:other_particle | particle_pattern_associated_with_class | class:label_Hqql | 0.0425 | 1.0526 | MEDIUM | route-neighbor trace and heldout stability |
| 0.6414 | 1 | pattern:particle0 | particle_pattern_associated_with_class | class:label_Wqq | 4.3206 | 3.7500 | LOW | particle0/top-k/random controls |
| 0.6414 | 1 | pattern:core_high_pt | particle_pattern_associated_with_class | class:label_Wqq | 4.3206 | 2.6087 | LOW | particle0/top-k/random controls |
| 0.5882 | 31 | pattern:other_particle | particle_pattern_associated_with_class | class:label_Tbl | 0.0838 | 0.9149 | MEDIUM | route-neighbor trace and heldout stability |
| 0.5247 | 18 | pattern:wide | particle_pattern_associated_with_class | class:label_Hqql | 0.1471 | 0.6311 | MEDIUM | route-neighbor trace and heldout stability |
| 0.5197 | 4 | pattern:charged | particle_pattern_associated_with_class | class:label_Zqq | 0.7553 | 1.2579 | LOW | route-neighbor trace and heldout stability |
| 0.4961 | 1 | pattern:particle0 | particle_pattern_associated_with_class | class:label_Zqq | 4.2334 | 0.6250 | LOW | particle0/top-k/random controls |
| 0.4812 | 2 | pattern:core_high_pt | particle_pattern_associated_with_class | class:label_Zqq | 1.7274 | 0.8696 | LOW | particle0/top-k/random controls |
| 0.4333 | 2 | pattern:other_particle | particle_pattern_associated_with_class | class:label_Zqq | 1.3594 | 1.0526 | LOW | route-neighbor trace and heldout stability |
| 0.3987 | 1 | pattern:wide | particle_pattern_associated_with_class | class:label_Zqq | 2.6378 | 1.0870 | LOW | route-neighbor trace and heldout stability |
| 0.2426 | 1 | task:T1_PARTICLE0_SHORTCUT_OR_CORE_ANCHOR | task_monitors_hypothesis | hypothesis:AH1 | 1.0000 | 1.0000 | HIGH | Run particle0 removal / keep-only particle0 / top-k removal / same-count random controls. |
| 0.2426 | 1 | task:T3_NEGATIVE_SUPPRESSIVE_GATES | task_monitors_hypothesis | hypothesis:NEGATIVE_GATES | 1.0000 | 1.0000 | HIGH | Add suppressive-head analysis and class-specific negative gate gradients. |
| 0.2426 | 1 | task:T5_PATCH_VS_GRADIENT_DIVERGENCE | task_monitors_hypothesis | hypothesis:AH3 | 1.0000 | 1.0000 | HIGH | Build patch-rank vs gate-rank report and run multi-head patch combinations. |
| 0.2403 | 1 | task:T4_HQQL_TBL_SIGNATURE | task_monitors_hypothesis | hypothesis:AH2 | 0.9750 | 1.0000 | HIGH | Run class-specific all-head gradients: Hqql, Tbl, Tbqq, Wqq, Zqq. |
| 0.2376 | 1 | task:T2_HEAD_RANK_STABILITY | task_monitors_hypothesis | hypothesis:AH4 | 0.9450 | 1.0000 | HIGH | Keep tracking; if unstable, split by class/sample size and run heldout stability. |

## Alerts / controls
| severity | relation | score | next_control | reason |
| --- | --- | --- | --- | --- |
| HIGH | task:T1_PARTICLE0_SHORTCUT_OR_CORE_ANCHOR->hypothesis:AH1 | 1.0000 | Run particle0 removal / keep-only particle0 / top-k removal / same-count random controls. | Is the all-head system over-dominated by particle0 / leading-core evidence? |
| MEDIUM | task:T3_NEGATIVE_SUPPRESSIVE_GATES->hypothesis:NEGATIVE_GATES | 1.0000 | Add suppressive-head analysis and class-specific negative gate gradients. | Are there heads that suppress the current class logit? |
| MEDIUM | task:T5_PATCH_VS_GRADIENT_DIVERGENCE->hypothesis:AH3 | 1.0000 | Build patch-rank vs gate-rank report and run multi-head patch combinations. | Which heads are patch-important but not gradient-important, or gradient-important but not patch-important? |
| HIGH | task:T4_HQQL_TBL_SIGNATURE->hypothesis:AH2 | 0.9750 | Run class-specific all-head gradients: Hqql, Tbl, Tbqq, Wqq, Zqq. | Is the current stream dominated by Hqql/Tbl high-confidence events? |
| HIGH | task:T2_HEAD_RANK_STABILITY->hypothesis:AH4 | 0.9450 | Keep tracking; if unstable, split by class/sample size and run heldout stability. | Do the same heads stay important across snapshots? |
| HIGH | pattern:wide->hypothesis:T6_WIDE_SECONDARY_CONTEXT | 0.6967 | route-neighbor trace | needs KNN neighbor and causal route controls |
| HIGH | pattern:wide->class:label_Tbl | 0.6574 | route-neighbor trace and heldout stability | co-occurrence only; can reflect sorting or class imbalance |
| HIGH | task:T1_PARTICLE0_SHORTCUT_OR_CORE_ANCHOR->hypothesis:AH1 | 0.2426 | Run particle0 removal / keep-only particle0 / top-k removal / same-count random controls. | task score is deterministic weak signal |
| HIGH | task:T3_NEGATIVE_SUPPRESSIVE_GATES->hypothesis:NEGATIVE_GATES | 0.2426 | Add suppressive-head analysis and class-specific negative gate gradients. | task score is deterministic weak signal |
| HIGH | task:T5_PATCH_VS_GRADIENT_DIVERGENCE->hypothesis:AH3 | 0.2426 | Build patch-rank vs gate-rank report and run multi-head patch combinations. | task score is deterministic weak signal |
| HIGH | task:T4_HQQL_TBL_SIGNATURE->hypothesis:AH2 | 0.2403 | Run class-specific all-head gradients: Hqql, Tbl, Tbqq, Wqq, Zqq. | task score is deterministic weak signal |
| HIGH | task:T2_HEAD_RANK_STABILITY->hypothesis:AH4 | 0.2376 | Keep tracking; if unstable, split by class/sample size and run heldout stability. | task score is deterministic weak signal |

## Interpretation

- Strong particle0/core relations are currently candidates, not proof. They require particle0/top-k controls.
- Head relations are mostly gradient/support relations until class-specific gradients and causal patches are added.
- Wide/secondary relations need route-neighbor trace.

## Files

- JSON: `manifests/latest/relation_signal_graph_v1.json`
- Edges: `reports/latest/tables/relation_signal_edges.csv`
- Nodes: `reports/latest/tables/relation_signal_nodes.csv`
- Alerts: `reports/latest/tables/relation_signal_alerts.csv`
