number = input()

number_box = []


for i in number:

    number_box.append(int(i))


number_box.sort(reverse=True)


number_box_str = list(map(str,number_box))


result = "".join(number_box_str)

print(result)