###.1

def solution(programs):

    max_value = 0

    min_value = 999999

    for i in range(len(programs)):

        if programs[i][0] > max_value:

            max_value = programs[i][0]

        if programs[i][1] < min_value:

            min_value = programs[i][1]

    common_3 = min_value-max_value
    




programs = [[1,6],[3,5],[2,8]]

solution(programs)