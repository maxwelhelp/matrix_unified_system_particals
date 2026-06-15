# Matrix Unified System — Particle Atlas

Private project for adapting the matrix-pseudocode / causal-tracing system from Qwen LLMs to particle-physics transformer models.

Primary target:

- Particle Transformer / ParT for jet tagging
- JetClass small subset first
- later: JetFormer / MIParT / other particle-cloud transformers

Core mapping:

```text
LLM token          -> jet constituent / particle
attention read     -> particle-to-particle read
QK score term      -> pair/geometry-aware interaction score
VO payload         -> information written from source particle
MLP group          -> class-logit writer/suppressor
lm_head logit      -> jet class logit / classifier head logit
why-token report   -> why-class report
```

Main goal:

```text
jet/event/particle cloud
  -> trained particle transformer
  -> static atlas
  -> runtime trace
  -> head/term/particle/pair/MLP patch controls
  -> class-logit attribution
  -> repeated mechanism mining
  -> physics hypothesis candidates
```

This is not automatic discovery by itself. It is a candidate-generator for mechanisms that must be validated with heldout jets, counterfactual tests, simulation checks, and physics expert review.

## Current status

This repo is the particles-specific fork target. Copy the lightweight core from `maxwelhelp/matrix_unified_system`, then implement particle adapters.

Heavy outputs stay local in `runs/` and are not committed.

## First milestone

1. copy core tools/scripts/docs from the base repo;
2. add `adapters/part_adapter.py`;
3. load a small JetClass subset;
4. load pretrained ParT;
5. run model probe;
6. produce first `WHY_CLASS_REPORT.md` on 100-1000 jets.
