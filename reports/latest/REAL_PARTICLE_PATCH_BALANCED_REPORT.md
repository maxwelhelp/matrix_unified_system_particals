# Real Particle Patch Controls v2 balanced

checkpoint=local_checkpoints/part/ParT_kin.pt
mode=kin
n=640 samples_per_file=64
missing=[] unexpected=[]

## Baseline
{
  "patch": "baseline",
  "layer": "",
  "group": "",
  "n": 640,
  "pred_counts": "[166, 10, 0, 8, 0, 0, 0, 453, 0, 3]",
  "true_counts": "[64, 64, 64, 64, 64, 64, 64, 64, 64, 64]",
  "acc": 0.11406250298023224
}

## Top patches
| rank | patch | layer | group | delta_logit | KL | top1 | acc->patch_acc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | cls_block_zero | 1 | cls_block | 5.9540 | 1.5021 | 0.2594 | 0.1141->0.1000 |
| 2 | cls_block_zero | 0 | cls_block | 1.8214 | 1.5107 | 0.7078 | 0.1141->0.1000 |
| 3 | pair_embed_zero |  | pair_bias | 1.3496 | 0.5472 | 0.6047 | 0.1141->0.0922 |
| 4 | particle_block_skip | 0 | block | 1.0132 | 0.5692 | 0.7078 | 0.1141->0.0969 |
| 5 | particle_block_skip | 4 | block | -0.9079 | 0.1877 | 0.8469 | 0.1141->0.1219 |
| 6 | particle_block_skip | 5 | block | -0.5569 | 0.2272 | 0.8469 | 0.1141->0.1203 |
| 7 | particle_block_skip | 1 | block | 0.4504 | 0.2349 | 0.7781 | 0.1141->0.1156 |
| 8 | particle_block_skip | 7 | block | 0.2984 | 0.2360 | 0.8500 | 0.1141->0.0984 |
| 9 | particle_block_skip | 3 | block | 0.2954 | 0.2762 | 0.8063 | 0.1141->0.0891 |
| 10 | particle_block_skip | 2 | block | 0.2561 | 0.2704 | 0.8203 | 0.1141->0.0969 |
| 11 | mlp_top_group_zero | 6 | top32 | -0.2114 | 0.0306 | 0.9313 | 0.1141->0.1219 |
| 12 | particle_block_skip | 6 | block | -0.2082 | 0.2529 | 0.8531 | 0.1141->0.1187 |
| 13 | mlp_top_group_zero | 4 | top32 | -0.1898 | 0.0150 | 0.9484 | 0.1141->0.1172 |
| 14 | mlp_top_group_zero | 5 | top32 | -0.1855 | 0.0242 | 0.9313 | 0.1141->0.1219 |
| 15 | mlp_top_group_zero | 3 | top32 | 0.1834 | 0.0196 | 0.9328 | 0.1141->0.1016 |
| 16 | mlp_top_group_zero | 1 | top32 | -0.1381 | 0.0237 | 0.9500 | 0.1141->0.1172 |
| 17 | mlp_top_group_zero | 0 | top32 | -0.1154 | 0.0284 | 0.9391 | 0.1141->0.1187 |
| 18 | mlp_top_group_zero | 7 | top32 | -0.0853 | 0.0130 | 0.9531 | 0.1141->0.1203 |
| 19 | mlp_top_group_zero | 2 | top32 | 0.0566 | 0.0291 | 0.9484 | 0.1141->0.1156 |
