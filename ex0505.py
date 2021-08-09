scores = []

while not len(scores) == 5:

    score = int(input("점수입력:"))

    scores.append(score)

seq = 0

for i in scores:

    seq = seq + 1

    rank = 1

    for j in scores:

        if i < j:

            rank = rank + 1

    print("%d번째 학생의 점수는 %d점이고 등수는 %d등 입니다."%(seq,i,rank))

