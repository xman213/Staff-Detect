# Made By xman
#Version 2.1.8
import wmi
import os
import plyer.platforms.win.notification
import win10toast
import plyer
import subprocess
import requests
import time
import sys
import os
import win32gui, win32con





the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)


f = wmi.WMI()

flag = 0


while True:
 for process in f.Win32_Process():

    if "msrdcw.exe" == process.Name:
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast("Please Shut Down Your Computer","Someone May Have Remoted In Your Computer!")
        flag = 1
        time.sleep(1.0)
        break
    if "msrdc.exe" == process.Name:
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast("Please Shut Down Your Computer","Someone May Have Remoted In Your Computer!")
        flag = 1
        time.sleep(1.0)
        break
    if "mstsc.exe" == process.Name:
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast("Please Shut Down Your Computer","Someone May Have Remoted In Your Computer!")
        flag = 1
        time.sleep(1.0)
        break
    if "msra.exe" == process.Name:
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast("Please Shut Down Your Computer","Someone May Have Remoted In Your Computer!")
        flag = 1
        time.sleep(1.0)
        break
    if "RDAgentBootLoader.exe" == process.Name:
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast("Please Shut Down Your Computer","Someone May Have Remoted In Your Computer!")
        flag = 1
        time.sleep(1.0)
        break
    if "rdpclip.exe" == process.Name:
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast("Please Shut Down Your Computer","Someone May Have Remoted In Your Computer!")
        flag = 1
        time.sleep(1.0)
        break
    if "rdpinit.exe" == process.Name:
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast("Please Shut Down Your Computer","Someone May Have Remoted In Your Computer!")
        flag = 1
        time.sleep(1.0)
        break
    if "rpdinput.exe" == process.Name:
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast("Please Shut Down Your Computer","Someone May Have Remoted In Your Computer!")
        flag = 1
        time.sleep(1.0)
        break
if flag == 0:
    print("Application is not Running")





