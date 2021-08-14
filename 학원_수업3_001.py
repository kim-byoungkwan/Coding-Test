num = int(input())

box = []

while True:

    box.append(num % 10)

    num = num // 10

    if num == 0:

        break

    else:

        continue

print("각 자리수 합:",sum(box))

