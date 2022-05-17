def maximum(*args):   
    max_number = args[0]
    for item in args:
        if item > max_number:
            max_number = item
    return max_number

print(maximum(5, 6, 7, 8))
