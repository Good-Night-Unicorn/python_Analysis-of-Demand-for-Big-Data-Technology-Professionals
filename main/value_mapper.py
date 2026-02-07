import os
import sys
from decimal import Decimal

# 读取环境变量中的 title 参数
x_index = int(sys.argv[1])
y_index =  sys.argv[2]
for line in sys.stdin:
    try:
        # 读取输入数据, 按照逗号分隔
        lists = line.strip().split(',')

        if lists[0]=="id":
            continue
        x_value = lists[x_index]
        if y_index.__contains__(","):
            y_value=""
            for i,y in enumerate(y_index.split(",")):
                if i >= len(y_index.split(","))-1:
                    y_value = y_value + lists[int(y)]
                else:
                    y_value = y_value + lists[int(y)] + ","
            print(f"{x_value}\t{y_value}")
        else:
            print(f"{x_value}\t{lists[int(y_index)]}")
    except Exception as e:
        continue
