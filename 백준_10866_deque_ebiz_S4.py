import sys

class Deque:

    def __init__(self):

        self.deque = []


    def push_front(self,X):

        self.deque.insert(0,X)

    def push_back(self,X):

        self.deque.append(X)

    def pop_front(self):

        if self.deque:

            return self.deque.pop(0)

        else:

            return -1

    def pop_back(self):

        if self.deque:

            return self.deque.pop()

        else:

            return -1

    def size(self):

        return len(self.deque)

    def empty(self):

        if len(self.deque) == 0:

            return 1

        else:

            return 0

    def front(self):

        if self.deque:

            return self.deque[0]

        else:

            return -1

    def back(self):

        if self.deque:

            return self.deque[-1]

        else:

            return -1

N = int(sys.stdin.readline())

a = Deque()

for _ in range(N):

    order_value = sys.stdin.readline().split()

    if order_value[0] == "push_back":

        a.push_back(order_value[1])

    elif order_value[0] == "push_front":

        a.push_front(order_value[1])

    elif order_value[0] == "front":

        print(a.front())

    elif order_value[0] == "back":

        print(a.back())

    elif order_value[0] == "size":

        print(a.size())

    elif order_value[0] == "pop_front":

        print(a.pop_front())

    elif order_value[0] == "pop_back":

        print(a.pop_back())

    elif order_value[0] == "empty":

        print(a.empty())

