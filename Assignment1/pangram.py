import string
def is_pangram(s):
    s = s.lower()
    alpha_set = set(string.ascii_lowercase)
    return alpha_set.issubset(set(s))


s = input("Enter a string: ")
#s = "abcdefghijklmnopqrstuvwxyz"
if is_pangram(s):
    print("The string is a pangram.")
else:
    print("The string is NOT a pangram.")

