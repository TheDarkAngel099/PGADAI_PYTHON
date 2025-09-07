def flip_vowel_case(s):
    vowels = "aeiouAEIOU"
    result = ""

    for char in s:
        if char in vowels:
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char
    return result

string = input("Enter a string: ")
print("Converted string:", flip_vowel_case(string))
