
# Binary search

## 使用条件
- 排序数组 (30-40%是二分)
- 当面试官要求你找一个比 O(n) 更小的时间复杂度算法的时候(99%)
- 找到数组中的一个分割位置，使得左半部分满足某个条件，右半部分不满足(100%)
- 找到一个最大/最小的值使得某个条件被满足(90%)

## 复杂度
- 时间复杂度：O(logn)
- 空间复杂度：O(1)

## 领扣例题
- LintCode 14. 二分查找(在排序的数据集上进行二分)
- LintCode 460. 在排序数组中找最接近的 K 个数 (在未排序的数据集上进行二分)
- LintCode 437. 书籍复印(在答案集上进行二分 )

## Code

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

# Reference
- [ninechapter-algorithm/leetcode-linghu-templete](https://github.com/ninechapter-algorithm/leetcode-linghu-templete)