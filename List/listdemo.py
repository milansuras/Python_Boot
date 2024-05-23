l=[3,4,5]
print(l)

# list are ordered collection of data items.
# They store multiple item in single variable.

print(type(l))
print(l[0])
print(l[1])
print(l[2])

#inside a list there may be different data type can be inserted 

l1=[1,"Hello",True,8.005]

print(type(l1))
print(l1[0])
print(l1[1])
print(l1[2])
print(l1[3])

print(len(l1))
print(len(l))

print(l[-2])

for i in l:
    print(i)


if "Hello" in l1:
    print("yes")

else:
    print("No")

list=[1,2,3,4,5]

for i in list:
    print(i)


list3=["C","C++","Java","Go","Python", 777, 1.2,True,"Kubernetes" ,"Docker"]
print(list3[1:10:2])
print(len(list3))

lst=[i for i in range(7)]
print(lst)

#methods in list
#append

numbers=[1,2,3,4,5,6]
numbers.append(7)
print(numbers)

numbers1=[2,34,5,56,777]
numbers1.sort()
print(numbers1)

numbers1.sort(reverse=True)
print(numbers1)

print(numbers1.index(5))


m=l.copy()
print(m)
print(l)

m.insert(1,7)
print(l)
print(m)
print(l)

n=[2,3,4]
l.extend(n)
print(n)
print(l)

#to concatenate to list

k=l+m
print(k)