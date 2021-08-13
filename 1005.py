def get_max():

    max = playerScore[0]

    for i in range(nPlayer):

        if max < playerScore[i]:

            max = playerScore[i]

    return max


def get_winner(max):

    winList = []

    for i in range(nPlayer):

        if playerScore[i] == max:

            winList.append(i+1)

    print("최종우승자는:")

    for i in winList:

        print("친구",i,"입니다.")



print("***다트 게임을 시작합니다.***")

nPlayer = int(input("게임에 참여할 인원 수:"))

goalScore = int(input("목표점수:"))

nRound = 0

playerScore = []


for i in range(nPlayer):

    playerScore.append(0)


judge = True


while judge:

    nRound = nRound + 1

    print(nRound,"라운드")

    print("현재점수:",playerScore)

    for j in range(nPlayer):

        print("친구",j+1)

        score = int(input("점수입력:"))

        playerScore[j] = playerScore[j] + score

    for score in playerScore:

        if score >= goalScore:

            judge = False

print("최종점수:",playerScore)

max = get_max()

get_winner(max)

