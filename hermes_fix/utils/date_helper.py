from datetime import datetime, timedelta
from dateutil import tz, parser

def inside_time_range(current_time, start_time, end_time):
    if (current_time >= start_time) and (current_time <= end_time):
        return True

    return False


def get_session_times(dt, time_zone, start_time_str, end_time_str):
    start_time = parser.parse(start_time_str, default=dt)
    end_time = parser.parse(end_time_str, default=dt)
    increment = timedelta(days=1)

    #To test if the weekly compare day of week in dt with offset by day dt
    dt_offset = dt + timedelta(days=1)
    if parser.parse(start_time_str, default=dt).weekday() == parser.parse(start_time_str, default=dt_offset).weekday():
        increment = timedelta(days=7)

    #if logout is before logon, move it forward
    if end_time < start_time:
        end_time += increment

    #if both times are in the future and de-incremented end_time is still greater than current, move both back 
    if start_time > dt and end_time > dt and end_time - increment > dt:
        start_time -= increment
        end_time -= increment

    return start_time, end_time, increment
