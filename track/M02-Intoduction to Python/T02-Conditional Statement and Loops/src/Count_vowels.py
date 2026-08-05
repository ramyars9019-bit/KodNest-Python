text = input()
vowel_count = 0

# Iterate directly over the string and count the vowels

for i in text:
    if i in "aeiou":
        vowel_count += 1

print(f"Vowel Count: {vowel_count}")