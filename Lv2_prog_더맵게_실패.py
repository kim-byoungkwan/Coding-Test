def solution(scoville, K):

    scoville.sort()

    count = 0

    for i in range(len(scoville)):

        if scoville[i] >= K:

            break

        else:

            scoville_first = scoville.pop(i)

            scoville_second = scoville.pop(i)

            scoville_final = scoville_first + (scoville_second*2)


            scoville.append(scoville_final)

            count = count + 1

            scoville.sort()


            if scoville[i] >= K:

                break

            else:

                continue


    return count


print(solution([1,2,3,9,10,12],7))


