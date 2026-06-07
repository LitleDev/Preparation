def find_duplicate(array):
    #write code here 
    largest_value = max(array)
    frequency = [0]*(largest_value+1)
    duplicate = []
    for ele in array:
        if frequency[ele] == False:
            frequency[ele] = 1
        else:
            if frequency[ele] == 1 :
                duplicate.append(ele)
            frequency[ele] += 1
    
    return duplicate

def two_sum(arr , target):
    # write your code here
    left = 0
    right = len(arr)-1
    
    while left < right:
        if arr[left] + arr[right] == target:
            return [left , right]
        elif target > arr[left] + arr[right]:
            left+=1
        else:
            right -=1
    return []
    



if __name__ == "__main__":
    array = [1,2,3,2,4,1]
    res = find_duplicate(array)
    print(res)
    array1 = [2,7,11,15]
    target = 9
    res1 = two_sum(array1 , target)
    print(res1)
    
    
