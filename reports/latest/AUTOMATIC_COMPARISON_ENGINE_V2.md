# Automatic Comparison Engine v2

v2 adds big-stream and discovery-readiness comparisons on top of v1. This report was postprocessed after particle0/top-k controls v2.

## P0 comparisons
| status | comparison | claim | missing | next |
| --- | --- | --- | --- | --- |
| MISSING_RESIDUAL_TEST | C10_KNOWN_OBSERVABLE_RESIDUAL | discovery-relevant signals must survive known-observable baselines | known-observable residual analysis | fit known observables then test whether head/particle signals explain residual errors or logits |
| NEEDS_HELDOUT | C13_PER_FILE_HELDOUT_STABILITY | relations should survive different ROOT files and tar parts | per-file/per-tar-part stability report | run stream over more ROOT files and compare head/rule signals per file and per class |
| ORDER_CONTROL_PARTIAL | C14_ORDERING_VS_PHYSICAL_COORDINATE | particle0 dominance must be separated from particle ordering/sorting |  | run particle order shuffle and compare index-based vs pt/deltaR-based signals |
| METHOD_DEBUG_NOT_DISCOVERY_READY | C15_DISCOVERY_READINESS_SCORE | a hypothesis is discovery-relevant only after controls, heldout, residual, and cross-model tests | C10_KNOWN_OBSERVABLE_RESIDUAL, C13_PER_FILE_HELDOUT_STABILITY, C2_WIDE_PATTERN_VS_ROUTE_TRACE, C5_CLASS_SIGNATURE_VS_CLASS_SPECIFIC_GRADIENT, C8_CLASS_CONCENTRATION_VS_IMBALANCE | complete P0 controls before claiming physics/discovery relevance |
| RUN_SAMPLED_LARGE_STREAM_BUT_PRIORITIZE_CONTROLS | C16_BIG_STREAM_READINESS | large stream should run with summaries and known P0 controls tracked | run sampled large stream plus immediately run controls | run staged large stream: 64 smoke -> 256 -> 512/1024, then particle0/top-k controls |
| SUPPORTED_BY_TARGETED_CONTROL_BUT_NEEDS_ORDER_RESIDUAL_TEST | C1_STREAM_RELATION_VS_MISSING_CONTROL | particle0/core_high_pt relation supports AH1 core-anchor hypothesis | order/residual/class-specific controls | run particle order shuffle, known-observable residual, and class-specific all-head gradients |
| NEEDS_ROUTE_TRACE | C2_WIDE_PATTERN_VS_ROUTE_TRACE | wide particle pattern may be secondary context rather than noise | route-neighbor trace / causal route controls | run route-neighbor trace for top all-head particles and wide non-particle0 particles |
| NEEDS_CLASS_SPECIFIC_TEST | C5_CLASS_SIGNATURE_VS_CLASS_SPECIFIC_GRADIENT | Hqql/Tbl signature is strong in stream but global gradients are not class-specific | class-specific all-head gradients | run class-specific all-head gradients for Hqql/Tbl/Tbqq/Wqq/Zqq |
| SCALING_PARTIAL | C7_SAMPLE_SIZE_SCALING | signals must scale from small snapshots to larger streams |  | run stream cycles at SAMPLES_PER_FILE=64,256,512,1024 with HISTORY_COPY=1 and compare ranks/signals |
| NEEDS_CLASS_DISTRIBUTION_CHECK | C8_CLASS_CONCENTRATION_VS_IMBALANCE | Hqql/Tbl dominance may be real class signature or sampling bias | balanced-vs-natural stream comparison | run one balanced stream and one natural/random-file stream, compare class signatures |

## All comparisons
| priority | status | comparison | support | risk |
| --- | --- | --- | --- | --- |
| P0 | MISSING_RESIDUAL_TEST | C10_KNOWN_OBSERVABLE_RESIDUAL | current signals use particles/heads but not residual after mass/tau/nparticles/pt | particle0/core may be explained by pt/mass/nparticles/tau variables |
| P0 | NEEDS_HELDOUT | C13_PER_FILE_HELDOUT_STABILITY | snapshots=15 but no per-file heldout breakdown | same extracted tiny files can fake stable patterns |
| P0 | ORDER_CONTROL_PARTIAL | C14_ORDERING_VS_PHYSICAL_COORDINATE | particle0_edge_signal=0.9288178736074759 support=120 | particle index can encode sorting by pt, not a physical interaction |
| P0 | METHOD_DEBUG_NOT_DISCOVERY_READY | C15_DISCOVERY_READINESS_SCORE | p0_missing_count=5 readiness=method_debug | correlation-only relation is not a discovery claim |
| P0 | RUN_SAMPLED_LARGE_STREAM_BUT_PRIORITIZE_CONTROLS | C16_BIG_STREAM_READINESS | current_snapshots=15 stream_events=6795 | big data can make wrong shortcut look very confident |
| P0 | SUPPORTED_BY_TARGETED_CONTROL_BUT_NEEDS_ORDER_RESIDUAL_TEST | C1_STREAM_RELATION_VS_MISSING_CONTROL | particle0 control available: remove_particle0_acc_drop=0.1941, random_remove1_acc_drop_mean=0.0146, ratio=13.3125, keep_only_particle0_acc=0.2027 | particle0 is causally important, but may still be sorting/leading-pT or known-observable proxy |
| P0 | NEEDS_ROUTE_TRACE | C2_WIDE_PATTERN_VS_ROUTE_TRACE | relation_signal=0.7525254963492034 support=20 dst=hypothesis:T6_WIDE_SECONDARY_CONTEXT | wide relation can be class imbalance, loose fragments, or sorting artifact |
| P0 | NEEDS_CLASS_SPECIFIC_TEST | C5_CLASS_SIGNATURE_VS_CLASS_SPECIFIC_GRADIENT | watcher_score=0.9625 state=HIGH | global all-head gradient can hide class-specific roles |
| P0 | SCALING_PARTIAL | C7_SAMPLE_SIZE_SCALING | distinct_n_events=[640, 2560, 5120, 10240] snapshots=15 | large stream can amplify shortcuts if controls are missing |
| P0 | NEEDS_CLASS_DISTRIBUTION_CHECK | C8_CLASS_CONCENTRATION_VS_IMBALANCE | watcher_score=0.9625 state=HIGH | balanced tiny subset can overstate class signatures; natural distribution can hide rare patterns |
| P1 | NEEDS_HEAD_PAIR_SYNERGY | C11_HEAD_PAIR_SYNERGY | divergent_gate_strong_patch_weak_heads=['L1_ch112:128', 'L1_ch16:32', 'L0_ch40:48', 'L2_ch224:256', 'L0_ch48:56', 'L0_ch8:16', 'L2_ch128:160', 'L2_ch64:96'] count=12 | single-head tests can miss redundancy, compensation, and synergy |
| P1 | NEEDS_CROSS_MODEL_TEST | C12_CROSS_MODEL_CHECKPOINT_AGREEMENT | current main stream is ParticleNet_kinpid-focused | architecture-specific artifact can look like physics in one model |
| P1 | NEEDS_CLASS_SPECIFIC_TEST | C3_PATCH_VS_GRADIENT_DIVERGENCE | divergent_heads=12 top=[{'head_id': 'L1_ch112:128', 'gate_abs_grad': 0.8689268512214768, 'patch_acc_drop': 0.0, 'role': 'middle learned-neighborhood / route-composition head'}, {'head_id': 'L1_ch16:32', 'gate_abs_grad': 0.748019616522652, 'patch_acc_drop': 0.0, 'role': 'middle learned-neighborhood / route-composition head'}, {'head_id': 'L0_ch40:48', 'gate_abs_grad': 0.715566657370073, 'patch_acc_drop': 0.0, 'role': 'early feature/geometry/PID reader'}] | gradient support is local; patch may reveal redundancy or compensation |
| P1 | NEEDS_HELDOUT | C4_HEAD_RANK_STABILITY_VS_RUN_CHANGES | stability_score=0.9455 top_heads=['L1_ch112:128', 'L0_ch40:48', 'L2_ch224:256', 'L1_ch16:32', 'L0_ch48:56'] | repeated same data can fake stability |
| P1 | NEEDS_CLASS_SPECIFIC_TEST | C6_NEGATIVE_GATES_VS_SUPPRESSIVE_ROLE | watcher_score=1.0 state=HIGH | not causal until class-specific and patch tests agree |
| P1 | NEEDS_ERROR_ATLAS | C9_CORRECT_VS_WRONG_SPLIT | current stream stores pred/true but no dedicated error-head atlas | heads on wrong examples may support predicted class rather than true class |

## Particle0 control update

- remove_particle0 acc_drop: **0.1941**
- random_remove1 acc_drop mean: **0.0146**
- targeted/random drop ratio: **13.3125**
- keep_only_particle0 acc: **0.2027**

Interpretation: particle0/core is targeted-causal, but not sufficient alone globally. Remaining P0: order control, residual, class-specific gradients, heldout.

## Big-stream policy

Run staged large streams, but do not claim discovery until order/residual/heldout/cross-model tests pass.

## Files

- JSON: `manifests/latest/automatic_comparison_engine_v2.json`
- CSV: `reports/latest/tables/automatic_comparison_rows_v2.csv`
- Training rows: `reports/latest/tables/automatic_comparison_training_dataset_v2.jsonl`
