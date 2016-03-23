import os
import time
import signal
import signals_common

""" Signal Trapping Python Script """

""" Objective: Write a python script that redirects the signal you send it to a specified process via GNU/Linux. """


print('My PID is ', os.getpid())

# Print Signal Received
def printsignal(signum, stack):
    print('Received a signal called ', signum)
    targetpid = input('Specify the PID of your deepest enemy.')
    try:
       val = int(targetpid)
    except ValueError:
       print("That's not an int!")
    os.kill(targetpid, signum)

# Look back to beginning
while True:
    signals_common.cycle()
    print('Waiting...')
    time.sleep(3)
