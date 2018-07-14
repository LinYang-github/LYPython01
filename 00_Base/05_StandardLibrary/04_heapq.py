# heappush(heap, x) 将x入堆
# heappop(heap) 将堆中最小的元素弹出
# heapify(heap) 将heap属性强制应用到任意一个列表
# heapreplace(heap, x) 将堆中最小的元素弹出，同时将x入堆
# nlargest(n, iter) 返回iter中第n大的元素
# nsmallest(n, iter) 返回iter中第n小的元素


# 堆属性：位于i位置上的元素总比i/2位置处的元素大
#         i位置处的元素总比2i以及2i+1位置处的元素小
from heapq import *
from random import shuffle
data = range(10)
shuffle(data)
heap = []
for n in data:
    heappush(heap, n)
print heap
heappush(heap, 0.5)
print heap
heappop(heap)
print heap

heap1 = [5,8,0,3,6,7,9,1,4,2]
heapify(heap1)
print heap
