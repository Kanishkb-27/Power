def power2(number):
    if(number==0):
        return 0
    if((number&(~(number-1)))==number):
        return 1
    return 0
number=int(input("Enter the number"))
if(power2(number)):
    print("The number is the power of two")
else:
    print("The number is not the power of two")