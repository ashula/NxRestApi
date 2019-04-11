# 
#  get dateime(timezone JST) in unix epoch uSec.
#
#    Ver-0.10, 11Apr2019, 1st implemntation.
#
#    timezone handling ,  Still not correct!!!!
#
'''
#   Usage1:  Get current JST local time in uSec from Unix Epoch.
#       $ python get_datetime_tz.py
#       1555010929
#
#   Usage2:  Get current time with timezone(JST or UCT) in uSec from Unix Epoch
#       $ python get_datetime_tz.py  JST         # int(datetime.now().strftime('%s'))
#       1555010929
#
#       $ python get_datetime_tz.py  UCT         # int(datetime.utcnow().strftime('%s'))
#       1554978524
#
#   Usage3:  Get current time with timezone('JST'only now) from Unix Epoch # datetime.datetime(2019, 4, 11, 19, 27, 47, 592963)
#       $ python get_datetime_tz.py 2019 4 11 19 27 47 592963 JST
#       1555010929
#
#       Usage3 is not well implemented yet.
#
'''
import sys
from datetime import datetime, timedelta
import pytz

def get_unix_epoch_uSec(dt,tz):
    if tz=='JST':
        dt.strftime('%s')


def get_datetime_tz_uSec(year, month, day, h, m, s, msec, tz):
    if tz =='JST':
#       print 'JST'
        r =  int(datetime(year, month, day, h, m, s, msec, tzinfo=pytz.timezone('Asia/Tokyo')).strftime('%s')) * 1000
    else:
        r=  int(datetime(year, month, day, h, m, s, msec,tzinfo=pytz.utc).strftime('%s')) * 1000
    return r

if __name__ == '__main__':
    sys_argv = sys.argv
#    print sys_argv
#    print len(sys_argv)
    if len(sys_argv) ==1:
        dt_tz = datetime.now()  # get local datetime in uSec
        print get_datetime_tz_uSec( \
            dt_tz.year,             \
            dt_tz.month,            \
            dt_tz.day,              \
            dt_tz.hour,             \
            dt_tz.minute,           \
            dt_tz.second,           \
            dt_tz.microsecond,      \
            'JST')
    elif len(sys_argv) ==2:
        if sys_argv[1]=='JST':
            dt_tz=datetime.now()   # get local datetime in uSec
        else:
            dt_tz=datetime.utcnow()   # get utc datetime in uSec
#        dt_tz = now.astimezone(pytz.timezone('Asia/Tokyo'))
        print get_datetime_tz_uSec( \
            dt_tz.year,             \
            dt_tz.month,            \
            dt_tz.day,              \
            dt_tz.hour,             \
            dt_tz.minute,           \
            dt_tz.second,           \
            dt_tz.microsecond,      \
            'JST')
    else:
        now=datetime.utcnow()     # get UTC datetime in uSec
        print get_datetime_tz_uSec( \
                int(sys_argv[1]),       # year  \
                int(sys_argv[2]),       # month \
                int(sys_argv[3]),       # day   \
                int(sys_argv[4]),       # hour  \
                int(sys_argv[5]),       # minute \
                int(sys_argv[6]),       # second \
                int(sys_argv[7]),       # micro second \
                pytz.utc        # tz   \
            )

