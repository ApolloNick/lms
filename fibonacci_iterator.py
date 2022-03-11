def fibonacci(n):
    if n < 0:
        raise ValueError('Cannot find negative value')
    if n == 0:
        fib_seq = [0]
    elif n == 1:
        fib_seq = [0, 1]
    else:
        fib_seq = [0, 1]
        for i in range(2, n):
            fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    return fib_seq


for index, item in enumerate(fibonacci(10), start=1):
    if index > 10:
        break
    else:
        print(index, item)
