def main():
    num_cases = int(input())
    values = input().split(" ")
    results = ""
    while num_cases != 0:
        num_cases -= 1
        res = weighted(values[num_cases])
        results = str(res) + " " + results

    print(results.rstrip())


def weighted(value):
    result = 0
    cont = 0
    for x in value: 
        result += int(x) * (cont + 1)
        cont += 1
    return result


main()