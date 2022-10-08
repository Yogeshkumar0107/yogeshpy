from operator import truediv


a="Hello world"
#length of a
print(len(a))
#print 1 of a
print(a[1])
#print2 to 5 not included
print(a[2:5])
#slice from the start
print(a[2:])
print(a[:5])
print(a[-5:-2])
#b is a sentence 

b="how are you google"
#length of b
print(len(b))

#print  2 of b
print(b[2])

print(b[2:10])

print(b[11])

#modify stringsin python using built in methods

x='Hi everyone'
print(x.upper())
print(x.lower())

#remove whitspaces

x='   Lets study python'
print(x)
print(x.strip())

#replace

x='Hi everyone'
print(x.replace('H','A'))
print(x.split())
print(x.split(','))
y=x.split()
print(y[1])

#string cocatenation
x='Hi'
y='Everyone'
z=x+y
print(z)









# BOOLEAN

print(5>2)
print(7 -- 4)
print(9<6)

#values are true

#any value has data will be written true

#for any string it writes true except empty

#for any number it writes true except 0

#values that are false

print(bool(False))
print(bool(None))
print(bool(0))
print(bool([]))
print(bool({}))


# lists
List=[10,20,30,40,50]
print(list)
print(type(list))

  #hange list items

list1=[30,60,80,120,81]
list1[2]=90
print(list1)
list1[1:2]=["hi","hello"]
print(list1)


#extend a list
list1=[10,20,30,40]
list2=[50,60,70,80]
tuple=(50,60)
list1.extend(list2)
print(list1)
list1.extend(tuple)
print(list1)

#remove specified items from the list
list3=['john','peter','viraj','raman']
list3.remove('viraj')
print(list3)

#removing item from specified index
list=['john','peter','viraj']
list.pop()
print(list)
