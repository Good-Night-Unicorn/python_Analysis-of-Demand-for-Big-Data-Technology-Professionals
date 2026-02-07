# -*- coding:utf-8 -*-
import os
import sys
import json

json_list=[]
c_name = sys.argv[1]
# 输入来自标准输入 (STDIN)
for line in sys.stdin:
    line = line.strip()
    try:
        role = line.split('\t')[0]
    except Exception as e:
        continue
    d = next((item for item in json_list if item.get(c_name) == role), None)
    if d:
        d["total"] += 1
    else:
        json_list.append({
            c_name: role,
            "total": 1
        })
print(json.dumps(json_list,ensure_ascii=False))
