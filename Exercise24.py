char = str(input("Please provide the character:"))

def check (char):
    vowels = "aeiou"
    return char in vowels

print(check(char))
