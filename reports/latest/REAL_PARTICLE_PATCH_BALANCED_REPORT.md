# Real Particle Patch Controls v2 balanced

checkpoint=local_checkpoints/part/ParT_full.pt
mode=full
n=320 samples_per_file=32
missing=[] unexpected=[]

## Baseline
{
  "patch": "baseline",
  "layer": "",
  "group": "",
  "n": 320,
  "pred_counts": "[124, 0, 14, 0, 3, 40, 124, 0, 0, 15]",
  "true_counts": "[32, 32, 32, 32, 32, 32, 32, 32, 32, 32]",
  "acc": 0.11250000447034836
}

## Top patches
| rank | patch | layer | group | delta_logit | KL | top1 | acc->patch_acc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | cls_block_zero | 1 | cls_block | 4.7232 | 1.4206 | 0.3875 | 0.1125->0.1000 |
| 2 | cls_block_zero | 0 | cls_block | 1.9857 | 3.7147 | 0.3875 | 0.1125->0.1000 |
| 3 | pair_embed_zero |  | pair_bias | 1.3248 | 0.9035 | 0.6656 | 0.1125->0.1031 |
| 4 | particle_block_skip | 0 | block | 0.6372 | 0.7712 | 0.6656 | 0.1125->0.1063 |
| 5 | particle_block_skip | 1 | block | 0.3771 | 0.3728 | 0.7438 | 0.1125->0.1250 |
| 6 | particle_block_skip | 7 | block | 0.3323 | 0.8167 | 0.6125 | 0.1125->0.1187 |
| 7 | particle_block_skip | 2 | block | 0.1707 | 0.2811 | 0.7969 | 0.1125->0.1313 |
| 8 | particle_block_skip | 5 | block | -0.1047 | 0.3938 | 0.7188 | 0.1125->0.1313 |
| 9 | particle_block_skip | 6 | block | 0.0887 | 0.4102 | 0.7125 | 0.1125->0.1219 |
| 10 | particle_block_skip | 3 | block | 0.0547 | 0.1783 | 0.8594 | 0.1125->0.1219 |
| 11 | mlp_top_group_zero | 7 | top32 | -0.0406 | 0.0637 | 0.9031 | 0.1125->0.1156 |
| 12 | mlp_top_group_zero | 1 | top32 | 0.0406 | 0.0238 | 0.9563 | 0.1125->0.1187 |
| 13 | mlp_top_group_zero | 6 | top32 | -0.0378 | 0.0214 | 0.9406 | 0.1125->0.1063 |
| 14 | mlp_top_group_zero | 4 | top32 | 0.0362 | 0.0152 | 0.9500 | 0.1125->0.1125 |
| 15 | mlp_top_group_zero | 2 | top32 | 0.0218 | 0.0128 | 0.9719 | 0.1125->0.1125 |
| 16 | particle_block_skip | 4 | block | -0.0184 | 0.2805 | 0.7906 | 0.1125->0.1094 |
| 17 | mlp_top_group_zero | 3 | top32 | 0.0151 | 0.0086 | 0.9750 | 0.1125->0.1156 |
| 18 | mlp_top_group_zero | 0 | top32 | -0.0062 | 0.0335 | 0.9313 | 0.1125->0.1187 |
| 19 | mlp_top_group_zero | 5 | top32 | 0.0017 | 0.0178 | 0.9469 | 0.1125->0.1156 |
