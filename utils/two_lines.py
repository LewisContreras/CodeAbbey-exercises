def main():
    num_cases = int(input())
    values = [int(i) for i in input().split(" ")]
    results = ""
    while num_cases != 0:
        num_cases -= 1
        res = other(values[num_cases])
        results = f"{res} {results}"

    print(results.rstrip())


def other(value):
    result = value
    return result

main()