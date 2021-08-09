def factorial(n):

    num = 1

    for i in range(1,n+1):

        num = num*i

    return num

s = int(input("숫자를 입력하세요:"))

result = factorial(s)

print("결과:",result)

