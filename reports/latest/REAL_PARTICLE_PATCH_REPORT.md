# Real Particle Patch Controls v1

checkpoint=local_checkpoints/part/ParT_full.pt
mode=full
n=512
missing=[] unexpected=[]

## Baseline
{
  "patch": "baseline",
  "layer": "",
  "group": "",
  "pred_counts": "[199, 0, 33, 0, 0, 15, 248, 0, 0, 17]",
  "acc": 0.0
}

## Top patches
| rank | patch | layer | group | delta_logit | KL | top1 | acc->patch_acc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | cls_block_zero | 1 | cls_block | 4.2830 | 1.2464 | 0.3887 | 0.0000->0.0000 |
| 2 | cls_block_zero | 0 | cls_block | 1.8830 | 4.2834 | 0.3867 | 0.0000->0.0000 |
| 3 | pair_embed_zero |  | pair_bias | 0.7494 | 0.7525 | 0.6406 | 0.0000->0.0000 |
| 4 | particle_block_skip | 0 | block | 0.6496 | 0.6710 | 0.6699 | 0.0000->0.0000 |
| 5 | particle_block_skip | 2 | block | 0.4344 | 0.2820 | 0.7734 | 0.0000->0.0000 |
| 6 | particle_block_skip | 7 | block | 0.4069 | 0.4862 | 0.6973 | 0.0000->0.0020 |
| 7 | particle_block_skip | 3 | block | 0.2812 | 0.2279 | 0.7910 | 0.0000->0.0020 |
| 8 | particle_block_skip | 6 | block | 0.2365 | 0.5809 | 0.6465 | 0.0000->0.0000 |
| 9 | particle_block_skip | 4 | block | 0.2236 | 0.2929 | 0.7441 | 0.0000->0.0000 |
| 10 | particle_block_skip | 1 | block | 0.1696 | 0.3476 | 0.7324 | 0.0000->0.0000 |
| 11 | mlp_top_group_zero | 7 | top32 | 0.1235 | 0.0578 | 0.8828 | 0.0000->0.0020 |
| 12 | particle_block_skip | 5 | block | 0.1017 | 0.5079 | 0.6660 | 0.0000->0.0000 |
| 13 | mlp_top_group_zero | 3 | top32 | 0.0758 | 0.0132 | 0.9512 | 0.0000->0.0000 |
| 14 | mlp_top_group_zero | 2 | top32 | 0.0453 | 0.0195 | 0.9395 | 0.0000->0.0000 |
| 15 | mlp_top_group_zero | 4 | top32 | 0.0340 | 0.0168 | 0.9316 | 0.0000->0.0000 |
| 16 | mlp_top_group_zero | 1 | top32 | 0.0260 | 0.0373 | 0.9082 | 0.0000->0.0000 |
| 17 | mlp_top_group_zero | 0 | top32 | 0.0174 | 0.0347 | 0.9219 | 0.0000->0.0000 |
| 18 | mlp_top_group_zero | 5 | top32 | 0.0157 | 0.0130 | 0.9453 | 0.0000->0.0000 |
| 19 | mlp_top_group_zero | 6 | top32 | 0.0134 | 0.0331 | 0.9141 | 0.0000->0.0000 |
