#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs

# Phase 1 goal: gather enough Hqql<->Tbl confused events to reason about
# physical regimes, not just a few examples.
#
# Use staged runs to avoid OOM:
#   PHASE1_STAGE=medium bash scripts/RUN_PHASE1_HQQL_TBL_FULL_STATISTICS_V1.sh
#   PHASE1_STAGE=large  bash scripts/RUN_PHASE1_HQQL_TBL_FULL_STATISTICS_V1.sh
#   PHASE1_STAGE=full   bash scripts/RUN_PHASE1_HQQL_TBL_FULL_STATISTICS_V1.sh

STAGE="${PHASE1_STAGE:-medium}"
case "$STAGE" in
  small)
    SPF="${SAMPLES_PER_FILE:-256}"
    MF="${MAX_FILES:-20}"
    ;;
  medium)
    SPF="${SAMPLES_PER_FILE:-1024}"
    MF="${MAX_FILES:-100}"
    ;;
  large)
    SPF="${SAMPLES_PER_FILE:-4096}"
    MF="${MAX_FILES:-1000}"
    ;;
  full)
    SPF="${SAMPLES_PER_FILE:-999999}"
    MF="${MAX_FILES:-999999}"
    ;;
  *)
    echo "Unknown PHASE1_STAGE=$STAGE. Use small|medium|large|full" >&2
    exit 2
    ;;
esac

echo "PHASE1 stage=$STAGE samples_per_file=$SPF max_files=$MF"

PYTHONUNBUFFERED=1 python tools/hqql_tbl_confusion_physics_regime_v1.py \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "$SPF" \
  --max-files "$MF" \
  --device "${DEVICE:-cuda}" \
  --out-events reports/latest/tables/hqql_tbl_confusion_physics_events.csv \
  --out-summary reports/latest/tables/hqql_tbl_confusion_physics_summary.csv \
  --out-json manifests/latest/hqql_tbl_confusion_physics_regime_v1.json \
  --out-md reports/latest/HQQL_TBL_CONFUSION_PHYSICS_REGIME_V1.md \
  2>&1 | tee "runs/phase1_hqql_tbl_${STAGE}.log"

PYTHONUNBUFFERED=1 python tools/phase1_hqql_tbl_stats_gate_v1.py \
  --summary reports/latest/tables/hqql_tbl_confusion_physics_summary.csv \
  --manifest manifests/latest/hqql_tbl_confusion_physics_regime_v1.json \
  --min-confused "${MIN_CONFUSED:-100}" \
  --out-json manifests/latest/phase1_hqql_tbl_stats_gate_v1.json \
  --out-md reports/latest/PHASE1_HQQL_TBL_STATS_GATE_V1.md \
  2>&1 | tee -a "runs/phase1_hqql_tbl_${STAGE}.log"

git add docs/02_physics/PHYSICS_DISCOVERY_4_PHASE_PIPELINE_v1.md \
  tools/phase1_hqql_tbl_stats_gate_v1.py scripts/RUN_PHASE1_HQQL_TBL_FULL_STATISTICS_V1.sh \
  reports/latest/HQQL_TBL_CONFUSION_PHYSICS_REGIME_V1.md reports/latest/PHASE1_HQQL_TBL_STATS_GATE_V1.md \
  reports/latest/tables/hqql_tbl_confusion_physics_events.csv reports/latest/tables/hqql_tbl_confusion_physics_summary.csv \
  manifests/latest/hqql_tbl_confusion_physics_regime_v1.json manifests/latest/phase1_hqql_tbl_stats_gate_v1.json

git commit -m "Update Phase 1 Hqql Tbl full statistics" || true
git push

echo "DONE Phase 1 Hqql/Tbl stats. Reports: reports/latest/HQQL_TBL_CONFUSION_PHYSICS_REGIME_V1.md and reports/latest/PHASE1_HQQL_TBL_STATS_GATE_V1.md"
