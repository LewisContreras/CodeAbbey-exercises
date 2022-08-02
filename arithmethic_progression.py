def main():
    num_cases = int(input())
    results = ""

    while num_cases != 0:
        num_cases -= 1
        value = input()
        res = progression(value)
        results += str(res) + " "
    
    print(results.rstrip())


def progression(values):
    [value_a, value_b, quantity] = values.split(" ")
    result = int(value_a) * int(quantity) + int(value_b) * sum(range(1, int(quantity)))
    return result
main()