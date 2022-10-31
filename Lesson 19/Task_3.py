class MyIter:
    def __init__(self, data: list):
        self.data = data
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data) - 1:
            raise StopIteration
        else:
            self.index += 1
        return self.data[self.index] * self.data[self.index]


res = MyIter([1, 3, 5, 7, 9])
for elem in res:
    print(elem)
res = MyIter([1, 3, 5, 7, 9])
res_1 = [i for i in res]
print(res_1)
