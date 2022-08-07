def main():
    num_cases = int(input())
    values = [float(i) for i in input().split(" ")]
    results = ""
    while num_cases != 0:
        num_cases -= 1
        res = smoothing(values, num_cases)
        results = str(res) + " " + results

    print(results.rstrip())


def smoothing(values, num_cases):
    if (num_cases == 0) or (num_cases == len(values) - 1):
        result = values[num_cases]
    else:
        result = (values[num_cases + 1] + values[num_cases] + values[num_cases - 1]) / 3
    return result

main()