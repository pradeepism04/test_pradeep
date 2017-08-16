from copy import deepcopy
def pathSum(self, root, sum1):
    temp=[]
    result=[]
    len1=0
    self.find_sum_len(root,sum1,result,temp,len1)
    return result

def find_sum_len(slef,root,s,result,temp,len1):
    if root is None:
        return 0
    else: 
        currentvalue=root.val

        temp.insert(len1,currentvalue)
        len1+=1
        if(root.left is None and root.right is None):
            if(sum(temp)==s):
                result.append(deepcopy(temp))

        else:
            if(root.left):
                slef.find_sum_len(root.left,s,result,temp,len1) 
                if(len(temp)>0):
                    temp.pop()
            if(root.right):
                slef.find_sum_len(root.right,s,result,temp,len1)
                if(len(temp)>0):
                    temp.pop()
    return result
    