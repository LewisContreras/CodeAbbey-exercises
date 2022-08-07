def main():
    num_cases = int(input())
    results = ""

    while num_cases != 0:
        num_cases -= 1
        value = input()
        res = race(value)
        results = f"{results} {res}"
    
    print(results.lstrip())


def race(values):
    [distance, bic_1, bic_2] = [int(i) for i in values.split(" ")]

    result = distance * (bic_1 / (bic_1 + bic_2))
    return result

main()