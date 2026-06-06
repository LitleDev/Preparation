
#valid anamgram 
# group anamgram 


def valid_anagram(s1,s2):
    # write your code here
    if len(s1) != len(s2):
        return False
    frequency = [0]*26
    for ele in s1:
        idx = ord(ele)-97
        frequency[idx]+=1
    for ele in s2:
        idx = ord(ele)-97
        if frequency[idx] <= 0:
            return False
        frequency[idx]-=1
    return True

def valid_anagram_simple(s1,s2):
    #write code here
    if len(s1) != len(s2):
        return False
    if sorted(s1) == sorted(s2):
        return True
    return False
    
    
def group_anagram(arr):
    # write your code here
    # brute forec
    visted = [0]*len(arr)
    group = []
    for start in range(0,len(arr)):
        if visted[start] == 1:
            continue
        visted[start] = 1
        sub = [arr[start]]
        for end in range(start+1 ,len(arr)):
            s1 = arr[start] 
            s2 = arr[end]
            if valid_anagram_simple(s1,s2) and visted[end] == 0:
                sub.append(s2)
                visted[end] = 1
        group.append(sub)
    return group
    
def group_anagram_optimized(strs):
    # write your code here 
    group = {}
    
    for word in strs:
        key = "".join(sorted(word))
        if key not in group:
            group[key] = []
        group[key].append(word)
    return list(group.values())

if __name__ == "__main__":
    s1 = 'alelrgy'
    s2 = 'allergy'
    res = valid_anagram(s1,s2)
    print(res)
    print(valid_anagram_simple(s1,s2))
    # strs = ["eat","tea","tan","ate","nat","bat"]
    # strs = []
    # strs = ["hello"]
    # strs = ["dog", "cat", "fish"]
    strs = ["aaa", "aaa", "aaa"]
    res2 = group_anagram(strs)
    print(res2)
    print(group_anagram_optimized(strs))
    
