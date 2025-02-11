
from time import localtime

current_time = localtime()

current_hourspassed = current_time.tm_hour
current_minute = current_time.tm_min

target_hoursleft = 0
target_day = 14
target_month = 2

days_leftinhr = (target_day - current_time.tm_mday) * 24


hours_left = days_leftinhr + (target_hoursleft - current_hourspassed) - (current_minute / 60)

# target_hour - current_hourspassed is just seeing how many hours have passed and subtracts the passing hours until
#  hours_left reaches 0, target_hoursleft = 0 isnt defined as 12:00AM, it is defined as the amount of hours we WANT left until it reaches 12:00AM, which is 0.

print("There are", hours_left, "hours left until Valentine's Day!")
