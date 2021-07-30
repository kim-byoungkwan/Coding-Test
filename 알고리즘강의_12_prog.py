###.1 스택의 응용

##.중위표기법
# 연산자가 피연산자들의 사이에 위치하는 연산 표기법으로 일반적인 연산 표기법이다.

##.후위표기법
# 연산자가 피연산자들의 뒤에 위치하는 표기법이다. 이러한 연산 표기법을 사용하면 괄호를 사용할 필요도 없어진다.


# 연산자의 우선순위를 정의하는 딕셔너리로서 곱셉과 나눗셈의 우선순위가 3으로 가장 높다.

class ArrayStack:

    def __init__(self):

        self.data = []

    def size(self):

        return len(self.data)

    def isEmpty(self):

        return self.size() == 0

    def push(self, item):

        self.data.append(item)

    def pop(self):

        return self.data.pop()

    def peek(self):

        return self.data[-1]

prec = {

    '*' : 3,
    '/' : 3,
    '+' : 2,
    '-' : 2,
    '(' : 1

}

def solution(S):

    opStack = ArrayStack()

    answer = ''

    for i in S:

        if i == '(':

            if opStack.isEmpty() == True:

                opStack.push(i)

            else:

                opStack.push(i)


        else:

            if opStack.isEmpty() == True:

                if i in prec:

                    opStack.push(i)

                else:

                    answer = answer + i

            else:

                if i in prec:

                    temp = opStack.peek()

                    if prec[temp] < prec[i]:

                        opStack.push(i)

                    else:

                        out = opStack.pop()

                        answer = answer + out

                        opStack.push(i)

                else:

                    if i == ')':

                        while True:

                            out = opStack.pop()

                            answer = answer + out

                            peek = opStack.peek()

                            if peek == '(':

                                break

                    else:

                        answer = answer + i

    while True:

        peek = opStack.peek()

        if peek == '(':

            break

        else:

            out = opStack.pop()

            answer = answer + out
            


    return answer


print(solution('A*(B+C)'))