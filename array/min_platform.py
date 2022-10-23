def minimumNumberPlatform(arrival, departure, n):
    # [100, 140, 150, 200, 215, 400]
    # [110, 220, 230, 300, 315, 600]
    departure.sort()
    platform = 1
    max_platform = 1
    j = 0
    i = 1
    while i < n and j < n:
        if arrival[i] <= departure[j]:
            platform += 1
            i += 1
            if platform > max_platform:
                max_platform = platform
        else:
            platform -= 1
            j += 1
    return max_platform


#arrival = [100, 140, 150, 200, 215, 400]
#departure = [110, 300, 220, 230, 315, 600]
arrival = [900,  940, 950,  1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arrival)

print("Minimum Number Platforms = ", minimumNumberPlatform(arrival, departure, n))

