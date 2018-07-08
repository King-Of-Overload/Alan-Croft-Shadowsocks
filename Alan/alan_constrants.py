## basic constrants
import re

'''
@ file: alan_constrants
@ coding: utf-8 -*- 
@ Author: Alan-Croft-Mac (LXT)
'''
shadowAddress = 'https://my.ishadowx.net/' # main address
shadowHeaders = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0', }
# にほんのサーバ
Nihonn_mode_A = re.compile(
r'<span id=".*?jpa">(.+?)</span>.+<span id="port.*?">(.+?)</span>.+<span id="pwjpa">(.+?)</span>.+<h4>Method.(.+?)</h4>', re.S)
Nihonn_mode_B = re.compile(
    r'<span id=".*?jpb">(.+?)</span>.+<span id="port.*?">(.+?)</span>.+<span id="pwjpb">(.+?)</span>.+<h4>Method.(.+?)</h4>', re.S)
Nihonn_mode_C = re.compile(
    r'<span id=".*?jpc">(.+?)</span>.+<span id="port.*?">(.+?)</span>.+<span id="pwjpc">(.+?)</span>.+<h4>Method.(.+?)</h4>', re.S)
# シンガポールのサーバ
Singaporu_mode_A = re.compile(
    r'<span id=".*?sga">(.+?)</span>.+<span id="port.*?">(.+?)</span>.+<span id="pwsga">(.+?)</span>.+<h4>Method.(.+?)</h4>', re.S)
Singaporu_mode_B = re.compile(
    r'<span id=".*?sgb">(.+?)</span>.+<span id="port.*?">(.+?)</span>.+<span id="pwsgb">(.+?)</span>.+<h4>Method.(.+?)</h4>', re.S)
Singaporu_mode_C = re.compile(
    r'<span id=".*?sgc">(.+?)</span>.+<span id="port.*?">(.+?)</span>.+<span id="pwsgc">(.+?)</span>.+<h4>Method.(.+?)</h4>', re.S)

 # アメリカのサーバ
Amerika_mode_A = re.compile(
    r'<span id=".*?usa">(.+?)</span>.+<span id="port.*?">(.+?)</span>.+<span id="pwusa">(.+?)</span>.+<h4>Method.(.+?)</h4>', re.S)