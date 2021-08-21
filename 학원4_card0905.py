import random

def func_random_card():

    cards = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

    card = random.choice(cards)

    return card

def func_to_num(card):

    if card == "A":

        card = 1

    elif card =="J":

        card = 11

    elif card =="Q":

        card = 12

    elif card == "K":

        card = 13

    else:

        card = int(card)

    return card


def func_to_score(card1,card2):

    c1 = func_to_num(card1)

    c2 = func_to_num(card2)

    score = (c1 + c2) % 10

    return score


cheolsu_point = 100

computer_point = 100

game_round = 0

cheolsu_card = []

computer_card = []


while True:

    game_round = game_round + 1

    if game_round > 1:

        next1 = input("계속하시겠습니까? y/n")

        if next1 == "n":

            print("게임종료!!")

            break

    print("==================================================")

    print(game_round,"라운드")

    print("==================================================")


    card1 = input("카드 입력:")

    cheolsu_card.append(card1)

    card1 = func_random_card()

    cheolsu_card.append(card1)


    for i in range(0,2):

        card2 = func_random_card()

        computer_card.append(card2)


    print("철수 카드:",cheolsu_card)

    print("컴퓨터 카드:",computer_card)


    print("카드를 바꿀 수 있습니다!!!!")

    count1 = int(input("슷자입력(숫자 번만큼 바꿀수 있음)==>"))

    for i in range(1,count1+1):

        card1 = func_random_card()

        if func_to_num(cheolsu_card[0]) < func_to_num(cheolsu_card[1]):

            tmp = cheolsu_card[0]

            cheolsu_card[0] = card1

            card1 = tmp

        else:

            tmp = cheolsu_card[1]

            cheolsu_card[1] = card1

            card1 = tmp

        print("철수 카드:",cheolsu_card)


        card2 = func_random_card()

        if func_to_num(computer_card[0]) < func_to_num(computer_card[1]):

            tmp = computer_card[0]

            computer_card[0] = card2

            card2 = tmp

        else:

            tmp = computer_card[1]

            computer_card[1] = card2

            card2 = tmp

        print("컴퓨터 카드:",computer_card)

        cheolsu_score = func_to_score(cheolsu_card[0],cheolsu_card[1])

        computer_score = func_to_score(computer_card[0],computer_card[1])


        print("철수 카드 점수:",cheolsu_score)

        print("컴퓨터 카드 점수:",computer_score)


        if i == count1:

            point = 20

        else:

            point = 5


        print(point,"점 판")


        if cheolsu_score > computer_score:

            cheolsu_point = cheolsu_point + point

            computer_score = computer_score - point

            print("철수가 이겼습니다.")

        elif cheolsu_score < computer_score:

            computer_point = computer_point + point

            cheolsu_point = cheolsu_point - point

            print("컴퓨터가 이겼습니다.")

        else:

            print("비겼습니다.")


    print("철수와 컴퓨터의 현재 점수는")

    print("철수:",cheolsu_point)

    print("컴퓨터:",computer_point)

    print("--------------------------------------")


del cheolsu_card[1]

del cheolsu_card[0]

del computer_card[1]

del computer_card[0]



















