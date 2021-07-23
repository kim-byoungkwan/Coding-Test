###.1

import time

n = int(input("Number of elements: "))

haystack = [k for k in range(n)]

print("Searching for the maximum value...")

ts = time.time()
maximum = max(haystack)
elaspsed = time.time() - ts

print("Maximum element = %d, Elapsed time = %.2f" % (maximum, elaspsed))

# 리스트의 요소값의 최대값을 구하는 데에 얼마의 시간이 걸리는 지를 구하는 프로그램이다.
# 리스트의 요소값의 최대값을 구하기 위해선 반드시 리스트의 모든 요소값을 확인해보지 않고는 불가능하다.
# 그러므로 이렇게 리스트의 모든 요소값을 확인해야 하는 비효율성을 극복하기 위해선 효율적인 자료구조를 만들어서 사용해야한다.

# 프로그래밍에서 알고리즘이란 주어진 문제의 해결을 위한 자료구조와 연산 방법에 대한 선택을 의미한다.

# 해결하고자 하는 문제가 어떤 형태인지에 따라서, 최적의 해법은 서로 다르다. 그러므로 이러한 선택을 효율적으로 하기 위해서 자료구조를 이해해야 한다.



