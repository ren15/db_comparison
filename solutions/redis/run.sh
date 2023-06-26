#!/bin/bash

set -ueo pipefail

cd "$(dirname "$0")"

# start redis
docker run --net=host -d redis:lastest


