num = 1

while not num >=2:

    num = int(input("피보나치 수열 항 개수:"))


fibo = [0,1]


for i in range(2,num):

    f1 = fibo[i-2]

    f2 = fibo[i-1]

    fibo.append(f1 + f2)


for j in fibo:

    print(j)


