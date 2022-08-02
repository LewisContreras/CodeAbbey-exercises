def checksum():
    num_cases = int(input())
    values = input().split(" ")
    results = 0
    for i in range(num_cases):
        num_cases -= 1
        value = int(values[i])
        results = ((results + value) * 113) % 10000007

    print(results)


checksum()