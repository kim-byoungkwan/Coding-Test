import random

chance = 5

right_answer_count = 0

user_answer = []

question_word_tmp = []

alphabets = "abcdefghijklmlopqrstuvwxyz"

words = ["print","input","continue","break","for","while"]


question_word = random.choice(words)


for i in question_word:

    user_answer.append("_")

    question_word_tmp.append(i)


print("현재 남은 기회:",chance)


while True:

    print(alphabets)

    print(" ".join(user_answer))

    alphabet = input("알파벳 입력:")


    right_answer_flag = False

    for i in range(len(question_word)):

        if question_word_tmp[i] == alphabet:

            user_answer[i] = alphabet

            question_word_tmp[i] ='/'

            right_answer_count = right_answer_count + 1

            right_answer_flag = True


    if (right_answer_flag == False) and (alphabet in question_word):

        print("이미 입력한 글자 입니다.")

    elif right_answer_flag == True:

        print("정답에 해당하는 알파벳 입니다.")

    else:

        print("해당 글자는 단어에 없습니다.")

        chance = chance -1



    alphabets = alphabets.replace(alphabet,"/")


    if chance ==0:

        print("GAME OVER")

        break

    else:

        print("현재 남은 기회:",chance)


    if right_answer_count == len(question_word):

        print(" ".join(user_answer))

        print("정답입니다!")

        break







