#!/bin/bash

import signal

class JsDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__

signal_map = JsDict()
for attr,val in vars(signal).items():
    if attr.startswith('SIG'):
        signal_map[attr] = val

# Print Signal Received
def printsignal(signum, stack):
    print('Received a signal called ', signum)
    
# Cycle through targets to find
def cycle():
    signal.signal(signal.SIGABRT, printsignal)
    signal.signal(signal.SIGALRM, printsignal)
    signal.signal(signal.SIGBUS, printsignal)
    signal.signal(signal.SIGCHLD, printsignal)
    signal.signal(signal.SIGCONT, printsignal)
    signal.signal(signal.SIGFPE, printsignal)
    signal.signal(signal.SIGHUP, printsignal)
    signal.signal(signal.SIGILL, printsignal)
    signal.signal(signal.SIGINT, printsignal)
    signal.signal(signal.SIGPIPE, printsignal)
    signal.signal(signal.SIGPOLL, printsignal)
    signal.signal(signal.SIGPROF, printsignal)
    signal.signal(signal.SIGQUIT, printsignal)
    signal.signal(signal.SIGSEGV, printsignal)
    signal.signal(signal.SIGSYS, printsignal)
    signal.signal(signal.SIGTERM, printsignal)
    signal.signal(signal.SIGTRAP, printsignal)
    signal.signal(signal.SIGTSTP, printsignal)
    signal.signal(signal.SIGTTIN, printsignal)
    signal.signal(signal.SIGTTOU, printsignal)
    signal.signal(signal.SIGURG, printsignal)
    signal.signal(signal.SIGUSR1, printsignal)
    signal.signal(signal.SIGUSR2, printsignal)
    signal.signal(signal.SIGVTALRM, printsignal)
    signal.signal(signal.SIGXCPU, printsignal)
    signal.signal(signal.SIGXFSZ, printsignal)

print 'SIGKILL is signal #%d' % signal_map.SIGKILL
