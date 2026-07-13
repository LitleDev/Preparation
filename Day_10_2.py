# WAP to change Decimal number to Binary number 

def decimal_to_binaery(val):
    # write code here
    if val == 0:
        return 0
    if val < 0:
        val = abs(val)
    binary = ""
    while val >= 1:
        remainder = val % 2
        binary = str(remainder)+ binary
        val = val//2
    return binary


val = int(input())
res = decimal_to_binaery(val)
print(res)

