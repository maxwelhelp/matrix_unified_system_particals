# Real Particle Patch Controls v2 balanced

checkpoint=local_checkpoints/part/ParT_full.pt
mode=full
n=1280 samples_per_file=128
missing=[] unexpected=[]

## Baseline
{
  "patch": "baseline",
  "layer": "",
  "group": "",
  "n": 1280,
  "pred_counts": "[459, 0, 104, 0, 12, 162, 477, 0, 0, 66]",
  "true_counts": "[128, 128, 128, 128, 128, 128, 128, 128, 128, 128]",
  "acc": 0.11015625298023224
}

## Top patches
| rank | patch | layer | group | delta_logit | KL | top1 | acc->patch_acc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | cls_block_zero | 1 | cls_block | 4.6342 | 1.4145 | 0.3586 | 0.1102->0.1000 |
| 2 | cls_block_zero | 0 | cls_block | 2.1227 | 3.8319 | 0.3586 | 0.1102->0.1008 |
| 3 | pair_embed_zero |  | pair_bias | 1.3657 | 0.9760 | 0.6164 | 0.1102->0.1078 |
| 4 | particle_block_skip | 0 | block | 0.7062 | 0.7814 | 0.6570 | 0.1102->0.1055 |
| 5 | particle_block_skip | 1 | block | 0.4469 | 0.3980 | 0.7125 | 0.1102->0.1125 |
| 6 | particle_block_skip | 7 | block | 0.4193 | 0.8113 | 0.6289 | 0.1102->0.1094 |
| 7 | particle_block_skip | 2 | block | 0.1581 | 0.2823 | 0.7656 | 0.1102->0.1148 |
| 8 | particle_block_skip | 6 | block | 0.1320 | 0.4224 | 0.7031 | 0.1102->0.1187 |
| 9 | particle_block_skip | 3 | block | 0.0982 | 0.1876 | 0.8313 | 0.1102->0.1125 |
| 10 | particle_block_skip | 5 | block | -0.0638 | 0.3905 | 0.7078 | 0.1102->0.1266 |
| 11 | mlp_top_group_zero | 6 | top32 | -0.0608 | 0.0233 | 0.9398 | 0.1102->0.1070 |
| 12 | mlp_top_group_zero | 7 | top32 | -0.0518 | 0.0854 | 0.8992 | 0.1102->0.1133 |
| 13 | particle_block_skip | 4 | block | -0.0394 | 0.2519 | 0.7812 | 0.1102->0.1172 |
| 14 | mlp_top_group_zero | 1 | top32 | 0.0352 | 0.0245 | 0.9438 | 0.1102->0.1109 |
| 15 | mlp_top_group_zero | 2 | top32 | 0.0184 | 0.0127 | 0.9555 | 0.1102->0.1102 |
| 16 | mlp_top_group_zero | 3 | top32 | 0.0125 | 0.0073 | 0.9656 | 0.1102->0.1102 |
| 17 | mlp_top_group_zero | 4 | top32 | 0.0106 | 0.0137 | 0.9492 | 0.1102->0.1133 |
| 18 | mlp_top_group_zero | 0 | top32 | 0.0099 | 0.0337 | 0.9273 | 0.1102->0.1102 |
| 19 | mlp_top_group_zero | 5 | top32 | -0.0083 | 0.0195 | 0.9398 | 0.1102->0.1141 |
