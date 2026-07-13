# WAP string compression
def string_compression(string):
    # write code here 
    previous = None 
    count = 0 
    short = ""
    for current in string:
        if previous == None:
            previous = current
            count += 1
        else:
            if current == previous:
                count+=1
            else:
                short += previous+str(count)
                count = 1
                previous = current
    short += previous+str(count)
    return short


string = "aaddeeefffdfggg"
res = string_compression(string)
print(res)
