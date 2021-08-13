import random

def f_discount_price(purchase_price):

    if purchase_price >= 200000:

        discount_price = int(purchase_price*0.8)

    elif purchase_price >= 100000:

        discount_price = int(purchase_price*0.9)

    else:

        discount_price = int(purchase_price*0.95)

    return discount_price


def f_lottery(discount_price):

    count = 0

    for i in range(1,4):

        num1 = int(input("숫자입력(1~5):"))

        num2 = random.randint(1,5) # 20% 확률로 당첨되는 상황을 표현한다.

        print("컴퓨터가 뽑은 랜덤 숫자:",num2)

        if num1 == num2:

            print("당첨되었습니다.")

            count = count + 1

        else:

            print("꽝")

    if count > 0:

        discount_price = int(discount_price*0.8)

    return discount_price



good_list = ["0", "지갑", "구두","화장품","티셔츠","케익"]

good_prcie = [0,360000,240000,180000,120000,40000]

purchase_goods_list = []

purchase_price = 0



while True:

    print("구매할 상품번호 입력")

    goods_num = int(input("():구매종료 1:지갑 2:구두 3:화장품 4:티셔츠 5:케익 ==>"))

    if goods_num == 0:

        break

    elif goods_num <= 5:

        purchase_goods_list.append(good_list[goods_num])

        purchase_price = purchase_price + int(good_prcie[goods_num])

    else:

        print("해당 상품번호가 없습니다.")


discount_price = f_discount_price(purchase_price)

discount_price = f_lottery(discount_price)


print("구매리스트:",purchase_goods_list)

print("할인 받은 실제 총 구매 금액:",discount_price,"원")

