#coding: utf-8
# make day-time based label
#
#

import datetime
import os
import sys

def get_now_daytime_label():
    now = datetime.datetime.now()
    label = now.strftime('%Y%m%d-%H:%M')
    return label
    
def get_now_day_label():
    now = datetime.datetime.now()
    label = now.strftime('%Y%m%d')
    return label

if (__name__ == '__main__'):
   label = get_now_day_label()
   print 'Now Day =%s.' %  label 
   label = get_now_daytime_label()
   print 'Now Time=%s.' %  label 
else:
   pass