# WAP to implement binary search 

def binary_search(arr,k):
    # write code here 
    left = 0 
    right = len(arr)-1
    
    while left <= right: 
        mid = (left+ right) //2
        val = arr[mid]
        if val == k:
            return mid
        elif val > k:
            # go left 
            right=mid-1
        else:
            # go right 
            left = mid +1
    return


if __name__ == "__main__":
    arr = [2,3,4,10,40]
    x = 10
    res = binary_search(arr,x)
    print(res)
    
