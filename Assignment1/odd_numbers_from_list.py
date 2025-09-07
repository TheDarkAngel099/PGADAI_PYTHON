def print_odd_numbers(list):
    print("Odd numbers in the list:", [num for num in list if num % 2 != 0])

numbers = list(range(1, 101))  
print_odd_numbers(numbers)
