def in_range(start, end, step=1):
    while start < end:
        yield start
        start += step


res = in_range(1, 10, 2)

for elem in res:
    print(elem)
