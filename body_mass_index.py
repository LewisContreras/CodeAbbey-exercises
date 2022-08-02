def main():
    num_cases = int(input())
    results = ""

    while num_cases != 0:
        num_cases -= 1
        value = input()
        res = bmi(value)
        results += str(res) + " "
    
    print(results.rstrip())


def bmi(values):
    [weight, height] = values.split(" ")
    body_index = int(weight) / (float(height)**2)
    if (body_index < 18.5):
        result = "under"
    elif (18.5 <= body_index < 25.0):
        result = "normal"
    elif (25.0 <= body_index < 30.0):
        result = "over"
    else:
        result = "obese"
    return result
main()
