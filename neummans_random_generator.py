def main():
    num_cases = int(input())
    values = input().split(" ")
    results = ""
    while num_cases != 0:
        num_cases -= 1
        res = neumanns(values[num_cases])
        results = str(res) + " " + results

    print(results.rstrip())


def neumanns(value):
    previous = []
    next_value = value
    cont = 0
    while not (next_value in previous):
        previous.append(next_value)
        square = (int(next_value))**2
        next_value = '{:0>8}'.format(str(square))[2:6]
        cont += 1

    return cont

main()