class Mathematician:
    def square_nums(self, list_: list):
        return [i*i for i in list_]

    def remove_positives(self, list_: list):
        return [i for i in list_ if i <= 0]

    def filter_leaps(self, list_: list):
        return [min(list_), max(list_)]


m = Mathematician()


print(m.square_nums([7, 11, 5, 4]))

print(m.remove_positives([26, -11, -8, 13, -90]))

print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))
