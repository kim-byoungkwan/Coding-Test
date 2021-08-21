###.1

n,k = map(int,input().split())

result = 0

while n >= k:

    while n % k != 0:

        n = n -1

        result = result +1

    n = n // k

    result = result + 1

while n > 1:

    n = n -1

    result = result + 1

print(result)


###.2

n,k = map(int,input().split())

result = 0

n = 26, k =5

while True:   1    5
              5    5
    target = (n // k)*k
    5                  1    0
    result = result + (n - target)

# result에는 현재 1을 빼야하는 횟수가 저장되어 있다.
    0    0
    n = target
    5
# 이때의 n은 k로 나눠떨어지는 최초의 n을 표현한다.

    if n < k:

        break

    result = result + 1

    n = n//k



# n을 k로 한번 나눴을 때의 횟수를 표현한다.



result = result + (n-1)


print(result)


