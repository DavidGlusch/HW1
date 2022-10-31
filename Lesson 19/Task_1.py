def with_index(data, counter=0):
    for elem in data:
        yield counter, elem
        counter += 1


res = with_index(['a', 'b', 'c'])
for elem in res:
    print(elem)
