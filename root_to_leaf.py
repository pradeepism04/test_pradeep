from copy import deepcopy
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

def root_to_leaf(node,s,result,temp):
    global dict1,i
    if node is None:
        return 0
    else: 
        currentvalue=node.data
        temp.append(currentvalue)
        if(node.left is None and node.right is None):
            if(s-currentvalue==0):
            
                result.append(deepcopy(temp))
        if(s>0):
            root_to_leaf(node.left,s-node.data,result,temp) 
            root_to_leaf(node.right,s-node.data,result,temp)
            temp.pop()
    return result


sum1 = 22
root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right.left = Node(13)
root.right.right = Node(4)
root.right.right.left = Node(5)
root.right.right.right = Node(1)
                      
temp=[]
result=[]
x=root_to_leaf(root, sum1,result,temp)
if len(x)>0:
    print(x)
else:
    print("Not found ")