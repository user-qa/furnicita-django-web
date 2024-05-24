numbers = [f'n{i}' for i in range(10)]
print(numbers)

for number in numbers:
    if numbers.index(number)%2 != 1:
        print(number)
        print(numbers[numbers.index(number) + 1])

