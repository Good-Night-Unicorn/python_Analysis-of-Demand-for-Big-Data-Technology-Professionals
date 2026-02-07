# -*- coding:utf-8 -*-
import sys
import csv
import os
# 读取环境变量中的 参数
index = int(sys.argv[1])
# 输入来自标准输入 (STDIN)
for line in sys.stdin:
    try:
        line = line.strip()
        lists = line.split(',')
        if lists[0] == "id":
            continue
        if sys.stdin.isatty():
            print(f"{lists[index]}")
        else:
            print(f"{lists[index]}\t")
    except Exception as e:
        continue