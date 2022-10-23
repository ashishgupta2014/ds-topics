from collections import OrderedDict


def isIsomorphic(s: str, t: str):
    if len(s) == len(t):
        f1 = frequency_order(s)
        f2 = frequency_order(t)
        if len(f1) == len(f2):
            return compare(f1, f2)
    return False


def compare(f1, f2):
    for (_, v1), (_, v2) in zip(f1.items(), f2.items()):
        if v1[0] != v2[0] or v1[1] != v2[1]:
            return False
    return True


def frequency_order(s):
    f = OrderedDict()
    for i, ele in enumerate(s):
        if ele in f:
            f[ele][0] += 1
            f[ele][1].append(i)
        else:
            f[ele] = [1, [i]]
    return f


# s = "egg"
# t = "add"
# print(isIsomorphic(s, t))
#
# s = "foo"
# t = "bar"
# print(isIsomorphic(s, t))
#
# s = "paper"
# t = "title"
# print(isIsomorphic(s, t))
#
s = "bbbaaaba"
t = "aaabbbba"
print(isIsomorphic(s, t))

# s = "papap"
# t = "titii"
# print(isIsomorphic(s, t))
