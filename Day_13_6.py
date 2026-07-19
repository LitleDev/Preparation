# WAP to find the longest substring without repeating Character

def longest_substring(words: str):
    # write code here 
    dict = {}
    left = 0 
    max_length = 0 
    for key,ch in enumerate(words):
        if ch in dict:
            if dict[ch] >= left:
                left= dict[ch] +1
            dict[ch] = key
        else:
            dict[ch] = key
        max_length = max(max_length , key-left+1)
            
    return max_length


if __name__ == "__main__":
    string = "abcabcdb"
    res = longest_substring(string)
    print(res)
