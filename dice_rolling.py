import math

def main():
    num_cases = int(input())
    results = ""

    while num_cases != 0:
        num_cases -= 1
        value = input()
        res = rolling(value)
        results += str(res) + " "
    
    print(results.rstrip())


def rolling(value):
    sides = 6
    result = math.floor((sides * float(value)) + 1)
    return result

main()