###.1 양방향 연결리스트

# 연결리스트의 노드의 링크를 한 쪽 방향의 노드로만 연결하지 말고, 양쪽 방향의 노드로 연결하여 원하는 노드의 앞/뒤 방향 모두로 이동가능하도록 하는 노드를 가진 연결리스트를 양방향 연결리스트라고 한다.

# 양방향 연결리스트는 단방향 연결리스트가 head노드를 더미노드로 설정하는 것과는 달리 head 노드와 tail 노드 모두에 더미노드를 설정한다. 이와 같이 설정하게 되면 양방향 연결리스트에서 데이터를 담고있는 모든 노드들이 모두 같은 모양의 형태로 유지될 수 있는 장점이 있다.



class Node:

    def __init__(self,item):

        self.data = item

        self.prev = None

        self.next = None

# 데이터 인자 값이 담기는 공간을 data 변수를 Node 클래스를 의미하는 self 클래스에 생성하고, 이전 노드를 가리키는 링크를 포함하는 공간을 prev 변수를 생성하여 만들고, 다음 노드를 가리키는 링크를 포함하는 공간을 next 변수를 생성하여 만든다.

class DoublyLinkedList:

    def __init__(self,item):

        self.nodeCount = 0

        self.head = Node(None)

        self.tail = Node(None)

# 이 경우의 head 노드와 tail 노드는 모두 양방향 노드를 생성하는 클래스인 Node 클래스로 생성되었으므로 모두 다음 노드와 연결하는 링크 공간과 이전 노드와 연결하는 링크 공간을 갖고 있는 양방향 노드를 의미한다.

        self.head.prev = None

        # head 노드에 더미노드를 설정해준다.

        self.head.next = self.tail

        self.tail.prev = self.head

        self.tail.next = None

        # tail 노드에 더미노드를 설정해준다.

# 위에서 처럼 head노드와 tail 노드를 양방향 연결 노드로 정의한 순간 위와 같이 head 노드와 tail 노드를 각각의 양방향 노드와 모두 연결지어 정의할 수 있게 되는 것이다.


    def traverse(self):

        result = []

        curr = self.head

        while curr.next.next:

# while 조건문의 값이 None인 경우는 False 이다. None이 아닌 어떠한 값이 존재해야만 True인 것이다. 따라서, 만약 head 더미노드와 tail 더미노드 외에 어떠한 노드도 갖고 있지 않은 연결리스트의 경우에도 result 값이 빈 배열 [] 로 표현되게되므로 옳다.

# 즉, head와 self노드에 정의된 더미노드는 None이 아니라, 어떠한 값이 존재하는 상태로 인정되는 노드인 것이다.

            curr = curr.next

            result.append(curr.data)

        return result

        # return 값으로는 더미노드를 제외한 실질적인 값을 보유한 노드만이 출력된다.

    def reverse(self):

# 양방향 연결노드로 정의된 리스트를 노드의 끝 값에서부터 처음 값의 방향으로 순회하면서 값을 저장하는 메소드이다.

        result = []

        curr = self.tail

        while curr.prev.prev:

            curr = curr.prev

            result.append(curr.data)

        return result


    def insertAfter(self,prev,newNode):

        next = prev.next

        newNode.prev = prev

        newNode.next = next

        prev.next = newNode

        next.prev = newNode

        self.nodeCount += 1

        return True


    def getAt(self,pos):

        if pos < 0 or pos > self.nodeCount:

            return None

# head 더미노드와 tail 더미노드에 모두 None 이라는 값이 할당되어 있으므로, 0번째 위치의 노드와 nodeCount 번째 위치의 노드로 부터 모두 None 라는 값을 얻을 수 있다. 그러므로, 노드 값을 얻는 것이 불가능한 범위로 위와 같이 0 보다도 작거나, nodeCount 보다는 큰 범위로 범위가 설정된 것이다.

# 더미변수가 존재하므로, 노드가 0번째에도 존재하게 된다. 그러므로, 출력할 수 없는 노드의 위치는 0보다 작은 경우이다.

        if pos > self.nodeCount // 2:

# 내가 찾고자 하는 위치의 노드가 양방향 연결리스트의 전체에서 중간보다 오른쪽에 위치하는 노드일 땐, tail 노드부터 내가 찾고자 하는 노드를 찾아가는 것이 더 효율적이다.

            i = 0

# i = 0 은 노드의 맨 끝 tail 노드부터 시작함을 의미하는 것이다.

            curr = self.tail

            while i < self.nodeCount - pos + 1:

# tail 더미노드는 nodeCount 를 측정할 때엔 제외되는 노드이다. 그러므로 curr 노드가 tail 노드로 정의하였으므로, +1 tail 더미노드에 대한 +1을 더해주는 것이다. 즉, tail 더미노드가 저장된 위치는 nodeCount + 1 번재 위치에 저장되어 있다.

                curr = curr.prev

                i += 1

        # 위의 if 절은 else 조건과는 달리 맨 뒤의 tail 변수로부터 찾아가는 코드이다.

        else:

            i = 0

            curr = self.head

            while i < pos:

# head 더미노드는 연결리스트의 0번째 위치에 존재하고, 1번째 위치부터 실질적인 값을 갖는 노드가 존재하게 된다.

                curr = curr.next

                i += 1

        return curr

#위와 같이 코드를 형성하게 되면 맨 끝의 노드가 필요한 경우 효율적으로 가져올 수 있다.


    def insertAt(self,pos,newNode):

        if pos < 1 or pos > self.nodeCount + 1:

            return False

# head 더미변수는 0번째에 존재하고, 0번째 더미변수에는 노드 값을 삽일 할 수 없다. 마찬가지로, tail 더미변수는 nodeCount +1 번째에 존재하고 이 더미변수에도 노드 값을 삽일 할 수가 없다. 따라서 위와 같은 노드 삽입 불가 범위가 형성된 것이다.

        prev = self.getAt(pos-1)

        return self.insertAfter(prev,newNode)





























