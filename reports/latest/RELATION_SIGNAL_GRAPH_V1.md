# Relation Signal Graph v1

Automatic relationship mining over the stream/evidence graph. Signals are prioritization, not causal proof.

- Latest run index: **9**
- Nodes: **47**
- Edges: **89**

## Top relation signals
| signal | support | src | relation | dst | strength | lift | confidence | next_control |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.9338 | 161 | pattern:core_high_pt | pattern_supports_hypothesis | hypothesis:AH1 | 0.1168 | 1.8634 | MEDIUM | remove particle0 / keep only particle0 / top-k controls |
| 0.8789 | 120 | pattern:particle0 | pattern_supports_hypothesis | hypothesis:AH1 | 0.1758 | 1.2500 | MEDIUM | remove particle0 / keep only particle0 / top-k controls |
| 0.8085 | 62 | pattern:particle0 | particle_pattern_associated_with_class | class:label_Hqql | 0.0699 | 1.0403 | MEDIUM | particle0/top-k/random controls |
| 0.8002 | 87 | pattern:core_high_pt | particle_pattern_associated_with_class | class:label_Hqql | 0.0449 | 1.0880 | MEDIUM | particle0/top-k/random controls |
| 0.7924 | 87 | pattern:charged | particle_pattern_associated_with_class | class:label_Hqql | 0.0447 | 1.0244 | MEDIUM | route-neighbor trace and heldout stability |
| 0.7773 | 49 | pattern:particle0 | particle_pattern_associated_with_class | class:label_Tbl | 0.0866 | 0.9879 | MEDIUM | particle0/top-k/random controls |
| 0.7629 | 69 | pattern:charged | particle_pattern_associated_with_class | class:label_Tbl | 0.0553 | 0.9762 | MEDIUM | route-neighbor trace and heldout stability |
| 0.7608 | 59 | pattern:core_high_pt | particle_pattern_associated_with_class | class:label_Tbl | 0.0681 | 0.8866 | MEDIUM | particle0/top-k/random controls |
| 0.6788 | 42 | pattern:wide | pattern_supports_hypothesis | hypothesis:T6_WIDE_SECONDARY_CONTEXT | 0.2620 | 1.3825 | HIGH | route-neighbor trace |
| 0.6304 | 24 | pattern:wide | particle_pattern_associated_with_class | class:label_Tbl | 0.1148 | 1.3825 | HIGH | route-neighbor trace and heldout stability |
| 0.6244 | 38 | pattern:other_particle | particle_pattern_associated_with_class | class:label_Hqql | 0.0715 | 1.0201 | MEDIUM | route-neighbor trace and heldout stability |
| 0.6242 | 33 | pattern:other_particle | particle_pattern_associated_with_class | class:label_Tbl | 0.0843 | 1.0645 | MEDIUM | route-neighbor trace and heldout stability |
| 0.6199 | 4 | pattern:core_high_pt | particle_pattern_associated_with_class | class:label_QCD | 0.8653 | 1.8634 | LOW | particle0/top-k/random controls |
| 0.6041 | 8 | pattern:core_high_pt | particle_pattern_associated_with_class | class:label_Wqq | 0.4695 | 0.9938 | MEDIUM | particle0/top-k/random controls |
| 0.5953 | 5 | pattern:particle0 | particle_pattern_associated_with_class | class:label_Wqq | 0.8359 | 0.8333 | MEDIUM | particle0/top-k/random controls |
| 0.5840 | 2 | pattern:particle0 | particle_pattern_associated_with_class | class:label_QCD | 2.0870 | 1.2500 | LOW | particle0/top-k/random controls |
| 0.5446 | 8 | pattern:charged | particle_pattern_associated_with_class | class:label_Wqq | 0.3950 | 0.9357 | MEDIUM | route-neighbor trace and heldout stability |
| 0.5387 | 5 | pattern:charged | particle_pattern_associated_with_class | class:label_Zqq | 0.6515 | 1.0965 | MEDIUM | route-neighbor trace and heldout stability |
| 0.5317 | 15 | pattern:wide | particle_pattern_associated_with_class | class:label_Hqql | 0.1848 | 0.7191 | MEDIUM | route-neighbor trace and heldout stability |
| 0.5204 | 2 | pattern:particle0 | particle_pattern_associated_with_class | class:label_Zqq | 2.0809 | 0.6250 | LOW | particle0/top-k/random controls |
| 0.5050 | 3 | pattern:core_high_pt | particle_pattern_associated_with_class | class:label_Zqq | 1.2222 | 0.6988 | LOW | particle0/top-k/random controls |
| 0.5009 | 3 | pattern:other_particle | particle_pattern_associated_with_class | class:label_Zqq | 0.9103 | 1.5000 | LOW | route-neighbor trace and heldout stability |
| 0.4339 | 2 | pattern:wide | particle_pattern_associated_with_class | class:label_Wqq | 1.4186 | 0.9524 | LOW | route-neighbor trace and heldout stability |
| 0.4184 | 2 | pattern:charged | particle_pattern_associated_with_class | class:label_QCD | 1.3744 | 0.8772 | LOW | route-neighbor trace and heldout stability |
| 0.3793 | 1 | pattern:wide | particle_pattern_associated_with_class | class:label_Zqq | 2.6378 | 0.8929 | LOW | route-neighbor trace and heldout stability |

## Alerts / controls
| severity | relation | score | next_control | reason |
| --- | --- | --- | --- | --- |
| HIGH | task:T1_PARTICLE0_SHORTCUT_OR_CORE_ANCHOR->hypothesis:AH1 | 1.0000 | Run particle0 removal / keep-only particle0 / top-k removal / same-count random controls. | Is the all-head system over-dominated by particle0 / leading-core evidence? |
| MEDIUM | task:T3_NEGATIVE_SUPPRESSIVE_GATES->hypothesis:NEGATIVE_GATES | 1.0000 | Add suppressive-head analysis and class-specific negative gate gradients. | Are there heads that suppress the current class logit? |
| MEDIUM | task:T5_PATCH_VS_GRADIENT_DIVERGENCE->hypothesis:AH3 | 1.0000 | Build patch-rank vs gate-rank report and run multi-head patch combinations. | Which heads are patch-important but not gradient-important, or gradient-important but not patch-important? |
| HIGH | task:T4_HQQL_TBL_SIGNATURE->hypothesis:AH2 | 0.9750 | Run class-specific all-head gradients: Hqql, Tbl, Tbqq, Wqq, Zqq. | Is the current stream dominated by Hqql/Tbl high-confidence events? |
| HIGH | task:T2_HEAD_RANK_STABILITY->hypothesis:AH4 | 0.9511 | Keep tracking; if unstable, split by class/sample size and run heldout stability. | Do the same heads stay important across snapshots? |
| HIGH | pattern:wide->hypothesis:T6_WIDE_SECONDARY_CONTEXT | 0.6788 | route-neighbor trace | needs KNN neighbor and causal route controls |
| HIGH | pattern:wide->class:label_Tbl | 0.6304 | route-neighbor trace and heldout stability | co-occurrence only; can reflect sorting or class imbalance |
| HIGH | task:T1_PARTICLE0_SHORTCUT_OR_CORE_ANCHOR->hypothesis:AH1 | 0.2426 | Run particle0 removal / keep-only particle0 / top-k removal / same-count random controls. | task score is deterministic weak signal |
| HIGH | task:T3_NEGATIVE_SUPPRESSIVE_GATES->hypothesis:NEGATIVE_GATES | 0.2426 | Add suppressive-head analysis and class-specific negative gate gradients. | task score is deterministic weak signal |
| HIGH | task:T5_PATCH_VS_GRADIENT_DIVERGENCE->hypothesis:AH3 | 0.2426 | Build patch-rank vs gate-rank report and run multi-head patch combinations. | task score is deterministic weak signal |
| HIGH | task:T4_HQQL_TBL_SIGNATURE->hypothesis:AH2 | 0.2403 | Run class-specific all-head gradients: Hqql, Tbl, Tbqq, Wqq, Zqq. | task score is deterministic weak signal |

## Interpretation

- Strong particle0/core relations are currently candidates, not proof. They require particle0/top-k controls.
- Head relations are mostly gradient/support relations until class-specific gradients and causal patches are added.
- Wide/secondary relations need route-neighbor trace.

## Files

- JSON: `manifests/latest/relation_signal_graph_v1.json`
- Edges: `reports/latest/tables/relation_signal_edges.csv`
- Nodes: `reports/latest/tables/relation_signal_nodes.csv`
- Alerts: `reports/latest/tables/relation_signal_alerts.csv`
