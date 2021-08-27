# -*- coding: UTF-8 -*-
import sys
import os
import time

if len(sys.argv) < 2:
    print("参数个数异常")
    exit(-1)

nodeNum = int(sys.argv[1])
if nodeNum < 1:
    print("节点编号参数异常")
    exit(-1)

nodeNum = str(nodeNum)
print("正在kill节点：", nodeNum)

fileName = "pid" + nodeNum + "run.pid"
try:
    file = open(fileName, 'r')
except:
    print("节点：" + nodeNum + "已被杀死")
    exit(-1)

pid = file.read()
cmd_string = "kill -9 " + pid
os.system(cmd_string)

file.close()

cmd_string = "rm -rf " + fileName
os.system(cmd_string)

# 移动之前的日志
fileName = "log" + nodeNum + "run.log"
if os.path.exists(fileName):
    cmd_string = "mv " + fileName + " done" + nodeNum + "_" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + "run.log"
    os.system(cmd_string)
