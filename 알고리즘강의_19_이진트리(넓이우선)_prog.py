###.1 이진트리(넓이우선순회)

# 넓이우선순회의 원칙은 수준이 낮은 노드를 우선으로 방문한다는 것이다. 즉, 깊이우선순회의 방식처럼 종적인 방향으로 들어갔다가 나갔다가 하는 것이 아니라 횡적인 방향으로 같은 레벨의 노드들을 방문하는 방식인 것이다. 이때, 같은 수준의 노드들 사이에서는 부모 노도가 먼저 방문된 노드들이 먼저 방문되고, 같은 부모노드를 갖는 자식 노드들 사이에서는 왼쪽 자식 노드를 오른쪽 자식노드보다 먼저 방문하는 것이다.

# 이러한 넓이우선순회 방식에서는 깊이우선순회 방식에서와 달리 재귀적인 방법은 적합하지 않다.

# 넓이우선순회 방식에서는 뿌리노드의 레벨이 가장 낮으므로 항상 뿌리노드부터 방문하게 된다.

class ArrayQueue:

    def __init__(self):
        self.data = []


    def size(self):
        return len(self.data)


    def isEmpty(self):
        return self.size() == 0


    def enqueue(self, item):
        self.data.append(item)


    def dequeue(self):
        return self.data.pop(0)


    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):

        self.data = item

        self.left = None

        self.right = None




class BinaryTree:

    def __init__(self,r):

        self.root = r


    def bft(self):

        traversal = []

        q = ArrayQueue()


        if self.root:

            q.enqueue(self.root)

        while q.isEmpty() == False:

            out = q.dequeue()

            traversal.append(out.data)

            if out.left:

                q.enqueue(out.left)

            if out.right:

                q.enqueue(out.right)


        return traversal

# append 할때는 실질적인 노드의 데이터 값이 인자로 설정되어야 하고, enqueue와 dequeue할때는 노드 그자체가 인자로 포함되어야 한다.



















        return traversal








