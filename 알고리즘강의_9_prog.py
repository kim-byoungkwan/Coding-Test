###.1 더미변수를 포함한 연결리스트


class Node:

    def __init__(self,data):

        self.data = data

        self.next = None

class LinkedList:

    def __init__(self):

        self.nodeCount = 0

        self.head = Node(None)

        # Node 클래스를 head 변수에 상속하여 데이터 공간과 링크 공간을 갖지만 그에 대한 값        은 할당되지 않은 더미노드를 생성하는 코드이다.

        self.tail = None

        self.head.next = self.tail


    def traverse(self):

        result = []

        curr = self.head

        # 현재 LinkedList 클래스의 head 변수에는 더미노드가 할당되어 있으므로, curr 변         수는 더미변수를 의미한다.

        while curr.next:

            # curr.next 값이 존재하면 True 존재하지 않으면 False

            curr = curr.next

            # 더미변수가 할당된 curr 변수의 다음 노드는 실제 값이 저장된 1번째 노드이므로,            이때 curr 변수는 첫번째 데이터 값이 할당된다.

            result.append(curr.data)

            # 0번째 더미노드 부터 시작하는 연결리스트의 첫번째 노드의 데이터 값부터                   result 배열에 할당한다

        return result


    def getAt(self,pos):

        if pos < 0 or pos > self.nodeCount:

# 연결리스트가 0번째 더미노드 부터 시작되므로, 연결리스트의 범위를 벗어나는 pos 값은 0보다 작은 것에서부터 발생된다.

            return None

        i = 0

        # 연결리스트에 0번째 더미노드가 포함되어 있으므로 i는 0부터 시작된다.

        curr = self.head

        # 현재 curr 변수엔 더미노드인 head 가 할당된다.

        while i < pos:

            curr = curr.next

            i += 1

        return curr

    def insertAfter(self,prev,newNode):

        # prev 변수가 가리키는 node의 다음에 newNode를 삽입하고 성공/실패 여부에 따라서         True/False를 리턴하는 메소드이다.

        # 여기서 prev 또한 newNode 인자값 처럼 분명히 노드를 의미하는 변수이다.

        # 이처럼 insertAfter 메소드의 인자가 이 경우 LinkedList 클래스를 의미하는           self를 인자로 포함하는 순간, insertAfter 메소드는 LinkedList 클래스에 의해         결정되는 메소드임을 의미하고, 이는 곧 insertAfter 메소드는 LinkedList 클래스        의 모든 것을 접근하여 이용할 수 있게 됨을 의미한다.


        newNode.next = prev,next

        if prev.next is None:

        # prev노드의 next가 None 이었다면 prev 노드는 tail 노드였다는 것을 의미한다.

            self.tail = newNode

        # 특이한 경우로 newNode가 tail 노드 뒤에 삽입되는 경우는 위와 같은 조건에 의해         삽입시켜야 한다.

        prev.next = newNode

        self.nodeCount += 1

        return True

    def insertAt(self,pos,newNode):

        if pos < 1 or pos > self.nodeCount + 1:

            return False

        if pos != 1 and pos == self.nodeCount + 1:

            prev = self.tail

        else:

            prev = self.getAt(pos-1)

        return self.insertAfter(prev,newNode)

        # 여기에선 LinkedList 클래스의 메소드인 insertAfter가 이미 LinkedList를 의         미하는 self에 접근하여 불러들여진 것이므로, insertAfter인자값에 LinkedList         를 의미하는 self는 포함시키지 않아도 된다.


    def popAfter(self,prev):

        # prev의 다음 node를 삭제하고 그 node의 data를 리턴한다.

        if prev.next == None:

            return None

        curr = prev.next

        if curr.next == None:

            if self.nodeCount == 1:

                self.tail = prev

                prev.next = None



            else:

                self.tail = prev

                prev.next = None


        else:

            prev.next = curr.next


        self.nodeCount -= 1

        return curr.data


    def popAt(self,pos):

        if pos < 1 or pos > self.nodeCount:

        # 연결리스트의 0번째 더미노드는 아무런 값도 갖고 있지 않으므로 실질적으로 이미 없는        노드라고도 볼 수 있으므로, 내가 삭제하고자 하는 노드의 위치는 1번째 부터 시작된다.
            raise IndexError

        prev = self.getAt(pos-1)

        return self.popAfter(prev)


    def concat(self,L):

        self.tail.next = L.head.next

        # L 리스트의 head 또한 더미노드 이므로, L 리스트의 head의 다음 노드로 연결해줘야        한다.

        if L.tail:

            self.tail = L.tail

            # 최종적으로 생성된 리스트의 끝 값을 의미하는 tail 노드를 이어 붙이는 L 리스             트의 tail으로 정의해주게 되면 최종적으로 연결된 하나의 리스트의 끝 값이                L.tail로 결정되는 것이다.

        self.nodeCount += L.nodeCount














































