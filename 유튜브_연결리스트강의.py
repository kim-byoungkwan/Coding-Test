###.1 연결리스트 생성


##.cf
# 파이썬에서 None는 일반적인 데이터베이스에서의 Null 값에 대응되는 개념인데, 파이썬에서 None는 별도의 데이터 타입으로의 객체로서 존재한다. 즉, "값의 부재"를 나타내는 개념이다.

class ListNode:

    def __init__(self,val):

        self.val = val

        self.next = None

# ListNode라는 클래스는 생성자에 val 이라는 인자값을 입력받아 그 값을 ListNode 클래스 자체에 존재하는 변수 val 에 할당하고, ListNode 클래스 자체에 next라는 변수를 생성하여 그 변수에 None를 할당한다. 이러한 클래스의 형태가 연결리스트의 본질인 Node를 형성하여 연결리스트를 생성하게 될 것이다.


head_node = ListNode(1)
#.1 head_node 라는 객체변수에 ListNode 클래스에 1을 인자값으로 할당하여 ListNode 클래스의 생성자에 의해 1값이 val 변수에 할당되고, next 변수를 생성하여 None를 할당한 ListNode 클래스를 생성한다. 이렇게 생성된 클래스를 head_node 객체변수에 할당하면, 객체변수 head_node에는 val 변수가 1의 값이 할당된 상태로 존재하게 되고, next 변수가 None 이 할당된 상태로 존재하게 된다. (그림참조)

head_node.next = ListNode(2)

head_node.next.next = ListNode(3)

head_node.next.next.next = ListNode(4)

# head_node에 val 변수에 1이 할당된 것을 헤드 노드로 하는 연결리스트가 생성된다.


def printNodes(node:ListNode):

    # 여기서 printNodes 함수의 인자에 node가 쓰이고, 이 노드는 ListNode 연결리스트를 생성하는 클래   스에 의해 생성된 연결리스트의 node 라는 의미를 ":" 기호에 의해 추가적으로 더해 준 것이다. 즉, 함수   인자에 쓰인 ":" 기호는 사용되어야 할 인자에 대한 의미를 부연적으로 더해주는 기능을 나타내는 주석의     기능을 한다고 볼 수 있다.

    crnt_node = node

    while crnt_node is not None:

        # crnt_node엔 val변수의 값과 next 변수의 값 2개가 포함되어 있는데, 이 2개의 값중 None이          포함되어 있기만 하면 참이 된다.즉, 이 경우 head_node를 인자로 넣었을 경우 next에                 ListNode(2)에 의해 생성된 두번째 노드가 할당되어 있으므로, None 이 아니므로 while 조건          이 참이 된다.

        print(crnt_node.val, end=' ')

        crnt_node = crnt_node.next


printNodes(head_node)

# 위의 코드는 연결리스트의 값을 iterative한 방법으로 출력하는 코드이다.

def printNodesRecur(node:ListNode):

    print(node.val, end=' ')

    if node.next is not None:

        printNodesRecur(node.next)

printNodesRecur(head_node)

# 위의 코드는 연결리스트의 값을 recursive한 방법으로 출력하는 코드이다.






