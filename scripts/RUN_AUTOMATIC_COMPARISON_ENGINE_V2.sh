#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs
PYTHONUNBUFFERED=1 python tools/build_automatic_comparison_engine_v2.py \
  --v1-json manifests/latest/automatic_comparison_engine_v1.json \
  --relation-edges reports/latest/tables/relation_signal_edges.csv \
  --watcher manifests/latest/stream_task_watcher_v1.json \
  --dynamics manifests/latest/research_dynamics_v1.json \
  --dynamics-heads reports/latest/tables/dynamics_head_ranks.csv \
  --stream-index manifests/latest/research_stream_index_v1.json \
  --head-vectors reports/latest/tables/evidence_head_vectors.csv \
  --out-json manifests/latest/automatic_comparison_engine_v2.json \
  --out-md reports/latest/AUTOMATIC_COMPARISON_ENGINE_V2.md \
  --out-csv reports/latest/tables/automatic_comparison_rows_v2.csv \
  --out-dataset reports/latest/tables/automatic_comparison_training_dataset_v2.jsonl \
  2>&1 | tee runs/automatic_comparison_engine_v2.log

git add docs/AUTOMATIC_COMPARISON_ENGINE_v2.md \
  tools/build_automatic_comparison_engine_v2.py \
  scripts/RUN_AUTOMATIC_COMPARISON_ENGINE_V2.sh \
  reports/latest/AUTOMATIC_COMPARISON_ENGINE_V2.md \
  reports/latest/tables/automatic_comparison_rows_v2.csv \
  reports/latest/tables/automatic_comparison_training_dataset_v2.jsonl \
  manifests/latest/automatic_comparison_engine_v2.json

git commit -m "Update automatic comparison engine v2" || true
git push

echo "DONE automatic comparison engine v2. Main report: reports/latest/AUTOMATIC_COMPARISON_ENGINE_V2.md"
