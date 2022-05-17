def number_to_time_conversion(number):
    hour = number // 60
    minutes = number % 60
    plural_hour = "hour,"
    min_plural = "minute"
    if number == 0:
        plural_hour = "hours,"
        min_plural = "minutes"
    if hour > 1 or hour == 0:
        plural_hour = "hours,"
    if minutes > 1 or minutes == 0:
        min_plural = "minutes"

    print(hour, plural_hour, minutes, min_plural)


number_to_time_conversion(61)
