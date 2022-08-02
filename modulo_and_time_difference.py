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
    [day1, h1, min1, sec1, day2, h2, min2, sec2] = [int(i) for i in values.split(" ")]
    sec_per_day =  24 * 60 * 60
    sec_per_hour = 60 * 60
    sec_per_minute = 60
    sec_time1 = (day1 * sec_per_day) + (h1 * sec_per_hour) + (min1 * sec_per_minute) + sec1
    sec_time2 = (day2 * sec_per_day) + (h2 * sec_per_hour) + (min2 * sec_per_minute) + sec2
    sec_time_diff = sec_time2 - sec_time1
    day_diff = sec_time_diff // sec_per_day
    day_remainer = sec_time_diff - (day_diff * sec_per_day)
    hour_diff = (day_remainer) // sec_per_hour
    hour_remainer = day_remainer - (hour_diff * sec_per_hour)
    min_diff = (hour_remainer) // sec_per_minute
    secs = hour_remainer - (min_diff * sec_per_minute)
    return f"({day_diff} {hour_diff} {min_diff} {secs})"

main()