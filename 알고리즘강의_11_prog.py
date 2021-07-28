###.1 스택

# 선형배열이나, 연결리스트 같은 것들은 다른 자료구조를 이루는 데에 기본이 되는 구조라고 한다면, 앞으로 할 스택과 같은 것은 특정한 유형의 문제를 푸는데에 유용한 알고리즘을 의미한다.

# 스택이란 데이터를 보관할 수 있는 선형의 구조를 의미하는데, 이때 선형의 구조란 데이터가 일렬로 나란히 저장되는 구조를 의미한다. 단, 스택 자료구조는 데이터를 넣을 때엔 한 쪽 끝에서 밀어넣어야 하고, 데이터를 꺼낼 때에는 데이터를 밀어 넣었던 쪽과 같은 쪽에서 뽑아서 꺼내야하는 제약이 있는 자료구조이다.

# 이때, 한쪽 끝에서 데이터를 밀어넣는 연산을 푸쉬(push)연산 이라고 하고, 데이터를 꺼내는 연산을 팝(pop) 연산이라고 한다.

# 이와 같은 자료 구조에선 push에 의해 들어간 데이터중에 가장 나중에 들어간 데이터가 가장 먼저 pop 되어 나오게 된다. 즉 Last in First out 구조이다.

# 스택의 초기 상태는 데이터가 존재하지 않는 비어있는 상태이다.

# 스택 자료구조의 핵심은 데이터를 넣는 방향과 데이터를 꺼내는 방향이 같은 방향이라는 것이다.

# 스택에 데이터가 존재하지 않음에도 불구하고 pop 연산을 스택에 적용했을 때 발생하는 오류는 "스택 언더플로우" 라고 한다.

# 스택에 데이터가 꽉차서 더이상 들어갈 공간이 없음에도 불구하고 스택에 데이터를 push 하려고 했을 때에 발생하는 오류를 "스택 오버플로우" 라고 한다.

##.1 배열로 구현한 스택

class ArrayStack:

    def __init__(self):

        self.data = []

    def size(self):

        return len(self.data)

# 스택의 크기를 출력하는 메소드이다.

    def isEmpty(self):

        return self.size() == 0

# 스택이 비어있는지를 판단하는 메소드이다.

    def push(self,item):

        self.data.append(item)

# 스택에 데이터 원소를 추가하는 메소드이다.

    def pop(self):

        return self.data.pop()

# 스택에 데이터 원소를 제거하는 메소드이다.

    def peek(self):

        return self.data[-1]

# 스택의 가장 꼭대기에 있는 원소를 보여준다. 즉, 스택의 원소 구성의 본질은 변화시키지 않으면서 꼭대기에 있는 원소가 무엇인지만을 보여주는 것이다.

# 스택의 가장 밑바닥에 있는 원소의 인덱스가 0 스택의 가장 꼭대기에 있는 원소의 인덱스는 -1로 결정된다.



##.2 양방향 연결리스트로 구현한 스택


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



class LinkedListStack:

    def __init__(self):

        self.data = DoublyLinkedList()

# LinkedListStack 클래스에 data 객체를 생성하여 head 더미변수와 tail 더미변수를 갖는 양방향 연결리스트의 초기 상태를 할당한다.

    def size(self):

        return self.data.getLength()






















