from datetime import datetime
import pytz

utc_now = datetime.now(tz=pytz.utc)
print("UTC now: ", utc_now)

pacific_time = utc_now.astimezone(pytz.timezone('US/Pacific'))
print("Pacific time now: ", pacific_time.strftime("%Y-%m-%d %H:%M:%S %z"))

unit = 1000
if 100 < unit <=200:
    print("between")
else:
    print("out")

a1, b1, c1 = 1, 2, 3
print(a1, b1, c1)

i=9
print(int(i**0.5))

