def has_two_or_more_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count >= 2

def filter_strings_with_vowels(strings):
    return [s for s in strings if has_two_or_more_vowels(s)]

words = ["sky", "apple", "orange", "fly", "grape", "dry", "education"]

print("Original list:", words)
print("Strings with 2 or more vowels:", filter_strings_with_vowels(words))
