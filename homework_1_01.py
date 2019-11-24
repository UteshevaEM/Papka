#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def IntOrNot(n):
    return int(n) == float(n)

number=0
print("Введите ваше число")
number=int(input())
divided=0
divisors=[]
for i in range(1, number+1):
    if(i!=0):
        divided=number/i
    if(IntOrNot(divided)==True):
        divisors.append(i)
print(divisors)


# In[ ]:


def Backwards(stringg):
    n=len(stringg)
    stringback=''
    for i in range(1,n+1):
        stringback+=stringg[n-i]
    return stringback
    

print("Введите строку ")
stringg = str(input())
string2 = Backwards(stringg)
print(string2)
if(stringg==string2):
    print("Это палиндром")
if(stringg!=string2):
    print("Это не палиндром")


# In[ ]:


def IntOrNot(n):
    return int(n) == float(n)

flag=1
array=[]
while(flag==1):
    print("Хотите ли вы добавить элемент?")
    decision=int(input())
    if(decision==1):
        elem=int(input())
        array.append(elem)
    else:
        flag=0
print(array)
n=len(array)
even=[]
for i in range(n):
    if(IntOrNot(array[i]/2)==True):
        even.append(array[i])
print(even)


# In[ ]:


import random

number=0
array=[]
print("Сколько элементов вы хотите добавить?")
number=int(input())
for i in range(number):
    random_numb=random.randint(0,100)
    array.append(random_numb)
print(array)

maxnum=0
print("Каким может быть максимальное число?")
maxnum=int(input())

smaller=[]
for i in range(number):
    if(array[i]<=maxnum):
        smaller.append(array[i])
print(smaller)


# In[ ]:


number=0
print("Сколько элементов вы хотите? ")
number=int(input())

array=[]
i0=0
i1=1
i2=0
for i in range(0,2):
    array.append(i)
for i in range(number+1):
    i2=i0+i1
    array.append(i2)
    i0=i1
    i1=i2
print(array)


# In[ ]:


def IntOrNot(n):
    return int(n) == float(n)

number=0
print("Введите ваше число")
number=int(input())
divided=0
flag=0
for i in range(2, number):
    if(i!=0):
        divided=number/i
    if(IntOrNot(divided)==True):
        flag=1
if(flag==1):
    print("Нет, оно не простое")
else:
    print("Это число простое!")


# In[ ]:





# In[ ]:




