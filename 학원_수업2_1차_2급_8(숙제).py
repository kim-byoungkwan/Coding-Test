###.1

def solution(sentence):

    trash = [" ",",","."]

    word_real = []

    for i in sentence:

        if i in trash:

            continue

        else:

            word_real.append(i)

    stack = []

    que = []

    for i in word_real:

        stack.append(i)

        que.append(i)

    while stack:

        if stack.pop() == que.pop(0):

            continue

        else:

            return False

    return True

sentence ="palindrome"


print(solution(sentence))





