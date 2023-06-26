#!/bin/bash

set -ueo pipefail

cd "$(dirname "$0")"

# start redis
docker run --net=host -d redis:7

python3 read_and_insert.py


