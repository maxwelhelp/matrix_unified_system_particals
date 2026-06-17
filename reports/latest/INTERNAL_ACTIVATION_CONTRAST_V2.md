# INTERNAL_ACTIVATION_CONTRAST_V2

Direct hook-based A/B/C activation contrast. Includes approximate class-direction projection and safer zero-slice ablation contribution.

- A protected_highiso: **32**
- B confused_highiso: **11**
- C Tbl_correct: **128**
- projection: `effective_linear_approx_from_2_linear_layers`

## Head diagnosis summary
| head | diag | B_close_C | B-A hqql_proj | B-A tbl_proj | B-A hqql_contrib | B-A tbl_contrib | A hqql/tbl | B hqql/tbl | C hqql/tbl |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L1_ch80:96 | active_tbl_like_readout_candidate | 107.7441 | 170.7955 | 103.4572 | -0.1101 | 1.1220 | 1190.1986/1152.2983 | 1360.9941/1255.7555 | 1313.4933/1334.4764 |
| L2_ch224:256 | lost_hqql_evidence_candidate | -27.9287 | -1.6834 | -0.7152 | 0.2378 | -0.4670 | 22.3679/21.0772 | 20.6845/20.3620 | 41.9434/41.1847 |
| L2_ch32:64 | mixed_or_unclear | -19.2769 | 4.6974 | 8.0105 | -0.4246 | 0.3246 | 9.3685/9.9281 | 14.0659/17.9386 | 29.3177/42.0889 |
| L2_ch160:192 | mixed_or_unclear | -8.3213 | 3.1764 | 4.4483 | -1.0202 | -0.0235 | 15.3746/19.2787 | 18.5511/23.7270 | 26.5158/34.9811 |
| L1_ch32:48 | active_tbl_like_readout_candidate | 7.8095 | 140.4912 | 167.3082 | -0.2127 | 0.3607 | 304.3802/347.0692 | 444.8714/514.3775 | 654.1567/538.4224 |
| L2_ch128:160 | lost_hqql_evidence_candidate | -6.6534 | -4.1474 | 0.9384 | -0.2256 | -0.0576 | 24.6162/23.3001 | 20.4688/24.2385 | 21.5606/35.0894 |
| L2_ch0:32 | lost_hqql_evidence_candidate | -2.3092 | -0.8316 | 1.6008 | 0.0875 | 0.0778 | 9.9492/7.7741 | 9.1176/9.3749 | 10.8239/13.1174 |

## Interpretation guide

- `active_tbl_like_readout_candidate`: B is closer to C than A in projected class-evidence space.
- `lost_hqql_evidence_candidate`: B loses Hqql projection/contribution without clean Tbl-like activation.
- `mixed_or_unclear`: inspect event rows and top particles.

Use `internal_activation_contrast_v2_top_particles.csv` to check whether top activations in B land on second leptons, particle0/lepton, or hadronic neighbors.
