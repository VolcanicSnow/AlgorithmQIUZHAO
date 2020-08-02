学习笔记学习总结

使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方。

- 首先理解半有序数组不是无序数组，在某种程度上还是有序的，只是经过了某种旋转。
- 观察发现：将将半有序数组从中间一分为二，这两部分至少一部分是有序的。这其实就是规律。

问题来了？如何确定中分后的两部分那一部分是有序的？以升序数组为例。

```python
[4, 5, 6, 7, 0, 1, 2]
 ^        ^        ^
 i       mid       j
```

```python
mid = (i + j) // 2
```

因为原数组是递增数组：故将**中值** 与右边界进行比较，

- 中值  > 右边界。分割后的两个子数组，[mid: j]不满足升序条件，[i: mid] 满足升序条件，故可以排除[i: mid],继续在[mid : j]中查找。令i = mid.

- 中值 < 右边界 。分割后的两个子数组，[i, mid] 不满足升序条件, [mid: j]满足升序条件。故可以排除[mid: j],继续在[i : mid ]中查找。令j  = mid.

- 否则，整个数组是有序的

  当i , j 相邻的时候，就找的了旋转点。

```python
def search(nums):
    i, j = 0, len(nums) - 1

    while j - i != 1:
        mid = (i + j) // 2
        if nums[mid] < nums[j]:
            j = mid
        else:
            i = mid
    return j       
```

测试：

```python
num1 = [4, 5, 6, 7, 0, 1, 2]
num2 = [5, 6, 7, 0, 1, 2, 4]
num3 = [6, 7, 0, 1, 2, 4, 5]
num4 = [7, 0, 1, 2, 4, 5, 6]
num5 = [0, 1, 2, 4, 5, 6, 7]
num6 = [1, 2, 4, 5, 6, 7, 0]
num7 = [2, 4, 5, 6, 7, 0, 1]

print(search(num1))
print(search(num2))
print(search(num3))
print(search(num4))
print(search(num5))
print(search(num6))
print(search(num7))
```

执行结果

```
D:\Anaconda\setup\python.exe C:/Users/火山飘雪/Desktop/leetcode/python文件/Week_03/search.py
4
3
2
1
1
6
5
```

