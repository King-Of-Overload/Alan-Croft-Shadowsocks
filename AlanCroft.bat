@echo off
cd Alan
rem 关闭命令的回显状态,避免显示盘符等操作

echo 么么哒(づ￣ 3￣)づ，亲爱的同学，动一动你的小手指，选择一小下下，大千世界等着你，科学上网，可不要贪杯哦，回车键走着~~
rem 海外のサーバーを選ぶ

@echo ******************a. にほんのサーバ(一つ)******************
@echo.
@echo ******************b. にほんのサーバ(二つ)******************
@echo.
@echo ******************c. にほんのサーバ(三つ)******************
@echo.
@echo ******************d. シンガポールのサーバ(一つ)*************
@echo.
@echo ******************e. シンガポールのサーバ(二つ)*************
@echo.
@echo ******************f. シンガポールのサーバ(三つ)*************
@echo.
@echo ******************g. アメリカのサーバ(一つ)*************
@echo.

rem 接收用户输入的字符，进行判断
CHOICE /C abcdefg /M  一つ選んでください

rem execute main entrance
start python executeShadow.py %errorLevel%
pause

