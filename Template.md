# Table of Contents
- [Table of Contents](#table-of-contents)
- [Binary search](#binary-search)
- [Two pointers](#two-pointers)
- [Reference](#reference)


# Binary search
1. 使用条件
- 排序数组 (30-40%是二分)
- 当面试官要求你找一个比 O(n) 更小的时间复杂度算法的时候(99%)
- 找到数组中的一个分割位置，使得左半部分满足某个条件，右半部分不满足(100%)
- 找到一个最大/最小的值使得某个条件被满足(90%)

2. 复杂度
- 时间复杂度：`O(logn)`
- 空间复杂度：`O(1)`

3. 领扣例题
- LintCode 14. 二分查找(在排序的数据集上进行二分)
- LintCode 460. 在排序数组中找最接近的 K 个数 (在未排序的数据集上进行二分)
- LintCode 437. 书籍复印(在答案集上进行二分 )

4. 代码模版
```python
def binary_search(self, nums, target):
    # corner case 处理
    # 这里等价于 nums is None or len(nums) == 0
    if not nums:
        return -1
    
    start, end = 0, len(nums) - 1

    # 用 start + 1 < end 而不是 start < end 的目的是为了避免死循环
    # 在 first position of target 的情况下不会出现死循环
    # 但是在 last position of target 的情况下会出现死循环
    # 样例：nums=[1，1] target = 1
    # 为了统一模板，我们就都采用 start + 1 < end，就保证不会出现死循环

    while start + 1 < end:
        # python 没有 overflow 的问题，直接 // 2 就可以了
        # java 和 C++ 最好写成 mid = start + (end - start) / 2
        # 防止在 start = 2^31 - 1, end = 2^31 - 1 的情况下出现加法 overflow
        mid = (start + end) // 2
        # > , =, < 的逻辑先分开写，然后在看看 = 的情况是否能合并到其他分支里

        if nums[mid] < target:
            start = mid
        elif nums[mid] == target:
            end = mid
        else:
            end = mid

        # 因为上面的循环退出条件是 start + 1 < end
        # 因此这里循环结束的时候，start 和 end 的关系是相邻关系（1 和 2，3 和 4 这种）
        # 因此需要再单独判断 start 和 end 这两个数谁是我们要的答案
        # 如果是找 first position of target 就先看 start，否则就先看 end
        if nums[start] == target:
            return start
        
        if nums[end] == target:
            return end
        return -1
```

# Two pointers
1. 使用条件
- 滑动窗口 (90%)
- 时间复杂度要求 `O(n)` (80%是双指针)
- 要求原地操作，只可以使用交换，不能使用额外空间 (80%)
- 有子数组 subarray /子字符串 substring 的关键词 (50%)
- 有回文 Palindrome 关键词(50%)

2. 复杂度
- 时间复杂度：`O(n)` 。时间复杂度与最内层循环主体的执行次数有关。与有多少重循环无关
- 空间复杂度：`O(1)` 。只需要分配两个指针的额外内存

3. 领扣例题
- LintCode 1879. 两数之和 VII(同向双指针)
- LintCode 1712. 和相同的二元子数组(相向双指针)
- LintCode 627. 最长回文串 (背向双指针)
- LintCode 64: 合并有序数组

4. 代码模版

4.1  相向双指针(patition in quicksort)
```python
def patition(self, A, start, end):
    if start >= end:
        return

    left, right = start, end
    
    # key point 1: pivot is the value, not the index
    pivot = A[(start + end) // 2]

    # key point 2: every time you compare left & right, it should be
    # left <= right
    while left <= right:
        while left <= right and A[left] < pivot:
            left += 1
        
        while left <= right and A[right] > pivot:
            right -= 1
        
        if left <= right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1
        

```


# Reference
- [ninechapter-algorithm/leetcode-linghu-templete](https://github.com/ninechapter-algorithm/leetcode-linghu-templete)