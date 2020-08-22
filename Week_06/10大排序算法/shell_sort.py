"""
    Author:VolcanicSnow
    Email:liupf2792@gmail.com
    Function：希尔排序
    Version：1.0
    Date：2020/8/22 14:39
"""


def shell_sort(array):
    length = len(array)
    gap = length // 2
    while gap >= 1:
        for i in range(gap, length):
            pointer, cur = i - gap, array[i]
            while pointer >= 0 and array[pointer] > cur:
                array[pointer + gap] = array[pointer]
                pointer -= gap
            array[pointer + gap] = cur
        gap = gap // 2
    return array


nums = [5, 7, 4, 6, 3, 1, 2, 9, 8]
shell_sort(nums)
print(nums)
