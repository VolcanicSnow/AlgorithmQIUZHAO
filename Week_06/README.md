学习笔记

- ##### 选择排序

  ```python
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
  ```

- ##### 插入排序

  ```python
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
  ```

- ##### 冒泡排序

  ```python
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
  ```

- ##### 希尔排序

  ```python
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
  ```

- ##### 快速排序

  ```python
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
  ```

- ##### 堆排序

  ```python
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
  
  ```

- ##### 归并排序

  ```python
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
  ```

- ##### 计数排序

  ```python
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
  ```

- ##### 桶排序

  ```python
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
  ```

- ##### 基数排序

  ```python
  def RadixSort(array):
      max_value = max(array)
      num_digits = len(str(max_value))
      for i in range(num_digits):
          buckets = [[] for k in range(10)]
          for j in array:
              buckets[int(j / (10 ** i)) % 10].append(j)
          output = [m for bucket in buckets for m in bucket]
      return output
  ```

  