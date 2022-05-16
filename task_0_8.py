def number_to_time_conversion(number):
    hour = number//60
    minutes = number % 60
    if number == 0:
        print(hour, "hours,", minutes, "minutes")
    elif hour == 1 and minutes > 1:
        print(hour, "hour,", minutes, "minutes")
    elif hour > 1 and minutes == 1:
        print(hour, "hours,", minutes, "minute")
    elif hour == 1 and minutes == 0:
        print(hour, "hour,", minutes, "minutes")
    elif hour == 0 and minutes == 1:
        print(hour, "hours,", minutes, "minute")
    else:
        print(hour, "hours,", minutes, "minutes")

number_to_time_conversion()

