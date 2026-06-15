# ParticleNet Real Patch Controls v1

checkpoint=local_checkpoints/part/ParticleNet_kinpid.pt
mode=kinpid
n=640
missing=[] unexpected=[]

## Baseline
{
  "patch": "baseline",
  "layer": "",
  "group": "",
  "n": 640,
  "acc": 0.7718750238418579,
  "pred_counts": "[62, 61, 54, 74, 69, 60, 69, 62, 63, 66]",
  "true_counts": "[64, 64, 64, 64, 64, 64, 64, 64, 64, 64]"
}

## Adapter
{
  "has_edge_convs": true,
  "n_edge_convs": 3,
  "has_fc": true,
  "n_fc": 2,
  "has_bn_fts": true,
  "use_counts": true,
  "use_fusion": false
}

## Top causal patches
| rank | patch | layer | group | delta_logit | KL | top1 | acc->patch_acc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | edge_conv_zero | 1 | edge_conv | 248.4882 | 92.9039 | 0.1031 | 0.7719->0.1000 |
| 2 | edge_conv_zero | 0 | edge_conv | 237.9274 | 19.5161 | 0.0938 | 0.7719->0.1000 |
| 3 | features_zero | input | features_zero | 108.0024 | 47.6685 | 0.1047 | 0.7719->0.1031 |
| 4 | feature_group_zero | input | coords_last2 | 34.3938 | 7.3169 | 0.1547 | 0.7719->0.1437 |
| 5 | edge_conv_zero | 2 | edge_conv | 21.7590 | 4.6169 | 0.0969 | 0.7719->0.1000 |
| 6 | feature_group_zero | input | kin_logs_0_4 | 13.6753 | 4.4214 | 0.1781 | 0.7719->0.1531 |
| 7 | mask_all_true | input | mask_all_true | 8.1220 | 2.3193 | 0.2703 | 0.7719->0.2484 |
| 8 | feature_group_zero | input | pid_charge_5_10 | 6.6895 | 3.6066 | 0.1078 | 0.7719->0.1109 |
| 9 | points_zero | input | points_zero | 1.3214 | 0.3228 | 0.7734 | 0.7719->0.6859 |
| 10 | fc_zero | 0 | fc | 0.9227 | 1.7757 | 0.0984 | 0.7719->0.1000 |
| 11 | fc_zero | 1 | fc | 0.8942 | 1.6531 | 0.0969 | 0.7719->0.1000 |
