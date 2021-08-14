# 트럭 운송비

def func_transport_cost():

    truck_size = int(input("트럭 크기 입력(단위 톤):"))

    if truck_size >= 5:

        transport_cost = 40

    elif truck_size >=1:

        transport_cost = 30

    else:

        transport_cost = 20

    return transport_cost

# 인건비

def func_payroll_cost():

    payroll_cost = 0

    payroll_cost_part = 0

    while True:

        print("0:종료 1:레몬농장 2:망고스틴농장 3:포도농장 4:사과농장")

        farm = int(input("농장번호 입력:"))

        if farm == 0:

            break

        people_number = int(input("수확 시 필요한 일일 채용 인원 수 입력:"))

        if farm == 4:

            payroll_cost_part = people_number*8

        else:

            payroll_cost_part = people_number*7

        payroll_cost = payroll_cost + payroll_cost_part

    return payroll_cost


# 하루 과일매출

def func_day_fruit_sales():

    day_fruit_sales = 0

    day_fruit_sales_part = 0

    fruit_kind_number = int(input("판매한 과일 종류 수 입력:"))

    for i in range(0,fruit_kind_number):

        print("1:레몬 2:망고스틴 3:포도 4:사과")

        fruit_kind = int(input("판매한 과일 번호 입력:"))

        fruit_box = int(input("판매한 과일 상자 수:"))

        if fruit_kind == 1:

            day_fruit_sales_part = fruit_box*2

        elif fruit_kind == 2:

            day_fruit_sales_part = fruit_box*3

        elif fruit_kind == 3:

            day_fruit_sales_part = fruit_box*4

        else:

            day_fruit_sales_part = fruit_box*5

        day_fruit_sales = day_fruit_sales + day_fruit_sales_part

    return day_fruit_sales

# 출력

def func_day_profit_print():

    print("---------------------------------------")

    print("하루 과일매출:",day_fruit_sales,"만원")

    print("인건비:",payroll_cost,"만원")

    print("트럭운송비:",transport_cost,"만원")

    print("---------------------------------------")

    print("하루 순익:",day_profit,"만원")

    print("---------------------------------------")

# 메인 프로그램

print("******농장 순익 계산 시작******")

sum_profit = 0

while True:

    print("0:종료, 해당날짜:순익계산")

    sales_day = input("판매 날짜 입력:")

    if sales_day == '0':

        break

    print("---------------------------------------")

    print(sales_day,"순익현황")

    print("---------------------------------------")

    transport_cost = func_transport_cost()

    payroll_cost = func_payroll_cost()

    day_fruit_sales = func_day_fruit_sales()

    day_profit = day_fruit_sales - payroll_cost - transport_cost

    func_day_profit_print()

    sum_profit = sum_profit + day_profit


print("---------------------------------------")

print("총 순익은:",sum_profit,"만원")

print("---------------------------------------")

print("******농장 순익 계산 종료******")



