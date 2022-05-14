# this function changes a number into hours and minutes
def number_to_time_conversion(number):
    hour = number//60
    minutes = number % 60
    if hour == 1 and minutes > 1:
        print(hour, "hour", minutes, "minutes")
    elif hour > 1 and minutes == 1:
        print(hour, "hours", minutes, "minute")
    elif minutes == 1 or minutes == 0:
        print(hour, "hour", minutes, "minute")
    else:
        print(hour, "hours", minutes, "minutes")

number_to_time_conversion()

