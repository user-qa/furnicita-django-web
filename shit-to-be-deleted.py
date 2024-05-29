numbers = [f'n{i}' for i in range(10)]
print(numbers)
nums = []
for number in numbers[:-1]:
    if numbers.index(number) % 2 == 0:
        nums.append([number, numbers[numbers.index(number) + 1]])
print(nums)


