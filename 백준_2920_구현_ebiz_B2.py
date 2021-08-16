def identifier(x):

    box = []

    for i in range(1,len(x)):

        if x[i-1] < x[i]:

            box.append("ascending")

        elif x[i-1] > x[i]:

            box.append("descending")

        else:

            box.append("mixed")

    box = set(box)

    box_list = list(box)

    if len(box_list) == 1:

        result = box_list[0]

    else:

        result = "mixed"


    return result


x = list(map(int,input().split()))


print(identifier(x))
