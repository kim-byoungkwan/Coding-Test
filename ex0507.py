s_count = int(input())

scores = []

names = []

while not len(scores) == s_count:

    name = input("이름을 입력하세요:")

    score = int(input("점수를 입력하세요:"))

    print("------------------------")

    names.append(name)

    scores.append(score)

sum1 = 0

seq = 0

for i in scores:

    sum1 = sum1 + i

    rank =1

    for j in scores:

        if i < j:

            rank = rank + 1

    print("%s학생의 점수는 %d점이고 등수는 %d등 입니다."%(names[seq],i,rank))

    seq = seq + 1

print("--------------------------------------------")

print("전체 학생의 평균 점수는:",sum1/s_count)