#................calculater................................

print("\nWelcome user to our calculating service..........\n")
retry  = 'yy'
while retry.lower() == 'yy':
    print("\n.........     Let's start  !!     ...........\n")

    while True :
        try:
            a = int(input("Enter the valuse of a : "))
            b = int(input("Enter the valuse of b : ")) 
            break        
    
        except ValueError :
            print("Enter  correct integer input")
    

    ret = 'y'
    while ret.lower() == 'y':    
        while True :
            choise = input("Select operation :\n1--> Addition\n2--. Subtraction\n3--> Multiplication\n4--> Division\n5--> Exit from this operation : ")
            if choise in ['1' , '2' , '3' , '4' , '5']:
                break
            print("ENter correct input for operation...")
            
        if choise == '1':
            print(f"\nThe result of Addition : {a}+{b} = {a + b}")
        elif choise == '2':
            print(f"\nThe result of Subtraction : {a}-{b} = {a - b}")
        elif choise == '3':
            print(f"\nThe result of Multiplication : {a}*{b} = {a * b}")
        elif choise == '4':
            if b == 0 :
                print("\nDivision by 0 is not allowed.")
            else:
                print(f"\nThe result of Division : {a}/{b} = {a / b}")
        elif choise == '5':
            break    

    
        ret = input("\nEnter 'Y' or 'y' for regenerate with.....SAME parameter\nOR Something else to Exit this operation : ")    
        
    if ret.lower() != 'y':
        retry = input("\nEnter 'yy' or 'YY' for regenerate with.....NEW parameter\nOR press any other key to Exit...!!! : ")

6
     
print("\n...........Thank You...VIsit again (*_*)..........\n\n")
        
