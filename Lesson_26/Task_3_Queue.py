class Queue:

    def __init__(self, size):
        self.size = size
        self.my_list = []
        # self.element = element

    def push(self, item):
        if len(self.my_list) < self.size:
            return self.my_list.append(item)
        else:
            self.my_list.pop(0)
            self.my_list.append(item)

    def pop(self):
        return self.my_list.pop(0)

    def list_size(self):
        return len(self.my_list)

    def is_empty(self):
        return True if self.my_list else False

    def get_from_queue(self, element):  # Task 3
        for _ in self.my_list:
            if element in self.my_list:
                return element
            else:
                raise ValueError('Element not found')


    def __str__(self):
        return str(self.my_list)

    def __repr__(self):
        return self.__str__()