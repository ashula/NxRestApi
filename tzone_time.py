# Python3 script
#
"""
#
#   tzone_time.py  in Python3 script
#   Ver-0.01, 03Apr2019, (c) Ashula
#
#  usage 1, no argument, use now() at Tokyo
#
#  $ python3 tzone_time.py
#  Asia/Tokyo          , 2019-04-03 23:40:47
#  Asia/Kolkata        , 2019-04-03 20:10:47
#  America/Los_Angeles , 2019-04-03 07:40:47
#
#  usage 2, specify Tokyo time only, date is from now()
#
#   $ python3 tzone_time.py  12:30:00
#   Asia/Tokyo          , 2019-04-03 12:30:00
#   Asia/Kolkata        , 2019-04-03 09:00:00
#   America/Los_Angeles , 2019-04-02 20:30:00
#
#  usage 3, specify date and Tokyo time
#  $ python3 tzone_time.py  2019-04-15 12:30:00
#  Asia/Tokyo          , 2019-04-15 12:30:00
#  Asia/Kolkata        , 2019-04-15 09:00:00
#  America/Los_Angeles , 2019-04-14 20:30:00
#
#
"""

import sys
from datetime import datetime, timedelta, timezone
import pytz      # need pip3 installation

JST = timezone(timedelta(hours=+9), 'JST')
tz_list = ['Asia/Tokyo','Asia/Kolkata','America/Los_Angeles']
localFormat = "%Y-%m-%d %H:%M:%S"

# Asia/Tokyo          2019-04-03 15:27:05
# Asia/Kolkata        2019-04-03 11:57:05
# America/Los_Angeles 2019-04-02 23:27:05

if __name__=='__main__':
    argv = sys.argv
    argc = len(argv)
#    print ("%d,%s" % (argc,argv))
    if argc == 1 :         # use current clock time
#        print ("argc==1")
        utcmoment_naive = datetime.now(JST)
    elif argc == 2 :       # use current clock date & get time from argv
#        print ("argc==2")
#        print ("%s" % argv[1])

        tdate = datetime.now(JST)
        tstr  = str(tdate.year) + '-' + str(tdate.month) + '-' + str(tdate.day) + ' ' + argv[1]
        utcmoment_naive = datetime.strptime(tstr,'%Y-%m-%d %H:%M:%S')        
    elif argc == 3:        # get date and time from argv
#        print ("argc==3")
#        print ("%s" % argv[1])
        tstr = argv[1] + ' ' + argv[2]
        utcmoment_naive = datetime.strptime(tstr,'%Y-%m-%d %H:%M:%S')
        
    else:
#        print ("argc=%d" % argc)
        print (argv)
        utcmoment_naive = datetime.now(JST)

    localFormat = "%Y-%m-%d %H:%M:%S"

    for tz in tz_list:
        localDatetime= utcmoment_naive.astimezone(pytz.timezone(tz))
        print ("%-20s, %s" % (tz, localDatetime.strftime(localFormat)))

