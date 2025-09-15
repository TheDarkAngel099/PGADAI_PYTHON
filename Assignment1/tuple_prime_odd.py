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


def count_primes_and_odds(numbers):
    prime_count = 0
    odd_count = 0

    for num in numbers:
        if num % 2 != 0:
            odd_count += 1
        if is_prime(num):
            prime_count += 1

    return prime_count, odd_count

data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19, 20)
primes, odds = count_primes_and_odds(data)

print("Total prime numbers:", primes)
print("Total odd numbers:", odds)
