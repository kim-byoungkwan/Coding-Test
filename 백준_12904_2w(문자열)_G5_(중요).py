###.1

import sys

input = sys.stdin.readline

def change(s):

    if s == "A":

        s = "B"

    else:

        s = "A"

    result = s

    return result



def solution(word):

    box = []

    temp = word

    out = ''

    for i in range(len(temp)):

        out = out + change(temp[i])

    out = out + "B"

    temp = out

    box.append(temp)

    temp = word

    temp = temp + "A"

    box.append(temp)

    return box


S = input()

T = input()

box_start = [S]

box_append_all = []

box_append_all.append(S)


new = []


judge = True


while judge:

    for i in box_start:

        box_append_all = box_append_all + solution(i)

        new = new + solution(i)

    box_start = new

    new = []

    if len(box_append_all[-1]) == len(T):

        judge = False

    else:

        continue


if T in box_append_all:

    print(1)

else:

    print(0)

