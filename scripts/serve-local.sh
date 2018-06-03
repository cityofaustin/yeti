#!/usr/bin/env bash

set -o errexit

TAG='yeti:local'

docker build --tag "$TAG" .
docker run \
    --rm \
    --name yeti \
    --tty --interactive \
    --publish 8888:80 \
    --volume "$PWD:/app" \
    "$TAG" "$@"
