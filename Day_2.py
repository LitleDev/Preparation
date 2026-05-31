def merge_interval(arr):
    # write code here 
    merge = []
    for intervl in arr:
        if not merge or merge[-1][1] < intervl[0]:
            merge.append(intervl)
        else:
            merge[-1][1] = max(merge[-1][1],intervl[1])
    print(not merge)
    print(bool(merge))
    
    return merge

def merge_2(arr,ins):
    # write code here
    arr.append(ins)
    arr.sort(key=lambda x: x[0])
    
    merge = []
    
    for interval in arr:
        if not merge or merge[-1][1] < interval[0]:
            merge.append(interval)
        else:
            merge[-1][1] = max(merge[-1][1], interval[1])
    return merge

def overlay(arr1 , arr2):
    # write code here
    arr1.extend(arr2)
    arr1.sort(key= lambda x : x[0])
    
    merge = []
    overlap = []
    
    for interval in arr1:
        if not merge or merge[-1][1] < interval[0]:
            merge.append(interval)
        else:
            temp1 = max(merge[-1][0],interval[0])
            temp2 = min(merge[-1][1], interval[1])
            overlap.append([temp1,temp2])
            merge[-1][1] = max(merge[-1][1],interval[1])
    return overlap
    
def meeting_room(arr):
    # write code here 
    merge = []
    count = 0
    for interval in arr:
        if not merge or merge[-1][1] < interval[0]:
            merge.append(interval)
        else:
            merge[-1][1] = max(merge[-1][1],interval[1])
            count += 1
    return count
    
def meeting_room_corrected(arr):
    # write your code here 
    # separte the start and end and sort the array 
    start = []
    end = []
    for s,p in arr:
        start.append(s)
        end.append(p)
    start.sort()
    end.sort()
    
    # now keep two pointer for start and end 
    s_pntr = e_pntrm = 0
    rooms = ongoing = 0
    
    while s_pntr < len(arr):
        if start[s_pntr] < end[e_pntrm]:
            ongoing+=1
            rooms = max(rooms , ongoing)
            s_pntr+=1
        else:
            ongoing -=1
            e_pntrm +=1

    return rooms
    
    
def common_frre_time(arr):
    # write your code here
    meetings = []
    merge = []
    free_time = []
    for emp in arr:
        meetings.extend(emp)
    meetings.sort(key=lambda k : k[0])
    print(meetings)
    
    for meeting in meetings:
        if not merge or merge[-1][1] < meeting[0]:
            merge.append(meeting)
        else:
            merge[-1][1]= max(merge[-1][1], meeting[1])
    
    for i in range(1,len(merge)):
        start = merge[i-1][1]
        end = merge[i][0]
        if start < end : 
            free_time.append([start ,end])
    
    return free_time

if __name__ == "__main__":
    arr = [[1,3],[6,9],[10,12]]
    ins = [4,5]
    res = merge_interval(arr)
    print(res)
    
    res2 = merge_2(arr,ins)
    print(res2)
    
    # over laying
    #arr1 = [[1,3],[5,6]] 
    #arr2 = [[2,4],[5,7]] 
    # arr1 = [[1,2],[4,5]]
    # arr2 = [[6,7],[8,9]]
    # arr1 = [[1,3]]
    # arr2 = [[1,3]]
    # arr1 = [[1,2]]
    # arr2 = [[2,3]]
    arr1 = [[1,10]]
    arr2 = [[3,5],[6,8]]
    # arr1 = [[1,3],[6,9]]
    # arr2 = [[2,5],[7,10]]
    # [[2,3],[5,6]]
    res3 = overlay(arr1 , arr2)
    print(res3)
    # arr2 = [[0,30],[5,10],[15,20]]
    # arr2 = [[5,10]]
    # arr2 = [[0,10],[2,6],[4,8]]
    # arr2 = [[1,2],[3,4],[5,6]]
    arr2 = [[1,10],[2,3],[4,5],[6,7]]
    res4 = meeting_room(arr2)
    print(res4)
    res5 = meeting_room_corrected(arr2)
    print(res5)
    # arr3 = [[[1,2],[5,6]], [[1,3]], [[4,10]]]
    # arr3 = [[[1,5]]]
    # arr3 = [[[1,10]], [[2,9]], [[3,8]]]
    # arr3 = []
    arr3 = [[[1,2],[5,6]], [[1,3]], [[4,10]], [[11,12]]]
    res6 = common_frre_time(arr3)
    print(res6)
    
    
