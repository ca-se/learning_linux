import os
import time
import signal

import signals_common

""" Signal Trapping Python Script """

""" Objective: Write a python script that prints the signal you send it via GNU/Linux. """

print('My PID is ', os.getpid())

# Look back to beginning
while True:
    signals_common.cycle()
    print('Waiting...')
    time.sleep(3)
