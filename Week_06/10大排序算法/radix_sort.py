"""
    Author:VolcanicSnow
    Email:liupf2792@gmail.com
    Function：基数排序
    Version：1.0
    Date：2020/8/22 16:11
"""


def RadixSort(array):
    max_value = max(array)
    num_digits = len(str(max_value))
    for i in range(num_digits):
        buckets = [[] for k in range(10)]
        for j in array:
            buckets[int(j / (10 ** i)) % 10].append(j)
        output = [m for bucket in buckets for m in bucket]
    return output