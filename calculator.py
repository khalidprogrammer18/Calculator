import math
print("\n     --- Wellcome to calculation program ---")
while True:
    choice = input("\nChoose calculator(A) or geometric calculations(B): ").upper().strip()
    if choice == "A":
        print()
        while True:
            try:
                num1 = float(input("Enter first number: "))
                break
            except ValueError:
                print("     --- You should enter a number --- ")
        while True:
            smb = input("Choose a symbol ( + or - or / or * or pow): ").lower().strip()
            if smb in ("+","-","/","*","pow"):
                break
            else:
                print("     --- You should choose a symbol --- ")
        while True:
            try:
                num2 = float(input("Enter second number: "))
                break
            except ValueError:
                print("     --- You should enter a number --- ")
        if smb == "+":
            print(f"The result is: {round( num1 + num2 , 2 )} ")
        elif smb == "-":
            print(f"The result is: {round( num1 - num2 , 2 )} ")
        elif smb == "/":
            try:
                print(f"The result is: {round( num1 / num2 , 2 )} ")
            except ZeroDivisionError:
                print("     --- Math error: You can't divide by zero --- ")
        elif smb == "*":
            print(f"The result is: {round( num1 * num2 , 2 )} ")
        elif smb.lower() == "pow":
            print(f"The result is: {round( num1 ** num2 , 2 )} ")
            continue
    elif choice == "B":
        while True:
            pros = input("\nChoose area(A) or perimeter(P) or volume(V): ").upper().strip()
            if pros == "A":
                while True:
                    shape = input("\nChoose the shape: square(S) or rectangle(R) or triangle(T) or circle(C): ").upper().strip()
                    if shape == "S":
                        print()
                        while True:
                            try:
                                side = float(input("Enter the square side: "))
                                print(f"The result is: {round( side ** 2 , 2 )}")
                                break
                            except ValueError:
                                print("     --- You should enter a number --- ")
                    elif shape == "R":
                        print()
                        while True:
                            try:
                                wid = float(input("Enter the width: "))
                                break
                            except ValueError:
                                print("     --- You should enter a number --- ")
                        while True:
                            try:
                                lnth = float(input("Enter the length: "))
                                print(f"The result is: {round( wid * lnth , 2 )}")
                                break
                            except ValueError:
                                print("     --- You should enter a number --- ")
                        break
                    elif shape == "T":
                        print()
                        while True:
                            try:
                                base = float(input("Enter the base: "))
                                break
                            except ValueError:
                                print("     --- You should enter a number --- ")
                        while True:
                            try:
                                hight = float(input("Enter the hight: "))
                                print(f"The result is: {round( 0.5 * base * hight , 2 )}")
                                break
                            except ValueError:
                                print("     --- You should enter a number --- ")
                        break
                    elif shape == "C":
                        print()
                        while True:
                            try:
                                rad = float(input("Enter the radius: "))
                                print(f"The result is: {round( math.pi * ( rad ** 2 ) , 2 )}")
                                break
                            except ValueError:
                                print("     --- You should enter a number --- ")
                        break
                    else:
                        print("\n     --- You must choose ( S or R or T or C ) --- ")
                        continue
                    break
            elif pros == "P":
                while True:
                    shape = input("\nChoose the shape: square(S) or rectangle(R) or triangle(T) or circle(C): ").upper().strip()
                    if shape == "S":
                        print()
                        while True:
                            try:
                                side = float(input("Enter the square side: "))
                                print(f"The result is: {round( side * 4 , 2 )}")
                                break
                            except ValueError:
                                print("     --- You should enter a number --- ")
                        break
                    elif shape == "R":
                        print()
                        while True:
                            try:
                                wid = float(input("Enter the width: "))
                                break
                            except ValueError:
                                print("     --- You should enter a number --- ")
                        while True:
                            try:
                                leg = float(input("Enter the length: "))
                                print(f"The result is: {round( 2 * ( wid + leg ) , 2 )}")
                                break
                            except ValueError:
                                print("     --- You should enter a number --- ")
                        break
                    elif shape == "T":
                        print()
                        while True:
                            try:
                                side1 = float(input("Enter the first side: "))
                                break
                            except ValueError:
                                print("     --- You should enter a number --- ")
                        while True:
                            try:
                                side2 = float(input("Enter the second side: "))
                                break
                            except ValueError:
                                print("     --- You should enter a number --- ")
                        while True:
                            try:
                                side3 = float(input("Enter the third side: "))
                                print(f"The result is: {round( side1 + side2 + side3 , 2 )}")
                                break
                            except ValueError:
                                print("     --- You should enter a number --- ")
                        break
                    elif shape == "C":
                        print()
                        while True:
                            try:
                                rad = float(input("Enter the radius: "))
                                print(f"The result is: {round( 2 * math.pi * rad , 2 )}")
                                break
                            except ValueError:
                                print("     --- You should enter a number --- ")
                        break
                    else:
                        print("\n     --- You must choose ( S or R or T or C ) --- ")
                        continue
            elif pros == "V":
                while True:
                    shape = input("\nChoose the shape: cube(C) or rectangular prism(R) or cylinder(D) or sphere(S): ").upper().strip()
                    if shape == "C":
                        print()
                        while True:
                            try:
                                side = float(input("Enter the cube side: "))
                                print(f"The result is: {round( side ** 3 , 2 )}")
                                break
                            except ValueError:
                                print("     --- You should enter a number --- ")
                        break
                    elif shape == "R":
                        print()
                        while True:
                            try:
                                wdth = float(input("Enter the width: "))
                                break
                            except ValueError:
                                print("     --- You should enter a number --- ")
                        while True:
                            try:
                                lgth = float(input("Enter the length: "))
                                break
                            except ValueError:
                                print("     --- You should enter a number --- ")
                        while True:
                            try:
                                high = float(input("Enter the hight: "))
                                print(f"The result is: {round( wdth * high * lgth , 2 )}")
                                break
                            except ValueError:
                                print("     --- You should enter a number --- ")
                        break
                    elif shape == "D":
                        print()
                        while True:
                            try:
                                rad1 = float(input("Enter the radius: "))
                                break
                            except ValueError:
                                print("     --- You should enter a number --- ")
                        while True:
                            try:
                                high1 = float(input("Enter the hight: "))
                                print(f"The result is: {round( math.pi * high1 * ( rad1 ** 2) , 2 )}")
                                break
                            except ValueError:
                                print("     --- You should enter a number --- ")
                        break
                    elif shape == "S":
                        print()
                        while True:
                            try:
                                radc1 = float(input("Enter the radius: "))
                                print(f"The result is: {round( (4/3) * math.pi * ( radc1 ** 3 ) , 2 )}")
                                break
                            except ValueError:
                                print("     --- You should enter a number --- ")
                        break
                    else:
                        print("\n     --- You must choose ( C or R or D or S ) --- ")
                        continue
            else:
                print("\n     --- You must choose ( A or P or V ) --- ")
                continue
            break
    else:
        print("\n     --- You must choose ( A or B ) --- ")