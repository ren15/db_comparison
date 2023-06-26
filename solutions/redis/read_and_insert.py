import time

import pandas as pd
import redis

if __name__ == "__main__":
    df = pd.read_csv("../../data/trades.csv")
    r = redis.Redis(host="localhost", port=6379, db=0)
    start_time = time.time()
    for index, row in df.iterrows():
        r.set(row["id"], row.to_json())
    print(f"--- {time.time() - start_time} seconds ---")
