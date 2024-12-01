
input_lists = open("inputs.txt","r")

lines = input_lists.read().split('\n')


left_list = []
right_list = []

for i in lines:
    print(i.split("   "))
    left_list.append(i.split("   ")[0])
    right_list.append(i.split("   ")[1])

left_list.sort()
right_list.sort()

pair_distance = 0

for i in range(len(left_list)):
    pair_distance += abs(int(left_list[i]) - int(right_list[i]))


print(pair_distance)

right_list_dict = {}
for i in right_list:
    if i not in right_list_dict:
        right_list_dict[i] = 1
    else:
        right_list_dict[i] += 1



left_sum = 0
for i in left_list:
    if i in right_list_dict:
        left_sum += int(i) * right_list_dict[i]
print(left_sum)
