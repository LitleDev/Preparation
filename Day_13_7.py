# Group Anagrams

def is_anagram(dict,visted,strs,idx):
    freq = dict.copy()
    for ch in strs[idx]:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False
    return True

def group_anagram(strs):
    # write code here
    dict_1 = {}
    visted = [False ]*len(strs)
    
    for i in range(len(strs)):
        if visted[i]:
            continue
        
        visted[i] = True
        dict = {}
        val = strs[i]
        for ele in val:
            if ele in dict:
                dict[ele] += 1
            else:
                dict[ele] = 1
        dict_1[val] = [val]
        for j in range(i+1, len(strs)):
            if is_anagram(dict,visted,strs,j):
                dict_1[val].append(strs[j])
                visted[j] = True
        i+=1 
    return dict_1


if __name__ == "__main__": 
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = group_anagram(strs)
    print(res)
    
