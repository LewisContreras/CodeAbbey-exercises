def main():
    num_cases = int(input())
    values = [int(i) for i in input().split(" ")]
    total_swaps = 0
    num_pass = 0
    temp_swaps = False
    while True:
        for i in range(num_cases - 1):
            if not (values[i] <= values[i + 1]):
                values[i], values[i + 1] = values[i + 1], values[i]
                total_swaps += 1
                temp_swaps = True

        num_pass += 1
        if (temp_swaps == True):

            temp_swaps = False
        else:
            break

    print(f"{num_pass} {total_swaps}")


main()