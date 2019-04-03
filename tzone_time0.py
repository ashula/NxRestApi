# Python3 script
#
#
#  Version-0.10, 03Apr2019, (c)t.m
#
#
#
#
import sys
import get_argv
from datetime import datetime
import pytz      # need pip3 installation


tz_list = ['Asia/Tokyo','Asia/Kolkata','America/Los_Angeles']

utcmoment_naive = datetime.utcnow()
utcmoment = utcmoment_naive.replace(tzinfo=pytz.utc)

localFormat = "%Y-%m-%d %H:%M:%S"

for tz in tz_list:
    localDatetime= utcmoment.astimezone(pytz.timezone(tz))
    print ("%-20s, %s" % (tz, localDatetime.strftime(localFormat)))

# Asia/Tokyo          2019-04-03 15:27:05
# Asia/Kolkata        2019-04-03 11:57:05
# America/Los_Angeles 2019-04-02 23:27:05
#
#if __name__=='__main__':
#    if get_argc ==0 :
#        utcmoment_naive = datetime.utcnow()
#     
#    els if get_argc ==1:
#        argv = get_argv()
#        h = argv[1][1]
#        m = argv[1][2]
#        s = argv[1][3]
#
#    utcmoment = utcmoment_naive.replace(tzinfo=pytz.utc)
#
#    else:

