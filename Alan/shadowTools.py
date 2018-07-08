from alan_constrants import *
import requests
import json
import subprocess
import os

'''
@ class: ShadowTools
@ coding: utf-8 -*- 
@ Author: Alan-Croft-Mac(LXT)
'''
class ShadowTools (object):

    # 初始化构造方法
    '''
    Parameters:
    @ shadowPath  ShadowSocks 可执行文件路径
    @ shadowConfigPath ShadowSocks用户配置文件路径
    '''
    def __init__(self, shadowPath, shadowConfigPath):
        super(ShadowTools, self).__init__()
        self.shadowPath = shadowPath #声明类属性
        self.shadowConfigPath = shadowConfigPath #声明类属性
        self.isCrash = False #应用是否崩溃
        # 获取页面的html数据
        self.retrieveHtmlContent()
    
    '''
    Parameters:
    @ nil
    Functions:
    获取html页面内容
    '''
    def retrieveHtmlContent(self):
        try:
            response = requests.get(url = shadowAddress, headers = shadowHeaders)
            if response.status_code:
                self.htmlContent = response.text
                with open('content.txt', 'w+') as fileData:
                    fileData.write(self.htmlContent)
        except Exception as croft:
            print('Net Error:', croft)
            self.isCrash = True
            os.system('pause')
        finally:
            if self.isCrash:
                exit(0) #若出现异常，则退出
    

    #设置访问的数据服务器参数类型
    '''
    Parameters:
      @ mode 请求服务器类型

    "configs": [
    {
      "server": "jpa.isxa.top",
      "server_port": 10759,
      "password": "isx.yt-05218725",
      "method": "aes-256-cfb",
      "plugin": "",
      "plugin_opts": "",
      "plugin_args": "",
      "remarks": "",
      "timeout": 5
    },
    '''
    def shadowToolsWithServerMode(self, mode):
        #使用正则表达式匹配html前缀
        matchResult = re.findall(mode, self.htmlContent)[0] #list 类型
        with open('mathresult.txt', 'w+') as fileData:
            resultStr = ''
            for result in matchResult:
                resultStr += result
            fileData.write(resultStr)

        #获取数据
        serverName = matchResult[0].replace('\n', '') # server address
        serverPort = matchResult[1].replace('\n', '') # server port
        serverPwd = matchResult[2].replace('\n', '')  #  server password
        serverMethod = matchResult[3].replace('\n', '') # server request method

        writeData = None # 创建一个变量用于存放一个json数据
        try:
            with open(self.shadowConfigPath, 'r+', encoding = 'utf-8') as f:
                writeData = json.load(f) #用json模块加载json文件
            writeData['configs'][0]['server'] = serverName
            writeData['configs'][0]['server_port'] = serverPort
            writeData['configs'][0]['password'] = serverPwd
            writeData['configs'][0]['method'] = serverMethod
            with open(self.shadowConfigPath, 'w', encoding = 'utf-8') as f:
                json.dump(writeData, f, indent= 4) #序列化json对象并写入文件,缩进4个字符
        except Exception as croft:
            print('IO Error:', croft)
            os.system('pause')

        # 如果主程序正在运行，那么杀掉 调用子进程模块 tashkill命令 /f为强制  /im为镜像名
        subprocess.call('taskkill /f /im shadowsocks.exe', stdout = subprocess.PIPE)
        subprocess.Popen(self.shadowPath) #调用线程管道重新打开
        
        








