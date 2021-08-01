##.2 배열로 구현한 환형 큐

class CircularQueue:

    def __init__(self,n):

# 여기서 인자 n은 배열로 구현한 환형큐의 저장공간인 환형큐의 길이를 의미하는 값이다.

        self.maxCount = n

# 큐의 최대 저장공간의 크기를 maxCount 라는 변수에 저장한다.

        self.data = [None] * n

# 큐의 실제 데이터 원소가 저장되는 공간을 data 변수로 표현하고, 그 공간이 n개 이므로 위와같이 n개의 데이터 원소가 포함될 수 있는 공간을 형성해준다.

        self.count = 0

# 현재 큐에 들어있는 데이터 원소의 개수는 현재 환형 큐가 빈 큐이므로 count는 0으로 표현된다.

        self.front = -1

# 데이터를 꺼내는 곳의 위치(인덱스)를 front가 표현한다.

        self.rear = -1

# 데이터를 집어 넣는 곳의 위치(인덱스)를 rear가 표현한다.


    def size(self):

        return self.count

# 현재의 환형 큐의 길이를 반환하는 메소드이다.

    def isEmpty(self):

        return self.count == 0


    def isFull(self):

        return self.count == self.maxCount


    def enqueue(self,x):

        if self.isFull():

            raise IndexError('Queue full')

        self.rear = (self.rear +1) % self.maxCount

# 이와 같이 self.rear를 설정하면, 이경우 환형큐의 저장공간이 6인 상태이므로, self.rear의 값은 0,1,2,3,4,5,1,2 와 같은 값을 갖게 되고,이러한 값이 계속 반복되는 효과로 인해서 큐의 가장 끝값에 데이터를 집어넣은 다음에 다시 첫번째 값으로 데이터를 집어넣는 흐름이 형성될 수 있게 되면서 환형큐가 형성되게 된다.

        self.data[self.rear] = x

# 위의 코드로 인해 enqueue 동작은 환형 큐의 각 위치에 값을 덮어 씌우는 방식으로 동작하게 되는 것이다.

        self.count += 1

# enqueue 동작이 발생하면 큐에 존재하는 데이터의 개수가 1개 증가하게 되므로 위의 동작을 실행해줘야 한다.


    def dequeue(self):

        if self.isEmpty():

            raise IndexError('Queue empty')

        self.front = (self.front +1) % self.maxCount

# self.rear의 경우와 마찬가지로 이와 같이 self.front를 정의하게 되면 self.front 값은 0,1,2,3,4,5,1,2 와 같은 값을 갖게 되면서 현재 큐의 처음부터 끝의 모든 값을 순환하며 데이터를 빼낼 수 있는 상태가 완성되고, 이러한 동작으로 인해 환형큐에서의 dequeue 메소드가 성립되게 된다.

        x = self.data[self.front]

        self.count -= 1

# dequeue 동작이 실행되고 나면 count 값이 -1 감소 되므로, 환형 큐에서 dequeue 이후에 self.front 인덱스 위치에 존재하는 값을 굳이 삭제하지 않아도 count 값이 0이 된 순간에 환형큐에 값이 존재하더라도 서두에 규정한 if 문에 의해 dequeue 동작이 불가능하다는 출력을 해줄 수 있게된다.

        return x


    def peek(self):

        if self.isEmpty():

            raise IndexError('Queue empty')

        return self.data[self.front +1 % self.maxCount]

# peek 값 또한 이경우의 환형 큐에서는 0,1,2,3,4,5,1,2 의 순서로 값이 반복되어야 하므로, maxCount로 나누는 동작을 구현하지 않으면 self.front 가 환형 큐의 맨끝 위치인 5를 표현하는 경우에 위의 코드에서 self.front +1 동작이 수행되므로 self.data[6] 의 동작이 수행되게 되어 오류가 발생하게 된다. 즉, self.front 가 5 인 경우엔 환형큐의 마지막 값이 출력된 상태라는 것이므로 peek동작은 환형큐의 0번째 위치의 값을 보여주어야 하는 상황이다. 즉, 5+1 % 6 = 0 이므로 위와 같이 인덱스 값에 % maxCount 동작을 포함시켜주어야 한다.

