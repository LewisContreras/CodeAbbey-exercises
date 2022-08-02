def main():
    [num_cases, top_number] = [int(i) for i in input().split(" ")]
    values = input().split(" ")
    my_arrays = [[] for x in range(top_number)]
    while num_cases != 0:
        num_cases -= 1
        value = int(values[num_cases])
        my_arrays[value - 1].append("*")
        
    results = " ".join([str(len(x)) for x in my_arrays])
    print(results)

main()