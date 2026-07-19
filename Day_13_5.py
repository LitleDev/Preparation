# WAP to check a valid palindrom after removing atmost one character
# Palindrom II

def plaindrom(left, right,s):
    while left < right:
        if s[left] != s[right]:
            return False
        left +=1 
        right += 1
    return True
    

def palindrom_two(s):
    # write your code here 
    left = 0 
    right = len(s)-1
    
    count = 0
    while left < right: 
        if s[left] != s[right] and count == 0:
            return (plaindrom(left+1, right,s) or plaindrom(left , right-1,s))
            
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    array = ["aba", "abc","abca","abcaa"]
    for ele in array:
        res = palindrom_two(ele)
        print(res)
    
    
