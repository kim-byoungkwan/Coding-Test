num_T = int(input())

result = 0

for i in range(num_T):

    count = 0

    num_child = int(input())

    num_candy = list(map(int, input().split()))

    # 모두 짝수로 초기화

    for m in range(num_child):

        if num_candy[m] % 2 != 0:

            num_candy[m] = num_candy[m] + 1

        else:

            continue

    while len(list(set(num_candy))) != 1:

        count = count + 1

        list_count_half = []

# 절반 값이 할당된 리스트를 형성하고, 원래 리스트 값에서 절반을 뺌

        for k in range(num_child):

            list_count_half.append((num_candy[k] // 2))

            num_candy[k] = (num_candy[k] // 2)


        for j in range(1,num_child):

            if j == num_child-1:

                num_candy[0] = num_candy[0] + list_count_half[j]

                num_candy[j] = num_candy[j] + list_count_half[j-1]

            else:

                num_candy[j] = num_candy[j] + list_count_half[j-1]


        for n in range(num_child):

            if num_candy[n] % 2 != 0:

                num_candy[n] = num_candy[n] + 1

            else:

                continue

    print(count)

