def checksum(values):
    results = 0
    for i in values:
        results = ((results + i) * 113) % 10000007

    return results

def main():
    values_str = input().split(" ")
    values_str.pop()
    values = [int(i) for i in values_str]
    print(values)
    total_swaps = 0

    for i in range(len(values) - 1):
        if not (values[i] <= values[i + 1]):
            values[i], values[i + 1] = values[i + 1], values[i]
            total_swaps += 1


    check = checksum(values)
    print(f"{total_swaps} {check}")


main()