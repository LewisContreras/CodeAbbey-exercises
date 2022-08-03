def main():
    num_cases = int(input())
    results = ""

    while num_cases != 0:
        num_cases -= 1
        value = input()
        res = fibonacci(int(value))
        results += str(res) + " "
    
    print(results.rstrip())


def fibonacci(value):
    if value == 0 or value == 1: return value
    index_fibo = 0
    pre = 0
    nextv = 1
    while value != pre:
        pre, nextv = nextv, pre + nextv
        index_fibo += 1
    return index_fibo

main()