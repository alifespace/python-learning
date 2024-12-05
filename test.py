from datetime import datetime
import pytz

utc_now = datetime.now(tz=pytz.utc)
print("UTC now: ", utc_now)

pacific_time = utc_now.astimezone(pytz.timezone('US/Pacific'))
print("Pacific time now: ", pacific_time.strftime("%Y-%m-%d %H:%M:%S %z"))

