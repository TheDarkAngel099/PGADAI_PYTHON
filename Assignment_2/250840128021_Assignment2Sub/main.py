def add_numbers(numbers):
    return sum(numbers)

def my_add(*n):
    res =0
    for num in n:
        res += num
    return res


def performAction(mylist, n):
    return [mylist[i:i+n] for i in range(0, len(mylist), n)]



def combine_names(namelist, surnamelist):
    return [f"{name} {surname}" for name, surname in zip(namelist, surnamelist)]




def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5 ) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def separate_numbers(iterable):
    odd = []
    even = []
    prime = []

    for num in iterable:
        if isinstance(num, int):
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
            if is_prime(num):
                prime.append(num)

    return odd, even, prime




nums = [10, 20, 30, 40]
#print("Sum:", add_numbers(nums))

print("Sum :" , my_add(2,25,4,3242,324,24,24,234,2,34,24,2,4,234,234,2,42))

print("-" * 40)

data = [1, 2, 3, 4, 5, 6, 7]
print("Split list:", performAction(data, 3))

print("-" * 40)


names = ["John", "Seth", "Jane", "Ben", "Priyanka"]
surnames = ["Doe", "Rollins", "Smith", "Dover", "Chopra"]

print(names)
print(surnames)
print("-" * 40)
print("Full names:", combine_names(names, surnames))

print("-" * 40)

data = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
odd_list, even_list, prime_list = separate_numbers(data)
print("Odd:", odd_list)
print("Even:", even_list)
print("Prime:", prime_list)
