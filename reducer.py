#!/usr/bin/env python3
import sys

AGGREGATION = "avg"   # choose from: sum, avg, max, min, count

current_key = None
values = []

def output_result(key, vals):
    if AGGREGATION == "sum":
        result = sum(vals)
    elif AGGREGATION == "avg":
        result = sum(vals) / len(vals)
    elif AGGREGATION == "max":
        result = max(vals)
    elif AGGREGATION == "min":
        result = min(vals)
    elif AGGREGATION == "count":
        result = len(vals)
    else:
        result = sum(vals)
    print(f"{key}\t{result}")

for line in sys.stdin:
    key, val = line.strip().split('\t')
    val = float(val)
    if current_key == key:
        values.append(val)
    else:
        if current_key is not None:
            output_result(current_key, values)
        current_key = key
        values = [val]

if current_key is not None:
    output_result(current_key, values)