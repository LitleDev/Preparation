def fibonacci(n):
    # write your code here 
    first = 0 
    second = 1
    if n == 0 or n == 1: return first
    if n == 2: return second
    while n > 1:
        temp = first+ second
        first = second 
        second = temp
        n-= 1
    return second


n = int(input())
res = fibonacci(n)
print(res)
