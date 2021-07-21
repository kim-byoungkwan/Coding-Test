
def solution(progresses, speeds):

    count = 0

    final = []

    final_count = []


    for i in range(len(progresses)):

        progresses_left = 100 - progresses[i]

        if progresses_left % speeds[i] == 0:

            final.append(progresses_left // speeds[i])

        else:

            final.append((progresses_left // speeds[i])+1)


    for j in range(len(progresses)-1):

        if final[j] >= final[j+1]:

            count = count + 1

            continue

        else:

            count = count + 1

            final_count.append(count)

            count = 0

            continue

    final_count.append(count+1)

    return final_count



print(solution([93,93,93,93,93],[1,1,1,1,1]))