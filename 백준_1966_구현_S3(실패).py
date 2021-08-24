from collections import deque

queue = deque()

T = int(input())

for i in range(T):

    N, M = map(int, input().split())

    priority = list(map(int,input().split()))


for i in priority:

    queue.append(i)

if queue[0] == max(queue):





print(queue)

print(max(queue))





