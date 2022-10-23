'''
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

Input: nums = [3,4,2]
Output: 6

'''

a = [2, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5]
d = {
    2: 4,
    4: 3,
    5: 2,
    3: 2
}

d = {2: 2, 4: 3, 5: 2}

keys = {2, 3, 4, 5}
a = 2-1
b = 2+1

def main(arr):
    scores = []
    d = Counter(arr)
    for k in range(len(keys)):
        temp = []
        for i in range(k, len(keys)):
            c = d.copy()
            score = 0
            flag = False
            a = keys[k]+1
            b = keys[k]
            if a in c:
                c[k+1] = abs(d[k] - c[a+1])
                flag = True
            if keys[k]-1 in c:
                c[k-1] = abs(d[k]-c[k-1])
                flag = True
            if flag:
                del c[k]
                score += k
            for k, v in c.items:
                if v > 0:
                    score += k*v
            temp.append(score)
        scores.append(max(temp))
    return max(scores)


