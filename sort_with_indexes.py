from operator import indexOf


def main():
    num_cases = int(input())
    values = [int(i) for i in input().split(" ")]
    copy_values = [*values]
    temp_swaps = False
    while True:
        for i in range(num_cases - 1):
            if not (values[i] <= values[i + 1]):
                values[i], values[i + 1] = values[i + 1], values[i]
                temp_swaps = True

        if (temp_swaps == True):

            temp_swaps = False
        else:
            break

    print(" ".join([str(copy_values.index(i) + 1) for i in values]))


main()