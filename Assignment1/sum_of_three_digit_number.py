
def sum_of_digits_of_three_digit_number(number):
    if 100 <= number <= 999:
        return (number //100) + ((number // 10) % 10) + number % 10
    else:
        return "Enter a valid three digit number"

num = 555
print("Sum of digits: ", sum_of_digits_of_three_digit_number(num))
