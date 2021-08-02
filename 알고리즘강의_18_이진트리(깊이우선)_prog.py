###.1 이진트리(깊이우선순회)

# 스택이나 큐, 연결리스트에서 노드를 정의할 때 노드의 데이터가 저장되는 data 변수외에 노드의 다음 노드와 이전노드가 뭔지를 알려주는 next 변수와 prev 변수를 생성했던 것 처럼 이진트리를 생성할때에도 이진트리의 노드에 left 포인터 변수와 right 포인터 변수를 생성하여 어떠한 노드의 왼쪽 자식노드와 오른쪽 자식노드가 무엇인지를 지정해주어 이진트리를 생성하게 된다.

class Node:

    def __init__(self, item):

        self.data = item

        self.left = None

        self.right = None


    def size(self):

        l = self.left.size() if self.left else 0

        r = self.right.size() if self.right else 0

        return l + r + 1


    def depth(self):

        l = self.left.depth() if self.left else 0

        r = self.right.depth() if self.right else 0

        return max(l, r) + 1


    def inorder(self):

        traversal = []

        if self.left:

            traversal += self.left.inorder()

        traversal.append(self.data)

        if self.right:

            traversal += self.right.inorder()

        return traversal


    def preorder(self):

        traversal = []

        traversal.append(self.data)

        if self.left:

            traversal += self.left.preorder()

        if self.right:

            traversal += self.right.preorder()

        return traversal


    def postorder(self):

        traversal = []

        if self.left:

            traversal += self.left.postorder()

        if self.right:

            traversal += self.right.postorder()

        traversal.append(self.data)

        return traversal




class BinaryTree:

    def __init__(self,r):

        self.root = r


    def size(self):

        if self.root:

            return self.root.size()

        else:

            return 0


    def depth(self):

        if self.root:

            return self.root.depth()

        else:

            return 0


    def inorder(self):

        if self.root:

            return self.root.inorder()

        else:

            return []


    def preorder(self):

        if self.root:

            return self.root.preorder()

        else:

            return []


    def postorder(self):

        if self.root:

            return self.root.postorder()

        else:

            return 0













###.2 이진트리의 순회

##.1 깊이우선순회
# 중위순회 : 왼쪽 서브트리 - 자기자신 x 트리 - 오른쪽 서브트리
# 자기자신 x 트리를 왼쪽 서브트리와 오른쪽 서브트리 중간에 방문한다. 즉, 왼쪽 서브          트리를 방문하고 자기 자신 x트리를 방문한 뒤 오른쪽 서브트리를 방문하는 순서로 트           리를 순회하는 방법이다.

# 전위순회 : 자기자신 x 트리 - 왼쪽 서브트리 - 오른쪽 서브트리

# 후위순회 : 왼쪽 서브트리 - 오른쪽 서브트리 - 자기자신 x 트리


##.2 넓이우선순회




