
class Node:

    def __init__(self,item):

        self.data = item

        self.prev = None

        self.next = None

class DoublyLinkedList:

    def __init__(self,item):

        self.nodeCount = 0

        self.head = Node(None)

        self.tail = Node(None)

        self.head.prev = None

        self.head.next = self.tail

        self.tail.prev = self.head

        self.tail.next = None


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


    def insertAfter(self, prev, newNode):

        next = prev.next

        newNode.prev = prev

        newNode.next = next

        prev.next = newNode

        next.prev = newNode

        self.nodeCount += 1

        return True


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


    def insertAt(self,pos,newNode):

        if pos < 1 or pos > self.nodeCount + 1:

            return False

        prev = self.getAt(pos - 1)

        return self.insertAfter(prev, newNode)



    def insertBefore(self,next,newNode):

# 주어지는 next 노드보다 앞에 newNode를 삽입하는 메소드를 의미한다.

# 양방향 메소드를 사용하면 메모리 공간의 소비가 커지긴 하지만, 동작을 구현하는데에 있어서는 매우 유용하게 된다.

        prev = next.prev

        newNode.next = next

        newNode.prev = prev

        prev.next = newNode

        next.prev = newNode

        self.nodeCount += 1

        return True




    def popAfter(self,prev):

# 주어지는 prev 노드 뒤의 노드를 삭제하고, 삭제한 노드를 출력하는 메소드를 의미한다.

        if prev.next == None:

            return None

        elif prev.prev == None:

            curr = prev.next

            next = prev.next.next

            prev.next = next

            next.prev = prev

        else:

            curr = prev.next

            next = prev.next.next

            prev.next = next

            next.prev = prev


        self.nodeCount -= 1


        return curr.data


    def popBefore(self,next):

# 주어지는 next 노드 앞의 노드를 삭제하고, 삭제한 노드를 출력하는 메소드를 의미한다.

        if next.next == None:

            curr = next.prev

            prev = next.prev.prev

            prev.next = next

            next.prev = prev

        elif next.prev == None:

            return None

        else:

            curr = next.prev

            prev = next.prev.prev

            prev.next = next

            next.prev = prev


        self.nodeCount -= 1

        return curr.data


    def popAt(self,pos):

# 주어지는 pos 위치 값에 해당하는 양방향 연결리스트의 노드를 삭제하고, 삭제한 노드를 출력하는 메소드를 의미한다.

        if pos < 0 or pos > self.nodeCount:

            raise IndexError

        prev = self.getAt(pos-1)

        return self.popAfter(prev)



    def concat(self,L):

# 주어지는 리스트 L을 원래 존재하던 리스트에 연결하여 하나의 리스트로 만드는 메소드로써 메소드가 실행된 결과 원래존재하던 리스트에 L 리스트의 모든 원소가 합쳐진 리스트가 출력되어야 한다.

# 이경우엔, 연결해야하는 리스트 L과 원래 존재하던 리스트가 모두 양방향 연결 리스트이므로, 두 양방향 연결리스트를 단순히 연결시켰을때, 각 리스트에 존재하는 heal 더미노드, tail 더미노드가  중복되는 문제가 발생할 수 있으므로, 최종적으로 생성된 하나의 양방향 연결리스트에 head 더미노드 1개, tail 더미노드 1개를 갖도록 연결시켜줘야 한다.

        prev = self.tail.prev

        next = L.head.next

        prev.next = next

        next.prev = prev

        self.tail = L.tail

        self.nodeCount += L.nodeCount

























