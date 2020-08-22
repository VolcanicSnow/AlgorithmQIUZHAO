"""
    Author:VolcanicSnow
    Email:liupf2792@gmail.com
    Function：快速排序
    Version：1.0
    Date：2020/8/21 17:16
"""


def partition(array, left, right):  # 归位函数，使得最终列表中，标杆左边的数都比其小，右边的数都比其大
    pivot = array[left]             # 标杆
    while left < right:
        while left < right and array[right] > pivot:    # 从右边找比标杆小的值，然后放到左边
            right -= 1              # 向左走一步，继续寻找
        array[left] = array[right]  # 找到了比标杆小的值，并将其放置于左边
        while left < right and array[left] < pivot:     # 从左边找比标杆大的值，然后放置到右边
            left += 1               # 向右走一步，继续寻找
        array[right] = array[left]  # 找到了比标杆大的值，并将其放置于右边
    array[left] = pivot             # 将标杆归位
    return left                     # 返回标杆的索引


def quick_sort(array, left, right):
    if left < right:
        pivot_index = partition(array, left, right)     # 获取归位后的标杆索引
        quick_sort(array, left, pivot_index - 1)        # 对标杆左侧进行快排
        quick_sort(array, pivot_index + 1, right)       # 对标杆右侧进行快排
    return array


nums = [5, 7, 4, 6, 3, 1, 2, 9, 8]
# partition(nums, 0, len(nums) - 1)
# print(nums)

nums2 = quick_sort(nums, 0, len(nums) - 1)
print(nums2)
