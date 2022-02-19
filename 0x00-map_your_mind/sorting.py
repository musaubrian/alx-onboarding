A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
C = int(input("Enter third number: "))

if(A > B):
    if(B > C):
        print("Option 1: ", A, B, C)
    else:
        if A > C:
            print("Option 2:", A, C, B)
        else:
            print("Option 3:",C, A, B)
else:
    if A < C:
        if B > C:
            print("Option 4:", B, C, A)
        else:
            print("Option 5:", C, B, A)
    else:
         print("Option 6:", B, A, C)
