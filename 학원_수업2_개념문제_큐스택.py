def f_r_check(s):

    que = []

    stack = []

    for i in s:

        if i.isalpha():

            que.append(i.lower())

            stack.append(i.lower())

    while que:

        if que.pop(0) != stack.pop():

            return False

    return True

print(f_r_check("Wow"))

print(f_r_check("Madam, I'm Adam."))

print(f_r_check("Madam, I am Adam."))

