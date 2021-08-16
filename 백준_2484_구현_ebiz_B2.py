def dice_calculator(a,b,c,d):

    result = [a,b,c,d]

    dict = {}

    box = []

    box_value = []

    box_key = []

    for i in result:

        dict[i] = dict.get(i,0) + 1

    dict_value = list(dict.values())

    if max(dict_value) == 1:

        dict_sorted_key = sorted(dict.items(),key= lambda x: x[0], reverse=True)

        for key,value in dict_sorted_key:

            box.append((key)*100)

            break

    else:

        dict_sorted_value = sorted(dict.items(),key= lambda x:x[1],reverse=True)

        for key,value in dict_sorted_value:

            box_value.append(value)

            box_key.append(key)

        for key, value in dict_sorted_value:

            if value == 4:

                box.append(50000+(key)*5000)

                break

            elif value == 3:

                box.append(10000+(key)*1000)

                break

            elif value == 2 and box_value.count(2) == 2:

                box.append(1000+key*500)

                continue

            elif value == 2 and box_value.count(1) == 2:

                box.append(1000+key*100)

                break

    final = sum(box)

    return final


N = int(input())

last_box = []

for i in range(N):

    a,b,c,d = map(int,input().split())

    last_box.append(dice_calculator(a,b,c,d))


print(max(last_box))
























