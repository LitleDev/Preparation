
'''
class singletoneMeta(type): 
    _instance = {}
    
    def __class__ (cls , *args , **kwargs ):
        if cls not in cls._instance:
            cls._instance[cls] = super().__class__( *args , **kwargs)
        return cls._instance[cls]
        
'''
# set in python 
# heapq in python 
# collection in python 

my_set = {1,2,3,4,3,4,5,6,5,6,7,8}

print(my_set)
my_set.remove(5)
print(my_set)
my_set.add(9)
print(my_set)
my_set.update([5,10,21,14])
print(my_set)

val = my_set.pop()
print(val)
val = my_set.pop()
print(val)

set_a = {1,2,4}
set_b = {3,4,5}

print("Union below ")
print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_a.difference(set_b))

array = [12, 35, 188, 10, 34, 1]

second_largest = sorted(set(array),reverse=True)[1]
print(second_largest)

# list or array
nums = [1,2]
nums.append(10)
print(nums)
nums.extend([3,5])
print(nums)
nums2 = [3,9,1,5]
nums.extend(nums2)
print(nums)
print(set(nums))
nums.insert(2,0)
print(nums)
nums.remove(5)
print(nums)
nums.remove(5)
print(nums)
nums.pop(0)
print(nums)
nums.clear()
print(nums)

# Dictionary
studnt = {
    "name": "Suvit ",
    'age': 32,
    'address': "some place on earth " , 
    'course': "some Course"
}
print(studnt)

del studnt["course"]

print(studnt)

print(studnt.items())

print(" ")
print(" ")

for ele in studnt.items():
    print(ele)
    
    

new_dict = studnt.copy()
print(new_dict is studnt)
print(new_dict == studnt)

d = {"a":1, "b":2, 'c':3 ,'d':4}

val = d.popitem()

print(val)
print(d)

d.update({'e':5,'d':4})

print(d)

print(d.pop('f', 0))
print(d)


# heapq in python 

# collection in python 

import heapq

nums3 = [20,15,25,40,50]

heapq.heapify(nums3)
print(nums3)

heapq.heappush(nums3 , 30)
print(nums3)
heapq.heappop(nums3)
print("before " ,nums3)
heapq.heapify(nums3)
print(nums3)
heapq.heappop(nums3)
print("before", nums3)
print(nums3)
print("before", nums3)
heapq.heappop(nums3)
print("before", nums3)
print(nums3)




