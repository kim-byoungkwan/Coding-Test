standard = ['c=','c-','dz=','d-','lj','nj','s=','z=']

count_box = []

word = input()

for i in range(len(standard)):

    count_box.append(word.count(standard[i]))

    word = word.replace(standard[i],"0")

word = word.replace('0','')

number_rest = len(word)

num_count = sum(count_box)


print(number_rest+num_count)