"""
    Author:VolcanicSnow
    Email:liupf2792@gmail.com
    Function：
    Version：1.0
    Date：2020/8/22 14:38
"""


def insertion_sort(array):  # 插入排序； 时间复杂度：O(n^2), 空间复杂度：O(1)
    """
    通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
    """
    n = len(array)
    for i in range(1, n):
        pointer, cur = i - 1, array[i]
        while pointer >= 0 and array[pointer] > cur:
            array[pointer + 1] = array[pointer]
            pointer -= 1
        array[pointer + 1] = cur
    return array


nums = [5, 7, 4, 6, 3, 1, 2, 9, 8]
insertion_sort(nums)
print(nums)
