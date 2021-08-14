def solution(attack,recovery,hp):

    count = 0

    while hp > 0:

        hp = hp - attack

        count += 1

        hp = hp + recovery

    return count


attack = 30

recovery = 10

hp = 60

print(solution(attack,recovery,hp))