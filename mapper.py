#!/usr/bin/env python3
import sys
import csv

group_col = 7      # column index for categorical field (e.g., Education)
value_col = 3      # column index for numeric field (e.g., Income)

for line in sys.stdin:
    line = line.strip()
    if not line or line.startswith("ID"):  # skip header
        continue
    fields = next(csv.reader([line]))
    try:
        key = fields[group_col]
        value = float(fields[value_col])
        print(f"{key}\t{value}")
    except Exception:
        continue