###.1 해시(지문이해)

# 문제의 크기는 무엇에 지배되는지를 생각한다.
# 어떠한 제약조건이 문제에 존재하는지를 생각한다.

##.1 처음 완성 답안
# def solution(participant, completion):
#
#     answer = ''
#
#     for i in participant:
#
#         num_p = participant.count(i)
#
#         num_c = completion.count(i)
#
#         if num_p > 1:
#
#             if num_p != num_c:
#
#                 answer = answer + i
#
#                 break
#
#         else:
#
#             if num_p != num_c:
#
#                 answer = answer + i
#
#                 break
#
#     return answer
#
#
participant = ['leo','eden','kiki','leo']

completion = ['eden', 'kiki','leo']
#
#
# print(solution(participant,completion))



##.2 해시(Hash)

# 해시란 일반적인 배열 자료구조의 경우 인덱스로 배열에 포함된 데이터를 찾아갈 수 있는 것과는 달리, 문자열 형태의 키(key)를 통해서 그 키에 저장된 값을 해시 테이블에 매핑(mapping)하여 찾아갈 수 있는 형태의 자료구조를 의미한다. 이때, 값을 가진 키를 해시 테이블에 어떠한 공간에 할당할 때, 해시함수(hash function)를 이용해 값을 출력하여 그 출력된 값을 기준으로하여 해시테이블에 할당하게 된다. 해시함수는 가급적이면 값을 가진 키가 해시 테이블의 서로 다른 칸에 할당될 수 있도록 값을 출력하는 함수이다.

# 이때 해시테이블의 각각의 칸들을 해시버킷(hash bucket)이라고 한다. 이러한 해시버킷의 수가 많을 수록 서로다른키가 서로다른 버킷에 할당될 수 있는 확률이 높아진다.

# 만약 해시함수를 이용해 키를 해쉬(키를 해시 테이블에 할당하는 것)할 때, 서로 다른 키값이 동일한 값으로 할당될 때, 이를 충돌이 일어났다고 한다.

# 파이썬에서는 사전(dictionary) 자료구조를 구현할 때, 내부적으로 해시테이블을 이용하기 때문에 사전의 원소들을 해시를 이용해서 O(1) 시간에 접근 가능하다.




def solution(participant, completion):

    answer =''

    dict = {}

    for x in participant:

        dict[x] = dict.get(x,0) + 1

# 딕셔너리 자료구조의 메소드인 get를 이용하면 위와같이 dict에 x 키가 존재하면 그에 대한 value 값을 출력해주고, x 키가 dict에 존재하지 않으면 0을 value로 출력해줄 수 있다. 따라서, 위의 코드에서 dict의 키의 값인 x에는 원래 x 키의 value 값 + 1이 할당되게 된다.

# 이러한 딕셔너리의 메소드를 이용할 때 기억해야 할 점은 파이썬에서 딕셔너리 자료구조는 내부 본질적으로 해쉬테이블을 이용하여 구현되기 때문에 파이썬 딕셔너리 자료구조의 원소에 접근하는 동작은 상수시간에 이루어진다는 것이다.

# 위의 for문의 시간 복잡도는 파이썬에서 딕셔너리 자료형은 해시테이블의 형태로 접근하게 되므로 각각의 key를 표현하는 x에 접근하는데에 상수시간 O(1)이 소요되게된다. 따라서 위의 for문을 수행하는데에 최종적으로 걸리는 시간은 participant 배열의 모든원소n에 접근하는 시간인 O(n) 으로 결정되게 된다.

    for x in completion:

        dict[x] = dict[x] -1

# 위의 for문의 시간복잡도는 O(n-1) 이다.

    dnf = [k for k,v in dict.items() if v > 0]

# 위의 dnf 변수에 대한 코드는 현재 key와 value가 할당된 자료구조인 dict의 key와 value를 출력해주는 메소드인 item()를 이용해 for 문의 변수 k와 v에 각각 할당하고, for문의 각 회차마다 k를 출력값으로 출력해주어 그 값을 dnf 리스트에 할당해주는 코드이다. 이때, for 문의 변수인 v는 dict의 value를 표현하고, if 조건문에 의해 0이 아닌 value값에 대해서만 적용된다.

# 위의 for문과 if문의 시간복잡도는 우선 dict 딕셔너리의 모든 key와 value에 접근해야 하므로 딕셔너리의 모든 원소의 개수만큼 시간이 소요되게 된다.

    answer = dnf[0]

    return answer

# 최종적으로 위의 코드의 시간복잡도는 모든 코드가 O(n)의 시간복잡도를 가지므로, n에 대하여 선형 시간복잡도를 갖게된다. (시간복잡도는 코드를 구성하고 있는 각각의 코드에서 발생하는 최대 시간복잡도로 결정되게 된다. 이 경우 최대 시간 복잡도는 모든 코드에서 O(n) 이므로 최종적인 전체 코드의 시간복잡도는 O(n) 으로 결정되게 된다)


##.3 다른 코드

def solution(participant, completion):

    participant.sort()

    completion.sort()

    for i in range(len(completion)):

        if participant[i] != completion[i]:

            return participant[i]

    return participant[len(participant)-1]

# 위와 같이 배열을 이용한 코드는 sort()라는 메소드를 이용해야하고, sort() 메소드의 동작의 시간복잡도는 O(nlogn) 이라는 것이 알려져 있으므로, 해시를 이용한 코드의 시간복잡도가 O(n)인 것보다 더 큰 시간복잡도인 O(nlogn)의 시간복잡도를 갖게되므로 시간효율성 면에서 비효율적이다.





















