def main():
    num_cases = int(input())
    results = ""

    while num_cases != 0:
        num_cases -= 1
        value = input()
        res = triangles(value)
        results += str(res) + " "
    
    print(results.rstrip())


def triangles(values):
    [value_a, value_b, value_c] = [int(i) for i in values.split(" ")]
    side_1 = value_a + value_b >= value_c
    side_2 = value_a + value_c >= value_b
    side_3 = value_c + value_b >= value_a
    result = 1 if side_1 & side_2 & side_3 else 0
    return result
main()