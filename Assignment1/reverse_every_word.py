def reverse_words(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)



s = input("Enter a sentence: ")

print("Reversed words:", reverse_words(s))
