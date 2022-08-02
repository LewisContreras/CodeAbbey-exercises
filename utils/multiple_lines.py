def main():
    num_cases = int(input())
    results = ""

    while num_cases != 0:
        num_cases -= 1
        value = input()
        res = other(value)
        results += str(res) + " "
    
    print(results.rstrip())


def other(values):
    [value_a, value_b, value_c] = [int(i) for i in values.split(" ")]

    result = value_a + value_b + value_c
    return result

main()