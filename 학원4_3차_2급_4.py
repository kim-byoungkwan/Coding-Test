###.1

def solution(words,word):

    count = 0

    for find in words:

        for a,b, in zip(find,word):

            if a != b:

                count = count + 1

            else:

                continue

    return count

words = ["CODE","COED","CDEO"]

word = "CODE"

print(solution(words,word))


