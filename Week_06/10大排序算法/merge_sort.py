"""
    Author:VolcanicSnow
    Email:liupf2792@gmail.com
    Function：
    Version：1.0
    Date：2020/8/22 9:31
"""


def merge(nums, left, mid, right):
    temp = []
    i = left        # 左边部分的第一个元素索引
    j = mid + 1     # 右边部分的第一个元素索引
    # 开始对两边进行比较合并
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1
    # 当某一边元素合并完了之后，将另一边元素全部加到 temp 中
    while i <= mid:
        temp.append(nums[i])
        i += 1
    while j <= right:
        temp.append(nums[j])
        j += 1
    nums[left:right + 1] = temp     # 将合并后的结果替换掉原来


def merge_sort(nums, left, right):
    if left == right:   # ，左右指针相遇，列表中只有一个元素
        return
    mid = (left + right) >> 1
    merge_sort(nums, left, mid)     # 左分
    merge_sort(nums, mid + 1, right)    # 右分
    merge(nums, left, mid, right)   # 并


nums = [5, 7, 4, 6, 3, 1, 2, 9, 8]
# print(nums)
# merge(nums, 0, len(nums) // 2, len(nums))
# print(nums)
merge_sort(nums, 0, len(nums) - 1)
print(nums)
