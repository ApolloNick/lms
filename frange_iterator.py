def frange(start, end, step):
    i = 0
    while start+(i*step) < end:
        yield start+(i*step)
        i += 1


for item in frange(1, 5, 1.5):
    print(item)
