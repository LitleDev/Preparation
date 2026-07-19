# WAP to revers words in string

def reverse_word(s : str) -> str:
    # write code hete 
    s = s.split()
    # print(s)
    left = 0 
    right = len(s)-1
    while left < right :
        s[left], s[right] = s[right], s[left]
        left += 1 
        right -= 1
    
    return " ".join(s)


if __name__ == "__main__":
    # s = "the sky is blue" 
    s = "a good   example"
    res = reverse_word(s)
    print(res)
    
    
    
