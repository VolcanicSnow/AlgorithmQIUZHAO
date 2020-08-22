"""
    Author:VolcanicSnow
    Email:liupf2792@gmail.com
    Function：桶排序
    Version：1.0
    Date：2020/8/22 15:24
"""


def bucket_sort(arr, bucketSize):
    if len(arr) == 0: return arr
    minValue = min(arr)
    maxValue = max(arr)
    bucketsCount = (maxValue - minValue) // bucketSize + 1
    buckets = [[]] * bucketsCount
    for i in range(len(arr)):
        ind = (arr[i] - minValue) // bucketSize
        buckets[ind] = buckets[ind] + [arr[i]]
    arr = []
    for i in range(len(buckets)):
        buckets[i] = insertSort(buckets[i])
        for j in range(len(buckets[i])):
            arr.append(buckets[i][j])
    return arr


def insertSort(bucket):
    for i in range(1, len(bucket)):
        temp = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > temp:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = temp
    return bucket


nums = [8, 79, 23, 85, 62, 34, 30, 95, 81, 70]
nums = bucket_sort(nums, 3)
print(nums)
