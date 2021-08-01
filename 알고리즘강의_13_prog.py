###.1 스택의 응용

# 후위 표기법의 특징은, 앞에서부터 뒤로 후위 표기법 연산으로 나타낸 수식을 먼저 나타난 연산기호의 순서에 따라서 연산을 행하면 괄호와 사칙연산의 우선순위를 그대로 지키면서 연산을 할 수 있다는 것이다.

# 후위 표기법으로 나타낸 수식의 연산은 앞에 나온 두개의 피연산자를 뒤에 나온 연산자를 이용해 연산한다는 규칙으로 행해지는 것이 원칙이다.

# 그러므로, 이러한 원칙을 스택을 이용하여 구현해보면, 피연산자를 만나면 스택에 집어넣고 연산자를 만나면 스택에 존재하는 피연산자를 꺼내서 계산하고, 그 계산결과를 다시 스택에 집어넣어 나중에 나오는 연산을 적용하는 방식으로 구현할 수 있다.

# 이와같이 스택으로 후위표기법을 구현할 때, 항상 연산자를 만나면 연산자는 "두개"의 피연산자에 적용된다는 원칙을 유지해야한다.

##.1 알고리즘 구현 원칙

# 피연산자를 만나면 스택에 push한다

# 연산자를 만나면 스택에서 pop(1), pop(2) 와같이 pop을 "2회"한다.

# "(2) 연산 (1)"을 계산한다. 그리고 이 결과를 다시 스택에 push한다.

# 이러한 과정을 반복하며 수식의 끝값에 도달했을 때, 스택엔 하나의 결과값만이 존재하게 되고 이 하나의 결과값이 계산 결과가 된다.



def splitTokens(exprStr):
# exprStr 인자는 중위표현식으로 표현된 문자열 수식이다.

    tokens = []

    val = 0

    valProcessing = False

    for c in exprStr:

        if c == ' ':

            continue

        if c in '0123456789':

            val = val * 10 + int(c)

            valProcessing = True

        else:

# 숫자가 아닌 괄호나 +,-,*,/ 등의 연산자를 만난 경우를 표현한다.

            if valProcessing:

                tokens.append(val)

                val = 0

# val변수에 0을 할당하여 다시 새롭게 숫자를 처리할 수 있는 세팅을 갖추는 것이다.

            valProcessing = False

# 현재 10진수를 처리하고 있지 않았음을 valProcessing 에 False를 할당하여 표현한다.

            tokens.append(c)

# 현재 c는 괄호또는 연산자인 상태이므로, 이러한 괄호 또는 연산자를 token에 표현한다.

    if valProcessing:

        tokens.append(val)

    return tokens




























