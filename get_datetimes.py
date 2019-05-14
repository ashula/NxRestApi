#! 
#    get uSEC
#
#    Ver-0.10, 20190513, 1st inplementation.
#
#
#    get pair of date-time values to Unix epoch uSec values.
#
#    dtz1,dtz2 = get_datetimes([y1,M1,d1,h1,m1,s1,'JST'],[y2,M2,d2,h2,m2,s2,'JST'])
#
#
import sys
from datetime import datetime, timedelta
import pytz 
import get_datetime_tz as dttz

def get_datetimes(dt1,dt2):
    print dt1
    print dt2
    year1 = dt1[0]
    month1= dt1[1]
    day1  = dt1[2]
    hour1 = dt1[3]
    minute1 = dt1[4]
    second1 = dt1[5]
    dtz_uSec1 = dttz.get_datetime_tz_uSec(year1, month1, day1, hour1, minute1, second1,0,'JST')
    year2 = dt2[0]
    month2 = dt2[1]
    day2  = dt2[2]
    hour2 = dt2[3]
    minute2 = dt2[4]
    second2 = dt2[5]
    dtz_uSec2 = dttz.get_datetime_tz_uSec(year2, month2, day2, hour2, minute2, second2,0,'JST')

    return dtz_uSec1, dtz_uSec2


if  __name__=='__main__':
    dt1 = [2019, 04, 15,  8, 20, 55]
    dt2 = [2019, 05, 13,  0,  0,  0]
  
    dtz_uSec1, dtz_uSec2 = get_datetimes(dt1,dt2)
    
    print dtz_uSec1*1000, dtz_uSec2*1000
