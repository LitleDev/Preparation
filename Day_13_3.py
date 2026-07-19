# WAP to find the first occurenc of a subtring in a string 

def strStr(haystack , needle):
    # write code here
    # use sliding window of length needle
    window = len(needle)
    start= 0
    while start < len(haystack)-window:
        if haystack[start:start+window] == needle:
            return start
        start+=1
    return -1

if __name__ == "__main__":
    haystack = "sadbutsad"
    needle = "sad"
    res = strStr(haystack , needle)
    print(res)
    
