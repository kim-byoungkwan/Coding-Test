###.1 이진 탐색 트리에서의 원소 삭제

#.1 키(key)를 이용해서 노드를 찾고, 만약 해당하는 키의 노드가 없으면 삭제할 노드고 없는 것이다.

#.2 키를 이용해서 노드를 찾았으면 찾은 노드의 부모 노드 또한 알고 있어야한다.(lookup 메소드를 이용하면 key 뿐만 아니라 부모노드 또한 return 해줄 수 있다.) 왜냐하면, 찾은 노드를 제거하고 나서도 이진 탐색 트리의 성질을 만족하는 상태를 유지하기 위해선 부모노도를 알고있어야 하기 때문이다.

#.3 remove 메소드를 구현하려면 삭제되는 노드가 어떤 노드인지에 따라서 이진 탐색 트리의 구조를 유지하기 위한 조건이 필요하다

# 삭제되는 노드가 말단노드인 경우: 말단 노드를 제거하고, 부모노드의 링크를 조정한다. 이때 말단 노드는 부모노드의 왼쪽에 붙어있는 말단 노드일 수도 있고, 오른쪽에 붙어있는 말단 노드일 수도 있다.
# 삭제되는 노드가 자식을 하나 가지고 있는 경우: 삭제되는 노드 자리에 그 자식노드를 대신 배치한다.
# 삭제되는 노드가 자식을 둘 가지고 있는 경우: 삭제되는 노드보다 바로 다음 키를 가지는 노드를 찾아 그 노드를 삭제되는 노드 자리에 대신 배치하고 이 노드를 대신 삭제한다.
# 삭제되는 노드가 뿌리노드인 경우: 대신 들어오는 자식 노드가 새로운 뿌리노드가 된다.

##.1 이진 탐색 트리가 별로 효율적이지 못한 경우
# 한쪽으로 치우친 경우의 이진 트리의 경우는 이진 탐색 트리가 별로 효율적이지 못하다.



class Node:

    def __init__(self,key,data):

        self.key = key

        self.data = data

        self.left = None

        self.right = None

    def inorder(self):

        traversal = []

        if self.left:

            traversal += self.left.inorder()

        traversal.append(self)

        if self.right:

            traversal += self.right.inorder()

        return traversal

    def lookup(self,key,parent=None):

        if key < self.key:

            if self.left:

                return self.left.lookup(key,self)

            else:

                return None,None

        elif key > self.key:

            if self.right:

                return self.right.lookup(key,self)

            else:

                return None,None

        else:

            return self,parent

    def insert(self,key,data):

        if key < self.key:

            if self.left:

                self.left.insert(key,data)

            else:

                self.left = Node(key,data)

        elif key > self.key:

            if self.right:

                self.right.insert(key,data)

            else:

                self.right = Node(key,data)

        else:

            raise KeyError('...')


    def countChildren(self):

        count = 0

        if self.left:

            count += 1

        if self.right:

            count += 1

        return count



class BinSearchTree:

    def __init__(self):

        self.root = None

    def inorder(self):

        if self.root:

            return self.root.inorder()

        else:

            return []

    def min(self):

        if self.root:

            return self.root.min()

        else:

            return None

    def lookup(self,key):

        if self.root:

            return self.root.lookup(key)

        else:

            return None,None

    def insert(self,key,data):

        if self.root:

            self.root.insert(key,data)

        else:

            self.root = Node(key,data)

    def remove(self, key):

        node, parent = self.lookup(key)

        if node:







