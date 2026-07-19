# WAP to find if a string is palindrom with sepcial char

def palindrom(s : str):
    # write code here
    left = 0 
    right = len(s)-1
    
    while left < right: 
        
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    string = "A man, a plan, a canal: Panama"
    if palindrom(string):
        print(f" '{string}' is a Palindrom")
    else:
        print(f" {string} is not a Palindrom")
    
