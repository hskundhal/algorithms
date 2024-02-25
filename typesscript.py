
# dictionaries are using same location in memoory
dict1 = { 'value':11}
dict2 = dict1

print(dict1)
print(dict2)

dict1['value'] = 12
print(dict1)
print(dict2)

# Numpy arrays use continous in memory ---- 
# pythons built in List have reference to location in memory for data. reference itself 
# is 8 bytes
# python is built using c,c++
# Linked List is spread around and dont have indexes.

j=(1,2,3,4) #tuple
m=list(j) # to list
print(m)

d = {"name":"python", "version":3.9}
new_list = list(d.items())
print("items : ",new_list)`


new_list = list(d.keys())
print("keys :",new_list)


new_list = list(d.values())
print(new_list)

new_list = zip(d.keys(), d.values()) 
print(new_list)

new_list = []
 
for i in d:
  k = [i, d[i]]
  print("i ",i, " d[i] ", d[i] )
  new_list.append(k)
 
print(new_list)

nameTuple = ('P','Y','T','H','O','N', 'P','O','O','L')
separator=""
print(separator.join(nameTuple))

#sort using inbuilt list.Sort()
#tuple having structure(name, age)
list_siblings=[("Rohit",19),("Rishabh",14),("Ram",23),
("Navya",17),("Aditi",22)]
list_siblings.sort(key= lambda x:x[1])
print(list_siblings)



late = ('19', '17', '14', '10', '11')
print(sorted(late))

from collections import deque
doublelinklistfromdeque = deque()
doublelinklistfromdeque.append(1)
doublelinklistfromdeque.append(9)
doublelinklistfromdeque.append(2)
print(doublelinklistfromdeque)


#JSON
# The reason is that the json.load() method can only handle a single JSON object.