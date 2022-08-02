def main():
    num_cases = int(input())
    results = ""

    while num_cases != 0:
        num_cases -= 1
        value = input()
        res = other(value)
        results += str(res) + " "
    
    print(results.rstrip())


def other(values):
    [x1, y1, x2,  y2] = [int(i) for i in values.split(" ")]
    slope = (y2 - y1) / (x2 - x1)
    intercept = y1 - (slope * x1)
    result = f"({int(slope)} {int(intercept)})"
    return result

main()