###.1 우선순위 큐

# 우선순위 큐란 일반적인 큐가 먼저 들어간 데이터가 먼저 출력되는 선입선출의 방식을 따르는 것과 갈리 데이터 간에 우선순위가 정해져 있어서 그 우선순위에 맞게 데이터가 출력되는 형식의 큐를 말한다.

# 이러한 우선순위 큐의 구현 방식에는 enqueue 할때 우선순위 순서를 유지하도록 하는 방식과 dequeue할 때 무작위로 배열된 데이터를 우선순위가 높은 것을 기준으로 하는 방식이 존재한다. 이러한 두가지 방식 중에 더 효율성이 높은 방식은 첫번째 방식이다. 왜냐하면 두번째 방식과 같은 경우에는 데이터가 큐에 무작위로 배열되어 있으므로 dequeue를 하기 위해선 큐에 존재하는 데이터를 큐의 길이만큼 읽어들이는 동작을 수행해야 하므로 비효율적이기 때문이다. 그러나, 첫번째 방식에서는 이미 데이터의 우선순위를 기준으로 큐에 데이터가 배열되어 있으므로 데이터의 출력을 큐에 존재하는 모든 데이터를 다 읽어들이지 않고도 가능하기 때문이다.

class Node:

    def __init__(self, item):

        self.data = item

        self.prev = None

        self.next = None


class DoublyLinkedList:

    def __init__(self):

        self.nodeCount = 0

        self.head = Node(None)

        self.tail = Node(None)

        self.head.prev = None

        self.head.next = self.tail

        self.tail.prev = self.head

        self.tail.next = None


    def __repr__(self):

        if self.nodeCount == 0:

            return 'LinkedList: empty'

        s = ''

        curr = self.head

        while curr.next.next:

            curr = curr.next

            s += repr(curr.data)

            if curr.next.next is not None:

                s += ' -> '

        return s


    def getLength(self):

        return self.nodeCount


    def traverse(self):

        result = []

        curr = self.head

        while curr.next.next:

            curr = curr.next

            result.append(curr.data)

        return result


    def reverse(self):

        result = []

        curr = self.tail

        while curr.prev.prev:

            curr = curr.prev

            result.append(curr.data)

        return result


    def getAt(self, pos):

        if pos < 0 or pos > self.nodeCount:

            return None

        if pos > self.nodeCount // 2:

            i = 0

            curr = self.tail

            while i < self.nodeCount - pos + 1:

                curr = curr.prev

                i += 1

        else:

            i = 0

            curr = self.head

            while i < pos:

                curr = curr.next

                i += 1

        return curr


    def insertAfter(self, prev, newNode):

        next = prev.next

        newNode.prev = prev

        newNode.next = next

        prev.next = newNode

        next.prev = newNode

        self.nodeCount += 1

        return True


    def insertAt(self, pos, newNode):

        if pos < 1 or pos > self.nodeCount + 1:

            return False

        prev = self.getAt(pos - 1)

        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):

        curr = prev.next

        next = curr.next

        prev.next = next

        next.prev = prev

        self.nodeCount -= 1

        return curr.data


    def popAt(self, pos):

        if pos < 1 or pos > self.nodeCount:

            raise IndexError('Index out of range')

        prev = self.getAt(pos - 1)

        return self.popAfter(prev)


    def concat(self, L):

        self.tail.prev.next = L.head.next

        L.head.next.prev = self.tail.prev

        self.tail = L.tail

        self.nodeCount += L.nodeCount



class PriorityQueue:

    def __init__(self,x):

        self.queue = DoublyLinkedList()


    def size(self):

        return self.queue.getLength()


    def isEmpty(self):

        return self.size() == 0


    def enqueue(self,x):

        newNode = Node(x)

        curr = self.queue.head

        while curr.next.data != None and x < curr.next.data:

            curr = curr.next

        self.queue.insertAfter(curr,newNode)

# 이와같은 코드로 인해 연결리스트로 이루어진 큐에 데이터를 포함한 노드가 큰 값부터 작은 값의 순서로 배열되게 되며,


    def dequeue(self):

        return self.queue.popAt(self.queue.getLength())

# enqueue 코드의 결과 dequeue를 하게되면, 크기가 작은 값부터 먼저 출력되게 되는데, 이러한 동작에 의해 우선순위를 크기가 작은 값의 데이터에 높은 것으로 부여하여 크기가 작은 값이 먼저 큐로 부터 출력되도록 할 수 있게된다. 즉, 이와 같은 enqueue , dequeue 방식은 먼저 enqueue 과정에서 큐에 노드 값의 순서대로 배열하고 출력을 했을 때 우선순위에 맞는 값이 먼저 출력되도록 하는 것이다.

    def peek(self):

        return self.queue.getAt(self.queue.getLength()).data





