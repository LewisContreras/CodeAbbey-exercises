def main():
    num_cases = int(input())
    values = input().split(" ")
    results = ""
    while num_cases != 0:
        num_cases -= 1
        res = other(values[num_cases])
        results = str(res) + " " + results

    print(results.rstrip())


def other(value):
    result = value
    return result

main()