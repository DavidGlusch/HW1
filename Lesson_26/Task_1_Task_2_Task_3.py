class Stack:

    def __init__(self, size):
        self.size = size
        self.data = list()

    def push(self, item):
        if len(self.data) < self.size:
            self.data.append(item)
        else:
            self.data.pop(0)
            self.data.append(item)

    def read_sequence(self):  # Task_1
        print(self.data[::-1])

    @staticmethod
    def brackets(data: str):  # Task_2
        stack = []
        opening = []
        closing = []
        ex_opening = '([{'
        ex_closing = ')}}'
        pair = {')': '(', ']': '[', '}': '{'}
        for i in data:
            if i in ex_opening:
                opening.append(i)
            elif i in ex_closing:
                closing.append(i)
        opening.extend(closing)
        for i in opening:
            if i in ex_opening:
                stack.append(i)
            if i in ex_closing:
                if not stack:
                    return False
                elif stack.pop() != pair[i]:
                    return False
                else:
                    continue
        if not stack:
            return True
        else:
            return False

    def get_from_stack(self, element):  # Task_3
        for _ in self.data:
            if element in self.data:
                return element
            else:
                raise ValueError('Element not found')

    def pop(self):
        return self.data.pop()

    def is_empty(self):
        return not bool(self.data)

    def list_size(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return self.__str__()


stack_1 = Stack(3)
stack_1.push('a')
stack_1.push('b')
stack_1.push('c')
# print(stack_1.data)
# stack_1.read_sequence()
# print(stack_1.brackets('((())))'))
print(stack_1.get_from_stack('d'))
