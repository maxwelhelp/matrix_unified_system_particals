# Real Particle Patch Controls v2 balanced

checkpoint=local_checkpoints/part/ParT_full.pt
mode=full
n=640 samples_per_file=64
missing=[] unexpected=[]

## Baseline
{
  "patch": "baseline",
  "layer": "",
  "group": "",
  "n": 640,
  "pred_counts": "[243, 0, 45, 0, 7, 81, 241, 0, 0, 23]",
  "true_counts": "[64, 64, 64, 64, 64, 64, 64, 64, 64, 64]",
  "acc": 0.09687500447034836
}

## Top patches
| rank | patch | layer | group | delta_logit | KL | top1 | acc->patch_acc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | cls_block_zero | 1 | cls_block | 4.5362 | 1.3820 | 0.3797 | 0.0969->0.1000 |
| 2 | cls_block_zero | 0 | cls_block | 1.8613 | 3.7463 | 0.3797 | 0.0969->0.1000 |
| 3 | pair_embed_zero |  | pair_bias | 1.3019 | 0.9642 | 0.6219 | 0.0969->0.1047 |
| 4 | particle_block_skip | 0 | block | 0.6167 | 0.7729 | 0.6469 | 0.0969->0.1063 |
| 5 | particle_block_skip | 1 | block | 0.4217 | 0.4100 | 0.7016 | 0.0969->0.1063 |
| 6 | particle_block_skip | 7 | block | 0.3856 | 0.8321 | 0.6156 | 0.0969->0.0984 |
| 7 | particle_block_skip | 2 | block | 0.2035 | 0.2944 | 0.7672 | 0.0969->0.1094 |
| 8 | particle_block_skip | 3 | block | 0.1087 | 0.1870 | 0.8344 | 0.0969->0.1047 |
| 9 | particle_block_skip | 5 | block | -0.0792 | 0.4033 | 0.7125 | 0.0969->0.1234 |
| 10 | particle_block_skip | 6 | block | 0.0717 | 0.4221 | 0.7141 | 0.0969->0.1125 |
| 11 | mlp_top_group_zero | 6 | top32 | -0.0522 | 0.0228 | 0.9422 | 0.0969->0.0938 |
| 12 | mlp_top_group_zero | 1 | top32 | 0.0479 | 0.0246 | 0.9406 | 0.0969->0.1031 |
| 13 | mlp_top_group_zero | 7 | top32 | -0.0307 | 0.0795 | 0.8922 | 0.0969->0.0984 |
| 14 | mlp_top_group_zero | 3 | top32 | 0.0218 | 0.0079 | 0.9609 | 0.0969->0.0984 |
| 15 | mlp_top_group_zero | 4 | top32 | 0.0218 | 0.0141 | 0.9516 | 0.0969->0.0984 |
| 16 | mlp_top_group_zero | 2 | top32 | 0.0193 | 0.0127 | 0.9578 | 0.0969->0.0969 |
| 17 | mlp_top_group_zero | 5 | top32 | -0.0134 | 0.0194 | 0.9438 | 0.0969->0.1016 |
| 18 | mlp_top_group_zero | 0 | top32 | -0.0035 | 0.0300 | 0.9313 | 0.0969->0.1000 |
| 19 | particle_block_skip | 4 | block | -0.0033 | 0.2546 | 0.7797 | 0.0969->0.1078 |
