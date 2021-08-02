###.1 이진탐색트리

# 이진 탐색 트리란, 이진 트리의 모든 노드에 대해서 현재 노드의 왼쪽 서브트리에 있는 데이터는 모두 현재 노드의 값보다 작고, 오른쪽 서브트리에 있는 데이터는 모두 현재 노드의 값보다 큰 성질을 만족하는 이진트리를 의미한다.

# 이진탐색트리의 이러한 성질을 이용하면 데이터 검색을 쉽게 할 수 있게되어 데이터 원소의 추가 삭제가 용이 하게 된다. 그러나 공간 소요가 커진다는 단점도 있다. 왜냐하면 트리는 데이터들을 단순히 정렬한 배열에 비해 어떠한 노드의 왼쪽 자식 노드와 오른쪽 자식 노드를 항상 기록해놓아야 하기 때문에 이로인한 공간소모가 발생되기 때문이다.

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








