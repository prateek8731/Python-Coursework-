from Binary_convert import binary_conversion
from binaryadder import binaryAdder
print("This is the Binary Adder system")
inp = "yes"
while inp =="yes" or inp =="y":
    out = False
    while out == False:
        try:
            a=int(input("Please enter the first number: "))
            if a>255:
                print("The number should be in range of 0 and 255")
            else:
                out = True
        except:
            print("Please Enter a valid input!")
    out = False
    while out == False:
        try:
            b= int(input("Please enter the second number: "))
            if b>255:
                print("The number must be in range of 255: ")
            else:
                out= True
        except:
            print("please input a valid number!")
        print("The binary value of {}is:{}\n".format(a,binary_conversion(a)))
        print("The binary value of {}is:{}\n".format(b,binary_conversion(b)))
              
        x=binary_conversion(a)
        y=binary_conversion(b)
        sum1= binaryAdder(str(x),str(y))
        print("The sum of {} and {} is:{}\n".format(a,b,sum1))
        inp = input("Do u wish to continue? yes/no : ")
              
              



            
    
        
            
    
    
