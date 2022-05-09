#1 
def func1(name, age):
    print(name,age)
    
func1("ram",25)

#2 
def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60)
func1(80, 100)

#3 
a = "nagraj"
x = a.capitalize()
print(x)

#4 
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
res = []

l3 = l1[1::2]
l4 = l2[0::2]


res.extend(l3)
res.extend(l4)
print(res)    
res.sort()
print(res)

#5 
list1 = [54, 44, 27, 79, 91, 41]
list1.pop(4)
list1.append(91)
list1.insert(2,91)
print(list1)


#6
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

chunk1 = sample_list[0:3]
print(chunk1)
chunk1.reverse()
print(chunk1)

chunk2 = sample_list[3:6]
print(chunk2)
chunk2.reverse()
print(chunk2)

chunk3 = sample_list[6::]
print(chunk3)
chunk3.reverse()
print(chunk3)

#7
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
dict1 = {}

for i in sample_list:
    if i in dict1:
        dict1[i] += 1
    else :
        dict1[i] = 1
        
print(dict1)

#8
a = [2, 3, 4, 5, 6, 7, 8]
b = [4, 9, 16, 25, 36, 49, 64]

c= zip(a,b)

d = set(c)
print(d)

#9
set1 = {23, 42, 65, 57, 78, 83, 29}
set2 = {57, 83, 29, 67, 73, 43, 48}

set3 = set1.intersection(set2)
print(set3)

for i in set3 :
    set1.remove(i)
print(set1)

#10
x = {27, 43, 34}
y = {34, 93, 22, 27, 43, 53, 48}

z = x.intersection(y)

for i in z :
    x.remove(i)
    
print(x)
print(y)
    
