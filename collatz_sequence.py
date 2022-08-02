def main():
    num_cases = int(input())
    values = input().split(" ")
    results = ""
    while num_cases != 0:
        num_cases -= 1
        res = collatz(int(values[num_cases]))
        results = str(res) + " " + results

    print(results.rstrip())


def collatz(value):
    cont = 0
    while value != 1:
        if (value % 2 == 0):
            value = value / 2
        else:
            value = (value * 3) + 1
        cont += 1
    return cont

main()