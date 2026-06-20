# generator and iterators
def mymethod(n):
    i = 0
    while i < n:
        yield(i)
        i+=1

gen = mymethod(5)
print(next(gen))
print(next(gen))
print(next(gen))


genr = (i*i   for i in range(10) )
print(list(genr), type(genr))


def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

for num in fibonacci(50):
    print(num, end=" ")

# Try Exception else Finally 
def mymethod(val):
    try:
        val = int(val)
        res = 100/val
    except ZeroDivisionError:
        print("cANNOTE DIVIDE BY ZERO  ")
    except ValueError:
        print("Not a value")
    else:
        print(f" {res} , {val}")
    finally:
        print("process complete")
        
def method_2(val):
    try:
        val = int(val)
        res = 100//val
    except Exception as e:
        print(f"Excpetion : ->  {e}")
        
    else:
        print("No exception")
    finally:
        print("Execution complete Relase resouce")


if __name__ == "__main__":
    val = input()
    mymethod(val)
    method_2(val)
