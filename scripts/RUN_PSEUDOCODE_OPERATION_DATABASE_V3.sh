#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs
PYTHONUNBUFFERED=1 python tools/build_pseudocode_operation_database_v3.py \
  --pseudo-v2 reports/latest/tables/pseudocode_operation_database_v2.csv \
  --inner-heads reports/latest/tables/edgeconv_inner_trace_heads.csv \
  --inner-events reports/latest/tables/edgeconv_inner_trace_events.csv \
  --rankings reports/latest/tables/question_driven_head_rankings.csv \
  --residual manifests/latest/known_observable_residual_v1.json \
  --out-csv reports/latest/tables/pseudocode_operation_database_v3.csv \
  --out-jsonl reports/latest/tables/pseudocode_operation_database_v3.jsonl \
  --out-json manifests/latest/pseudocode_operation_database_v3.json \
  --out-md reports/latest/PSEUDOCODE_OPERATION_DATABASE_V3.md \
  2>&1 | tee runs/pseudocode_operation_database_v3.log

git add docs/01_method/ROUTE_AWARE_PSEUDOCODE_v3.md \
  tools/build_pseudocode_operation_database_v3.py scripts/RUN_PSEUDOCODE_OPERATION_DATABASE_V3.sh \
  reports/latest/PSEUDOCODE_OPERATION_DATABASE_V3.md reports/latest/tables/pseudocode_operation_database_v3.csv reports/latest/tables/pseudocode_operation_database_v3.jsonl manifests/latest/pseudocode_operation_database_v3.json

git commit -m "Update route-aware pseudocode operation database v3" || true
git push

echo "DONE route-aware pseudocode v3. Main report: reports/latest/PSEUDOCODE_OPERATION_DATABASE_V3.md"
