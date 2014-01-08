#!/usr/bin/env sh

TABLE_NAME=insert_perf

dropdb --if-exists "$TABLE_NAME"
createdb "$TABLE_NAME"

psql "$TABLE_NAME" < create.sql
