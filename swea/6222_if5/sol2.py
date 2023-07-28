import sys
sys.stdin = open('input.txt')

char = input()

if char.isupper():
    result = char.lower()
elif char.islower():
    result = char.upper()
else:
    result = char

print(char, result)
print(ord(char), ord(result))
