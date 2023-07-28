numbers = range(1, 201)
result = []

for number in numbers:
    if number %7 == 0 and number %5 != 0:
        result.append(number)
    else:
        pass

print(result)

result = list(map(str, result))
print(','.join(result))