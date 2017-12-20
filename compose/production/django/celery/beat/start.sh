#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset


celery -A investment_portfolio.taskapp beat -l INFO
