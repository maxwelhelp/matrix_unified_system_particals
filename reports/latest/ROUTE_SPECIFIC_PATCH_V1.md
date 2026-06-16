# Route Specific Patch v1

Causal patch test for event-level active L2/core routes.

## Summary by head/mode
| head | mode | n | flip_rate | mean_delta_base_logit | mean_patched_conf |
| --- | --- | --- | --- | --- | --- |
| L2_ch224:256 | remove_top_particle | 12 | 1.0000 | -20.3062 | 0.0015 |
| L2_ch224:256 | remove_knn_neighbors | 12 | 0.9167 | -20.7754 | 0.0758 |
| L2_ch224:256 | remove_top_plus_knn | 12 | 1.0000 | -21.7738 | 0.0006 |
| L2_ch224:256 | random_same_count | 12 | 0.0833 | 1.5899 | 0.9007 |
| L2_ch128:160 | remove_top_particle | 12 | 1.0000 | -20.3062 | 0.0015 |
| L2_ch128:160 | remove_knn_neighbors | 12 | 0.9167 | -20.7754 | 0.0758 |
| L2_ch128:160 | remove_top_plus_knn | 12 | 1.0000 | -21.7738 | 0.0006 |
| L2_ch128:160 | random_same_count | 12 | 0.0833 | 0.8492 | 0.8062 |
| L2_ch32:64 | remove_top_particle | 12 | 1.0000 | -20.3062 | 0.0015 |
| L2_ch32:64 | remove_knn_neighbors | 12 | 0.9167 | -20.7754 | 0.0758 |
| L2_ch32:64 | remove_top_plus_knn | 12 | 1.0000 | -21.7738 | 0.0006 |
| L2_ch32:64 | random_same_count | 12 | 0.0000 | 1.0907 | 0.9380 |
| L2_ch0:32 | remove_top_particle | 12 | 1.0000 | -20.3062 | 0.0015 |
| L2_ch0:32 | remove_knn_neighbors | 12 | 0.9167 | -20.7754 | 0.0758 |
| L2_ch0:32 | remove_top_plus_knn | 12 | 1.0000 | -21.7738 | 0.0006 |
| L2_ch0:32 | random_same_count | 12 | 0.1667 | 1.4503 | 0.8753 |

## Rows
| event | true | base | patched | head | mode | flip | d_base_logit | indices |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 197 | label_Hqql | label_Tbl | label_QCD | L2_ch224:256 | remove_top_particle | 1 | -25.8225 | [0] |
| 197 | label_Hqql | label_Tbl | label_QCD | L2_ch224:256 | remove_knn_neighbors | 1 | -26.6623 | [0, 10, 18, 23, 25, 35, 43, 60, 68, 75, 85, 93, 100, 110, 118, 125] |
| 197 | label_Hqql | label_Tbl | label_QCD | L2_ch224:256 | remove_top_plus_knn | 1 | -26.6623 | [0, 10, 18, 23, 25, 35, 43, 60, 68, 75, 85, 93, 100, 110, 118, 125] |
| 197 | label_Hqql | label_Tbl | label_Hqql | L2_ch224:256 | random_same_count | 1 | 0.3532 | [1, 2, 3, 4, 6, 7, 9, 11, 12, 13, 14, 15, 16, 19, 20, 22] |
| 197 | label_Hqql | label_Tbl | label_QCD | L2_ch128:160 | remove_top_particle | 1 | -25.8225 | [0] |
| 197 | label_Hqql | label_Tbl | label_QCD | L2_ch128:160 | remove_knn_neighbors | 1 | -26.6623 | [0, 10, 18, 23, 25, 35, 43, 60, 68, 75, 85, 93, 100, 110, 118, 125] |
| 197 | label_Hqql | label_Tbl | label_QCD | L2_ch128:160 | remove_top_plus_knn | 1 | -26.6623 | [0, 10, 18, 23, 25, 35, 43, 60, 68, 75, 85, 93, 100, 110, 118, 125] |
| 197 | label_Hqql | label_Tbl | label_Hqql | L2_ch128:160 | random_same_count | 1 | 0.3182 | [1, 2, 3, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 20, 21, 24] |
| 197 | label_Hqql | label_Tbl | label_QCD | L2_ch32:64 | remove_top_particle | 1 | -25.8225 | [0] |
| 197 | label_Hqql | label_Tbl | label_QCD | L2_ch32:64 | remove_knn_neighbors | 1 | -26.6623 | [0, 10, 18, 23, 25, 35, 43, 60, 68, 75, 85, 93, 100, 110, 118, 125] |
| 197 | label_Hqql | label_Tbl | label_QCD | L2_ch32:64 | remove_top_plus_knn | 1 | -26.6623 | [0, 10, 18, 23, 25, 35, 43, 60, 68, 75, 85, 93, 100, 110, 118, 125] |
| 197 | label_Hqql | label_Tbl | label_Tbl | L2_ch32:64 | random_same_count | 0 | 0.8904 | [1, 2, 3, 4, 5, 7, 8, 11, 12, 13, 14, 15, 16, 17, 19, 24] |
| 197 | label_Hqql | label_Tbl | label_QCD | L2_ch0:32 | remove_top_particle | 1 | -25.8225 | [0] |
| 197 | label_Hqql | label_Tbl | label_QCD | L2_ch0:32 | remove_knn_neighbors | 1 | -26.6623 | [0, 10, 18, 23, 25, 35, 43, 60, 68, 75, 85, 93, 100, 110, 118, 125] |
| 197 | label_Hqql | label_Tbl | label_QCD | L2_ch0:32 | remove_top_plus_knn | 1 | -26.6623 | [0, 10, 18, 23, 25, 35, 43, 60, 68, 75, 85, 93, 100, 110, 118, 125] |
| 197 | label_Hqql | label_Tbl | label_Hqql | L2_ch0:32 | random_same_count | 1 | -0.2757 | [1, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 17, 19, 20, 21, 22] |
| 369 | label_Tbl | label_Tbl | label_Hcc | L2_ch224:256 | remove_top_particle | 1 | -15.3691 | [0] |
| 369 | label_Tbl | label_Tbl | label_Hcc | L2_ch224:256 | remove_knn_neighbors | 1 | -15.9132 | [0, 8, 14, 24, 31, 44, 50, 60, 67, 72, 80, 86, 96, 103, 108, 116] |
| 369 | label_Tbl | label_Tbl | label_Hcc | L2_ch224:256 | remove_top_plus_knn | 1 | -15.9132 | [0, 8, 14, 24, 31, 44, 50, 60, 67, 72, 80, 86, 96, 103, 108, 116] |
| 369 | label_Tbl | label_Tbl | label_Tbl | L2_ch224:256 | random_same_count | 0 | 1.1683 | [2, 3, 6, 10, 12, 13, 15, 16, 18, 19, 21, 23, 26, 27, 28, 30] |
| 369 | label_Tbl | label_Tbl | label_Hcc | L2_ch128:160 | remove_top_particle | 1 | -15.3691 | [0] |
| 369 | label_Tbl | label_Tbl | label_Hcc | L2_ch128:160 | remove_knn_neighbors | 1 | -15.9132 | [0, 8, 14, 24, 31, 44, 50, 60, 67, 72, 80, 86, 96, 103, 108, 116] |
| 369 | label_Tbl | label_Tbl | label_Hcc | L2_ch128:160 | remove_top_plus_knn | 1 | -15.9132 | [0, 8, 14, 24, 31, 44, 50, 60, 67, 72, 80, 86, 96, 103, 108, 116] |
| 369 | label_Tbl | label_Tbl | label_Tbl | L2_ch128:160 | random_same_count | 0 | 0.3766 | [1, 3, 7, 9, 12, 13, 15, 17, 21, 22, 23, 27, 28, 30, 32, 33] |
| 369 | label_Tbl | label_Tbl | label_Hcc | L2_ch32:64 | remove_top_particle | 1 | -15.3691 | [0] |
| 369 | label_Tbl | label_Tbl | label_Hcc | L2_ch32:64 | remove_knn_neighbors | 1 | -15.9132 | [0, 8, 14, 24, 31, 44, 50, 60, 67, 72, 80, 86, 96, 103, 108, 116] |
| 369 | label_Tbl | label_Tbl | label_Hcc | L2_ch32:64 | remove_top_plus_knn | 1 | -15.9132 | [0, 8, 14, 24, 31, 44, 50, 60, 67, 72, 80, 86, 96, 103, 108, 116] |
| 369 | label_Tbl | label_Tbl | label_Tbl | L2_ch32:64 | random_same_count | 0 | 0.1927 | [2, 5, 6, 9, 11, 15, 17, 18, 19, 20, 23, 27, 29, 30, 33, 35] |
| 369 | label_Tbl | label_Tbl | label_Hcc | L2_ch0:32 | remove_top_particle | 1 | -15.3691 | [0] |
| 369 | label_Tbl | label_Tbl | label_Hcc | L2_ch0:32 | remove_knn_neighbors | 1 | -15.9132 | [0, 8, 14, 24, 31, 44, 50, 60, 67, 72, 80, 86, 96, 103, 108, 116] |
| 369 | label_Tbl | label_Tbl | label_Hcc | L2_ch0:32 | remove_top_plus_knn | 1 | -15.9132 | [0, 8, 14, 24, 31, 44, 50, 60, 67, 72, 80, 86, 96, 103, 108, 116] |
| 369 | label_Tbl | label_Tbl | label_Tbl | L2_ch0:32 | random_same_count | 0 | -1.1231 | [1, 2, 3, 4, 5, 7, 10, 13, 16, 17, 22, 26, 27, 28, 32, 34] |
| 355 | label_Tbl | label_Tbl | label_Tbqq | L2_ch224:256 | remove_top_particle | 1 | -36.0323 | [0] |
| 355 | label_Tbl | label_Tbl | label_Tbqq | L2_ch224:256 | remove_knn_neighbors | 1 | -37.9889 | [0, 15, 17, 18, 33, 35, 36, 53, 71, 72, 89, 90, 107, 108, 125, 126] |
| 355 | label_Tbl | label_Tbl | label_Tbqq | L2_ch224:256 | remove_top_plus_knn | 1 | -37.9889 | [0, 15, 17, 18, 33, 35, 36, 53, 71, 72, 89, 90, 107, 108, 125, 126] |
| 355 | label_Tbl | label_Tbl | label_Tbl | L2_ch224:256 | random_same_count | 0 | -2.0430 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16] |
| 355 | label_Tbl | label_Tbl | label_Tbqq | L2_ch128:160 | remove_top_particle | 1 | -36.0323 | [0] |
| 355 | label_Tbl | label_Tbl | label_Tbqq | L2_ch128:160 | remove_knn_neighbors | 1 | -37.9889 | [0, 15, 17, 18, 33, 35, 36, 53, 71, 72, 89, 90, 107, 108, 125, 126] |
| 355 | label_Tbl | label_Tbl | label_Tbqq | L2_ch128:160 | remove_top_plus_knn | 1 | -37.9889 | [0, 15, 17, 18, 33, 35, 36, 53, 71, 72, 89, 90, 107, 108, 125, 126] |
| 355 | label_Tbl | label_Tbl | label_Tbl | L2_ch128:160 | random_same_count | 0 | -2.0430 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16] |
| 355 | label_Tbl | label_Tbl | label_Tbqq | L2_ch32:64 | remove_top_particle | 1 | -36.0323 | [0] |
| 355 | label_Tbl | label_Tbl | label_Tbqq | L2_ch32:64 | remove_knn_neighbors | 1 | -37.9889 | [0, 15, 17, 18, 33, 35, 36, 53, 71, 72, 89, 90, 107, 108, 125, 126] |
| 355 | label_Tbl | label_Tbl | label_Tbqq | L2_ch32:64 | remove_top_plus_knn | 1 | -37.9889 | [0, 15, 17, 18, 33, 35, 36, 53, 71, 72, 89, 90, 107, 108, 125, 126] |
| 355 | label_Tbl | label_Tbl | label_Tbl | L2_ch32:64 | random_same_count | 0 | -2.0430 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16] |
| 355 | label_Tbl | label_Tbl | label_Tbqq | L2_ch0:32 | remove_top_particle | 1 | -36.0323 | [0] |
| 355 | label_Tbl | label_Tbl | label_Tbqq | L2_ch0:32 | remove_knn_neighbors | 1 | -37.9889 | [0, 15, 17, 18, 33, 35, 36, 53, 71, 72, 89, 90, 107, 108, 125, 126] |
| 355 | label_Tbl | label_Tbl | label_Tbqq | L2_ch0:32 | remove_top_plus_knn | 1 | -37.9889 | [0, 15, 17, 18, 33, 35, 36, 53, 71, 72, 89, 90, 107, 108, 125, 126] |
| 355 | label_Tbl | label_Tbl | label_Tbl | L2_ch0:32 | random_same_count | 0 | -2.0430 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16] |
| 332 | label_Tbl | label_Tbl | label_Tbqq | L2_ch224:256 | remove_top_particle | 1 | -11.9286 | [0] |
| 332 | label_Tbl | label_Tbl | label_Tbl | L2_ch224:256 | remove_knn_neighbors | 0 | -0.7436 | [1, 3, 11, 24, 39, 53, 63, 67, 70, 74, 76, 77, 79, 87, 100, 115] |
| 332 | label_Tbl | label_Tbl | label_H4q | L2_ch224:256 | remove_top_plus_knn | 1 | -12.7244 | [0, 1, 3, 11, 24, 39, 53, 63, 67, 70, 74, 76, 77, 79, 87, 100, 115] |
| 332 | label_Tbl | label_Tbl | label_Tbl | L2_ch224:256 | random_same_count | 0 | 0.3152 | [6, 9, 12, 14, 18, 25, 26, 28, 37, 38, 40, 41, 52, 61, 62, 65, 71] |
| 332 | label_Tbl | label_Tbl | label_Tbqq | L2_ch128:160 | remove_top_particle | 1 | -11.9286 | [0] |
| 332 | label_Tbl | label_Tbl | label_Tbl | L2_ch128:160 | remove_knn_neighbors | 0 | -0.7436 | [1, 3, 11, 24, 39, 53, 63, 67, 70, 74, 76, 77, 79, 87, 100, 115] |
| 332 | label_Tbl | label_Tbl | label_H4q | L2_ch128:160 | remove_top_plus_knn | 1 | -12.7244 | [0, 1, 3, 11, 24, 39, 53, 63, 67, 70, 74, 76, 77, 79, 87, 100, 115] |
| 332 | label_Tbl | label_Tbl | label_Tbl | L2_ch128:160 | random_same_count | 0 | -2.0189 | [5, 8, 15, 16, 17, 19, 20, 21, 25, 30, 37, 49, 57, 59, 64, 68, 69] |
| 332 | label_Tbl | label_Tbl | label_Tbqq | L2_ch32:64 | remove_top_particle | 1 | -11.9286 | [0] |
| 332 | label_Tbl | label_Tbl | label_Tbl | L2_ch32:64 | remove_knn_neighbors | 0 | -0.7436 | [1, 3, 11, 24, 39, 53, 63, 67, 70, 74, 76, 77, 79, 87, 100, 115] |
| 332 | label_Tbl | label_Tbl | label_H4q | L2_ch32:64 | remove_top_plus_knn | 1 | -12.7244 | [0, 1, 3, 11, 24, 39, 53, 63, 67, 70, 74, 76, 77, 79, 87, 100, 115] |
| 332 | label_Tbl | label_Tbl | label_Tbl | L2_ch32:64 | random_same_count | 0 | -0.8634 | [5, 8, 12, 18, 21, 25, 26, 29, 35, 40, 41, 42, 44, 58, 59, 60, 68] |
| 332 | label_Tbl | label_Tbl | label_Tbqq | L2_ch0:32 | remove_top_particle | 1 | -11.9286 | [0] |
| 332 | label_Tbl | label_Tbl | label_Tbl | L2_ch0:32 | remove_knn_neighbors | 0 | -0.7436 | [1, 3, 11, 24, 39, 53, 63, 67, 70, 74, 76, 77, 79, 87, 100, 115] |
| 332 | label_Tbl | label_Tbl | label_H4q | L2_ch0:32 | remove_top_plus_knn | 1 | -12.7244 | [0, 1, 3, 11, 24, 39, 53, 63, 67, 70, 74, 76, 77, 79, 87, 100, 115] |
| 332 | label_Tbl | label_Tbl | label_Tbl | L2_ch0:32 | random_same_count | 0 | -0.4038 | [4, 12, 18, 20, 26, 30, 36, 37, 42, 45, 51, 56, 57, 60, 62, 66, 73] |
| 323 | label_Tbl | label_Tbl | label_QCD | L2_ch224:256 | remove_top_particle | 1 | -19.7870 | [0] |
| 323 | label_Tbl | label_Tbl | label_QCD | L2_ch224:256 | remove_knn_neighbors | 1 | -20.9801 | [0, 16, 20, 26, 30, 46, 50, 56, 76, 80, 86, 90, 106, 110, 116, 120] |
| 323 | label_Tbl | label_Tbl | label_QCD | L2_ch224:256 | remove_top_plus_knn | 1 | -20.9801 | [0, 16, 20, 26, 30, 46, 50, 56, 76, 80, 86, 90, 106, 110, 116, 120] |
| 323 | label_Tbl | label_Tbl | label_Tbl | L2_ch224:256 | random_same_count | 0 | 2.0464 | [1, 2, 4, 6, 7, 11, 12, 15, 17, 18, 21, 22, 23, 24, 27, 29] |
| 323 | label_Tbl | label_Tbl | label_QCD | L2_ch128:160 | remove_top_particle | 1 | -19.7870 | [0] |
| 323 | label_Tbl | label_Tbl | label_QCD | L2_ch128:160 | remove_knn_neighbors | 1 | -20.9801 | [0, 16, 20, 26, 30, 46, 50, 56, 76, 80, 86, 90, 106, 110, 116, 120] |
| 323 | label_Tbl | label_Tbl | label_QCD | L2_ch128:160 | remove_top_plus_knn | 1 | -20.9801 | [0, 16, 20, 26, 30, 46, 50, 56, 76, 80, 86, 90, 106, 110, 116, 120] |
| 323 | label_Tbl | label_Tbl | label_Tbl | L2_ch128:160 | random_same_count | 0 | 2.4798 | [2, 3, 6, 7, 9, 11, 13, 14, 15, 17, 19, 22, 23, 24, 28, 29] |
| 323 | label_Tbl | label_Tbl | label_QCD | L2_ch32:64 | remove_top_particle | 1 | -19.7870 | [0] |
| 323 | label_Tbl | label_Tbl | label_QCD | L2_ch32:64 | remove_knn_neighbors | 1 | -20.9801 | [0, 16, 20, 26, 30, 46, 50, 56, 76, 80, 86, 90, 106, 110, 116, 120] |
| 323 | label_Tbl | label_Tbl | label_QCD | L2_ch32:64 | remove_top_plus_knn | 1 | -20.9801 | [0, 16, 20, 26, 30, 46, 50, 56, 76, 80, 86, 90, 106, 110, 116, 120] |
| 323 | label_Tbl | label_Tbl | label_Tbl | L2_ch32:64 | random_same_count | 0 | 2.3876 | [2, 3, 4, 5, 6, 8, 9, 10, 11, 13, 18, 19, 21, 22, 24, 28] |
| 323 | label_Tbl | label_Tbl | label_QCD | L2_ch0:32 | remove_top_particle | 1 | -19.7870 | [0] |
| 323 | label_Tbl | label_Tbl | label_QCD | L2_ch0:32 | remove_knn_neighbors | 1 | -20.9801 | [0, 16, 20, 26, 30, 46, 50, 56, 76, 80, 86, 90, 106, 110, 116, 120] |
| 323 | label_Tbl | label_Tbl | label_QCD | L2_ch0:32 | remove_top_plus_knn | 1 | -20.9801 | [0, 16, 20, 26, 30, 46, 50, 56, 76, 80, 86, 90, 106, 110, 116, 120] |
| 323 | label_Tbl | label_Tbl | label_Tbl | L2_ch0:32 | random_same_count | 0 | 2.5904 | [1, 2, 3, 6, 8, 9, 12, 14, 15, 21, 23, 24, 25, 27, 28, 29] |
| 334 | label_Tbl | label_Tbl | label_QCD | L2_ch224:256 | remove_top_particle | 1 | -21.2143 | [0] |
| 334 | label_Tbl | label_Tbl | label_Hbb | L2_ch224:256 | remove_knn_neighbors | 1 | -22.6387 | [0, 8, 9, 21, 24, 32, 45, 56, 69, 72, 80, 93, 96, 104, 117, 120] |
| 334 | label_Tbl | label_Tbl | label_Hbb | L2_ch224:256 | remove_top_plus_knn | 1 | -22.6387 | [0, 8, 9, 21, 24, 32, 45, 56, 69, 72, 80, 93, 96, 104, 117, 120] |
| 334 | label_Tbl | label_Tbl | label_Tbl | L2_ch224:256 | random_same_count | 0 | 1.4809 | [1, 2, 3, 4, 5, 6, 7, 10, 11, 14, 15, 16, 17, 18, 20, 22] |
| 334 | label_Tbl | label_Tbl | label_QCD | L2_ch128:160 | remove_top_particle | 1 | -21.2143 | [0] |
| 334 | label_Tbl | label_Tbl | label_Hbb | L2_ch128:160 | remove_knn_neighbors | 1 | -22.6387 | [0, 8, 9, 21, 24, 32, 45, 56, 69, 72, 80, 93, 96, 104, 117, 120] |
| 334 | label_Tbl | label_Tbl | label_Hbb | L2_ch128:160 | remove_top_plus_knn | 1 | -22.6387 | [0, 8, 9, 21, 24, 32, 45, 56, 69, 72, 80, 93, 96, 104, 117, 120] |
| 334 | label_Tbl | label_Tbl | label_Tbl | L2_ch128:160 | random_same_count | 0 | 1.0617 | [1, 2, 3, 5, 6, 7, 10, 12, 13, 14, 15, 17, 18, 19, 22, 23] |
| 334 | label_Tbl | label_Tbl | label_QCD | L2_ch32:64 | remove_top_particle | 1 | -21.2143 | [0] |
| 334 | label_Tbl | label_Tbl | label_Hbb | L2_ch32:64 | remove_knn_neighbors | 1 | -22.6387 | [0, 8, 9, 21, 24, 32, 45, 56, 69, 72, 80, 93, 96, 104, 117, 120] |
| 334 | label_Tbl | label_Tbl | label_Hbb | L2_ch32:64 | remove_top_plus_knn | 1 | -22.6387 | [0, 8, 9, 21, 24, 32, 45, 56, 69, 72, 80, 93, 96, 104, 117, 120] |
| 334 | label_Tbl | label_Tbl | label_Tbl | L2_ch32:64 | random_same_count | 0 | 2.0233 | [2, 3, 4, 5, 6, 7, 10, 11, 12, 14, 15, 17, 18, 19, 20, 23] |
| 334 | label_Tbl | label_Tbl | label_QCD | L2_ch0:32 | remove_top_particle | 1 | -21.2143 | [0] |
| 334 | label_Tbl | label_Tbl | label_Hbb | L2_ch0:32 | remove_knn_neighbors | 1 | -22.6387 | [0, 8, 9, 21, 24, 32, 45, 56, 69, 72, 80, 93, 96, 104, 117, 120] |
| 334 | label_Tbl | label_Tbl | label_Hbb | L2_ch0:32 | remove_top_plus_knn | 1 | -22.6387 | [0, 8, 9, 21, 24, 32, 45, 56, 69, 72, 80, 93, 96, 104, 117, 120] |
| 334 | label_Tbl | label_Tbl | label_Hqql | L2_ch0:32 | random_same_count | 1 | 1.3776 | [1, 2, 3, 4, 5, 7, 10, 11, 12, 13, 15, 16, 17, 19, 22, 23] |
| 340 | label_Tbl | label_Tbl | label_Tbqq | L2_ch224:256 | remove_top_particle | 1 | -21.5130 | [0] |
| 340 | label_Tbl | label_Tbl | label_Tbqq | L2_ch224:256 | remove_knn_neighbors | 1 | -24.8617 | [0, 11, 18, 30, 34, 38, 51, 58, 70, 78, 80, 91, 98, 110, 118, 120] |
| 340 | label_Tbl | label_Tbl | label_Tbqq | L2_ch224:256 | remove_top_plus_knn | 1 | -24.8617 | [0, 11, 18, 30, 34, 38, 51, 58, 70, 78, 80, 91, 98, 110, 118, 120] |
| 340 | label_Tbl | label_Tbl | label_Tbl | L2_ch224:256 | random_same_count | 0 | -3.2811 | [2, 3, 4, 5, 7, 8, 13, 14, 17, 19, 26, 27, 28, 31, 32, 37] |
| 340 | label_Tbl | label_Tbl | label_Tbqq | L2_ch128:160 | remove_top_particle | 1 | -21.5130 | [0] |
| 340 | label_Tbl | label_Tbl | label_Tbqq | L2_ch128:160 | remove_knn_neighbors | 1 | -24.8617 | [0, 11, 18, 30, 34, 38, 51, 58, 70, 78, 80, 91, 98, 110, 118, 120] |
| 340 | label_Tbl | label_Tbl | label_Tbqq | L2_ch128:160 | remove_top_plus_knn | 1 | -24.8617 | [0, 11, 18, 30, 34, 38, 51, 58, 70, 78, 80, 91, 98, 110, 118, 120] |
| 340 | label_Tbl | label_Tbl | label_Tbl | L2_ch128:160 | random_same_count | 0 | -0.5336 | [1, 2, 4, 6, 8, 10, 12, 15, 20, 23, 24, 25, 26, 29, 37, 39] |
| 340 | label_Tbl | label_Tbl | label_Tbqq | L2_ch32:64 | remove_top_particle | 1 | -21.5130 | [0] |
| 340 | label_Tbl | label_Tbl | label_Tbqq | L2_ch32:64 | remove_knn_neighbors | 1 | -24.8617 | [0, 11, 18, 30, 34, 38, 51, 58, 70, 78, 80, 91, 98, 110, 118, 120] |
| 340 | label_Tbl | label_Tbl | label_Tbqq | L2_ch32:64 | remove_top_plus_knn | 1 | -24.8617 | [0, 11, 18, 30, 34, 38, 51, 58, 70, 78, 80, 91, 98, 110, 118, 120] |
| 340 | label_Tbl | label_Tbl | label_Tbl | L2_ch32:64 | random_same_count | 0 | 0.2172 | [1, 5, 8, 13, 14, 15, 16, 19, 21, 23, 25, 26, 28, 32, 35, 36] |
| 340 | label_Tbl | label_Tbl | label_Tbqq | L2_ch0:32 | remove_top_particle | 1 | -21.5130 | [0] |
| 340 | label_Tbl | label_Tbl | label_Tbqq | L2_ch0:32 | remove_knn_neighbors | 1 | -24.8617 | [0, 11, 18, 30, 34, 38, 51, 58, 70, 78, 80, 91, 98, 110, 118, 120] |
| 340 | label_Tbl | label_Tbl | label_Tbqq | L2_ch0:32 | remove_top_plus_knn | 1 | -24.8617 | [0, 11, 18, 30, 34, 38, 51, 58, 70, 78, 80, 91, 98, 110, 118, 120] |
| 340 | label_Tbl | label_Tbl | label_Tbl | L2_ch0:32 | random_same_count | 0 | -0.9662 | [2, 4, 5, 10, 13, 14, 16, 17, 25, 26, 27, 28, 31, 32, 33, 36] |
| 337 | label_Tbl | label_Tbl | label_Tbqq | L2_ch224:256 | remove_top_particle | 1 | -16.8353 | [0] |
| 337 | label_Tbl | label_Tbl | label_Tbqq | L2_ch224:256 | remove_knn_neighbors | 1 | -17.6942 | [0, 11, 18, 20, 31, 38, 40, 51, 58, 71, 78, 80, 91, 100, 111, 120] |
| 337 | label_Tbl | label_Tbl | label_Tbqq | L2_ch224:256 | remove_top_plus_knn | 1 | -17.6942 | [0, 11, 18, 20, 31, 38, 40, 51, 58, 71, 78, 80, 91, 100, 111, 120] |
| 337 | label_Tbl | label_Tbl | label_Tbl | L2_ch224:256 | random_same_count | 0 | 10.9334 | [1, 2, 3, 4, 5, 6, 7, 9, 10, 12, 13, 14, 15, 16, 17, 19] |
| 337 | label_Tbl | label_Tbl | label_Tbqq | L2_ch128:160 | remove_top_particle | 1 | -16.8353 | [0] |
| 337 | label_Tbl | label_Tbl | label_Tbqq | L2_ch128:160 | remove_knn_neighbors | 1 | -17.6942 | [0, 11, 18, 20, 31, 38, 40, 51, 58, 71, 78, 80, 91, 100, 111, 120] |
| 337 | label_Tbl | label_Tbl | label_Tbqq | L2_ch128:160 | remove_top_plus_knn | 1 | -17.6942 | [0, 11, 18, 20, 31, 38, 40, 51, 58, 71, 78, 80, 91, 100, 111, 120] |
| 337 | label_Tbl | label_Tbl | label_Tbl | L2_ch128:160 | random_same_count | 0 | 9.5873 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 16, 17, 19] |
| 337 | label_Tbl | label_Tbl | label_Tbqq | L2_ch32:64 | remove_top_particle | 1 | -16.8353 | [0] |
| 337 | label_Tbl | label_Tbl | label_Tbqq | L2_ch32:64 | remove_knn_neighbors | 1 | -17.6942 | [0, 11, 18, 20, 31, 38, 40, 51, 58, 71, 78, 80, 91, 100, 111, 120] |
| 337 | label_Tbl | label_Tbl | label_Tbqq | L2_ch32:64 | remove_top_plus_knn | 1 | -17.6942 | [0, 11, 18, 20, 31, 38, 40, 51, 58, 71, 78, 80, 91, 100, 111, 120] |
| 337 | label_Tbl | label_Tbl | label_Tbl | L2_ch32:64 | random_same_count | 0 | 8.7346 | [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 19] |
| 337 | label_Tbl | label_Tbl | label_Tbqq | L2_ch0:32 | remove_top_particle | 1 | -16.8353 | [0] |
| 337 | label_Tbl | label_Tbl | label_Tbqq | L2_ch0:32 | remove_knn_neighbors | 1 | -17.6942 | [0, 11, 18, 20, 31, 38, 40, 51, 58, 71, 78, 80, 91, 100, 111, 120] |
| 337 | label_Tbl | label_Tbl | label_Tbqq | L2_ch0:32 | remove_top_plus_knn | 1 | -17.6942 | [0, 11, 18, 20, 31, 38, 40, 51, 58, 71, 78, 80, 91, 100, 111, 120] |
| 337 | label_Tbl | label_Tbl | label_Tbl | L2_ch0:32 | random_same_count | 0 | 12.0533 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 19] |
| 327 | label_Tbl | label_Tbl | label_Hbb | L2_ch224:256 | remove_top_particle | 1 | -24.4623 | [0] |
| 327 | label_Tbl | label_Tbl | label_Hbb | L2_ch224:256 | remove_knn_neighbors | 1 | -27.5753 | [0, 19, 23, 30, 31, 50, 54, 61, 81, 85, 92, 93, 112, 116, 123, 124] |
| 327 | label_Tbl | label_Tbl | label_Hbb | L2_ch224:256 | remove_top_plus_knn | 1 | -27.5753 | [0, 19, 23, 30, 31, 50, 54, 61, 81, 85, 92, 93, 112, 116, 123, 124] |
| 327 | label_Tbl | label_Tbl | label_Tbl | L2_ch224:256 | random_same_count | 0 | 4.6735 | [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 14, 16, 17, 18, 25, 28] |
| 327 | label_Tbl | label_Tbl | label_Hbb | L2_ch128:160 | remove_top_particle | 1 | -24.4623 | [0] |
| 327 | label_Tbl | label_Tbl | label_Hbb | L2_ch128:160 | remove_knn_neighbors | 1 | -27.5753 | [0, 19, 23, 30, 31, 50, 54, 61, 81, 85, 92, 93, 112, 116, 123, 124] |
| 327 | label_Tbl | label_Tbl | label_Hbb | L2_ch128:160 | remove_top_plus_knn | 1 | -27.5753 | [0, 19, 23, 30, 31, 50, 54, 61, 81, 85, 92, 93, 112, 116, 123, 124] |
| 327 | label_Tbl | label_Tbl | label_Tbl | L2_ch128:160 | random_same_count | 0 | 1.3544 | [1, 2, 3, 5, 7, 10, 11, 12, 14, 17, 20, 21, 24, 25, 26, 27] |
| 327 | label_Tbl | label_Tbl | label_Hbb | L2_ch32:64 | remove_top_particle | 1 | -24.4623 | [0] |
| 327 | label_Tbl | label_Tbl | label_Hbb | L2_ch32:64 | remove_knn_neighbors | 1 | -27.5753 | [0, 19, 23, 30, 31, 50, 54, 61, 81, 85, 92, 93, 112, 116, 123, 124] |
| 327 | label_Tbl | label_Tbl | label_Hbb | L2_ch32:64 | remove_top_plus_knn | 1 | -27.5753 | [0, 19, 23, 30, 31, 50, 54, 61, 81, 85, 92, 93, 112, 116, 123, 124] |
| 327 | label_Tbl | label_Tbl | label_Tbl | L2_ch32:64 | random_same_count | 0 | 4.9770 | [3, 4, 5, 7, 8, 11, 12, 13, 15, 17, 18, 21, 22, 24, 25, 29] |
| 327 | label_Tbl | label_Tbl | label_Hbb | L2_ch0:32 | remove_top_particle | 1 | -24.4623 | [0] |
| 327 | label_Tbl | label_Tbl | label_Hbb | L2_ch0:32 | remove_knn_neighbors | 1 | -27.5753 | [0, 19, 23, 30, 31, 50, 54, 61, 81, 85, 92, 93, 112, 116, 123, 124] |
| 327 | label_Tbl | label_Tbl | label_Hbb | L2_ch0:32 | remove_top_plus_knn | 1 | -27.5753 | [0, 19, 23, 30, 31, 50, 54, 61, 81, 85, 92, 93, 112, 116, 123, 124] |
| 327 | label_Tbl | label_Tbl | label_Tbl | L2_ch0:32 | random_same_count | 0 | 2.6600 | [1, 2, 3, 6, 7, 9, 10, 12, 13, 17, 18, 20, 22, 24, 26, 28] |
| 376 | label_Tbl | label_Tbl | label_QCD | L2_ch224:256 | remove_top_particle | 1 | -17.4169 | [0] |
| 376 | label_Tbl | label_Tbl | label_QCD | L2_ch224:256 | remove_knn_neighbors | 1 | -18.5951 | [0, 11, 23, 24, 29, 45, 57, 58, 63, 68, 79, 92, 97, 102, 113, 126] |
| 376 | label_Tbl | label_Tbl | label_QCD | L2_ch224:256 | remove_top_plus_knn | 1 | -18.5951 | [0, 11, 23, 24, 29, 45, 57, 58, 63, 68, 79, 92, 97, 102, 113, 126] |
| 376 | label_Tbl | label_Tbl | label_Tbl | L2_ch224:256 | random_same_count | 0 | 2.2621 | [2, 3, 4, 5, 9, 12, 13, 15, 18, 21, 26, 28, 30, 31, 32, 33] |
| 376 | label_Tbl | label_Tbl | label_QCD | L2_ch128:160 | remove_top_particle | 1 | -17.4169 | [0] |
| 376 | label_Tbl | label_Tbl | label_QCD | L2_ch128:160 | remove_knn_neighbors | 1 | -18.5951 | [0, 11, 23, 24, 29, 45, 57, 58, 63, 68, 79, 92, 97, 102, 113, 126] |
| 376 | label_Tbl | label_Tbl | label_QCD | L2_ch128:160 | remove_top_plus_knn | 1 | -18.5951 | [0, 11, 23, 24, 29, 45, 57, 58, 63, 68, 79, 92, 97, 102, 113, 126] |
| 376 | label_Tbl | label_Tbl | label_Tbl | L2_ch128:160 | random_same_count | 0 | -3.2902 | [1, 3, 4, 7, 8, 10, 12, 15, 16, 19, 22, 25, 27, 30, 31, 33] |
| 376 | label_Tbl | label_Tbl | label_QCD | L2_ch32:64 | remove_top_particle | 1 | -17.4169 | [0] |
| 376 | label_Tbl | label_Tbl | label_QCD | L2_ch32:64 | remove_knn_neighbors | 1 | -18.5951 | [0, 11, 23, 24, 29, 45, 57, 58, 63, 68, 79, 92, 97, 102, 113, 126] |
| 376 | label_Tbl | label_Tbl | label_QCD | L2_ch32:64 | remove_top_plus_knn | 1 | -18.5951 | [0, 11, 23, 24, 29, 45, 57, 58, 63, 68, 79, 92, 97, 102, 113, 126] |
| 376 | label_Tbl | label_Tbl | label_Tbl | L2_ch32:64 | random_same_count | 0 | -1.7473 | [1, 3, 5, 6, 7, 8, 9, 13, 14, 15, 17, 25, 26, 28, 31, 33] |
| 376 | label_Tbl | label_Tbl | label_QCD | L2_ch0:32 | remove_top_particle | 1 | -17.4169 | [0] |
| 376 | label_Tbl | label_Tbl | label_QCD | L2_ch0:32 | remove_knn_neighbors | 1 | -18.5951 | [0, 11, 23, 24, 29, 45, 57, 58, 63, 68, 79, 92, 97, 102, 113, 126] |
| 376 | label_Tbl | label_Tbl | label_QCD | L2_ch0:32 | remove_top_plus_knn | 1 | -18.5951 | [0, 11, 23, 24, 29, 45, 57, 58, 63, 68, 79, 92, 97, 102, 113, 126] |
| 376 | label_Tbl | label_Tbl | label_Tbl | L2_ch0:32 | random_same_count | 0 | 1.7786 | [1, 2, 3, 4, 5, 6, 7, 9, 10, 14, 15, 16, 20, 28, 30, 33] |

## Interpretation

Compare targeted remove_top/knn/top_plus_knn against random_same_count. Strong support means targeted route patch flips or reduces baseline logit more than random.
