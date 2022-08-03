from math import sqrt


def main():
    num_cases = int(input())
    results = ""

    while num_cases != 0:
        num_cases -= 1
        value = input()
        res = find_triangle(value)
        results += str(res) + " "
    
    print(results.rstrip())


def find_triangle(values):
    [value_a, value_b, longest] = [int(i) for i in values.split(" ")]
    hypo = int(sqrt((value_a**2 + value_b**2)))
    if (hypo == longest):
        result = "R"
    elif (hypo < longest):
        result = "O"
    else:
        result = "A"
    return result

main()