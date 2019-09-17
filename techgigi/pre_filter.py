# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 12:38:25 2019

@author: Thangarajan
"""

import datetime

class Logger(object):
    def log(self, message):
        print (message)

class TimestampLogger(Logger):
    def log(self, message):
        message = "{ts} {msg}".format(ts=datetime.datetime.now().isoformat(),
                                      msg=message)
        super(TimestampLogger, self).log(message)
        
l = Logger()
l.log('ERROR')

t = TimestampLogger()
t.log('ERROR')
