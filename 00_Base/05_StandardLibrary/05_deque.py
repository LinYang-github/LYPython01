# double-ended queue
# ˫�˶�������Ҫ����Ԫ�����ӵ�˳�������Ԫ��ʱ�ǳ�����

from collections import deque
# ˫�˶���ͨ���ɵ������󣨱��缯�ϣ�����
q = deque(range(5))
q.append(5)
q.appendleft(6)
print q
q.pop()
print q
q.popleft()
print q
q.rotate(3)
print q
q.rotate(-1)
print q
