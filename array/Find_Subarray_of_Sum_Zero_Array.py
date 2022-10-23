def findSubArrays(array, n):
    sum_dict = {}
    cur_sum = 0
    for i, num in enumerate(array):
        cur_sum += num
        if cur_sum in sum_dict:
            sum_dict[cur_sum].append(i)
        else:
            sum_dict[cur_sum] = [i]
    return sum_dict


def printResult(result):
    print(result)
    for k, v in result.items():
        if len(v) > 1:
            if len(v) > 2:
                print(f'Subarray found from Index {v[0] + 1} to {v[len(v) -1]}')
            for i in range(len(v)-1):
                print(f'Subarray found from Index {v[i]+1} to {v[i+1]}')


if __name__ == '__main__':
    array = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
    n = len(array)
    result = findSubArrays(array, n)
    printResult(result)