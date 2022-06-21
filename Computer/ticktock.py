from dateutil.tz import gettz
import datetime as dt


datatime = False
datatimesettings1 = False
if not datatime:
        ddatatime = dt.datetime.now(gettz('Australia/Melbourne'))
        dddatatime = f"Today is {ddatatime:%D %A %I:%M %p}"
        print(dddatatime)
        if not datatimesettings1:
            datatime = True