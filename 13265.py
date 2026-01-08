Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=[1,2,3,4]
a.count()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a.count()
TypeError: list.count() takes exactly one argument (0 given)
a.count(1)
1
a.count(4)
1
a.append(5)
print(a)
[1, 2, 3, 4, 5]
a.index(3)
2
a.pop(5)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.pop(5)
IndexError: pop index out of range
a.pop(4)
5
print(a)
[1, 2, 3, 4]
a.reverse()
print(a)
[4, 3, 2, 1]
a.sort()
print(a)
[1, 2, 3, 4]
a.remove(2)
print(a)
[1, 3, 4]
a.insert(1,2)
print(a)
[1, 2, 3, 4]
b=['cat','dog','cow']
a.extend(b)
print(a)
[1, 2, 3, 4, 'cat', 'dog', 'cow']
x=a.copy()
print(x)
[1, 2, 3, 4, 'cat', 'dog', 'cow']
a.clear()
print(a)
[]
c=('A','B','C')
c.count('A')
1
c.index('B')
1
myset={'Apple','Banana','Grape'}
mysetb={'Guava','Orange'}
mysetb.add{'Apple'}
SyntaxError: invalid syntax
mysetb.add('Apple')
c=myset.differnce(mysetb)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    c=myset.differnce(mysetb)
AttributeError: 'set' object has no attribute 'differnce'. Did you mean: 'difference'?
c=myset.difference(mysetb)
print(c)
{'Banana', 'Grape'}
myset.difference_update(mysetb)
print(myset)
{'Banana', 'Grape'}
mysetb.difference_update(myset)
print(mysetb)
{'Orange', 'Guava', 'Apple'}
print(myset)
{'Banana', 'Grape'}
>>> myset.add('Pineapple')
>>> mysetb.add('Pineapple')
>>> print(mysetb)
{'Orange', 'Guava', 'Pineapple', 'Apple'}
>>> mysetb.difference_update(myset)
>>> print(mysetb)
{'Orange', 'Guava', 'Apple'}
>>> x=[1,2,3,4,5]
>>> x.print(2)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    x.print(2)
AttributeError: 'list' object has no attribute 'print'
>>> print(x[2])
3
>>> x.insert(2,7)
>>> print(x)
[1, 2, 7, 3, 4, 5]
>>> x*5
[1, 2, 7, 3, 4, 5, 1, 2, 7, 3, 4, 5, 1, 2, 7, 3, 4, 5, 1, 2, 7, 3, 4, 5, 1, 2, 7, 3, 4, 5]
>>> for a in x
SyntaxError: expected ':'
>>> for a in x print(a)
SyntaxError: invalid syntax
>>> for a in x : print(a)
... print(a)
SyntaxError: invalid syntax
>>> for a in x:
...     print(a)
... 
...     
1
2
7
3
4
5
>>> x.remove(4)
>>> print(x)
[1, 2, 7, 3, 5]
