# Real Particle Patch Controls v3 official preprocess

checkpoint=local_checkpoints/part/ParT_kinpid.pt
mode=kinpid
preprocess=official_wrap_v3
n=640 samples_per_file=64
missing=[] unexpected=[]

## Baseline
{
  "patch": "baseline",
  "layer": "",
  "group": "",
  "n": 640,
  "pred_counts": "[395, 13, 28, 1, 11, 0, 179, 10, 0, 3]",
  "true_counts": "[64, 64, 64, 64, 64, 64, 64, 64, 64, 64]",
  "acc": 0.09531249850988388
}

## Top patches
| rank | patch | layer | group | delta_logit | KL | top1 | acc->patch_acc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | cls_block_zero | 0 | cls_block | 3.6519 | 2.1040 | 0.2750 | 0.0953->0.1000 |
| 2 | cls_block_zero | 1 | cls_block | 3.3743 | 1.1414 | 0.6172 | 0.0953->0.1000 |
| 3 | particle_block_skip | 4 | block | 0.2934 | 0.1594 | 0.8063 | 0.0953->0.1219 |
| 4 | particle_block_skip | 5 | block | 0.2333 | 0.1326 | 0.8297 | 0.0953->0.1141 |
| 5 | pair_embed_zero |  | pair_bias | -0.1812 | 1.0154 | 0.6922 | 0.0953->0.0906 |
| 6 | particle_block_skip | 6 | block | -0.1486 | 0.3244 | 0.7781 | 0.0953->0.0750 |
| 7 | particle_block_skip | 0 | block | -0.1147 | 0.9860 | 0.6500 | 0.0953->0.0938 |
| 8 | mlp_top_group_zero | 3 | top32 | -0.1068 | 0.0216 | 0.9438 | 0.0953->0.1047 |
| 9 | mlp_top_group_zero | 4 | top32 | -0.1013 | 0.0114 | 0.9703 | 0.0953->0.1000 |
| 10 | mlp_top_group_zero | 0 | top32 | -0.0828 | 0.0229 | 0.9453 | 0.0953->0.1000 |
| 11 | particle_block_skip | 2 | block | 0.0770 | 0.1507 | 0.8469 | 0.0953->0.0906 |
| 12 | mlp_top_group_zero | 7 | top32 | 0.0492 | 0.0209 | 0.9281 | 0.0953->0.0969 |
| 13 | particle_block_skip | 1 | block | 0.0430 | 0.3150 | 0.7641 | 0.0953->0.1172 |
| 14 | mlp_top_group_zero | 2 | top32 | -0.0337 | 0.0156 | 0.9484 | 0.0953->0.1063 |
| 15 | mlp_top_group_zero | 1 | top32 | 0.0321 | 0.0344 | 0.9234 | 0.0953->0.1047 |
| 16 | mlp_top_group_zero | 5 | top32 | -0.0305 | 0.0133 | 0.9656 | 0.0953->0.1063 |
| 17 | particle_block_skip | 7 | block | 0.0264 | 0.3663 | 0.7547 | 0.0953->0.0875 |
| 18 | particle_block_skip | 3 | block | -0.0165 | 0.2373 | 0.8094 | 0.0953->0.0906 |
| 19 | mlp_top_group_zero | 6 | top32 | -0.0019 | 0.0089 | 0.9563 | 0.0953->0.0984 |
