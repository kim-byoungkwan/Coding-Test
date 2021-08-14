def solution(words):

    box = []

    for i in words:

        if len(i) >= 5:

           box.append(i)

        else:

            continue

    result = "".join(box)

    if len(result) >0 :

        return result

    else:

        return "empty"


words = ["my","favorite","color","is","violet"]

words_2 = ["yes","i","am"]

print(solution(words))