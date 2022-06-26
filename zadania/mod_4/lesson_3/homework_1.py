first_list = [number for number in range(1, 31) if number % 3 == 0]
second_list = [number for number in range(1, 31) if number % 5 == 0]

all_lists = first_list + second_list
print(all_lists)


