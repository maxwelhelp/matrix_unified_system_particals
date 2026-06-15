# Real Particle Patch Controls v3 official preprocess

checkpoint=local_checkpoints/part/ParT_full.pt
mode=full
preprocess=official_wrap_v3
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
| 1 | cls_block_zero | 1 | cls_block | 4.5347 | 1.3815 | 0.3797 | 0.0969->0.1000 |
| 2 | cls_block_zero | 0 | cls_block | 1.8604 | 3.7471 | 0.3797 | 0.0969->0.1000 |
| 3 | pair_embed_zero |  | pair_bias | 1.2996 | 0.9640 | 0.6219 | 0.0969->0.1047 |
| 4 | particle_block_skip | 0 | block | 0.6158 | 0.7728 | 0.6453 | 0.0969->0.1063 |
| 5 | particle_block_skip | 1 | block | 0.4209 | 0.4095 | 0.7016 | 0.0969->0.1063 |
| 6 | particle_block_skip | 7 | block | 0.3846 | 0.8323 | 0.6172 | 0.0969->0.0984 |
| 7 | particle_block_skip | 2 | block | 0.2019 | 0.2939 | 0.7672 | 0.0969->0.1094 |
| 8 | particle_block_skip | 3 | block | 0.1081 | 0.1868 | 0.8344 | 0.0969->0.1047 |
| 9 | particle_block_skip | 5 | block | -0.0789 | 0.4033 | 0.7125 | 0.0969->0.1234 |
| 10 | particle_block_skip | 6 | block | 0.0715 | 0.4222 | 0.7141 | 0.0969->0.1125 |
| 11 | mlp_top_group_zero | 6 | top32 | -0.0521 | 0.0228 | 0.9422 | 0.0969->0.0938 |
| 12 | mlp_top_group_zero | 1 | top32 | 0.0477 | 0.0246 | 0.9406 | 0.0969->0.1031 |
| 13 | mlp_top_group_zero | 7 | top32 | -0.0328 | 0.0790 | 0.8953 | 0.0969->0.0969 |
| 14 | mlp_top_group_zero | 4 | top32 | 0.0217 | 0.0141 | 0.9500 | 0.0969->0.0984 |
| 15 | mlp_top_group_zero | 3 | top32 | 0.0216 | 0.0079 | 0.9609 | 0.0969->0.0984 |
| 16 | mlp_top_group_zero | 2 | top32 | 0.0198 | 0.0127 | 0.9578 | 0.0969->0.0969 |
| 17 | mlp_top_group_zero | 5 | top32 | -0.0138 | 0.0194 | 0.9422 | 0.0969->0.1016 |
| 18 | particle_block_skip | 4 | block | -0.0041 | 0.2546 | 0.7797 | 0.0969->0.1078 |
| 19 | mlp_top_group_zero | 0 | top32 | -0.0036 | 0.0300 | 0.9313 | 0.0969->0.1000 |
