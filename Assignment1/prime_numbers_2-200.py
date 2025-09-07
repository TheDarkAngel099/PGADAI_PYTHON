#from prime_number import is_prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5)+ 1, 2):
        if n % i == 0:
            return False
    return True

def prime_list(start = 2, end = 200):
    return [num for num in range(start, end + 1) if is_prime(num)]

print("Prime numbers from 2 to 100:")
print(prime_list())
