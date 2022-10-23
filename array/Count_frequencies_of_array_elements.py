# Function to find counts of all elements present in arr[0..n-1]. The array  elements must be range from 1 to n
def printfrequency(arr, n):
    arr = [i - 1 for i in arr]
    freq = arr.copy()
    for i in range(n - 1):
        freq[arr[i]] += n
    for i in range(n-1):
        freq[i] = freq[i]//n
    return freq


arr = [2, 3, 3, 2, 5]
n = len(arr)
print(printfrequency(arr, n))
