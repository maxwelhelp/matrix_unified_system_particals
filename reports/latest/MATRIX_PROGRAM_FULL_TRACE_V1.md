# MATRIX_PROGRAM_FULL_TRACE_V1

Postprocessor over INTERNAL_ACTIVATION_CONTRAST_V2/V2_1. It builds particle_role -> head -> class paths from top-particle activation and zero-slice class contribution.

## Top path mechanisms
| diag | role | head | class | A | B | C | B-A | B-C | trigger | loss | anomaly |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anomalous_third_topology_candidate | nearest_hadron_to_best_lepton | L1_ch80:96 | label_Tbl | 74.0160 | 0.0000 | 109.9731 | -74.0160 | -109.9731 | 0.6670 | 0.0000 | 8139.7744 |
| anomalous_third_topology_candidate | other_lepton | L1_ch80:96 | label_Tbl | 80.8757 | 0.0000 | 97.7791 | -80.8757 | -97.7791 | 0.8188 | 0.0000 | 7907.9486 |
| anomalous_third_topology_candidate | photon_neighbor | L1_ch80:96 | label_Hqql | 68.1021 | 119.2678 | -19.5422 | 51.1656 | 138.8100 | 0.0000 | 0.0000 | 7102.3003 |
| anomalous_third_topology_candidate | second_lepton | L1_ch80:96 | label_Tbl | 73.1873 | 0.0000 | 75.3624 | -73.1873 | -75.3624 | 0.9584 | 0.0000 | 5515.5750 |
| target_like_trigger_candidate | photon_neighbor | L1_ch80:96 | label_Tbl | 68.0336 | 136.9842 | 85.8536 | 68.9506 | 51.1306 | 1.3227 | 0.0000 | 3525.4863 |
| anomalous_third_topology_candidate | particle0 | L1_ch32:48 | label_Hqql | 0.0000 | 38.4981 | -4.8849 | 38.4981 | 43.3831 | 0.0000 | 0.0000 | 1670.1671 |
| source_evidence_loss_candidate | other_lepton | L1_ch80:96 | label_Hqql | 93.7284 | 0.0000 | -17.5912 | -93.7284 | 17.5912 | 0.0000 | 93.7284 | 1648.7966 |
| source_evidence_loss_candidate | nearest_hadron_to_best_lepton | L1_ch80:96 | label_Hqql | 85.2932 | 0.0000 | -16.0326 | -85.2932 | 16.0326 | 0.0000 | 85.2932 | 1367.4715 |
| anomalous_third_topology_candidate | particle0_best_lepton | L1_ch80:96 | label_Hqql | 31.1394 | 52.2317 | -12.0220 | 21.0923 | 64.2536 | 0.0000 | 0.0000 | 1355.2559 |
| target_like_trigger_candidate | hadron_neighbor | L1_ch80:96 | label_Tbl | 82.4797 | 131.8961 | 105.2786 | 49.4164 | 26.6174 | 1.7893 | 0.0000 | 1315.3372 |
| source_evidence_loss_candidate | hadron_neighbor | L1_ch80:96 | label_Hqql | 82.5403 | 72.0801 | -37.7346 | -10.4602 | 109.8147 | 0.0000 | 10.4602 | 1148.6833 |
| target_like_trigger_candidate | particle0_best_lepton | L1_ch80:96 | label_Tbl | 19.0465 | 123.2002 | 112.5232 | 104.1537 | 10.6770 | 8.9195 | 0.0000 | 1112.0531 |
| anomalous_third_topology_candidate | hardest_hadron | L1_ch32:48 | label_Tbl | 21.3250 | 0.0000 | 47.0138 | -21.3250 | -47.0138 | 0.4441 | 0.0000 | 1002.5663 |
| source_evidence_loss_candidate | second_lepton | L1_ch80:96 | label_Hqql | 84.8182 | 0.0000 | 7.6550 | -84.8182 | -7.6550 | 0.0000 | 84.8182 | 649.2842 |
| source_evidence_loss_candidate | hard_hadron | L1_ch80:96 | label_Hqql | 53.7795 | 42.3431 | -6.1674 | -11.4365 | 48.5104 | 0.0000 | 11.4365 | 554.7878 |
| anomalous_third_topology_candidate | photon_neighbor | L1_ch32:48 | label_Hqql | 6.1988 | 16.1889 | -31.8707 | 9.9900 | 48.0596 | 0.0000 | 0.0000 | 480.1179 |
| anomalous_third_topology_candidate | particle0 | L2_ch224:256 | label_Tbl | 12.4931 | 31.8709 | 11.6330 | 19.3778 | 20.2379 | 0.9124 | 0.0000 | 392.1660 |
| target_like_trigger_candidate | particle0 | L1_ch32:48 | label_Tbl | 0.0000 | 58.9975 | 52.4964 | 58.9975 | 6.5011 | 7.8652 | 0.0000 | 383.5476 |
| target_like_trigger_candidate | hard_hadron | L1_ch80:96 | label_Tbl | 60.1887 | 84.7825 | 69.4312 | 24.5938 | 15.3513 | 1.5041 | 0.0000 | 377.5475 |
| anomalous_third_topology_candidate | particle0 | L2_ch224:256 | label_Hqql | 11.8355 | 33.9618 | 19.8938 | 22.1263 | 14.0680 | 0.0000 | 0.0000 | 311.2725 |
| source_evidence_loss_candidate | nearest_hadron_to_best_lepton | L1_ch32:48 | label_Hqql | 12.4028 | 4.2903 | -28.6160 | -8.1125 | 32.9063 | 0.0000 | 8.1125 | 266.9526 |
| source_evidence_loss_candidate | hadron_neighbor | L1_ch32:48 | label_Hqql | 13.9077 | 3.7339 | -19.9127 | -10.1738 | 23.6466 | 0.0000 | 10.1738 | 240.5746 |
| target_like_trigger_candidate | particle0_best_lepton | L1_ch32:48 | label_Tbl | 19.2971 | 33.5978 | 43.0800 | 14.3007 | -9.4822 | 1.3643 | 0.0000 | 135.6024 |
| target_like_trigger_candidate | particle0 | L2_ch32:64 | label_Tbl | 0.0000 | 12.1376 | 1.1058 | 12.1376 | 11.0319 | 1.0088 | 0.0000 | 133.9008 |
| anomalous_third_topology_candidate | hard_hadron | L1_ch32:48 | label_Tbl | 23.0281 | 28.7486 | 47.2912 | 5.7205 | -18.5426 | 0.2927 | 0.0000 | 106.0729 |
| target_like_trigger_candidate | nearest_hadron_to_best_lepton | L1_ch32:48 | label_Tbl | 19.5989 | 35.7930 | 40.6022 | 16.1941 | -4.8092 | 2.7877 | 0.0000 | 77.8808 |
| anomalous_third_topology_candidate | particle0_best_lepton | L2_ch224:256 | label_Hqql | 15.8461 | 18.8897 | 37.9192 | 3.0437 | -19.0295 | 0.0000 | 0.0000 | 57.9193 |
| target_like_trigger_candidate | best_lepton | L2_ch32:64 | label_Tbl | -0.6211 | 8.4868 | 4.7391 | 9.1079 | 3.7477 | 1.9184 | 0.0000 | 34.1333 |
| source_evidence_loss_candidate | particle0_best_lepton | L2_ch160:192 | label_Hqql | 3.3236 | -2.1805 | -8.0423 | -5.5041 | 5.8618 | 0.0000 | 5.5041 | 32.2638 |
| target_like_trigger_candidate | hadron_neighbor | L1_ch32:48 | label_Tbl | 26.7495 | 39.3660 | 41.8067 | 12.6165 | -2.4407 | 3.6668 | 0.0000 | 30.7932 |
| anomalous_third_topology_candidate | particle0 | L2_ch0:32 | label_Tbl | -1.3800 | -5.8279 | 1.0418 | -4.4479 | -6.8697 | 0.5652 | 0.0000 | 30.5559 |
| source_evidence_loss_candidate | particle0 | L2_ch160:192 | label_Hqql | 0.0000 | -1.5501 | -19.4517 | -1.5501 | 17.9016 | 0.0000 | 1.5501 | 27.7488 |
| source_evidence_loss_candidate | hardest_hadron | L1_ch32:48 | label_Hqql | 8.9357 | 0.0000 | 2.8060 | -8.9357 | -2.8060 | 0.0000 | 8.9357 | 25.0732 |
| source_evidence_loss_candidate | best_lepton | L2_ch128:160 | label_Hqql | 11.7139 | 9.5782 | -1.0436 | -2.1358 | 10.6218 | 0.0000 | 2.1358 | 22.6858 |
| target_like_trigger_candidate | photon_neighbor | L1_ch32:48 | label_Tbl | 20.5164 | 40.5311 | 40.2450 | 20.0147 | 0.2861 | 15.5627 | 0.0000 | 5.7257 |
| source_evidence_loss_candidate | hardest_hadron | L2_ch224:256 | label_Hqql | 4.9461 | 3.1883 | 10.2675 | -1.7578 | -7.0793 | 0.0000 | 1.7578 | 12.4437 |
| anomalous_third_topology_candidate | other_lepton | L2_ch128:160 | label_Hqql | 0.0000 | 3.6611 | 0.2919 | 3.6611 | 3.3692 | 0.0000 | 0.0000 | 12.3350 |
| target_like_trigger_candidate | other_lepton | L2_ch224:256 | label_Tbl | 0.0000 | 7.7684 | 6.2875 | 7.7684 | 1.4808 | 3.1313 | 0.0000 | 11.5038 |
| anomalous_third_topology_candidate | particle0 | L2_ch0:32 | label_Hqql | 4.2951 | 6.5288 | 1.6343 | 2.2337 | 4.8945 | 0.0000 | 0.0000 | 10.9332 |
| source_evidence_loss_candidate | particle0 | L2_ch128:160 | label_Hqql | 6.5378 | 2.7147 | 0.2643 | -3.8231 | 2.4504 | 0.0000 | 3.8231 | 9.3681 |
| source_evidence_loss_candidate | particle0 | L2_ch32:64 | label_Hqql | 0.0000 | -4.0218 | -1.7466 | -4.0218 | -2.2752 | 0.0000 | 4.0218 | 9.1503 |
| source_evidence_loss_candidate | best_lepton | L2_ch32:64 | label_Hqql | 0.1324 | -2.8121 | 0.2813 | -2.9445 | -3.0934 | 0.0000 | 2.9445 | 9.1084 |
| anomalous_third_topology_candidate | hardest_hadron | L2_ch224:256 | label_Tbl | 4.8325 | 2.3761 | 6.0719 | -2.4564 | -3.6958 | 0.5231 | 0.0000 | 9.0782 |
| source_evidence_loss_candidate | photon_neighbor | L2_ch224:256 | label_Hqql | 5.0961 | 3.4735 | 8.9260 | -1.6226 | -5.4525 | 0.0000 | 1.6226 | 8.8473 |
| source_evidence_loss_candidate | second_lepton | L2_ch160:192 | label_Hqql | -0.0511 | -1.3242 | -8.1505 | -1.2731 | 6.8263 | 0.0000 | 1.2731 | 8.6904 |
| source_evidence_loss_candidate | best_lepton | L2_ch0:32 | label_Hqql | 2.6422 | 0.0000 | 3.1837 | -2.6422 | -3.1837 | 0.0000 | 2.6422 | 8.4120 |
| source_evidence_loss_candidate | hard_hadron | L1_ch32:48 | label_Hqql | 6.6337 | 6.2805 | -15.8303 | -0.3533 | 22.1108 | 0.0000 | 0.3533 | 7.8111 |
| source_evidence_loss_candidate | best_lepton | L2_ch160:192 | label_Hqql | 2.4495 | -5.1611 | -4.1409 | -7.6106 | -1.0202 | 0.0000 | 7.6106 | 7.7641 |
| source_evidence_loss_candidate | second_lepton | L2_ch128:160 | label_Hqql | 4.4963 | 2.3987 | -1.0067 | -2.0976 | 3.4054 | 0.0000 | 2.0976 | 7.1432 |
| anomalous_third_topology_candidate | other_lepton | L2_ch224:256 | label_Hqql | 0.0000 | 7.8625 | 8.7652 | 7.8625 | -0.9027 | 0.0000 | 0.0000 | 7.0971 |

## Top head programs
| head | diag | B_close_C | B-A source | B-A target | roles |
| --- | --- | --- | --- | --- | --- |
| L1_ch80:96 | active_tbl_like_readout_candidate | 107.7441 | -0.1101 | 1.1220 | hadron_neighbor:216;photon_neighbor:212;hard_hadron:36;particle0_best_lepton:23;nearest_hadron_to_best_lepton:12 |
| L2_ch224:256 | lost_hqql_evidence_candidate | -27.9287 | 0.2378 | -0.4670 | particle0_best_lepton:148;hardest_hadron:101;hard_hadron:86;photon_neighbor:70;hadron_neighbor:31 |
| L2_ch32:64 | mixed_or_unclear | -19.2769 | -0.4246 | 0.3246 | particle0_best_lepton:148;hard_hadron:96;hardest_hadron:61;hadron_neighbor:59;photon_neighbor:57 |
| L2_ch160:192 | mixed_or_unclear | -8.3213 | -1.0202 | -0.0235 | particle0_best_lepton:148;photon_neighbor:102;hadron_neighbor:94;hard_hadron:50;nearest_hadron_to_best_lepton:41 |
| L1_ch32:48 | active_tbl_like_readout_candidate | 7.8095 | -0.2127 | 0.3607 | hadron_neighbor:231;photon_neighbor:74;particle0_best_lepton:65;nearest_hadron_to_best_lepton:64;hard_hadron:55 |
| L2_ch128:160 | lost_hqql_evidence_candidate | -6.6534 | -0.2256 | -0.0576 | particle0_best_lepton:146;hard_hadron:82;photon_neighbor:67;hadron_neighbor:67;hardest_hadron:59 |
| L2_ch0:32 | lost_hqql_evidence_candidate | -2.3092 | 0.0875 | 0.0778 | particle0_best_lepton:147;hard_hadron:98;hardest_hadron:72;photon_neighbor:54;hadron_neighbor:51 |

## Note

This V1 uses existing V2/V2.1 tables. To make it truly all-head, run V2 with a full HEADS list, then rerun this postprocessor. Exact EdgeConv source-block weight decomposition is reserved for V2 after module parsing is validated.
