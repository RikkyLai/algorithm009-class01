# Week 8

## 位运算
位运算符号：

|  操作   | 符号  | 示例  |
|  ----  | ----  | ----  |
| 左移  | << | 0011<<1  左移一格 =》 0110 |
| 右移  | >> | 0011>>1  右移一格 =》 0011 |
| 按位与  | & | 0011 & 1011   =》 0011 |
| 按位或  | \| | 0011 \| 1011 =》 1011 |
| 按位取反  | ~ | ~0011    =》 1100 |
| 按位异或（相同为0不同为1）  | ^ | 0011 ^ 1011 =》 1000 |

异或操作：

> x^0 = x

> x^1s = ~x

> x^(~x) = 1s

> x^x = 0

> c=a^b  =>  a^c=b, b^c=a

指定位置的位运算：

1. 将x最右边的n位清零： x&（~0<<n）
2. 获取x的第n位值（0或者1）： (x>>n)&1
3. 获取x的第n位幂值： x&(1<<n)
4. 仅将第n位位置置1： x|(1<<n)
5. 仅将第n位位置置0： x&(~(1<<n))
6. 将x最高位至第n位清0： x&((1<<n)-1)

实战位运算要点：

+ 判断奇数偶数： x%2==1 ->  x&1 == 1
+ x>>1 -> x/2
+ x&(x-1) 去掉最低位的1

## 布隆过滤器的实现和应用
Bloom Filter： 一个很长的二进制向量和一系列的随机映射函数。布隆过滤器可以用于检索一个元素是否在一个集合中

优点：空间效率和查询时间都远远超过一般的算法
缺点：有一定的误识别率和删除困难

案例：
+ 比特币网络
+ 分布式系统
+ Redis缓存
+ 垃圾邮件、评论等的过滤

#### LRU Cache （Least Recently used）
Hash Table + Double Linked List


## 排序算法
1. 比较类排序：通过比较来决定元素间的相对次序，由于其时间复杂度不能突破O(nlgn),由此称为非线性时间比较类排序
2. 非比较类排序： 不通过比较来决定元素间的相对次序，可以突破基于比较排序的时间下界，以线性时间排序

比较类排序：交换排序、插入排序、选择排序、归并排序

非比较类排序：计数排序、插排序、基数排序

```
# 冒泡排序
def bubble_sort(nums):

    for i in range(len(nums) - 1):  
        ex_flag = False  # 改进后的冒泡，设置一个交换标志位
        for j in range(len(nums) - i - 1):  
            
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                ex_flag = True
        if not ex_flag:
            return nums  # 如果标志位没有变化，提前结束交换

    return nums


# 快速排序
def partition(arr,low,high): 
    i = ( low-1 )         # 最小元素索引
    pivot = arr[high]     
  
    for j in range(low , high):  
        # 当前元素小于或等于 pivot 
        if   arr[j] <= pivot: 
          
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
 
# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引

def quickSort(arr,low,high): 
    if low < high: 
  
        pi = partition(arr,low,high) 
  
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)


# 归并排序
def merge(a, b):
    c = []
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])

    if len(a) == 0:
        c += b
    else:
        c += a
    return c

# 排序
def merge_sort(li):
    if len(li) <= 1:
        return li
    # 整除2
    m = len(li) // 2
    a = merge_sort(li[:m])
    b = merge_sort(li[m:])
    return merge(a, b)
```

