# Hqql/Tbl Confusion Physics Regime v1

This report asks what particle0/leading/core physically is in Hqql/Tbl confusion regimes.

## Group summary
| group | n | particle0_pid_modes | p0_lepton | p0_iso | has_lepton | lead_pid_modes | lead_lepton | missing_pt |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hqql_correct | 245 | electron:91, muon:89, charged_hadron:31, photon:19, neutral_hadron:15 | 0.7347 | 0.1617 | 0.9918 | electron:91, muon:89, charged_hadron:31, photon:19, neutral_hadron:15 | 0.7347 | 624.8198 |
| Hqql_to_Tbl | 4 | electron:2, neutral_hadron:1, muon:1 | 0.7500 | 0.1502 | 1.0000 | electron:2, neutral_hadron:1, muon:1 | 0.7500 | 527.8429 |
| Tbl_correct | 248 | muon:111, electron:94, neutral_hadron:16, photon:16, charged_hadron:11 | 0.8266 | 0.1688 | 1.0000 | muon:111, electron:94, neutral_hadron:16, photon:16, charged_hadron:11 | 0.8266 | 593.9866 |
| Tbl_to_Hqql | 7 | electron:4, muon:2, charged_hadron:1 | 0.8571 | 0.1426 | 1.0000 | electron:4, muon:2, charged_hadron:1 | 0.8571 | 631.9686 |

## Event examples
| event | group | true | pred | conf | p0_pid | p0_pt | p0_rank | p0_lep | lead_pid | lead_lep | has_lep | best_lep_iso |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 768 | Hqql_correct | label_Hqql | label_Hqql | 0.9999 | muon | 138.1330 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1589 |
| 769 | Hqql_correct | label_Hqql | label_Hqql | 0.9978 | electron | 186.8828 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1700 |
| 770 | Hqql_correct | label_Hqql | label_Hqql | 0.7015 | electron | 135.6346 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1239 |
| 771 | Hqql_correct | label_Hqql | label_Hqql | 0.9965 | electron | 185.7713 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1218 |
| 772 | Hqql_correct | label_Hqql | label_Hqql | 0.9964 | muon | 134.5411 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1255 |
| 773 | Hqql_to_Tbl | label_Hqql | label_Tbl | 0.9905 | electron | 420.1024 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1652 |
| 774 | Hqql_correct | label_Hqql | label_Hqql | 0.9999 | muon | 445.1895 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1885 |
| 775 | Hqql_correct | label_Hqql | label_Hqql | 0.9994 | charged_hadron | 195.5860 | 0 | 0.0000 | charged_hadron | 0.0000 | 1 | 0.1465 |
| 776 | Hqql_correct | label_Hqql | label_Hqql | 0.9744 | electron | 321.0246 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.2247 |
| 777 | Hqql_correct | label_Hqql | label_Hqql | 0.9413 | muon | 269.7216 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1967 |
| 778 | Hqql_to_Tbl | label_Hqql | label_Tbl | 0.8791 | electron | 153.0558 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.0893 |
| 779 | Hqql_correct | label_Hqql | label_Hqql | 0.6420 | electron | 245.8136 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.2876 |
| 780 | Hqql_correct | label_Hqql | label_Hqql | 0.9976 | muon | 97.4305 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1452 |
| 781 | Hqql_correct | label_Hqql | label_Hqql | 0.9997 | electron | 393.9726 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1362 |
| 782 | Hqql_correct | label_Hqql | label_Hqql | 0.9730 | charged_hadron | 132.3570 | 0 | 0.0000 | charged_hadron | 0.0000 | 1 | 0.2110 |
| 783 | Hqql_correct | label_Hqql | label_Hqql | 0.9983 | charged_hadron | 150.2936 | 0 | 0.0000 | charged_hadron | 0.0000 | 1 | 0.1510 |
| 784 | Hqql_correct | label_Hqql | label_Hqql | 0.9505 | electron | 526.1700 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1651 |
| 785 | Hqql_correct | label_Hqql | label_Hqql | 0.9904 | muon | 290.4164 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1577 |
| 786 | Hqql_correct | label_Hqql | label_Hqql | 0.9977 | electron | 380.5297 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1876 |
| 787 | Hqql_correct | label_Hqql | label_Hqql | 0.9898 | neutral_hadron | 125.7162 | 0 | 0.0000 | neutral_hadron | 0.0000 | 1 | 0.0783 |
| 788 | Hqql_correct | label_Hqql | label_Hqql | 0.6363 | electron | 210.9155 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.3043 |
| 789 | Hqql_correct | label_Hqql | label_Hqql | 0.9943 | electron | 326.9661 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1076 |
| 790 | Hqql_correct | label_Hqql | label_Hqql | 0.9993 | muon | 524.3685 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1230 |
| 791 | Hqql_correct | label_Hqql | label_Hqql | 0.9956 | charged_hadron | 151.2202 | 0 | 0.0000 | charged_hadron | 0.0000 | 1 | 0.1517 |
| 792 | Hqql_correct | label_Hqql | label_Hqql | 0.9901 | photon | 98.5999 | 0 | 0.0000 | photon | 0.0000 | 1 | 0.1675 |
| 793 | Hqql_correct | label_Hqql | label_Hqql | 0.9996 | electron | 372.7248 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.2192 |
| 794 | Hqql_correct | label_Hqql | label_Hqql | 1.0000 | photon | 203.4302 | 0 | 0.0000 | photon | 0.0000 | 1 | 0.0864 |
| 795 | Hqql_correct | label_Hqql | label_Hqql | 1.0000 | electron | 378.6483 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.0986 |
| 796 | Hqql_correct | label_Hqql | label_Hqql | 0.9999 | muon | 316.2993 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1228 |
| 797 | Hqql_correct | label_Hqql | label_Hqql | 1.0000 | electron | 423.7215 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1386 |
| 798 | Hqql_correct | label_Hqql | label_Hqql | 0.9999 | charged_hadron | 183.7744 | 0 | 0.0000 | charged_hadron | 0.0000 | 1 | 0.1698 |
| 799 | Hqql_correct | label_Hqql | label_Hqql | 0.9984 | muon | 426.8395 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.2323 |
| 800 | Hqql_correct | label_Hqql | label_Hqql | 1.0000 | muon | 194.7510 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1550 |
| 801 | Hqql_correct | label_Hqql | label_Hqql | 0.9995 | electron | 218.8318 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.2348 |
| 802 | Hqql_correct | label_Hqql | label_Hqql | 0.9718 | muon | 229.4073 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1773 |
| 803 | Hqql_correct | label_Hqql | label_Hqql | 0.9994 | electron | 156.0907 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1025 |
| 804 | Hqql_correct | label_Hqql | label_Hqql | 0.9999 | photon | 131.9997 | 0 | 0.0000 | photon | 0.0000 | 1 | 0.0955 |
| 805 | Hqql_correct | label_Hqql | label_Hqql | 0.9985 | muon | 166.6381 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1883 |
| 806 | Hqql_correct | label_Hqql | label_Hqql | 0.6425 | charged_hadron | 111.9360 | 0 | 0.0000 | charged_hadron | 0.0000 | 1 | 0.1720 |
| 807 | Hqql_correct | label_Hqql | label_Hqql | 0.9159 | charged_hadron | 208.3672 | 0 | 0.0000 | charged_hadron | 0.0000 | 1 | 0.1492 |
| 808 | Hqql_correct | label_Hqql | label_Hqql | 0.5396 | electron | 226.8067 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1682 |
| 809 | Hqql_correct | label_Hqql | label_Hqql | 0.9981 | muon | 345.6596 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.2020 |
| 810 | Hqql_correct | label_Hqql | label_Hqql | 0.9612 | muon | 382.8791 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1815 |
| 811 | Hqql_correct | label_Hqql | label_Hqql | 0.8661 | neutral_hadron | 94.6467 | 0 | 0.0000 | neutral_hadron | 0.0000 | 1 | 0.1781 |
| 812 | Hqql_correct | label_Hqql | label_Hqql | 0.9531 | muon | 256.5991 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1581 |
| 813 | Hqql_correct | label_Hqql | label_Hqql | 0.9999 | muon | 213.5150 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1104 |
| 814 | Hqql_correct | label_Hqql | label_Hqql | 0.9837 | neutral_hadron | 146.9194 | 0 | 0.0000 | neutral_hadron | 0.0000 | 1 | 0.1832 |
| 815 | Hqql_correct | label_Hqql | label_Hqql | 0.9993 | muon | 206.0280 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.2133 |
| 817 | Hqql_correct | label_Hqql | label_Hqql | 0.9996 | muon | 300.9614 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1534 |
| 818 | Hqql_correct | label_Hqql | label_Hqql | 0.9730 | electron | 468.0427 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1133 |
| 819 | Hqql_correct | label_Hqql | label_Hqql | 0.9996 | charged_hadron | 100.0284 | 0 | 0.0000 | charged_hadron | 0.0000 | 1 | 0.0876 |
| 820 | Hqql_correct | label_Hqql | label_Hqql | 0.8621 | electron | 467.6960 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1855 |
| 821 | Hqql_correct | label_Hqql | label_Hqql | 0.9866 | charged_hadron | 141.1927 | 0 | 0.0000 | charged_hadron | 0.0000 | 1 | 0.1509 |
| 822 | Hqql_correct | label_Hqql | label_Hqql | 0.9179 | muon | 319.1118 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1887 |
| 824 | Hqql_correct | label_Hqql | label_Hqql | 0.9990 | muon | 318.2348 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1767 |
| 825 | Hqql_correct | label_Hqql | label_Hqql | 0.9996 | photon | 94.6950 | 0 | 0.0000 | photon | 0.0000 | 1 | 0.1790 |
| 826 | Hqql_correct | label_Hqql | label_Hqql | 0.9998 | muon | 338.6584 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1398 |
| 827 | Hqql_correct | label_Hqql | label_Hqql | 0.9998 | electron | 431.3899 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.0904 |
| 828 | Hqql_correct | label_Hqql | label_Hqql | 0.9243 | neutral_hadron | 113.7045 | 0 | 0.0000 | neutral_hadron | 0.0000 | 0 | n/a |
| 829 | Hqql_correct | label_Hqql | label_Hqql | 0.9778 | electron | 146.2730 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1898 |
| 830 | Hqql_correct | label_Hqql | label_Hqql | 0.9981 | muon | 313.6549 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1366 |
| 831 | Hqql_correct | label_Hqql | label_Hqql | 0.9447 | electron | 185.6615 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.2645 |
| 832 | Hqql_correct | label_Hqql | label_Hqql | 0.9682 | neutral_hadron | 62.2505 | 0 | 0.0000 | neutral_hadron | 0.0000 | 1 | 0.1815 |
| 833 | Hqql_correct | label_Hqql | label_Hqql | 0.9987 | electron | 215.0694 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.0808 |
| 834 | Hqql_correct | label_Hqql | label_Hqql | 0.9999 | charged_hadron | 352.6854 | 0 | 0.0000 | charged_hadron | 0.0000 | 1 | 0.1448 |
| 835 | Hqql_correct | label_Hqql | label_Hqql | 0.9635 | muon | 357.0374 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1930 |
| 836 | Hqql_correct | label_Hqql | label_Hqql | 0.9972 | electron | 94.9290 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.2091 |
| 837 | Hqql_correct | label_Hqql | label_Hqql | 0.9816 | electron | 166.7803 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1211 |
| 838 | Hqql_correct | label_Hqql | label_Hqql | 0.9759 | electron | 229.0143 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.3057 |
| 839 | Hqql_correct | label_Hqql | label_Hqql | 0.9972 | muon | 293.4901 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1625 |
| 840 | Hqql_correct | label_Hqql | label_Hqql | 0.9822 | electron | 112.9613 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1577 |
| 841 | Hqql_correct | label_Hqql | label_Hqql | 0.9999 | neutral_hadron | 134.5491 | 0 | 0.0000 | neutral_hadron | 0.0000 | 1 | 0.0622 |
| 842 | Hqql_correct | label_Hqql | label_Hqql | 0.9999 | neutral_hadron | 148.1751 | 0 | 0.0000 | neutral_hadron | 0.0000 | 1 | 0.0719 |
| 843 | Hqql_correct | label_Hqql | label_Hqql | 0.8678 | neutral_hadron | 117.4525 | 0 | 0.0000 | neutral_hadron | 0.0000 | 1 | 0.1292 |
| 844 | Hqql_to_Tbl | label_Hqql | label_Tbl | 0.8333 | neutral_hadron | 184.2205 | 0 | 0.0000 | neutral_hadron | 0.0000 | 1 | 0.1203 |
| 845 | Hqql_correct | label_Hqql | label_Hqql | 0.9998 | neutral_hadron | 328.6471 | 0 | 0.0000 | neutral_hadron | 0.0000 | 1 | 0.1137 |
| 846 | Hqql_correct | label_Hqql | label_Hqql | 0.9994 | electron | 382.6726 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1597 |
| 847 | Hqql_correct | label_Hqql | label_Hqql | 0.6079 | electron | 233.9993 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.1801 |
| 848 | Hqql_correct | label_Hqql | label_Hqql | 0.8007 | muon | 352.1762 | 0 | 1.0000 | muon | 1.0000 | 1 | 0.1527 |
| 849 | Hqql_correct | label_Hqql | label_Hqql | 0.9893 | electron | 245.5711 | 0 | 1.0000 | electron | 1.0000 | 1 | 0.2403 |

## Interpretation

Compare Hqql_correct vs Hqql_to_Tbl vs Tbl_correct. If Hqql_to_Tbl particle0/leading/lepton/KNN profile matches Tbl_correct more than Hqql_correct, the confusion route has physical meaning.
