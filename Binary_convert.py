def binary_conversion(n):
    n = int(n)
    bit= []
    Binary=[]
    Binary_Num =""
    l = 0
    while n != 0:
        rem= n%2
        bit.append(rem)
        n= n//2
    for i in range(len(bit)-1,-1,-1):
        Binary.append(bit[i])
        Binary_Num = Binary_Num + str(bit[i])
        l = len(Binary_Num)
    if len(Binary_Num)<8:
        for i in range(1,8):
            Binary_Num= "0" + Binary_Num
    return Binary_Num

