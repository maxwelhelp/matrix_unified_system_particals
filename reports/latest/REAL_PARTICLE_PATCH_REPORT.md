# Real Particle Patch Controls v1

checkpoint=local_checkpoints/part/ParT_kinpid.pt
mode=kinpid
n=512
missing=[] unexpected=[]

## Baseline
{
  "patch": "baseline",
  "layer": "",
  "group": "",
  "pred_counts": "[406, 1, 7, 1, 6, 0, 72, 15, 0, 4]",
  "acc": 0.001953125
}

## Top patches
| rank | patch | layer | group | delta_logit | KL | top1 | acc->patch_acc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | cls_block_zero | 0 | cls_block | 4.8264 | 2.5694 | 0.1367 | 0.0020->0.0059 |
| 2 | cls_block_zero | 1 | cls_block | 4.0527 | 1.2444 | 0.7930 | 0.0020->0.0000 |
| 3 | particle_block_skip | 4 | block | 0.4491 | 0.1457 | 0.8594 | 0.0020->0.0039 |
| 4 | particle_block_skip | 5 | block | 0.4002 | 0.1276 | 0.8867 | 0.0020->0.0039 |
| 5 | pair_embed_zero |  | pair_bias | -0.3910 | 0.6360 | 0.8105 | 0.0020->0.0020 |
| 6 | particle_block_skip | 3 | block | -0.3557 | 0.1543 | 0.8730 | 0.0020->0.0059 |
| 7 | mlp_top_group_zero | 7 | top32 | 0.2854 | 0.0194 | 0.9531 | 0.0020->0.0020 |
| 8 | particle_block_skip | 0 | block | -0.2769 | 0.7180 | 0.7559 | 0.0020->0.0059 |
| 9 | mlp_top_group_zero | 4 | top32 | -0.1740 | 0.0083 | 0.9766 | 0.0020->0.0020 |
| 10 | particle_block_skip | 6 | block | -0.1487 | 0.2223 | 0.8594 | 0.0020->0.0020 |
| 11 | mlp_top_group_zero | 0 | top32 | -0.1323 | 0.0217 | 0.9570 | 0.0020->0.0039 |
| 12 | particle_block_skip | 7 | block | 0.1111 | 0.2686 | 0.8281 | 0.0020->0.0000 |
| 13 | mlp_top_group_zero | 2 | top32 | -0.1072 | 0.0136 | 0.9609 | 0.0020->0.0020 |
| 14 | mlp_top_group_zero | 3 | top32 | -0.0632 | 0.0112 | 0.9766 | 0.0020->0.0020 |
| 15 | mlp_top_group_zero | 5 | top32 | 0.0624 | 0.0085 | 0.9727 | 0.0020->0.0020 |
| 16 | particle_block_skip | 2 | block | -0.0623 | 0.1179 | 0.8887 | 0.0020->0.0000 |
| 17 | mlp_top_group_zero | 6 | top32 | 0.0513 | 0.0083 | 0.9727 | 0.0020->0.0020 |
| 18 | mlp_top_group_zero | 1 | top32 | 0.0481 | 0.0347 | 0.9355 | 0.0020->0.0020 |
| 19 | particle_block_skip | 1 | block | -0.0257 | 0.2684 | 0.8086 | 0.0020->0.0039 |
