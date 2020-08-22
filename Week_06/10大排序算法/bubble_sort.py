"""
    Author:VolcanicSnow
    Email:liupf2792@gmail.com
    Function：冒泡排序
    Version：1.0
    Date：2020/8/22 14:35
"""


def bubble_sort(array):  # 冒泡排序； 时间复杂度：O(n^2), 空间复杂度：O(1)
    """
    它重复地走访过要排序的数列，一次比较两个元素，如果它们的顺序错误就把它们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
    """
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


nums = [5, 7, 4, 6, 3, 1, 2, 9, 8]
bubble_sort(nums)
print(nums)
