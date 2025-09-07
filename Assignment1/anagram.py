def is_anagram(s1 , s2):
    return sorted(s1.lower()) == sorted(s2.lower())


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if is_anagram(s1, s2):
    print("The strings are anagrams.")
else:
    print("The strings are NOT anagrams.")
