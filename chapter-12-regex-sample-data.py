import re
all_numbers = list()

with open('py4e-data.dr-chuck.net-regex_sum_42.txt', 'r') as fo:
    for line in fo:
        lst = re.findall('\d+', line)
        all_numbers.extend(lst)

#print(all_numbers)

total = None

for number in all_numbers:
    if total is None:
        total = 0 + int(number)
    elif total is not None:
        total = total + int(number)

print(total)