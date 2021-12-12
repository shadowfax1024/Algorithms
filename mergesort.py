
def merge(x,y):
    print("IN MERGE",x,y)
    m,n = len(x),len(y)
    x.extend(y)
    x.sort()
    print("SORTED IN MERGE",x)
    return x


def divide(x):
    print("IN DIVIDE",x)
    if(len(x)==1):
        return x
    else:
        x1 = x[:len(x)//2]
        x2 = x[len(x)//2:]
        print("AFTER DIV",x1,x2)
        divide(x1)
        divide(x2)
        return merge(x1,x2)

print(divide([100,-10.99,4,1,0,2,5,99]))
