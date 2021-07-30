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


def solution(expr):

    match = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    S = ArrayStack()

    for c in expr:

        if c in '({[':

            S.push(c)

        elif c in match:

# 이때 c는 match 딕셔너리에서의 key를 의미하는 문법이다.

            if S.isEmpty() == 0 :

                return False

# 이 조건은 현재 c가 ),},] 중에 하나인 상태에서 S 스택에 아무것도 존재하지 않는 상태이면 ),},]중 하나인 c를 스택에 넣는 것은 오류임을 의미하는 코드이다.

            else:

                t = S.pop()

# 반드시 pop을 사용해야만, 다음에 올 ),],} 기호 중 하나와 그 이전에 들어간 (,{,[ 기호 중 하나가 대응되는 지를 확인할 수 있다.

                if t != match[c]:

                    return False

# 스택의 가장 위에 있는 값은 현재 c인 ),},] 에 대응되는 기호여야 등식이 성립한다.



return S.isEmpty()

# 그 어떤 (,[,{ 기호도 pop을 모두 수행했음에도 추가적으로 남아 있으면 안되므로 위의 코드로 reture 값을 출력해야한다.