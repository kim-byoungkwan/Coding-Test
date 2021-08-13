###.1

def solution(characters):

    box = []

    box.append(characters[0])

    for i in range(1,len(characters)):

        if characters[i-1] != characters[i]:

           box.append(characters[i])

        else:

            continue

    word = "".join(box)

    return word


characters = "senteeeenccccceeee"


print(solution(characters))


