from array import *

# arr = array("type", [])
# Type code	         C Type	    Python Type 	Minimum size in bytes
# 'b'	signed        char	        int	            1
# 'B'	unsigned        char	    int	             1
# 'u'	PY-UNICODE	    Unicode character	        2
# 'h'	signed short	int	2
# 'H'	unsigned short	int	2
# 'i'	signed int	int	2    
# 'I'	unsigned int	int	2
# 'l'	signed long	int	4
# 'L'	unsigned long	int	4
# 'q'	signed long long	int	8
# 'Q'	unsigned long long	int	8
# 'f'	float	float	4
# 'd'	double	float	8

arr1 = array('i', [1, 2, 3, 4, 5, 6, 7])
print(type(arr1))   #<class 'array.array'>
# print(arr1[2])
for item in arr1:
    print(item)

for i in range(7):
    print(arr1[i])

arr2 = array('u', ['a', 'b', 'c', 'd', 'e', 'f', 'g','a','c'])
print("itemsize:",arr2.itemsize)
# itemsize returns the size in bytes of one element in the array.
 
# i = 0
# while(i<len(arr2)):
#     print(arr2[i])
#     i+=1

arr2.append("5")
print(arr2[-1])
print(arr2.count('z'))   #0 =doesnt exist

#finding index
print(arr2.index("c"))   #1st occurence of the item

#insert(a,b) => insert b at index a
arr2.insert(1,'Z')
print(arr2[1])

#Slicing
slice_arr = arr2[1:4]

#extend
arr3=['x','y','z']
arr2.extend(arr3)
print(arr2)
arr2.remove('z')
print(arr2[-1])

#pop

last_element = arr2.pop() #removes and returns the last element
#index based pop
arr2.pop(0)  #removes  and returns the 0th index
print(last_element)

#revrsing array
arr2.reverse()  
#The arr.reverse() method in Python reverses the elements of the original array in place.
print(arr2)

#buffer info
buffer_info = arr2.buffer_info()
print(buffer_info)  # Output: (address, length) - e.g., (140485610982400, 8)


#converting arrray to list
list_array = arr2.tolist()
print(list_array[1])


arr2_copy = arr2[:]
print(arr2)
# The arr.copy() method in Python creates a shallow copy of the array.
#Shallow Copy: The copy() method creates a new array object, arr_copy,
#  which contains the same elements as arr.
#  This new array is a shallow copy, meaning that the elements themselves are copied,
#  but if the array contained complex objects (like lists or other arrays), 
# the objects themselves are not deeply copied—only their references are copied.