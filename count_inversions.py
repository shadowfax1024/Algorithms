def merge(x,y): #x,y are lists can be of unequal lengths
    res = []
    p,q= 0,0
    inversions=0
    for i in range(len(x)+len(y)):
        print(res)
        if(p==len(x)):
            for x in y[q:]:
                res.append(x)
            break
        elif(q==len(y)):
            for x in x[p:]:
                res.append(x)
            break
        elif(x[p] > y[q]):
            res.append(y[q])
            q +=1
            inversions += len(x) - p 
        elif(x[p] < y[q]):
            res.append(x[p])
            p +=1
    print(res)
    return res
def merge_sort(nums):  # proper implementation of merge sort algorithm
    if(len(nums)==1):
        return nums #nums,0
    else:
        len_ = len(nums)
        mid = len_//2
        inv_left = merge_sort(nums[:mid])
        inv_right = merge_sort(nums[mid:])
        print("LEFT RIGHT",inv_left,inv_right)
       # left,inv_left = merge_sort(nums[:mid])
        #right,inv_right = merge_sort(nums[mid:])
        return merge(inv_left,inv_right)
    
x =[2,4,3,5,1]
print(merge_sort(x))
