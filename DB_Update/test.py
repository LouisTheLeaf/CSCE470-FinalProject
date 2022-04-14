#python
# Python program to illustrate
# enumerate function
l1 = ["eat","sleep","repeat"]
s1 = "geek"
 
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
 
print (list(obj1))
# print (list(enumerate(l1)))
ints=["eat","sleep","repeat"]
for idx, val in enumerate(ints):
    print(idx, val)
# # changing start index to 2 from 0
# print (list(enumerate(s1,2)))