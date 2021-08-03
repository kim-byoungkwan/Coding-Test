###.1 힙의 원소 삽입과 삭제

class MaxHeap:

    def __init__(self):

        self.data = [None]


    def insert(self, item):

        self.data.append(item)

        index = len(self.data) - 1

        while index > 1:

            parent = index // 2

            if self.data[index] > self.data[parent]:

                self.data[index], self.data[parent] = self.data[parent], self.data[index]

                index = parent

            else:

                break


    def remove(self):

        if len(self.data) > 1:

# 힙에는 0번째 인덱스에 기본적으로 None이 할당되어 있으므로, 아무런 데이터가 할당되지 않은 상태에서도 힙의 len() 메소드의 값은 1로 결정되게 된다. 즉, 이때 len(self.data)의 값이 1보다 큰 경우여야만이 힙에 0번째 인덱스의 None이 아닌 실질적인 데이터가 존재한다는 것이므로 삭제 연산을 실행하기 위해서는 실질적인 값이 존재해야 하므로, len(self.data) 값은 1보다 커야하는 것이다.

            self.data[1], self.data[-1] = self.data[-1], self.data[1]

            data = self.data.pop(-1)

# 위의 pop 동작에서 힙의 1번째 인덱스에 존재하던 루트노드가 마지막 인덱스로 이동된 상태의 노드를 제거하게 되면서 우리가 제거하고자 하는 루트노드를 제거하여 힙의 최대값을 출력하게 되는 것이다.

            self.maxHeapify(1)

# maxHeapify 메소드의 인자 1은 여기서 힙의 루트노드를 의미하는 인덱스이다.

        else:

            data = None

# 힙에 0번째 인덱스에 할당된 None을 제외하고 어떤 실질적인 데이터도 할당되지 않은 상태를 의미한다.

        return data


    def maxHeapify(self,i):

# 인자 i 는 i 번재 인덱스를 기준으로 시작할 것인지를 결정하는 인자이다.

        left = 2*i

        right = 2*i +1

        smallest = i

        if left < len(self.data) and self.data[left] > self.data[smallest]:

            smallest = left

# 현재 left 인덱스가 힙의 총 데이터 숫자보다 작다면, left 인덱스에 해당하는 데이터가 존재한다는 것이므로, i인덱스에 대한 왼쪽자식값이 존재한다는 것이다. 그리고 이경우 왼쪽 노드의 값이 최초의 인덱스로 규정한 smallest 노드값보다 크므로, maxHeap을 구성하기 위해서 더 큰 left 인덱스의 노드에 대한 값이 smallest 인덱스의 노드에 대한 값으로 되어야한다. 우리가 현재 maxHeapify() 메소드를 통해서 구현하고자하는 것은 i번째 인덱스의 노드부터 가장 큰 값이 되도록 하여 노드를 정렬하고자 하는 것이기 때문이다.

        if right < len(self.data) and self.data[right] > self.data[smallest]:

            smallest = right

# 여기서의 smallest 인덱스 값은 위의 if 문에서 left 값으로 치환되었을 수도 있다. 즉, 만약 그러한 경우 right 인덱스에 대한 값과 left 인덱스에 대한 값의 비교 또한 이루어질 수 있게 되어 최종적으로 left, right, smallest 인덱스의 노드값에 대하여 가장 큰 값을 도출할 수 있게 되는 것이다.

        if smallest != i:

            self.data[smallest], self.data[i] = self.data[i], self.data[smallest]

# 위의 동작으로 인해서, 현재 가장 큰 값을 갖고 있는 노드의 인덱스인 smallest가 최초의 정렬하고자 했던 지점의 인덱스인 i의 노드로 치환되게 되며, 우리가 원했던 i인덱스부터 최대값을 갖는 힙의 구조의 조건을 갖추게 된다.
# 그런데 위의 동작을 완료하게 되면, i인덱스부터 왼쪽 자식 노드 오른쪽 자식노드까지만 최대힙의 구조를 갖게 되는데, 우리가 원하는 것은 i인덱스부터 시작하여 힙의 모든 노드까지의 형태가 최대힙의 조건을 만족시키는 형태로 구현하고자 하므로, 위의 코드에 더해서 다시한번 현재의 가장 작은 값을 표현하는 인덱스의 노드인 smallest 인덱스의 노드부터 또다시 최대힙정렬을 구현해줘야 한다.

            self.maxHeapify(smallest)












    def heapsort(unsorted):

        H = MaxHeap()

        for item in unsorted:

            H.insert(item)

        sorted = []

        d = H.remove()

        while d:

            sorted.append(d)

            d = H.remove()

        return sorted




















