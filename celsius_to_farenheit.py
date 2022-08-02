values = input()
listValues = values.split(" ")
listValues.pop(0)

result = ""
for value in listValues:
    int_value = int(value)
    to_far = round((int_value - 32) * (5 / 9))
    result += " " + str(to_far)
print(result.strip())