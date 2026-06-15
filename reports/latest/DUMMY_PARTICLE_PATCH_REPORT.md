# Dummy Particle Patch Controls v2

Checks causal patch handles on dummy ParT: pair-bias zero, particle-block skip, cls-block zero, MLP top-neuron group zero.

| rank | patch | layer | group | delta_top_logit | KL | top1 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | cls_block_zero | 0 | cls_block | 1.9470 | 0.4491 | 0.1250 |
| 2 | particle_block_skip | 0 | block | 1.5605 | 0.9389 | 0.1250 |
| 3 | particle_block_skip | 1 | block | 0.8209 | 0.6107 | 0.1250 |
| 4 | mlp_top_group_zero | 1 | top16 | -0.1021 | 0.0210 | 1.0000 |
| 5 | mlp_top_group_zero | 0 | top16 | 0.0223 | 0.0536 | 0.7500 |
| 6 | pair_embed_zero |  | pair_bias | -0.0064 | 1.574e-04 | 1.0000 |
