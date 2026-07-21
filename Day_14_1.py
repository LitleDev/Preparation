

def subset_combination(array):
    # write your code here 
    for i in range (0, len(array)-2):
        sub = []
        sub.append(array[i])
        for j in range(i+1,len(array)-1):
            sub.append(array[j])
            sub.append(array[j+1])
            
            if sub[0] < sub[1] < sub[2]:
                print(sub)
            sub = [array[i]]
            
    
def subset_brute_force(array):
    seen = []
    for i in range (0, len(array)-2):
        for j in range(i+1,len(array)-1):
            for k in range(j+1,len(array)):
                if array[i] < array[j] < array[k]:
                    if [array[i],array[j],array[k]] in seen:
                        continue
                    # print(array)
                    seen.append([array[i],array[j],array[k]])
    return len(seen)
    

if __name__ == "__main__":
    # array = [3,2,1,4,5]
    # array = [2,1,5,0,4,6]
    array= [1,1,1,2,2,2,3,3,4]
    res = subset_combination(array)
    print(res)
    res1 = subset_brute_force(array)
    print(res1)


