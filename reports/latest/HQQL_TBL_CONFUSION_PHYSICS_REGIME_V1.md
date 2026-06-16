# Hqql/Tbl Confusion Physics Regime v1

This report asks what particle0/leading/core physically is in Hqql/Tbl confusion regimes. Forward and KNN are microbatched for large Phase 1 runs.

## Group summary
| group | n | particle0_pid_modes | p0_lepton | p0_iso | has_lepton | lead_pid_modes | lead_lepton | missing_pt |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hqql_correct | 968 | muon:346, electron:343, charged_hadron:130, photon:86, neutral_hadron:63 | 0.7118 | 0.1582 | 0.9928 | muon:346, electron:343, charged_hadron:130, photon:86, neutral_hadron:63 | 0.7118 | 620.7088 |
| Hqql_to_Tbl | 35 | electron:21, muon:10, photon:2, neutral_hadron:1, charged_hadron:1 | 0.8857 | 0.2075 | 1.0000 | electron:21, muon:10, photon:2, neutral_hadron:1, charged_hadron:1 | 0.8857 | 596.3925 |
| Tbl_correct | 978 | muon:406, electron:400, charged_hadron:69, photon:60, neutral_hadron:43 | 0.8241 | 0.1684 | 0.9969 | muon:406, electron:400, charged_hadron:69, photon:60, neutral_hadron:43 | 0.8241 | 597.3284 |
| Tbl_to_Hqql | 43 | electron:16, muon:15, photon:6, charged_hadron:4, neutral_hadron:2 | 0.7209 | 0.1661 | 1.0000 | electron:16, muon:15, photon:6, charged_hadron:4, neutral_hadron:2 | 0.7209 | 597.0910 |

## Event examples
| event | group | true | pred | conf | p0_pid | p0_pt | p0_rank | p0_lep | lead_pid | lead_lep | has_lep | best_lep_iso |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3072 | Hqql_correct | label_Hqql | label_Hqql | 0.9999 | muon | 138.1330 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1589 |
| 3073 | Hqql_correct | label_Hqql | label_Hqql | 0.9978 | electron | 186.8828 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1700 |
| 3074 | Hqql_correct | label_Hqql | label_Hqql | 0.7015 | electron | 135.6346 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1239 |
| 3075 | Hqql_correct | label_Hqql | label_Hqql | 0.9965 | electron | 185.7713 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1218 |
| 3076 | Hqql_correct | label_Hqql | label_Hqql | 0.9964 | muon | 134.5411 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1255 |
| 3077 | Hqql_to_Tbl | label_Hqql | label_Tbl | 0.9905 | electron | 420.1024 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1652 |
| 3078 | Hqql_correct | label_Hqql | label_Hqql | 0.9999 | muon | 445.1895 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1885 |
| 3079 | Hqql_correct | label_Hqql | label_Hqql | 0.9994 | charged_hadron | 195.5860 | 0 | 0.0000 | charged_hadron | 0.0000 | 1 | 0.1465 |
| 3080 | Hqql_correct | label_Hqql | label_Hqql | 0.9744 | electron | 321.0246 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.2247 |
| 3081 | Hqql_correct | label_Hqql | label_Hqql | 0.9413 | muon | 269.7216 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1967 |
| 3082 | Hqql_to_Tbl | label_Hqql | label_Tbl | 0.8791 | electron | 153.0558 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.0893 |
| 3083 | Hqql_correct | label_Hqql | label_Hqql | 0.6420 | electron | 245.8136 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.2876 |
| 3084 | Hqql_correct | label_Hqql | label_Hqql | 0.9976 | muon | 97.4305 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1452 |
| 3085 | Hqql_correct | label_Hqql | label_Hqql | 0.9997 | electron | 393.9726 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1362 |
| 3086 | Hqql_correct | label_Hqql | label_Hqql | 0.9730 | charged_hadron | 132.3570 | 0 | 0.0000 | charged_hadron | 0.0000 | 1 | 0.2110 |
| 3087 | Hqql_correct | label_Hqql | label_Hqql | 0.9983 | charged_hadron | 150.2936 | 0 | 0.0000 | charged_hadron | 0.0000 | 1 | 0.1510 |
| 3088 | Hqql_correct | label_Hqql | label_Hqql | 0.9505 | electron | 526.1700 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1651 |
| 3089 | Hqql_correct | label_Hqql | label_Hqql | 0.9904 | muon | 290.4164 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1577 |
| 3090 | Hqql_correct | label_Hqql | label_Hqql | 0.9977 | electron | 380.5297 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1876 |
| 3091 | Hqql_correct | label_Hqql | label_Hqql | 0.9898 | neutral_hadron | 125.7162 | 0 | 0.0000 | neutral_hadron | 0.0000 | 1 | 0.0783 |
| 3092 | Hqql_correct | label_Hqql | label_Hqql | 0.6363 | electron | 210.9155 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.3043 |
| 3093 | Hqql_correct | label_Hqql | label_Hqql | 0.9943 | electron | 326.9661 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1076 |
| 3094 | Hqql_correct | label_Hqql | label_Hqql | 0.9993 | muon | 524.3685 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1230 |
| 3095 | Hqql_correct | label_Hqql | label_Hqql | 0.9956 | charged_hadron | 151.2202 | 0 | 0.0000 | charged_hadron | 0.0000 | 1 | 0.1517 |
| 3096 | Hqql_correct | label_Hqql | label_Hqql | 0.9901 | photon | 98.5999 | 0 | 0.0000 | photon | 0.0000 | 1 | 0.1675 |
| 3097 | Hqql_correct | label_Hqql | label_Hqql | 0.9996 | electron | 372.7248 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.2192 |
| 3098 | Hqql_correct | label_Hqql | label_Hqql | 1.0000 | photon | 203.4302 | 0 | 0.0000 | photon | 0.0000 | 1 | 0.0864 |
| 3099 | Hqql_correct | label_Hqql | label_Hqql | 1.0000 | electron | 378.6483 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.0986 |
| 3100 | Hqql_correct | label_Hqql | label_Hqql | 0.9999 | muon | 316.2993 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1228 |
| 3101 | Hqql_correct | label_Hqql | label_Hqql | 1.0000 | electron | 423.7215 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1386 |
| 3102 | Hqql_correct | label_Hqql | label_Hqql | 0.9999 | charged_hadron | 183.7744 | 0 | 0.0000 | charged_hadron | 0.0000 | 1 | 0.1698 |
| 3103 | Hqql_correct | label_Hqql | label_Hqql | 0.9984 | muon | 426.8395 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.2323 |
| 3104 | Hqql_correct | label_Hqql | label_Hqql | 1.0000 | muon | 194.7510 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1550 |
| 3105 | Hqql_correct | label_Hqql | label_Hqql | 0.9995 | electron | 218.8318 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.2348 |
| 3106 | Hqql_correct | label_Hqql | label_Hqql | 0.9718 | muon | 229.4073 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1773 |
| 3107 | Hqql_correct | label_Hqql | label_Hqql | 0.9994 | electron | 156.0907 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1025 |
| 3108 | Hqql_correct | label_Hqql | label_Hqql | 0.9999 | photon | 131.9997 | 0 | 0.0000 | photon | 0.0000 | 1 | 0.0955 |
| 3109 | Hqql_correct | label_Hqql | label_Hqql | 0.9985 | muon | 166.6381 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1883 |
| 3110 | Hqql_correct | label_Hqql | label_Hqql | 0.6425 | charged_hadron | 111.9360 | 0 | 0.0000 | charged_hadron | 0.0000 | 1 | 0.1720 |
| 3111 | Hqql_correct | label_Hqql | label_Hqql | 0.9159 | charged_hadron | 208.3672 | 0 | 0.0000 | charged_hadron | 0.0000 | 1 | 0.1492 |
| 3112 | Hqql_correct | label_Hqql | label_Hqql | 0.5396 | electron | 226.8067 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1682 |
| 3113 | Hqql_correct | label_Hqql | label_Hqql | 0.9981 | muon | 345.6596 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.2020 |
| 3114 | Hqql_correct | label_Hqql | label_Hqql | 0.9612 | muon | 382.8791 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1815 |
| 3115 | Hqql_correct | label_Hqql | label_Hqql | 0.8661 | neutral_hadron | 94.6467 | 0 | 0.0000 | neutral_hadron | 0.0000 | 1 | 0.1781 |
| 3116 | Hqql_correct | label_Hqql | label_Hqql | 0.9531 | muon | 256.5991 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1581 |
| 3117 | Hqql_correct | label_Hqql | label_Hqql | 0.9999 | muon | 213.5150 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1104 |
| 3118 | Hqql_correct | label_Hqql | label_Hqql | 0.9837 | neutral_hadron | 146.9194 | 0 | 0.0000 | neutral_hadron | 0.0000 | 1 | 0.1832 |
| 3119 | Hqql_correct | label_Hqql | label_Hqql | 0.9993 | muon | 206.0280 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.2133 |
| 3121 | Hqql_correct | label_Hqql | label_Hqql | 0.9996 | muon | 300.9614 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1534 |
| 3122 | Hqql_correct | label_Hqql | label_Hqql | 0.9730 | electron | 468.0427 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1133 |
| 3123 | Hqql_correct | label_Hqql | label_Hqql | 0.9996 | charged_hadron | 100.0284 | 0 | 0.0000 | charged_hadron | 0.0000 | 1 | 0.0876 |
| 3124 | Hqql_correct | label_Hqql | label_Hqql | 0.8621 | electron | 467.6960 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1855 |
| 3125 | Hqql_correct | label_Hqql | label_Hqql | 0.9866 | charged_hadron | 141.1927 | 0 | 0.0000 | charged_hadron | 0.0000 | 1 | 0.1509 |
| 3126 | Hqql_correct | label_Hqql | label_Hqql | 0.9179 | muon | 319.1118 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1887 |
| 3128 | Hqql_correct | label_Hqql | label_Hqql | 0.9990 | muon | 318.2348 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1767 |
| 3129 | Hqql_correct | label_Hqql | label_Hqql | 0.9996 | photon | 94.6950 | 0 | 0.0000 | photon | 0.0000 | 1 | 0.1790 |
| 3130 | Hqql_correct | label_Hqql | label_Hqql | 0.9998 | muon | 338.6584 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1398 |
| 3131 | Hqql_correct | label_Hqql | label_Hqql | 0.9998 | electron | 431.3899 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.0904 |
| 3132 | Hqql_correct | label_Hqql | label_Hqql | 0.9243 | neutral_hadron | 113.7045 | 0 | 0.0000 | neutral_hadron | 0.0000 | 0 | n/a |
| 3133 | Hqql_correct | label_Hqql | label_Hqql | 0.9778 | electron | 146.2730 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1898 |
| 3134 | Hqql_correct | label_Hqql | label_Hqql | 0.9981 | muon | 313.6549 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1366 |
| 3135 | Hqql_correct | label_Hqql | label_Hqql | 0.9447 | electron | 185.6615 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.2645 |
| 3136 | Hqql_correct | label_Hqql | label_Hqql | 0.9682 | neutral_hadron | 62.2505 | 0 | 0.0000 | neutral_hadron | 0.0000 | 1 | 0.1815 |
| 3137 | Hqql_correct | label_Hqql | label_Hqql | 0.9987 | electron | 215.0694 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.0808 |
| 3138 | Hqql_correct | label_Hqql | label_Hqql | 0.9999 | charged_hadron | 352.6854 | 0 | 0.0000 | charged_hadron | 0.0000 | 1 | 0.1448 |
| 3139 | Hqql_correct | label_Hqql | label_Hqql | 0.9635 | muon | 357.0374 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1930 |
| 3140 | Hqql_correct | label_Hqql | label_Hqql | 0.9972 | electron | 94.9290 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.2091 |
| 3141 | Hqql_correct | label_Hqql | label_Hqql | 0.9816 | electron | 166.7803 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1211 |
| 3142 | Hqql_correct | label_Hqql | label_Hqql | 0.9759 | electron | 229.0143 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.3057 |
| 3143 | Hqql_correct | label_Hqql | label_Hqql | 0.9972 | muon | 293.4901 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1625 |
| 3144 | Hqql_correct | label_Hqql | label_Hqql | 0.9822 | electron | 112.9613 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1577 |
| 3145 | Hqql_correct | label_Hqql | label_Hqql | 0.9999 | neutral_hadron | 134.5491 | 0 | 0.0000 | neutral_hadron | 0.0000 | 1 | 0.0622 |
| 3146 | Hqql_correct | label_Hqql | label_Hqql | 0.9999 | neutral_hadron | 148.1751 | 0 | 0.0000 | neutral_hadron | 0.0000 | 1 | 0.0719 |
| 3147 | Hqql_correct | label_Hqql | label_Hqql | 0.8678 | neutral_hadron | 117.4525 | 0 | 0.0000 | neutral_hadron | 0.0000 | 1 | 0.1292 |
| 3148 | Hqql_to_Tbl | label_Hqql | label_Tbl | 0.8333 | neutral_hadron | 184.2205 | 0 | 0.0000 | neutral_hadron | 0.0000 | 1 | 0.1203 |
| 3149 | Hqql_correct | label_Hqql | label_Hqql | 0.9998 | neutral_hadron | 328.6471 | 0 | 0.0000 | neutral_hadron | 0.0000 | 1 | 0.1137 |
| 3150 | Hqql_correct | label_Hqql | label_Hqql | 0.9994 | electron | 382.6726 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1597 |
| 3151 | Hqql_correct | label_Hqql | label_Hqql | 0.6079 | electron | 233.9993 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1801 |
| 3152 | Hqql_correct | label_Hqql | label_Hqql | 0.8007 | muon | 352.1762 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1527 |
| 3153 | Hqql_correct | label_Hqql | label_Hqql | 0.9893 | electron | 245.5711 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.2403 |

## Interpretation

Compare Hqql_correct vs Hqql_to_Tbl vs Tbl_correct. If Hqql_to_Tbl particle0/leading/lepton/KNN profile matches Tbl_correct more than Hqql_correct, the confusion route has physical meaning.
