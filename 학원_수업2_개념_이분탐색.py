def binary_search(a,x):

    start = 0

    end = len(a)-1

    while start <= end:

        mid = (start + end)//2

        if x == a[mid]:

            return mid

        elif x > a[mid]:

            start = mid + 1

        else:

            end = mid - 1

    return -1

box = [1,3,8,15,27,38,49,61,82]

print(binary_search(box,38))
print(binary_search(box,60))


