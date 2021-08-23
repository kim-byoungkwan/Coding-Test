def solution(member_age,transportation):

    if transportation == "Bus":

        transportation_cost = [40000,15000]

    elif transportation == "Ship":

        transportation_cost = [30000,13000]

    else:

        transportation_cost = [70000,45000]

    if len(member_age) >= 10:

        saled_price = [0.9,0.8]

    else:

        saled_price = [1,1]

    for i in member_age:

        if i >= 20:

            index = 0

            transportation_cost[index] * saled_price[index]

        else:

            index = 1



