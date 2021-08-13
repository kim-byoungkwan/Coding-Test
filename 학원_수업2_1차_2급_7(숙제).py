###.1

def solution(scores):

    box = []

    for i in scores:

        if i >= 650 and i < 800:

            box.append(i)

        else:

            continue

    return len(box)


scores = [650,722,914,558,714,803,650,679,669,800]

print(solution(scores))




