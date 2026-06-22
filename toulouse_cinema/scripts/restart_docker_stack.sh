#!/bin/bash
# Restart toulouse_cinema Docker stack after daily seances update.
set -euo pipefail

PROJECT_DIR="/home/massyl/vps_maths_cine_cv/toulouse_cinema"
LOG_FILE="$PROJECT_DIR/logs/docker-restart.log"

mkdir -p "$PROJECT_DIR/logs"
{
  echo "=== Docker stack restart at $(date) ==="
  cd "$PROJECT_DIR"
  docker-compose down
  sleep 2
  docker-compose up --build -d
  echo "=== Restart completed at $(date) ==="
} >> "$LOG_FILE" 2>&1
