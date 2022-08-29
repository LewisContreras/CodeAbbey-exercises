import math

def main():
    num_cases = int(input())
    results = ""

    while num_cases != 0:
        num_cases -= 1
        value = input()
        res = other(value)
        results = f"{results} {res}"
    
    print(results.lstrip())


def other(values):
    [starting, target, interest] = [int(i) for i in values.split(" ")]
    count = 0
    while starting <= target:
        temp = starting * (1 + (interest) / 100)
        starting = round(temp, 2)
        count += 1
    return count

main()