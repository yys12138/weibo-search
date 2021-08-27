# -*- coding: UTF-8 -*-
import sys
import os
import re

if len(sys.argv) < 2:
    print("参数个数异常")
    exit(-1)

nodeNum = int(sys.argv[1])
if nodeNum < 1:
    print("节点数参数异常")
    exit(-1)

# 获取开始下标
startIndex = 0
for fileName in os.listdir(os.path.dirname(os.path.abspath(__file__))):
    if fileName.endswith(".pid"):
        try:
            num = int(re.sub("\D", "", fileName))
        except:
            num = 0

        startIndex = num if num > startIndex else startIndex

print("当前节点：", startIndex)

for i in range(startIndex, startIndex + nodeNum):
    print("正在启动节点：", i + 1)
    # cmd_string = "nohup python -u main_Slave.py > run" + str(i + 1) + ".log 2>&1 &"
    cmd_string = "nohup python -u main_Slave.py > log" + str(i + 1) + "run.log 2>&1 & echo $! >> pid" + str(i + 1) + "run.pid"
    os.system(cmd_string)
