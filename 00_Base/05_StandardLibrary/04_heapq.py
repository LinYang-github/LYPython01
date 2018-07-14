# heappush(heap, x) ��x���
# heappop(heap) ��������С��Ԫ�ص���
# heapify(heap) ��heap����ǿ��Ӧ�õ�����һ���б�
# heapreplace(heap, x) ��������С��Ԫ�ص�����ͬʱ��x���
# nlargest(n, iter) ����iter�е�n���Ԫ��
# nsmallest(n, iter) ����iter�е�nС��Ԫ��


# �����ԣ�λ��iλ���ϵ�Ԫ���ܱ�i/2λ�ô���Ԫ�ش�
#         iλ�ô���Ԫ���ܱ�2i�Լ�2i+1λ�ô���Ԫ��С
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
