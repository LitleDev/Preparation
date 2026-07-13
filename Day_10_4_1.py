# WAP to find the sibling of givrn X 

class Node:
    def __init__(self , data ):
        self.data = data 
        self.left = None
        self.right = None
        
    def add_Node(self,data):
        if self.data == None:
            self.data = data
        else:
            new_node = Node(data)
            # general add operation 
            if data > self.data:
                # go right
                if self.right:
                    # data is there is right
                    self.right.add_Node(data)
                else:
                    self.right = new_node
            else:
                # go left 
                if self.left:
                    # data is there is right
                    self.left.add_Node(data)
                else:
                    self.left = new_node
    
def display(root):
    if root == None:
        return
    print(root.data)
    display(root.left)
    display(root.right)
        
def level_order(root, target, count):
    if root is None:
        return -1
    if root.data == target:
        return count 
    if target > root.data:
        # go right
        return level_order(root.right , target , count+1)
    else:
        #go to left
        return level_order(root.left , target , count+1)
        

def sibling( n , x , array):
    # write code here 
    idx = array.index(x)
    order = (idx+1).bit_length()
    print(array[2**(order-1)-1:2**(order)-1])
    # construct a binary tree for the above given
    root = Node(None)
    for ele in array:
        root.add_Node(ele)
    display(root)
    level = level_order(root , 13 , 0)
    print(f"the level is {level}")
    return 


if __name__ == "__main__":
    n = 5 
    array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24] 
    x = 14
    res = sibling(n,x,array)
    print(res)
    
    
    print((7).bit_length())
    print(array[2**2-1:2**3-1])

