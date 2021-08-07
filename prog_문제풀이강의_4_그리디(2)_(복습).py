###.1 그리디(큰 수 만들기)

# 그리디 알고리즘이 통하는 상황은, 앞 단계에서의 선택(앞자리에 큰수를 두는 것과 같은 선택)이 이후 단계에서의 동작에 의한 해(solution)의 최적성(optimality)에 영향을 주지 않는 상황이다.

# 문자열에 값을 모으는 것은 파이썬에서 문자열은 immutable한 특성이 있기 때문에 비효율적이다. 그러므로, mutable한 리스트를 생성하여 값을 모으는 것이 좋다.

# 파이썬에서 문자열의 대소관계는 사전순서를 따르는데 사전순서에 따르면 문자열 '1'과 '2'중 사전순서의 관점으로 봐도 '1'보다 '2'가 더 크기 때문에 문자열로 정의된 숫자의 비교도 int 형으로의 변환없이도 비교 가능하게 된다.

def solution(number,k):

    collected = []

    for i,num in enumerate(number):

# enumerate 메소드는 인덱스와 그 인덱스에 대한 값을 가지는 자료형에 대하여 인덱스와 그에 대한 자료형을 출력하여 할당해주는 메소드이다.

        while len(collected) > 0 and collected[-1] < num and k > 0:

            collected.pop()

            k -= 1

        if k == 0:

            collected = collected + list(number[i:])

            break

        collected.append(num)

# for문의 경우 이 경우 O(n)의 시간복잡도를 가지는 코드가 중첩되어있을지라도, 가장 바깥의 for문의 시간복잡도가 O(n) 이므로, 최종적으로 O(n)의 시간복잡도로 결정되게된다.

    collected = collected[:-k] if k > 0 else collected

# 위의 코드는 number에 '65432' 같은 문자열의 숫자가 정의되었을 때, k 값의 소멸 없이 append 동작만 이루어진채로 collected 리스트가 생성되었을 때 적용되어야하는 코드이다.

    answer = ''.join(collected)

    return answer


