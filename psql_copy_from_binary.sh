#!/usr/bin/env bash

set -e

TABLE_NAME=insert_perf

make setup

sh create.sh

python/_virtualenv/bin/python python/run_psycopg2.py

mkdir -p _copy
psql "$TABLE_NAME" -c "COPY albums TO STDOUT WITH (FORMAT binary)" > _copy/binary_albums
psql "$TABLE_NAME" -c "COPY songs TO STDOUT WITH (FORMAT binary)" > _copy/binary_songs

sh create.sh

time psql "$TABLE_NAME" -c "COPY albums FROM STDIN WITH (FORMAT binary)" < _copy/binary_albums
time psql "$TABLE_NAME" -c "COPY songs FROM STDIN WITH (FORMAT binary)" < _copy/binary_songs

