import multiprocessing

import paramiko
import pymysql
from util.configread import config_read
import pandas as pd
import configparser
import subprocess
from django.http import JsonResponse
from hdfs import InsecureClient
import os
from util.CustomJSONEncoder import CustomJsonEncoder
from util.codes import normal_code, system_error_code

# 获取当前文件路径的根目录
parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dbtype, host, port, user, passwd, dbName, charset,hasHadoop = config_read(os.path.join(parent_directory,"config.ini"))

# MySQL 连接配置
mysql_config = {
    'host': host,
    'user':user,
    'password': passwd,
    'database': dbName,
    'port':port
}

hadoop_path="D:/singlehadoop/hadoop-3.3.0"
# 连接到 MySQL 数据库
connection = pymysql.connect(**mysql_config)
# 初始化 HDFS 客户端
hadoop_client = InsecureClient('http://localhost:9870')

#上传分析数据和mapreduce代码
def upload_csv_mapreduce_hadoop():
    # 查询数据
    query = "SELECT * FROM zhipindsj"
    df = pd.read_sql(query, connection)
    local_csv_path = os.path.join(parent_directory,"zhipindsj.csv")
    # 导出为 CSV 文件
    df.to_csv(local_csv_path, index=False)
    print(f"数据成功导出到 CSV 文件: {local_csv_path}")
    hdfs_csv_path = '/input/zhipindsj.csv'
    # 目标 HDFS 路径
    if hadoop_client.status(hdfs_csv_path,strict=False):
        # 删除HDFS上的文件
        hadoop_client.delete(hdfs_csv_path)
    # 上传CSV文件到HDFS
    hadoop_client.upload(hdfs_csv_path, local_csv_path)
    print(f"CSV 文件成功上传到 HDFS: {hdfs_csv_path}")
    # 关闭连接
    connection.close()
    parent_path = os.path.dirname(os.path.abspath(__file__))

    #上传groupmapreduce代码
    group_mapper_local_path = os.path.join(parent_path,'group_mapper.py')
    group_mapper_hdfs_path = '/input/group_mapper.py'
    group_reducer_local_path = os.path.join(parent_path,'group_reducer.py')
    group_reducer_hdfs_path = '/input/group_reducer.py'
    if not hadoop_client.status(group_mapper_hdfs_path,strict=False):
        hadoop_client.upload(group_mapper_hdfs_path, group_mapper_local_path)
    if not hadoop_client.status(group_reducer_hdfs_path,strict=False):
        hadoop_client.upload(group_reducer_hdfs_path, group_reducer_local_path)

#执行分析命令
def send_cmd():

    job_commands = [
    [
        f"{hadoop_path}/bin/hadoop.cmd", "jar", f"{hadoop_path}/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar",
        "-files", "\"hdfs://localhost:9000/input/group_mapper.py,hdfs://localhost:9000/input/group_reducer.py\"",
        "-mapper", f"\"python group_mapper.py {csv_index('zhipindsj.csv','brandname')}\"",
        "-reducer", "\"python group_reducer.py brandname\"",
        "-input", "hdfs://localhost:9000/input/zhipindsj.csv",
        "-output", "hdfs://localhost:9000/output/zhipindsj/groupbrandname"
    ],
    [
        f"{hadoop_path}/bin/hadoop.cmd", "jar", f"{hadoop_path}/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar",
        "-files", "\"hdfs://localhost:9000/input/group_mapper.py,hdfs://localhost:9000/input/group_reducer.py\"",
        "-mapper", f"\"python group_mapper.py {csv_index('zhipindsj.csv','cityname')}\"",
        "-reducer", "\"python group_reducer.py cityname\"",
        "-input", "hdfs://localhost:9000/input/zhipindsj.csv",
        "-output", "hdfs://localhost:9000/output/zhipindsj/groupcityname"
    ],
    [
        f"{hadoop_path}/bin/hadoop.cmd", "jar", f"{hadoop_path}/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar",
        "-files", "\"hdfs://localhost:9000/input/group_mapper.py,hdfs://localhost:9000/input/group_reducer.py\"",
        "-mapper", f"\"python group_mapper.py {csv_index('zhipindsj.csv','jobdegree')}\"",
        "-reducer", "\"python group_reducer.py jobdegree\"",
        "-input", "hdfs://localhost:9000/input/zhipindsj.csv",
        "-output", "hdfs://localhost:9000/output/zhipindsj/groupjobdegree"
    ],
    [
        f"{hadoop_path}/bin/hadoop.cmd", "jar", f"{hadoop_path}/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar",
        "-files", "\"hdfs://localhost:9000/input/group_mapper.py,hdfs://localhost:9000/input/group_reducer.py\"",
        "-mapper", f"\"python group_mapper.py {csv_index('zhipindsj.csv','jobexperience')}\"",
        "-reducer", "\"python group_reducer.py jobexperience\"",
        "-input", "hdfs://localhost:9000/input/zhipindsj.csv",
        "-output", "hdfs://localhost:9000/output/zhipindsj/groupjobexperience"
    ],
    [
        f"{hadoop_path}/bin/hadoop.cmd", "jar", f"{hadoop_path}/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar",
        "-files", "\"hdfs://localhost:9000/input/group_mapper.py,hdfs://localhost:9000/input/group_reducer.py\"",
        "-mapper", f"\"python group_mapper.py {csv_index('zhipindsj.csv','brandIndustry')}\"",
        "-reducer", "\"python group_reducer.py brandIndustry\"",
        "-input", "hdfs://localhost:9000/input/zhipindsj.csv",
        "-output", "hdfs://localhost:9000/output/zhipindsj/groupbrandIndustry"
    ],
    [
        f"{hadoop_path}/bin/hadoop.cmd", "jar", f"{hadoop_path}/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar",
        "-files", "\"hdfs://localhost:9000/input/group_mapper.py,hdfs://localhost:9000/input/group_reducer.py\"",
        "-mapper", f"\"python group_mapper.py {csv_index('zhipindsj.csv','brandscalename')}\"",
        "-reducer", "\"python group_reducer.py brandscalename\"",
        "-input", "hdfs://localhost:9000/input/zhipindsj.csv",
        "-output", "hdfs://localhost:9000/output/zhipindsj/groupbrandscalename"
    ],
    ]

    processes = []
    for job_command in job_commands:
        fileName = job_command[-1].split("/output/")[1].split("/")[1].strip()
        table_name = job_command[-3].split("/input/")[1].split(".csv")[0].strip()
        p = multiprocessing.Process(target=run_mapreduce_job_on_remote,args=(job_command, table_name, fileName))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

def run_mapreduce_job_on_remote(job_command,tableName,fileName):
    try:
        output_path = f'/output/{tableName}/{fileName}'
        if hadoop_client.status(output_path, strict=False):
            #删除 HDFS 上的文件
            hadoop_client.delete(output_path,recursive=True)
        subprocess.run(job_command, check=True)
        hadoop_client.download(output_path+"/part-00000",os.path.join(parent_directory,f"{tableName}_{fileName}.json"),overwrite=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing Hadoop job: {e}")
#查找字段对应坐标
def csv_index(file_path,columnname):
    first_line = pd.read_csv(os.path.join(parent_directory,file_path)).columns.tolist()
    index = ""
    if columnname.__contains__(","):
        for i,column in enumerate(columnname.split(",")):
            if i >= len(columnname.split(","))-1:
                index = index + first_line.index(column)
            else:
                index = index + first_line.index(column) + ","
    else:
        index = first_line.index(columnname)
    return index

#hadoop分析
def hadoop_analyze(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": {}}
        try:
            upload_csv_mapreduce_hadoop()
            send_cmd()
            return JsonResponse(msg, encoder=CustomJsonEncoder)
        except Exception as e:
            msg['code']=system_error_code
            msg['msg'] = f"发生错误：{e}"
            return JsonResponse(msg, encoder=CustomJsonEncoder)
