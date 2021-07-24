###1. 정렬과 탐색

# sorted() 는 정렬된 새로운 리스트를 얻도록 해주는 내장함수이다.
# sort() 는 리스트의 메소드로서 해당 리스트를 정렬한다.

L = [3,8,2,7,6,10,9]

L2 = sorted(L)

print(L2)

print(L)

# 즉 sorted() 내장함수로 새로운 리스트를 생성하고, 원래의 리스트 L은 원래 그대로 보존되는 개념인 것이다.

L.sort()

print(L)

# sort() 메소드는 원래의 리스트에 메소드를 적용하여 변경시키게 된다.


L2 = sorted(L,reverse=True)

print(L2)

L.sort(reverse=True)

print(L)


# 리스트의 요소가 문자열로 이루어진 경우의 정렬은 알파벳의 순서를 따라서 정렬되게 된다.
# 만약 리스트 요소의 문자열의 길이를 순서로 정렬하려면 정렬에 이용하는 키(Key)를 지정해서 해야한다.

L_3 = ['abcd','xyz','spam']

L_3_new = sorted(L_3, key=lambda x:len(x))

print(L_3_new)


L_4 = ['spam','xyz','abcd']

L_4_new = sorted(L_4, key=lambda x:len(x))

print(L_4_new)

# 길이가 같은 문자열의 경우 원래 리스트에서의 위치가 앞선 문자열을 앞으로 하여 정렬하게 된다.


##.lamda 식
## lamda 형식은 함수표현식으로 lamda x,y : x+y(10,20) 이라는 lamda 함수식은 x와y를 변수로 하는 함수가 x+y의 함수식을 갖는 함수를 의미하는 약속이다.


L_5 = [{'name':'John','score':83},
       {'name':'Paul','score':92}]

# L_5 리스트는 두개의 딕셔너리로 각 요소가 구성된 리스트이다.

L_5.sort(key=lambda x:x['name'])

print(L_5)

# 리스트의 요소를 name를 기준으로 하여 기본값인 오름차순으로 정렬하는 식이다.

L_5.sort(key=lambda x:x['name'],reverse=True)

print(L_5)

# 리스트의 요소를 score를 기준으로 하여 기본값인 오름차순의 반대인 내림차순으로 정렬하는 식이다.



###.2 선형탐색

# 선형탐색은 리스트의 길이에 비례하여 시간이 소요되는 O(n)의 알고리즘이다. 즉, 최악의 경우 내가 찾고자하는 리스트의 요소값이 리스트의 가장 끝에 위치할 경우 모든 원소를 다 비교해야 할 정도로 시간이 오래 걸린다.


def linear_search(L,x):

    i=0

    while i < len(L) and L[i] != x:

        i+=1

    if i < len(L):

        return i

    else:

        return -1


S = [3,8,2,7,6,10,9]

print(linear_search(S,6))

# 선형탐색 함수이다.


###.3 이진탐색

# 탐색하려는 리스트가 이미 정렬되어있는 경우에만 적용가능하다. 즉, 크기 순으로 리스트의 요소값이 정렬되어 있다는 성질을 이용하는 알고리즘이다.

# 이진탐색 알고리즘을 사용하면, 한번의 비교가 일어날 때마다 리스트가 반씩 줄어들게 되므로 선형탐색의 방법보다 시간효율성이 높게 된다. 즉, O(logn)의 로그n에 비례하는 시간효율성을 갖게 된다. (divide & conquer)









