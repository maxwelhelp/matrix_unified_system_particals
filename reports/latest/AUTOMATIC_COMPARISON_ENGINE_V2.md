# Automatic Comparison Engine v2

v2 adds big-stream and discovery-readiness comparisons on top of v1.

## P0 comparisons
| status | comparison | claim | missing | next |
| --- | --- | --- | --- | --- |
| MISSING_RESIDUAL_TEST | C10_KNOWN_OBSERVABLE_RESIDUAL | discovery-relevant signals must survive known-observable baselines | known-observable residual analysis | fit known observables then test whether head/particle signals explain residual errors or logits |
| NEEDS_HELDOUT | C13_PER_FILE_HELDOUT_STABILITY | relations should survive different ROOT files and tar parts | per-file/per-tar-part stability report | run stream over more ROOT files and compare head/rule signals per file and per class |
| NEEDS_ORDER_CONTROL | C14_ORDERING_VS_PHYSICAL_COORDINATE | particle0 dominance must be separated from particle ordering/sorting | particle-order shuffle / coordinate-only comparison | run particle order shuffle and compare index-based vs pt/deltaR-based signals |
| METHOD_DEBUG_NOT_DISCOVERY_READY | C15_DISCOVERY_READINESS_SCORE | a hypothesis is discovery-relevant only after controls, heldout, residual, and cross-model tests | C1_STREAM_RELATION_VS_MISSING_CONTROL, C5_CLASS_SIGNATURE_VS_CLASS_SPECIFIC_GRADIENT, C2_WIDE_PATTERN_VS_ROUTE_TRACE, C8_CLASS_CONCENTRATION_VS_IMBALANCE, C10_KNOWN_OBSERVABLE_RESIDUAL, C13_PER_FILE_HELDOUT_STABILITY, C14_ORDERING_VS_PHYSICAL_COORDINATE | complete P0 controls before claiming physics/discovery relevance |
| RUN_SAMPLED_LARGE_STREAM_BUT_PRIORITIZE_CONTROLS | C16_BIG_STREAM_READINESS | large stream should run with summaries and known P0 controls tracked | run sampled large stream plus immediately run controls | run staged large stream: 64 smoke -> 256 -> 512/1024, then particle0/top-k controls |
| CANDIDATE_STRONG_MISSING_CONTROL | C1_STREAM_RELATION_VS_MISSING_CONTROL | particle0/core_high_pt relation supports AH1 core-anchor hypothesis | particle0/top-k/random controls | run particle0 removal / keep-only particle0 / top-k removal / same-count random controls |
| NEEDS_ROUTE_TRACE | C2_WIDE_PATTERN_VS_ROUTE_TRACE | wide particle pattern may be secondary context rather than noise | route-neighbor trace / causal route controls | run route-neighbor trace for top all-head particles and wide non-particle0 particles |
| NEEDS_CLASS_SPECIFIC_TEST | C5_CLASS_SIGNATURE_VS_CLASS_SPECIFIC_GRADIENT | Hqql/Tbl signature is strong in stream but global gradients are not class-specific | class-specific all-head gradients | run class-specific all-head gradients for Hqql/Tbl/Tbqq/Wqq/Zqq |
| SCALING_PARTIAL | C7_SAMPLE_SIZE_SCALING | signals must scale from small snapshots to larger streams |  | run stream cycles at SAMPLES_PER_FILE=64,256,512,1024 with HISTORY_COPY=1 and compare ranks/signals |
| NEEDS_CLASS_DISTRIBUTION_CHECK | C8_CLASS_CONCENTRATION_VS_IMBALANCE | Hqql/Tbl dominance may be real class signature or sampling bias | balanced-vs-natural stream comparison | run one balanced stream and one natural/random-file stream, compare class signatures |

## All comparisons
| priority | status | comparison | support | risk |
| --- | --- | --- | --- | --- |
| P0 | MISSING_RESIDUAL_TEST | C10_KNOWN_OBSERVABLE_RESIDUAL | current signals use particles/heads but not residual after mass/tau/nparticles/pt | particle0/core may be explained by pt/mass/nparticles/tau variables |
| P0 | NEEDS_HELDOUT | C13_PER_FILE_HELDOUT_STABILITY | snapshots=12 but no per-file heldout breakdown | same extracted tiny files can fake stable patterns |
| P0 | NEEDS_ORDER_CONTROL | C14_ORDERING_VS_PHYSICAL_COORDINATE | particle0_edge_signal=0.9288178736074759 support=120 | particle index can encode sorting by pt, not a physical interaction |
| P0 | METHOD_DEBUG_NOT_DISCOVERY_READY | C15_DISCOVERY_READINESS_SCORE | p0_missing_count=7 readiness=method_debug | correlation-only relation is not a discovery claim |
| P0 | RUN_SAMPLED_LARGE_STREAM_BUT_PRIORITIZE_CONTROLS | C16_BIG_STREAM_READINESS | current_snapshots=12 stream_events=5352 | big data can make wrong shortcut look very confident |
| P0 | CANDIDATE_STRONG_MISSING_CONTROL | C1_STREAM_RELATION_VS_MISSING_CONTROL | relation_signal=0.9474324892454034 support=151 | could be sorting shortcut or normal leading-particle bias |
| P0 | NEEDS_ROUTE_TRACE | C2_WIDE_PATTERN_VS_ROUTE_TRACE | relation_signal=0.7525254963492034 support=20 dst=hypothesis:T6_WIDE_SECONDARY_CONTEXT | wide relation can be class imbalance, loose fragments, or sorting artifact |
| P0 | NEEDS_CLASS_SPECIFIC_TEST | C5_CLASS_SIGNATURE_VS_CLASS_SPECIFIC_GRADIENT | watcher_score=0.9625 state=HIGH | global all-head gradient can hide class-specific roles |
| P0 | SCALING_PARTIAL | C7_SAMPLE_SIZE_SCALING | distinct_n_events=[640, 2560, 5120, 10240] snapshots=12 | large stream can amplify shortcuts if controls are missing |
| P0 | NEEDS_CLASS_DISTRIBUTION_CHECK | C8_CLASS_CONCENTRATION_VS_IMBALANCE | watcher_score=0.9625 state=HIGH | balanced tiny subset can overstate class signatures; natural distribution can hide rare patterns |
| P1 | NEEDS_HEAD_PAIR_SYNERGY | C11_HEAD_PAIR_SYNERGY | divergent_gate_strong_patch_weak_heads=['L1_ch112:128', 'L1_ch16:32', 'L0_ch40:48', 'L2_ch224:256', 'L0_ch48:56', 'L0_ch8:16', 'L2_ch128:160', 'L2_ch64:96'] count=12 | single-head tests can miss redundancy, compensation, and synergy |
| P1 | NEEDS_CROSS_MODEL_TEST | C12_CROSS_MODEL_CHECKPOINT_AGREEMENT | current main stream is ParticleNet_kinpid-focused | architecture-specific artifact can look like physics in one model |
| P1 | NEEDS_CLASS_SPECIFIC_TEST | C3_PATCH_VS_GRADIENT_DIVERGENCE | divergent_heads=12 top=[{'head_id': 'L1_ch112:128', 'gate_abs_grad': 0.8689268512214768, 'patch_acc_drop': 0.0, 'role': 'middle learned-neighborhood / route-composition head'}, {'head_id': 'L1_ch16:32', 'gate_abs_grad': 0.748019616522652, 'patch_acc_drop': 0.0, 'role': 'middle learned-neighborhood / route-composition head'}, {'head_id': 'L0_ch40:48', 'gate_abs_grad': 0.715566657370073, 'patch_acc_drop': 0.0, 'role': 'early feature/geometry/PID reader'}] | gradient support is local; patch may reveal redundancy or compensation |
| P1 | NEEDS_HELDOUT | C4_HEAD_RANK_STABILITY_VS_RUN_CHANGES | stability_score=0.9455 top_heads=['L1_ch112:128', 'L0_ch40:48', 'L2_ch224:256', 'L1_ch16:32', 'L0_ch48:56'] | repeated same data can fake stability |
| P1 | NEEDS_CLASS_SPECIFIC_TEST | C6_NEGATIVE_GATES_VS_SUPPRESSIVE_ROLE | watcher_score=1.0 state=HIGH | not causal until class-specific and patch tests agree |
| P1 | NEEDS_ERROR_ATLAS | C9_CORRECT_VS_WRONG_SPLIT | current stream stores pred/true but no dedicated error-head atlas | heads on wrong examples may support predicted class rather than true class |

## Big-stream policy

Run a staged large stream, not the whole downloaded dataset blindly:

1. smoke: SAMPLES_PER_FILE=64;
2. medium: SAMPLES_PER_FILE=256;
3. large sampled: SAMPLES_PER_FILE=512 or 1024 with MICRO_BATCH=16;
4. immediately run particle0/top-k controls and class-specific gradients;
5. only then expand to more ROOT files / tar parts.

## Files

- JSON: `manifests/latest/automatic_comparison_engine_v2.json`
- CSV: `reports/latest/tables/automatic_comparison_rows_v2.csv`
- Training rows: `reports/latest/tables/automatic_comparison_training_dataset_v2.jsonl`
