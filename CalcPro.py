import math
def calc (num1,symbol,num2):
    options = [ num1 + num2 , num1 - num2 , num1 * num2 , num1 / num2 , num1 ** num2 ]
    opperations = ["+","-","*","/","pow"]
    if symbol in opperations:
        print(f"The result is: {options[opperations.index(symbol)]}")
    else:
        print("\n     --- You must choose a symbol from ( + , - , * , / , pow) ---")

def shapes (choice):
    if choice == "A":
        choiceA = input("\nChoose square(S) or rectangle(R) or tringal(T) or circle(C): ").upper().strip()
        if choiceA == "S" : 
            print(f"The result is {round( int(input("\nEnter the side: ")) ** 2 , 2)}")
        elif choiceA == "R" : 
            print(f"The result is {round( int(input("\nEnter the width: ")) * int(input("Enter the legnth: ")) , 2)}")
        elif choiceA == "T" : 
            print(f"The result is {round( 0.5 * int(input("\nEnter the base: ")) * int(input("Enter the hight: ")) , 2)}")
        elif choiceA == "C" : 
            print(f"The result is {round( math.pi * (int(input("\nEnter the radius: ")) ** 2) , 2)}")
        else:
            print("     ---<( You should choose ( S or R or T or C ) )>---")
    elif choice == "P":
        choiceB = input("\nChoose square(S) or rectangle(R) or tringal(T) or circle(C): ").upper().strip()
        if choiceB == "S" :
            print(f"The result is {round( int(input("\nEnter the side: ")) * 4 , 2)}")
        elif choiceB == "R" :
            print(f"The result is {round( (int(input("\nEnter the width: ")) + int(input("Enter the legnth: "))) * 2 , 2)}")
        elif choiceB == "T" :
            print(f"The result is {round( int(input("\nEnter the side 1: ")) + int(input("Enter the side 2: ")) + int(input("Enter the side 3: ")) , 2)}")
        elif choiceB == "C" :
            print(f"The result is {round( math.pi * int(input("\nEnter the radius: ")) * 2 , 2)}")
        else:
            print("\n     ---<( You should choose ( S or R or T or C ) )>---")
    elif choice == "V":
        choiceC = input("\nChoose cube(C) or rectangular prism(R) or cylinder(D) or sphere(S): ").upper().strip()
        if choiceC == "C" :
            print(f"The result is {round( int(input("\nEnter the side: ")) ** 3 , 2)}")
        elif choiceC == "R" :
            print(f"The result is {round( int(input("\nEnter the width: ")) * int(input("Enter the legnth: ")) * int(input("Enter the hight: ")) , 2)}")
        elif choiceC == "D" :
            print(f"The result is {round( math.pi * ( int(input("\nEnter the radius: ")) ** 2 ) * int(input("Enter the hight: ")) , 2)}")
        elif choiceC == "S" :
            print(f"The result is {round( math.pi * (4/3) * (int(input("\nEnter the radius: ")) ** 3) , 2)}")
        else:
            print("\n     ---<( You should choose ( S or R or T or C ) )>---")
    else:
        print("\n     ---<( You should choose ( A or P or V ) )>---")
while True:
    choice = input("\nChoose between calculator(A) or geometric calculations(B): ").strip().upper()
    if choice == "A":
        try:
            calc(float(input("\nEnter first number: ")),
                input("Enter a symbol( + or - or / or * or pow): ").strip().lower(),
                float(input("Enter second number: ")))
        except ValueError:
            print("     ---<( You must enter a number )>---")
        except ZeroDivisionError:
            print("     ---<( MATH ERROR: You can't divide by zero )>---")
    elif choice == "B":
        try:
            shapes(input("\nChoose area(A) or perimeter(P) or volume(V): ").strip().upper())
        except ValueError:
            print("     ---<( You should enter a number )>---")
    else:
        print("\n     ---<( You should choose between ( A or B ) )>---")