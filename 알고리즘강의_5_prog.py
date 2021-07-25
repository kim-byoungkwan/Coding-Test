###.1 재귀 알고리즘의 응용

# 재귀적 알고리즘이 사람의 생각을 코드로 옮기기에 직관적인 측면이 있지만, 항상 반복적인 방법에 비해 효율적인 측면에서 비효율적일 수 있다.

# 재귀함수란 하나의 함수에서 자신을 다시 호출하여 작업을 수행하는 함수를 말한다.

##.1 조합의 표현

from math import factorial as f

def combi(n,m):

    return f(n)/ (f(m)*f(n-m))

print(combi(5,2))


#. m개에서 n개를 택하는 조합의 개념은 특정한 한개를 포함하여 n개를 택하는 조합과 특정한 한개를 포함하지 않고 n개를 택하는 두가지의 방법으로 나누어 생각해볼 수 있다.

def combi(n,m):

    if n == m:

        return 1

    elif m == 0:

        return 1

    else:

        return combi(n-1,m) + combi(n-1,m-1)


import time


def rec(n):

    if n <= 1:

        return n

    else:

        return rec(n -1) + rec(n - 2)


def iter(n):

    if n <= 1:

        return n

    else:

        i = 2
        t0 = 0
        t1 = 1

        while i <= n:

            t0, t1 = t1, t0+t1

            i += 1

        return t1


while True:

    nbr = int(input("Enter a number: "))
    if nbr == -1:

        break

    ts = time.time()
    fibo = iter(nbr)
    ts = time.time() - ts
    print("Iterative version: %d (%.3f)" %(fibo, ts))

    ts = time.time()
    fibo = rec(nbr)
    ts = time.time() - ts
    print("Recursive version: %d (%.3f)" %(fibo, ts))


# 피보나치 수열의 재귀함수 버전과 반복버전의 시간차이가 얼마나 발생하는지를 확인할 수 있는 코드이다.
# 여기에서 확인할 수 있는 것처럼 재귀적인 방법에는 시간 성능적인 한계가 존재할 수 있다.














