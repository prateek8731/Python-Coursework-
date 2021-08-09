#This program calculates two binary addition

#not gate
def not_gate(x):
    if x==0:
        return 1
    else:
        return 0

#or gate
def or_gate(x,y):
    if x==y==0:
        return 0
    else:
        return 1

#and gate
def and_gate(x,y):
    if x==y==1:
        return 1
    else:
        return 0

#xor gate
def xor_gate(x,y):
    x1 = and_gate(x, not_gate(y))
    y1 = and_gate(y, not_gate(x))
    return int(or_gate(x1,y1))

def halfAdder(x,y):
    a = xor_gate(x,y)
    b = and_gate(x,y)
    return(a,b)

def fullAdder(x,y,c=0):
    sum1,c1=halfAdder(x,y)
    sum2,c2=halfAdder(sum1,c)
    return(sum2,or_gate(c1,c2))

def binaryAdder(x,y):
    if x>y:
        tmp=x
        x=y
        y = tmp
    c=0
    result=''
    for i in range(len(x)-1,-1,-1):
        sum1,c = fullAdder(int(x[i]),int(y[i]),c)
        result+= str(sum1)

    result=result[::-1]

    l = len(result)
    if len(result)<8:
        for i in range(1,8):
            result="0"+result
    return result
        
