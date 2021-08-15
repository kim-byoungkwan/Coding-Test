import sys


class stack_function:

    def __init__(self):

        self.stack = []

    def push(self,X):

        self.stack.append(X)

    def pop(self):

        if len(self.stack) == 0:

            return -1

        else:

            return self.stack.pop()

    def size(self):

        return len(self.stack)

    def empty(self):

        if len(self.stack) == 0:

            return 1

        else:

            return 0

    def top(self):

        if len(self.stack) == 0:

            return -1

        else:

            return self.stack[-1]


T = int(sys.stdin.readline())

a = stack_function()

box = []

for i in range(T):

    func = sys.stdin.readline().split()

    order = func[0]

    if order =="push":

        value = func[1]

        a.push(value)

    elif order =="pop":

        box.append(a.pop())

    elif order =="top":

        box.append(a.top())

    elif order =="size":

        box.append(a.size())

    elif order =="empty":

        box.append(a.empty())


for i in box:

    print(i)










