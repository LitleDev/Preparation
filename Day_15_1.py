# String Compression

def group_compression(chars):
    # write code here
    count = 1
    previous = chars[0]
    compresed = ""
    for i in range(1,len(chars)):
        if chars[i] == previous:
            count+=1
        else:
            if count == 1:
                compresed += previous
            else:
                compresed = compresed + previous + str(count)
            previous = chars[i]
            count = 1
        # print(previous,count)
    if count > 1:
        compresed = compresed + previous + str(count)
        return len(compresed)
    else:
        compresed+=previous
        return len(compresed)


if __name__ == "__main__":
    chars = ["a", "b", "b", "b","b"]
    res = group_compression(chars)
    print(res)
