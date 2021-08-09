def solution(price,grade):

    answer = 0

    if grade =="S":

        answer = int(price*0.95)

    if grade =="G":

        answer = int(price*0.9)

    if grade =="V":

        answer = int(price*0.85)


    return answer


price1 = 2500
grade1 = "V"

result = solution(price1,grade1)

print(result)


price2 = 96900
grade2 = "S"

result2 = solution(price2,grade2)

print(result2)