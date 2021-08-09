def sum(n):

    num = 0

    for i in range(1,n+1):

        num = num + i

    return num

n = int(input("숫자입력:"))

s = sum(n)

print("총합:",s)

