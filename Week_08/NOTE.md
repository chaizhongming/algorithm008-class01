本周主要学习了位运算、布隆过滤器、LRUCache和排序算法等几种算法。

课后习题练习了3道位运算的题，练习了把最后一位取出来和最后一位1敲掉等常用操作。LRUCache这道题感觉比较妙，把双向链表和字典结合起来，组合成一个复合的数据结构，这道题看得比较久才弄明白，收获还是挺大的。

另外自己理解并熟练默写了手写快牌、归并排序，比较了他们的相似点和区别，相似点都是都采用分治的思想，主要不同点是快排是先分再排，归并排序是先排再合，Python的代码模板如下。



**快速排序代码模板#Python**


def quick_sort(begin, end, nums):

    if begin >= end:
        return
    pivot_index = partition(begin, end, nums)
    quick_sort(begin, pivot_index-1, nums)
    quick_sort(pivot_index+1, end, nums)

def partition(begin, end, nums):

    pivot = nums[begin]
    mark = begin
    for i in range(begin+1, end+1):
        if nums[i] < pivot:
            mark +=1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[begin], nums[mark] = nums[mark], nums[begin]
    return mark

**归并排序代码示例#Python**

def mergesort(nums, left, right):

    if right <= left:
        return
    mid = (left+right) >> 1
    mergesort(nums, left, mid)
    mergesort(nums, mid+1, right)
    merge(nums, left, mid, right)

def merge(nums, left, mid, right):

    temp = []
    i = left
    j = mid+1
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i +=1
        else:
            temp.append(nums[j])
            j +=1
    while i<=mid:
        temp.append(nums[i])
        i +=1
    while j<=right:
        temp.append(nums[j])
        j +=1
    for k in range(len(temp)):
        nums[left+k] = temp[k]