"""
    Author:VolcanicSnow
    Email:liupf2792@gmail.com
    Function：选择排序
    Version：1.0
    Date：2020/8/22 14:37
"""


def selection_sort(array):  # 选择排序； 时间复杂度：O(n^2), 空间复杂度：O(1)
    """
    首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
    """
    n = len(array)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


nums = [5, 7, 4, 6, 3, 1, 2, 9, 8]
selection_sort(nums)
print(nums)
