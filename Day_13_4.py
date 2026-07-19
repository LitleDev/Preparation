# WAPto find if the given strings is anagram 

def anagram(s,t):
    # write code here 
    if len(s) != len(t):
        return False
    dict= {}
    for ele in s:
        if ele in dict:
            dict[ele]+=1
        else:
            dict[ele] = 1
        
    for val in t:
        if val not in dict:
            return False
        dict[val] -= 1
        
        if dict[val] < 0:
            return False
            
    return True


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    res = anagram(s,t)
    print(res)
