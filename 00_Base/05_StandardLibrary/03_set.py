set(range(10))
# set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

set([0, 1, 2, 3, 0, 1, 2, 3, 4, 5])
# set([0, 1, 2, 3, 4, 5])

set(['fee', 'fie', 'foe'])
# set(['foe', 'fee', 'fie'])
# ���ֵ�һ��������˳���������

a = set([1, 2, 3])
b = set([2, 3, 4])
print a.union(b)
print a|b

c = a & b
print c.issubset(a)
print c <= a
print c.issuperset(a)
print c >= a
print a.intersection(b)
print a & b
print a.difference(b)
print a - b
print a.symmetric_difference(b)
print a ^ b
print a.copy()
print a.copy() is a

# frozenset�����ɱ䣨��ɢ�У��ļ���
