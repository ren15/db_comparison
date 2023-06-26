# Why

This repo aims at comparing different DB performance in ingesting market data.

Note: "DB" is used in a broad sense, it can be a database, a file, a message queue, etc.

## Benchmark method & metrics

1. We will try to load one day of tick-level trades data, and see which "streaming" solution has the shortest walltime.
2. Test ability to select data by time range.
3. Use the benchmark code in Rust as much as possible.

## Solutions to test

- Shared memory by using https://github.com/cloudflare/mmap-sync/ (Appending to a Vec)
- PostgreSQL
- TimescaleDB
- Redis
- ScyllaDB
- Redpanda




