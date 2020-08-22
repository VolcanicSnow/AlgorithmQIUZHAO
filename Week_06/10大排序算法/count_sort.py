"""
    Author:VolcanicSnow
    Email:liupf2792@gmail.com
    Function：计数排序
    Version：1.0
    Date：2020/8/22 14:55
"""


def count_sort(nums):       # 假设都是大于等于0的整数
    max_count = max(nums)
    count = [0 for _ in range(max_count + 1)]
    for num in nums:
        count[num] += 1
    nums.clear()
    for index, val in enumerate(count):
        for _ in range(val):
            nums.append(index)
    return nums


nums = [5, 7, 4, 6, 3, 1, 2, 9, 8]
count_sort(nums)
print(nums)
