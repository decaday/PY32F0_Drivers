================================================================================
                                样例使用说明
                             Sample Description
================================================================================
功能描述：
此样例演示了通过软件方式将RESET引脚改为普通GPIO。

Function descriptions:
This example demonstrates changing the RESET pin to regular GPIO through software.
================================================================================
测试环境：
测试用板：PY32F002B_STK
MDK版本： 5.28
IAR版本： 9.20

Test environment:
Test board: PY32F002B_STK
MDK Version: 5.28
IAR Version: 9.20
================================================================================
使用步骤：
1. 编译下载程序到MCU，并运行；
2. 请将MCU断电并重新上电；
3. RST键变为GPIO功能，LED亮；
4. 注释掉"MODE_PC0 OB_SWD_PB6_GPIO_PC0",打开"MODE_PC0 OB_SWD_PB6_NRST_PC0",
编译重新下载到MCU;
5. 将MCU断电并重新上电；
6. RST键变为RESET功能，LED亮；

Example execution steps:
1. Compile and download the program to MCU and run it;
2. Please turn off the MCU and power it back on;
3. RST key changes to GPIO function and LED lights up;
4. Annotate "MODE-PC0 OB_SWD-PB6_GPIO-PC0" and open "MODE-PC0 OB_SWD-PB6NRST-PC0",
Compile and download again to MCU;
5. Turn off the MCU and power it back on;
6. The RST key changes to the RESET function, and the LED lights up;

================================================================================
注意事项：

Notes:
================================================================================