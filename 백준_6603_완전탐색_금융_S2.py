import itertools

def lotto_func(box_K_S):

    box = []

    K = box_K_S[0]

    S = [box_K_S[j] for j in range(len(box_K_S)) if j>0]


    combi_K = list(itertools.combinations(S,6))


    for m in combi_K:

        m = list(map(str,m))

        result = " ".join(m)

        box.append(result)

    return box


while True:

    box_K_S = list(map(int,input().split()))

    if box_K_S[0] == 0:

        break

    else:

        for j in lotto_func(box_K_S):

            print(j)

        print()

