import sys
import os
import alan_constrants
from alan_constrants import *
from shadowTools import *

'''
@ file: executeShadow
@ coding: utf-8 -*- 
@ Author: Alan-Croft-Mac (LXT)
'''

# shadow路径
shadowPath = '../Shadowsocks.exe' # relative path

#shadow config file path
shadowConfigPath = '../gui-config.json'

#判断是否被bat直接调用运行
if __name__ == '__main__':
    #TODO:传入exe执行程序与配置文件路径
    shadowTools = ShadowTools(shadowPath = shadowPath, shadowConfigPath = shadowConfigPath)
    #定义模式列表
    modeList = [Nihonn_mode_A, Nihonn_mode_B, Nihonn_mode_C, Singaporu_mode_A, Singaporu_mode_B, 
               Singaporu_mode_C, Amerika_mode_A]
    try:
        print(int(sys.argv[1]) - 1) #获得系统参数索引值
        #os.system('pause')
        mode = modeList[int(sys.argv[1]) - 1]# retrieve user paramter
        #TODO: 传入用户选择的模式
        shadowTools.shadowToolsWithServerMode(mode = mode)
        os.system('pause')
    except IndexError as croft:
        print('index error:.', croft)
        os.system('pause')


