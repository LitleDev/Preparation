# WAP for longest non repeating substring
def repating_element(string):
    #write your code here 
    seen= {}
    left = 0 
    right = 0 
    max_len = 0 
    while right < len(string):
        val = string[right]
        if  val in seen and seen[val] >= left:
            left = seen[val]+1
        seen[val] = right 
        max_len = max(max_len ,right - left+1)
        right += 1
    return max_len
    

if __name__ == "__main__":
    string = "abccodefghiyrkjldcab"
    res = repating_element(string)
    print(res)
