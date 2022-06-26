nums_1 = [num for num in range(30) if num % 3 == 0]
nums_2 = [num for num in range(30) if num % 5 == 0]
nums_1.extend(nums_2)
print(nums_1)

nums = [num for num in range(30) if num % 3 == 0 and num % 5 == 0]
print(nums)
