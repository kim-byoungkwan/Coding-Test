###.1 연결리스트에서의 노드의 삽입과 삭제 그리고 두 연결리스트 합치기




class Node:

    def __init__(self, item):

        self.data = item

        self.next = None


class LinkedList:

    def __init__(self):

        self.nodeCount = 0

        self.head = None

        self.tail = None

    def __repr__(self):

        if self.nodeCount == 0:

            return 'LinkedList: empty'

        s = ''

        curr = self.head

        while curr is not None:

            s += repr(curr.data)

            if curr.next is not None:

                s += ' -> '

            curr = curr.next

        return s


    def getAt(self, pos):

        if pos < 1 or pos > self.nodeCount:

            return None

        i = 1

        curr = self.head

        # curr 변수에 LinkedList 클래스를 의미하는 self의 head 변수를 할당했을 때, self.head         가 생성자에 의해 None로 설정되었다 하더라도, None 이라는 할당 인자가 data 값이 저장되는 공        간에도 아무것도 없고, link 값이 저장되는 공간에도 아무것도 없는 상태를 의미하므로, 현재            data 값이 저장되는 공간과 link 값이 저장되는 공간이 형성되어 있는 상태로 self.head에 유지        되어 있는 것이다. 그러므로,

        while i < pos:

            curr = curr.next

            # 위와 같이 curr 변수에 next 메소드를 link가 저장되는 next 변수 공간이 존재하므로,              curr변수에 next를 적용할 수 있게 된다.

            i += 1

        return curr


    def insertAt(self,pos,newNode):

        if pos < 1 or pos > self.nodeCount + 1:

            # 내가 삽입하고자 하는 위치가 올바른 위치인지를 검사하고, 올바르지 않다면 바로 False를               출력한다

            return False

        if pos == 1:

            # 삽입하고자 하는 노드의 원하는 위치가 연결리스트의 맨 앞인 경우

            newNode.next = self.head

            self.head = newNode

        else:

            if pos == self.nodeCount + 1:

                prev = self.tail

            else:

                prev = self.getAt(pos - 1)

                # 내가 삽입하고자 원하는 위치의 이전 노드를 getAt 메소드에 pos -1 을 인자값으로                   하여 출력하여 내가 원하는 노드의 이전 노드를 의미하는 prev 변수에 할당한다.

                newNode.next = prev.next

                # 내가 삽입하고자 원하는 노드를 의미하는 newNode는 아직 삽입되기 이전의 상태이고,                  만약 삽입되었을때 newNode의 다음 노드는 현재 prev 노드의 다음노드가 되어야 한다.

                prev.next = newNode

                # 내가 삽입하고자 원하는 newNode는 내가 삽입하고자 원하는 위치 이전의 노드를 의미하                 는 prev노드의 다음노드가 되어야 한다.

        if pos == self.nodeCount + 1:

            self.tail = newNode

        self.nodeCount += 1

        return True


    def traverse(self):

        result = []

        curr = self.head

        while curr != None:

            result.append(curr.data)

            curr = curr.next

        return result


    def concat(self, L):

        self.tail.next = L.head

        if L.tail:

            self.tail = L.tail

        self.nodeCount += L.nodeCount


    def popAt(self,pos):

        curr = self.getAt(pos)

        prev = self.getAt(pos-1)

        if pos < 1 or pos > self.nodeCount:

            raise IndexError

        if pos == 1:

            if pos == self.nodeCount:

                self.head = None

                self.tail = None

            else:

                self.head = curr.next

        elif pos == self.nodeCount:

            self.tail = prev

            prev.next = None


        else:

            prev.next = curr.next

        self.nodeCount -= 1

        return curr.data









































