class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


    def insert(self, key, data):
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Node(key, data)
        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Node(key, data)
        else:
            raise KeyError('Key %s already exists.' % key)


    def lookup(self, key, parent=None):
        if key < self.key:
            if self.left:
                return self.left.lookup(key, self)
            else:
                return None, None
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, self)
            else:
                return None, None
        else:
            return self, parent


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal


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


    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)


    def lookup(self, key):
        if self.root:
            return self.root.lookup(key)
        else:
            return None, None


    def remove(self, key):
        node, parent = self.lookup(key)
        if node:
            nChildren = node.countChildren()
            # The simplest case of no children

            if nChildren == 0:
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # parent.left 또는 parent.right 를 None 으로 하여
                # leaf node 였던 자식을 트리에서 끊어내어 없앱니다.

                if parent:

                    if node.key > parent.key:

                        parent.right = None

                    else:

                        parent.left = None

                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 를 None 으로 하여 빈 트리로 만듭니다.

                else:

                    self.root = None

            # When the node has only one child

            elif nChildren == 1:

                # 하나 있는 자식이 왼쪽인지 오른쪽인지를 판단하여
                # 그 자식을 어떤 변수가 가리키도록 합니다.

                if node.left:

                    temp_node = node.left

                else:

                    temp_node = node.right

                if parent:

                    if node.key > parent.key:

                        parent.right = temp_node

                    else:

                        parent.left = temp_node

                else:

                    self.root = temp_node

            else:

                parent = node

                successor = node.right

# 여기서 parent는 successor의 parent를 의미한다. 즉, 위의 코드는 첫번째 시행에서의 successor과 그에 대한 parent는 항상 위와 같이 정의되기 때문에 위와같은 코드가 생성된 것이다.

# successor가 삭제하고자 하는 주어진 노드의 바로 오른쪽 자식 노드에서 결정되는 경우 successor의 parent 노드는 주어진 노드 자기 자신이다. 즉, 이경우 successor가 successor의 parent 노드가 되어야 한다.

# successor 은 주어진 node 보다 오른쪽 서브트리에서 가장 가까운 큰 값을 의미한다. 그러므로, 이러한 successor을 찾기 위해선 오른쪽 서브트리에서 주어진 node 보다 가장 가까운 큰 값을 갖는 값을 찾는 과정을 거쳐야한다.

                while successor.left:

                    parent = successor

                    successor = successor.left

                node.key = successor.key

                node.data = successor.data

                if parent.left == successor:

                    if successor.right:

                        parent.left = successor.right

                    else:

                        parent.left = None

                else:

                    parent.right = successor.right







            return True

        else:
            return False


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


def solution(x):
    return 0