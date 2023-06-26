# Why

This repo aims at comparing different DB performance in ingesting market data.

Note: "DB" is used in a broad sense, it can be a database, a file, a message queue, etc.

## Benchmark method & metrics

1. We will try to load one day of tick-level trades data, and see which "streaming" solution has the shortest walltime.
2. Test ability to select data by time range.
3. Use the benchmark code in Rust as much as possible.

### Data to record
```
               exchange   symbol         timestamp   local_timestamp          id  side    price  amount
0       binance-futures  BTCUSDT  1672531204118000  1672531206257612  3166744581  sell  16537.5   0.004
1       binance-futures  BTCUSDT  1672531204178000  1672531206346873  3166744582   buy  16537.6   0.116
2       binance-futures  BTCUSDT  1672531204178000  1672531206346988  3166744583   buy  16537.6   0.034
3       binance-futures  BTCUSDT  1672531204198000  1672531206365813  3166744584   buy  16537.6   0.082
4       binance-futures  BTCUSDT  1672531204209000  1672531206390946  3166744585  sell  16537.5   0.002
```

## Solutions to test

- Shared memory by using https://github.com/cloudflare/mmap-sync/ (Appending to a Vec)
- PostgreSQL
- TimescaleDB
- Redis
- ScyllaDB
- Redpanda




