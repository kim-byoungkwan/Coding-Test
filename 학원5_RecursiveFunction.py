def factorial_iterative(n):

    result = 1

    for i in range(1,n+1):

        result = result * i

    return result


def factorial_recursive(n):

    if n <= 1:

        return 1

    else:

        return n * factorial_iterative(n-1)


print("반복적 구현 결과:",factorial_iterative(5))

print("재귀적 구현 결과:",factorial_recursive(5))