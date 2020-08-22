"""
    Author:VolcanicSnow
    Email:liupf2792@gmail.com
    Function：
    Version：1.0
    Date：2020/8/22 10:43
"""


def heapify(parent_index, length, nums):    # 堆的向下调整
    temp = nums[parent_index]               # 把父亲节点拿出来
    child_index = 2 * parent_index + 1      # 左边的孩子索引
    while child_index < length:
        if child_index + 1 < length and nums[child_index + 1] > nums[child_index]:  # 如果右边的孩子值大于左边的孩子值
            child_index = child_index + 1   # 选择右边孩子
        if temp > nums[child_index]:        # 如果父亲节点比孩子节点值大，说明堆正常，不同调整
            break
        # 孩子节点比父亲节点大，将孩子上移
        nums[parent_index] = nums[child_index]
        parent_index = child_index          # 继续向下调整
        child_index = 2 * parent_index + 1
        nums[parent_index] = temp


def heap_sort(nums):
    # 建堆，从最后一个子堆开始向上调整每一个子堆
    # last_index =  len(nums) - 1:nums中最后一个元素的索引，堆中最后一个元素的父亲节点的下标为：(last_index - 1) // 2
    for i in range((len(nums) - 2) // 2, -1, -1):
        heapify(i, len(nums), nums)
    # 建堆完毕

    for j in range(len(nums) - 1, 0, -1):
        nums[j], nums[0] = nums[0], nums[j]     # 将堆顶的元素依次放入 nums 的末尾
        heapify(0, j, nums)                     # 将num[0: j + 1] 再进行调整


nums = [5, 7, 4, 6, 3, 1, 2, 9, 8]
heap_sort(nums)
print(nums)
