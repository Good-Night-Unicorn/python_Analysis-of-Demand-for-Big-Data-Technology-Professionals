import json
import os
import sys
from decimal import Decimal

json_list=[]
x_name = sys.argv[1]
# 输入来自标准输入 (STDIN)
for line in sys.stdin:
    line = line.strip()
    try:
        xname = line.split('\t')[0]
        yname = line.split('\t')[1]
    except Exception as e:
        continue
    if yname.__contains__(","):
        if len(json_list)==0:
            for name in yname.split(","):
                json_list.append([])
        for i,name in enumerate(yname.split(",")):
            d = next((item for item in json_list[i] if item.get(x_name) == xname), None)
            if d:
                d["total"] = str(round(Decimal(d["total"])+Decimal(name), 2))
            else:
                json_list[i].append({
                    x_name: xname,
                    "total": str(round(Decimal(name), 2))
                })

    else:
        d = next((item for item in json_list if item.get(x_name) == xname), None)
        if d:
            d["total"] = str(round(Decimal(d["total"])+Decimal(yname), 2))
        else:
            json_list.append({
                x_name: xname,
                "total": str(round(Decimal(yname), 2))
            })
print(json.dumps(json_list,ensure_ascii=False))