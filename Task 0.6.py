def maximum(*args):   # *args lets us input multiple numbers as our argument
    max_number = 0
    for item in args:
        if item > max_number:
            max_number = item
    return max_number
	
print(maximum())