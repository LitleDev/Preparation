# WAP to find the combination of subarray lenth 3 having asceding order
def count_ascending_triplets(arr):
    if not isinstance(arr, list) or len(arr) < 3:
        raise ValueError("Input must be a list with at least 3 elements.")

    n = len(arr)
    count = 0

    # Triple nested loop to check all triplets
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] < arr[j] < arr[k]:
                    count += 1

    return count


# Example usage
arr = [4, 1, 3, 5, 6]
result = count_ascending_triplets(arr)
print("Count of ascending triplets:", result)


# using take not take 

def valid(temp):
    if temp[0]< temp[1] < temp[2]:
        return True
    return False

def helper(count , temp , n ):
    if len(temp) == 3:
        if valid(temp):
            return 1
        else:
            return 0
    if count >= n:
        return 0
    take = helper(count+1 , temp + [arr[count]] , n )
    note_take = helper(count+1 , temp , n )
    return take+note_take

def using_take_not_take(arr):
    n = len(arr)
    return helper(0 , [] , n)
    
print(using_take_not_take(arr))

