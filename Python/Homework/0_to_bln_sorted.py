import random
import sys

with open('0_to_bln.txt', 'w') as f:
    i = 0
    a = []
    while i < 1000000000:
        random_number = random.randint(0, 120)
        f.write(str(random_number) + " ")
        a.append(random_number)
        if sys.getsizeof(a) > 209715200:  # =200 mb
            a = []
            f.write("\n")
        i += 1
# generated 1 bln numbers

index_dict = {}
overall_dict = {}
for k in range(0, 121):
    overall_dict[k] = 0
file = open("0to1bln.txt", "r")
line_count = 0
for line in file:
    if line != "\n":
        line_count += 1
file.close()
# counted how many lines in my file
lines_to_print = list(range(0, line_count))
file = open('0to1bln.txt')
for index, line in enumerate(file):
    if index in lines_to_print:
        line_splitted = [int(x) for x in line.split()]

        for int_1 in range(0, 121):
            index_dict[int_1] = line_splitted.count(int_1)
        for key, value in index_dict.items():
            overall_dict[key] += value
print(sum(overall_dict.values()))  # to be sure that there are 1bln numbers
file.close()
# created a dictionary that shows how many numbers (from 0 to 120) there are
with open("sorted_0_to_bln.txt", "w") as fs:
    for num in range(0, 121):
        key_1 = 0
        while key_1 < overall_dict[num]:
            fs.write(str(num) + "\n")
            key_1 += 1
# created file with sorted 1bln numbers
