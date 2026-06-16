# Phase 2 Hqql/Tbl Physical Swaps v1

Physical causal tests for Hqql/Tbl ambiguity.

## Summary
| test | target_group | n | flip | success_to_Hqql | delta_margin | delta_base_logit |
| --- | --- | --- | --- | --- | --- | --- |
| 2A_isolation_hadronic_injection | Hqql_to_Tbl | 35 | 0.7143 | 0.6857 | 2.3936 | -3.2788 |
| 2C_neighbor_swap | Hqql_to_Tbl | 35 | 0.4571 | 0.4000 | 0.8168 | -3.0742 |
| random_same_count | Hqql_to_Tbl | 35 | 0.5429 | 0.4286 | 1.9292 | -1.7402 |
| 2B_lepton_core_swap | Tbl_correct | 80 | 0.3125 | 0.1500 | 4.5771 | -2.7291 |
| random_same_count | Tbl_correct | 80 | 0.1375 | 0.1375 | 4.3266 | -0.8663 |

## Example rows
| test | target | donor | group | base | patched | success_Hqql | d_margin | p0 | donor_p0 | idx |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2A_isolation_hadronic_injection | 3077 | 3713 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 7.3530 | electron | electron | [75, 25, 100, 125, 118, 93, 68, 18] |
| 2C_neighbor_swap | 3077 | 3713 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 3.2441 | electron | electron | [75, 25, 100, 125, 118, 93, 68, 18] |
| random_same_count | 3077 | 3713 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 8.5259 | electron | electron | [7, 35, 12, 99, 53, 14, 108, 116] |
| 2A_isolation_hadronic_injection | 3082 | 3285 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 5.1846 | electron | photon | [72, 48, 60, 12, 24, 36, 96, 120] |
| 2C_neighbor_swap | 3082 | 3285 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 3.1738 | electron | photon | [72, 48, 60, 12, 24, 36, 96, 120] |
| random_same_count | 3082 | 3285 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 1.7742 | electron | photon | [7, 21, 18, 44, 72, 43, 90, 32] |
| 2A_isolation_hadronic_injection | 3148 | 4062 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 3.8494 | neutral_hadron | photon | [32, 16, 80, 64, 96, 112, 116, 100] |
| 2C_neighbor_swap | 3148 | 4062 | Hqql_to_Tbl | label_Tbl | label_QCD | 0 | 3.0779 | neutral_hadron | photon | [32, 16, 80, 64, 96, 112, 116, 100] |
| random_same_count | 3148 | 4062 | Hqql_to_Tbl | label_Tbl | label_Wqq | 0 | 4.2157 | neutral_hadron | photon | [49, 9, 1, 41, 94, 58, 14, 116] |
| 2A_isolation_hadronic_injection | 3218 | 3789 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 1.4135 | muon | electron | [84, 126, 22, 106, 64, 96, 54, 12] |
| 2C_neighbor_swap | 3218 | 3789 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -0.6266 | muon | electron | [84, 126, 22, 106, 64, 96, 54, 12] |
| random_same_count | 3218 | 3789 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 3.7966 | muon | electron | [38, 117, 56, 74, 62, 34, 61, 108] |
| 2A_isolation_hadronic_injection | 3335 | 4070 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 0.6746 | electron | muon | [106, 96, 43, 119, 13, 66, 62, 9] |
| 2C_neighbor_swap | 3335 | 4070 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -3.4038 | electron | muon | [106, 96, 43, 119, 13, 66, 62, 9] |
| random_same_count | 3335 | 4070 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 1.0903 | electron | muon | [106, 78, 82, 68, 73, 104, 123, 41] |
| 2A_isolation_hadronic_injection | 3347 | 3333 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.2100 | muon | photon | [98, 89, 40, 114, 16, 65, 39, 88] |
| 2C_neighbor_swap | 3347 | 3333 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 1.1740 | muon | photon | [98, 89, 40, 114, 16, 65, 39, 88] |
| random_same_count | 3347 | 3333 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 1.0285 | muon | photon | [69, 82, 102, 86, 77, 114, 107, 63] |
| 2A_isolation_hadronic_injection | 3361 | 3827 | Hqql_to_Tbl | label_Tbl | label_QCD | 0 | 4.3143 | electron | neutral_hadron | [74, 111, 119, 82, 8, 45, 50, 13] |
| 2C_neighbor_swap | 3361 | 3827 | Hqql_to_Tbl | label_Tbl | label_QCD | 0 | 4.3252 | electron | neutral_hadron | [74, 111, 119, 82, 8, 45, 50, 13] |
| random_same_count | 3361 | 3827 | Hqql_to_Tbl | label_Tbl | label_Hcc | 0 | 5.2027 | electron | neutral_hadron | [83, 24, 93, 105, 11, 117, 63, 85] |
| 2A_isolation_hadronic_injection | 3382 | 3858 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 6.0553 | electron | neutral_hadron | [28, 84, 112, 123, 67, 95, 39, 11] |
| 2C_neighbor_swap | 3382 | 3858 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 4.7545 | electron | neutral_hadron | [28, 84, 112, 123, 67, 95, 39, 11] |
| random_same_count | 3382 | 3858 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 3.7204 | electron | neutral_hadron | [93, 59, 50, 74, 100, 44, 3, 25] |
| 2A_isolation_hadronic_injection | 3403 | 4092 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 1.8789 | electron | electron | [72, 108, 20, 92, 56, 106, 70, 34] |
| 2C_neighbor_swap | 3403 | 4092 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 0.6341 | electron | electron | [72, 108, 20, 92, 56, 106, 70, 34] |
| random_same_count | 3403 | 4092 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 3.2477 | electron | electron | [30, 52, 69, 65, 93, 106, 117, 8] |
| 2A_isolation_hadronic_injection | 3433 | 3408 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.9189 | muon | electron | [79, 64, 101, 22, 43, 122, 92, 13] |
| 2C_neighbor_swap | 3433 | 3408 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -0.4865 | muon | electron | [79, 64, 101, 22, 43, 122, 92, 13] |
| random_same_count | 3433 | 3408 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 1.6884 | muon | electron | [30, 70, 62, 126, 23, 20, 127, 69] |
| 2A_isolation_hadronic_injection | 3483 | 3619 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 4.3934 | muon | electron | [70, 105, 125, 90, 20, 55, 59, 24] |
| 2C_neighbor_swap | 3483 | 3619 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 0.5474 | muon | electron | [70, 105, 125, 90, 20, 55, 59, 24] |
| random_same_count | 3483 | 3619 | Hqql_to_Tbl | label_Tbl | label_Tbqq | 0 | 1.8390 | muon | electron | [25, 3, 33, 103, 46, 88, 35, 123] |
| 2A_isolation_hadronic_injection | 3491 | 4068 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 1.1731 | muon | muon | [28, 84, 112, 127, 71, 99, 15, 43] |
| 2C_neighbor_swap | 3491 | 4068 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -5.4574 | muon | muon | [28, 84, 112, 127, 71, 99, 15, 43] |
| random_same_count | 3491 | 4068 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 1.8209 | muon | muon | [46, 91, 12, 11, 56, 115, 2, 102] |
| 2A_isolation_hadronic_injection | 3501 | 3946 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 0.8786 | electron | charged_hadron | [86, 94, 8, 51, 73, 116, 30, 54] |
| 2C_neighbor_swap | 3501 | 3946 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 1.3126 | electron | charged_hadron | [86, 94, 8, 51, 73, 116, 30, 54] |
| random_same_count | 3501 | 3946 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 1.1164 | electron | charged_hadron | [127, 42, 34, 123, 61, 5, 97, 72] |
| 2A_isolation_hadronic_injection | 3562 | 3733 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 5.0240 | electron | muon | [26, 78, 104, 107, 55, 81, 3, 29] |
| 2C_neighbor_swap | 3562 | 3733 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 0.6074 | electron | muon | [26, 78, 104, 107, 55, 81, 3, 29] |
| random_same_count | 3562 | 3733 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 0.6644 | electron | muon | [124, 54, 9, 92, 112, 87, 19, 48] |
| 2A_isolation_hadronic_injection | 3603 | 3768 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.2298 | electron | muon | [114, 80, 23, 27, 84, 82, 25, 101] |
| 2C_neighbor_swap | 3603 | 3768 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -1.5952 | electron | muon | [114, 80, 23, 27, 84, 82, 25, 101] |
| random_same_count | 3603 | 3768 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 3.6688 | electron | muon | [98, 67, 50, 69, 40, 19, 117, 84] |
| 2A_isolation_hadronic_injection | 3611 | 3115 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.5734 | electron | neutral_hadron | [31, 93, 124, 81, 50, 112, 19, 44] |
| 2C_neighbor_swap | 3611 | 3115 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 1.0406 | electron | neutral_hadron | [31, 93, 124, 81, 50, 112, 19, 44] |
| random_same_count | 3611 | 3115 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 2.2031 | electron | neutral_hadron | [69, 125, 44, 67, 16, 81, 22, 103] |
| 2A_isolation_hadronic_injection | 3658 | 3902 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.4251 | muon | muon | [72, 108, 24, 96, 60, 92, 20, 56] |
| 2C_neighbor_swap | 3658 | 3902 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 0.4457 | muon | muon | [72, 108, 24, 96, 60, 92, 20, 56] |
| random_same_count | 3658 | 3902 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 0.3392 | muon | muon | [3, 45, 58, 112, 95, 93, 126, 92] |
| 2A_isolation_hadronic_injection | 3666 | 3810 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 1.5250 | electron | electron | [96, 85, 37, 42, 90, 121, 25, 73] |
| 2C_neighbor_swap | 3666 | 3810 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -0.7388 | electron | electron | [96, 85, 37, 42, 90, 121, 25, 73] |
| random_same_count | 3666 | 3810 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 1.5379 | electron | electron | [67, 42, 112, 66, 72, 18, 44, 65] |
| 2A_isolation_hadronic_injection | 3698 | 3205 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 3.0353 | photon | photon | [122, 126, 4, 65, 125, 64, 3, 67] |
| 2C_neighbor_swap | 3698 | 3205 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 1.3930 | photon | photon | [122, 126, 4, 65, 125, 64, 3, 67] |
| random_same_count | 3698 | 3205 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 1.4981 | photon | photon | [12, 35, 120, 65, 32, 27, 114, 42] |
| 2A_isolation_hadronic_injection | 3701 | 3152 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 0.2707 | electron | muon | [30, 90, 120, 38, 68, 98, 8, 80] |
| 2C_neighbor_swap | 3701 | 3152 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.0997 | electron | muon | [30, 90, 120, 38, 68, 98, 8, 80] |
| random_same_count | 3701 | 3152 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.3376 | electron | muon | [65, 26, 98, 115, 3, 25, 35, 73] |
| 2A_isolation_hadronic_injection | 3721 | 3391 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 1.8417 | electron | charged_hadron | [75, 25, 100, 125, 121, 96, 71, 21] |
| 2C_neighbor_swap | 3721 | 3391 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.2866 | electron | charged_hadron | [75, 25, 100, 125, 121, 96, 71, 21] |
| random_same_count | 3721 | 3391 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.0085 | electron | charged_hadron | [119, 114, 104, 120, 69, 18, 101, 116] |
| 2A_isolation_hadronic_injection | 3730 | 3204 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 3.3736 | muon | charged_hadron | [80, 120, 35, 115, 75, 108, 28, 68] |
| 2C_neighbor_swap | 3730 | 3204 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.4098 | muon | charged_hadron | [80, 120, 35, 115, 75, 108, 28, 68] |
| random_same_count | 3730 | 3204 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -0.9358 | muon | charged_hadron | [107, 74, 111, 63, 44, 51, 118, 29] |
| 2A_isolation_hadronic_injection | 3746 | 3505 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 3.9049 | muon | electron | [44, 22, 110, 88, 102, 124, 36, 14] |
| 2C_neighbor_swap | 3746 | 3505 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 3.0285 | muon | electron | [44, 22, 110, 88, 102, 124, 36, 14] |
| random_same_count | 3746 | 3505 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 1.8561 | muon | electron | [102, 77, 78, 125, 64, 44, 90, 75] |
| 2A_isolation_hadronic_injection | 3766 | 3819 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.6992 | electron | muon | [104, 82, 30, 119, 15, 67, 43, 95] |
| 2C_neighbor_swap | 3766 | 3819 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -1.6738 | electron | muon | [104, 82, 30, 119, 15, 67, 43, 95] |
| random_same_count | 3766 | 3819 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.4468 | electron | muon | [110, 54, 41, 46, 28, 99, 58, 44] |
| 2A_isolation_hadronic_injection | 3780 | 3965 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 3.8572 | muon | charged_hadron | [26, 78, 104, 120, 68, 94, 42, 16] |
| 2C_neighbor_swap | 3780 | 3965 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.6048 | muon | charged_hadron | [26, 78, 104, 120, 68, 94, 42, 16] |
| random_same_count | 3780 | 3965 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -0.8850 | muon | charged_hadron | [108, 54, 49, 65, 34, 107, 119, 23] |
| 2A_isolation_hadronic_injection | 3829 | 3707 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 0.7672 | electron | muon | [108, 122, 14, 68, 44, 98, 123, 15] |
| 2C_neighbor_swap | 3829 | 3707 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -0.9391 | electron | muon | [108, 122, 14, 68, 44, 98, 123, 15] |
| random_same_count | 3829 | 3707 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 1.7152 | electron | muon | [117, 34, 65, 105, 78, 42, 8, 121] |
| 2A_isolation_hadronic_injection | 3849 | 3946 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 0.6887 | charged_hadron | charged_hadron | [28, 84, 112, 122, 66, 94, 10, 38] |
| 2C_neighbor_swap | 3849 | 3946 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -1.3980 | charged_hadron | charged_hadron | [28, 84, 112, 122, 66, 94, 10, 38] |
| random_same_count | 3849 | 3946 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -2.0430 | charged_hadron | charged_hadron | [98, 124, 91, 42, 32, 83, 58, 35] |
| 2A_isolation_hadronic_injection | 3891 | 3727 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -1.3079 | photon | muon | [26, 78, 104, 111, 59, 85, 7, 33] |
| 2C_neighbor_swap | 3891 | 3727 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -6.4629 | photon | muon | [26, 78, 104, 111, 59, 85, 7, 33] |
| random_same_count | 3891 | 3727 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 0.5638 | photon | muon | [59, 65, 74, 116, 119, 36, 44, 123] |
| 2A_isolation_hadronic_injection | 3892 | 3735 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 0.4923 | electron | muon | [31, 93, 124, 45, 76, 107, 14, 82] |
| 2C_neighbor_swap | 3892 | 3735 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 4.5373 | electron | muon | [31, 93, 124, 45, 76, 107, 14, 82] |
| random_same_count | 3892 | 3735 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -0.8537 | electron | muon | [17, 62, 69, 6, 61, 70, 19, 42] |
| 2A_isolation_hadronic_injection | 3896 | 3756 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 0.8602 | electron | charged_hadron | [75, 25, 100, 125, 113, 88, 38, 13] |
| 2C_neighbor_swap | 3896 | 3756 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 2.4485 | electron | charged_hadron | [75, 25, 100, 125, 113, 88, 38, 13] |
| random_same_count | 3896 | 3756 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 3.9428 | electron | charged_hadron | [60, 65, 116, 117, 114, 77, 100, 122] |
| 2A_isolation_hadronic_injection | 3936 | 3556 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.3574 | electron | muon | [78, 117, 34, 112, 73, 93, 15, 54] |
| 2C_neighbor_swap | 3936 | 3556 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -2.4267 | electron | muon | [78, 117, 34, 112, 73, 93, 15, 54] |
| random_same_count | 3936 | 3556 | Hqql_to_Tbl | label_Tbl | label_H4q | 0 | 3.6974 | electron | muon | [50, 30, 89, 114, 9, 112, 33, 37] |
| 2A_isolation_hadronic_injection | 4020 | 3285 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 1.0510 | muon | photon | [26, 78, 104, 77, 51, 103, 25, 35] |
| 2C_neighbor_swap | 4020 | 3285 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.8652 | muon | photon | [26, 78, 104, 77, 51, 103, 25, 35] |
| random_same_count | 4020 | 3285 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -1.6639 | muon | photon | [87, 22, 26, 6, 35, 68, 98, 95] |
| 2A_isolation_hadronic_injection | 4023 | 3669 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 0.1475 | electron | charged_hadron | [84, 126, 11, 95, 53, 100, 16, 58] |
| 2C_neighbor_swap | 4023 | 3669 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 0.3797 | electron | charged_hadron | [84, 126, 11, 95, 53, 100, 16, 58] |
| random_same_count | 4023 | 3669 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -0.0244 | electron | charged_hadron | [60, 29, 37, 68, 12, 14, 57, 79] |
| 2A_isolation_hadronic_injection | 4036 | 3320 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 0.7668 | electron | electron | [29, 87, 116, 82, 53, 111, 24, 51] |
| 2C_neighbor_swap | 4036 | 3320 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 2.3885 | electron | electron | [29, 87, 116, 82, 53, 111, 24, 51] |
| random_same_count | 4036 | 3320 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 3.6148 | electron | electron | [9, 82, 121, 51, 53, 103, 102, 58] |
| 2A_isolation_hadronic_injection | 4086 | 3499 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.8955 | electron | photon | [104, 114, 10, 62, 75, 127, 23, 125] |
| 2C_neighbor_swap | 4086 | 3499 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 3.0188 | electron | photon | [104, 114, 10, 62, 75, 127, 23, 125] |
| random_same_count | 4086 | 3499 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.7678 | electron | photon | [20, 64, 18, 25, 119, 28, 126, 31] |
| 2B_lepton_core_swap | 5120 | 3357 | Tbl_correct | label_Tbl | label_Tbl | 0 | 7.9490 | muon | muon | [0] |
| random_same_count | 5120 | 3357 | Tbl_correct | label_Tbl | label_Tbl | 0 | 5.6066 | muon | muon | [4, 2, 53, 84, 42, 71, 6, 119] |
| 2B_lepton_core_swap | 5121 | 3856 | Tbl_correct | label_Tbl | label_Tbl | 0 | 7.6200 | muon | electron | [0] |
| random_same_count | 5121 | 3856 | Tbl_correct | label_Tbl | label_Tbl | 0 | 1.0978 | muon | electron | [38, 119, 24, 39, 15, 37, 86, 83] |
| 2B_lepton_core_swap | 5122 | 3705 | Tbl_correct | label_Tbl | label_Hqql | 1 | 9.6288 | muon | charged_hadron | [0] |
| random_same_count | 5122 | 3705 | Tbl_correct | label_Tbl | label_Tbl | 0 | 3.5165 | muon | charged_hadron | [20, 60, 29, 54, 66, 85, 118, 56] |
| 2B_lepton_core_swap | 5123 | 3254 | Tbl_correct | label_Tbl | label_Tbl | 0 | 1.8940 | muon | electron | [0] |
| random_same_count | 5123 | 3254 | Tbl_correct | label_Tbl | label_Tbl | 0 | 7.9238 | muon | electron | [112, 6, 37, 18, 61, 94, 93, 117] |
| 2B_lepton_core_swap | 5124 | 3514 | Tbl_correct | label_Tbl | label_Tbqq | 0 | 4.7547 | electron | neutral_hadron | [0] |
| random_same_count | 5124 | 3514 | Tbl_correct | label_Tbl | label_Tbl | 0 | 4.4451 | electron | neutral_hadron | [79, 3, 57, 67, 46, 37, 47, 28] |
| 2B_lepton_core_swap | 5125 | 3398 | Tbl_correct | label_Tbl | label_Tbl | 0 | 4.8549 | electron | muon | [0] |
| random_same_count | 5125 | 3398 | Tbl_correct | label_Tbl | label_Tbl | 0 | 7.7763 | electron | muon | [13, 76, 86, 42, 95, 11, 100, 27] |
| 2B_lepton_core_swap | 5126 | 3532 | Tbl_correct | label_Tbl | label_Tbl | 0 | -4.1358 | neutral_hadron | muon | [0] |
| random_same_count | 5126 | 3532 | Tbl_correct | label_Tbl | label_Hqql | 1 | 5.4017 | neutral_hadron | muon | [109, 111, 1, 21, 101, 102, 12, 43] |
| 2B_lepton_core_swap | 5127 | 3504 | Tbl_correct | label_Tbl | label_Tbl | 0 | 6.3346 | muon | electron | [0] |

## Interpretation

2A asks whether adding hadronic Hqql-like neighbors around the same lepton restores Hqql. 2B asks whether the lepton itself is enough. 2C asks whether neighbor context alone restores Hqql. Compare targeted tests against random_same_count for each target group.
