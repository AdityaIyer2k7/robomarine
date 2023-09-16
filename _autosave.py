# Place this file in your git folder
# Click to run, move mouse cursor to corner of screen to terminate
# Change commit rate by adjusting MINUTES constant

import time
import os

MINUTES = 1.5

try: import pyautogui
except Exception as e: os.system("pip install pyautogui")

import pyautogui as pgui

def saveAndCommit(timestamp):
  pgui.hotkey('ctrl', 's')
  time.sleep(5)
  os.system('git add *&git commit -m "Commit at {}"'.format(timestamp))

old = time.time()
while True:
  now = time.time()
  if now-old >= 60*MINUTES:
    saveAndCommit(now)
    old = now