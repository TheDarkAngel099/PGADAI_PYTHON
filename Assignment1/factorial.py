def factorial(num):
    if num < 0:
        return "can not define factorial of a negative number"
    elif num == 0 or num == 1:
        return 1
    else:
        res = 1
        for i in range(2, num + 1):
            res *= i
        return res


try:
    num = int(input("Enter a number: "))
    print("Factorial of", num, "is", factorial(num))
except ValueError:
    print("Please enter a valid integer.")

