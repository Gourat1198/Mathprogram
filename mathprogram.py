#my first python project, a Single-operation mathematical program.

import math
import sys
from fractions import Fraction
#importing standard python libary

print("this is a computer program that provides necessary solutions to mathematical problems".upper())

#this program perform a single operation at a time, operation precedences/multiple operations like BODMAS,PEDMAS are not supported

#THIS PROGRAM IS BASICALLY A CHAIN OF IF STATEMENT, SINCE PYTHON IS AN INTERPERTED LANGUAGE, PY WILL CHECK EVERY STATEMENT FOR A TRUE CONDITION, THEN IF NO CONDITION IS MET PY WILL END THE PROGRAM

operation=input("which operation will you like to perform, please input the operation name in full, e.g addition for (+): ")

#special operations:
if operation=="constant":
    X=input("enter constant: ".title())
    if X=="π":
        print(math.pi)
    if X=="e":
        print(math.e)
    if X=="g":
        print(3*math.pi+0.4)    
    exit()

if operation =='area of circle':
    try:        
        radius=int(input("enter the radius of the circle: ".title()))        
        print(math.pi*radius**2)
    except ValueError:
        print("enter a valid number for radius of circle")
    exit()
     
if operation =='area of triangle':
    try:        
        height=int(input("enter the height of the triangle: ".title()))
        base=int(input("enter base length of the triangle: ".title()))        
        print(0.5*base*height)
    except ValueError:
        print("enter a parmeters for the area of the triangle")
    exit()
    
if operation =='area of rectangle':
    L=int(input("enter the length of the circle: ".title()))
    W=int(input("enter the width of the rectangle: ".title()))
    print(L*W)
    exit()

if operation=='area of square':
     square_length=int(input("enter the square length".title()))
     print(square_length**2)
     exit()

#quadratic equation
if operation=="function-quadratic":
    try:
        ax=int(input("enter the value of a: "))
        bx=int(input('enter the value of b: '))
        cx=int(input("enter the value of c: "))
        print('x1: ',(-bx+((bx**2 -4*ax*cx)**0.5))/(2*ax))
        print('x2: ',(-bx-((bx**2 -4*ax*cx)**0.5))/(2*ax))
    except ValueError:
        print("enter a valid number")  
    exit() 

#simultaneous-equation
if operation=="simultaneous-equation":
    try:
        x_1=float(input('enter coefficent of x in the first equation: '))
        y_1=float(input('enter coefficent of y in the first equation: '))
        c_1=float(input('enter constant of the first equation: '))
        x_2=float(input('enter coefficent of x in the second equation: '))
        y_2=float(input('enter coefficent of y in the second equation: '))
        c_2=float(input('enter constant of the second equation: '))
    except ValueError:
        print("enter valid number")

#complex number operations
if operation=="complex-addition":
   try:
      num1=complex(input("enter any complex number: ".title()))
      num2=complex(input("enter any complex number: ".title()))
      print(num1+num2)
   except ValueError:
      print("please enter a valid number: ".title())  
   exit()
if operation=="complex-subtraction":
   try:
      num1=complex(input("enter any complex number: ".title()))
      num2=complex(input("enter any complex number: ".title()))
      print(num1-num2)
   except ValueError:
      print("please enter a valid number: ".title())  
   exit()
if operation=="complex-multiplication":
   try:
      num1=complex(input("enter any complex number: ".title()))
      num2=complex(input("enter any complex number: ".title()))
      print(num1*num2)
   except ValueError:
      print("please enter a valid number: ".title())  
   exit()
if operation=="complex-polar":
   try:
      real_part=int(input("enter the real part of the complex number: ".title()))
      img_part=int(input("enter the imginary part of the complex number: ".title()))
      print("calculating modulus.....")
      print('modulus: ',((real_part)**2 + (img_part)**2)**0.5)
   except ValueError:
      print("enter a valid number".title())
   mod_=((real_part)**2 + (img_part)**2)**0.5
   arg=math.atan(img_part/real_part) 
   print(f"{mod_}(cos {arg} + jsin {arg})")
   exit()
        
#matrix program 
if operation=="matrix":   
    matrix_order=str(input("enter order: "))  
    if matrix_order in ['1x1','1x2','1x3','2x1','2x2','2x3','3x1','3x2','3x3']:
        matrix_operation=input('which operation: ')
        if matrix_operation=="determinant":
            matrix_operation_order=matrix_order
            if matrix_operation_order=="2x2":
                num1_1=int(input("enter value for row1,column1: "))
                num1_2=int(input("enter value for row1,column2: "))
                num2_1=int(input("enter value for row2,column1: "))
                num2_2=int(input("enter value for row2,column2: "))
                print((num1_1*num2_2)-(num1_2*num2_1))
    else:
       print("enter a square matrix or a matrix that does not exceed the limit of order of 3x3")

#Arithemic sequence operation                       
if operation=="sequence":    
    first_term=int(input('enter the first term of the sequence: '.title()))
    d=int(input("enter common difference: ".title()))
    try:                            
      n=int(input("enter the first nth value: "))
    except ValueError:
        print("enter a valid number")
    while n<=20: 
        term=first_term+(n-1)*d
        print(f"{n} term:",term)
        n+=1      

#Boolean Operation                        
if operation=="boolean":                                                     
 boolean_operator=input("enter AND/OR : ")
 if boolean_operator=="AND":
    input_1=int(input("enter first input: "))
    input_2=int(input("enter second input: "))
    if -1<= input_1>=2:
        print("enter correct boolean variable")
    elif-1<=input_2>=2:
        print("enter correct boolean variable")
    else:
        print("output: ",input_1 and input_2)   
 if boolean_operator=="OR":
    input_1=int(input("enter first input: "))
    input_2=int(input("enter second input: "))
    if -1<= input_1>=2:
        print("enter correct boolean variable")
    elif-1<=input_2>=2:
        print("enter correct boolean variable")
    else:
        print('output: ',input_1 or input_2) 
 exit()             

#counting whole numbers
if operation=="count":
    try:
        first_count=int(input("enter the first number of your count: ".title()))
        Last_count=int(input("enter the last number of your count: ".title()))
    except ValueError:
        print("Enter a whole number")
    while first_count<=Last_count:
        print(first_count)
        first_count+=1  
    exit()          

#program for simple arithmetic operations
if operation=="addition":
 try:
    num1=int(input("enter first number of operation: "))
    num2=int(input("enter first number of operation: "))
    print(num1+num2)
 except ValueError:
    print("please enter a valid number")
 exit()
if operation=="subtraction":
 try:
    num1=int(input("enter first number of operation: "))
    num2=int(input("enter first number of operation: "))
    print(num1-num2)
 except ValueError:
    print("please enter a valid number")
 exit()
if operation=="multiplication":
 try:
    num1=int(input("enter first number of operation: "))
    num2=int(input("enter first number of operation: "))
    print(num1*num2)
 except ValueError:
    print("please enter a valid number")
 exit()
if operation=="division":
 try:
    num1=int(input("enter first number of operation: "))
    num2=int(input("enter first number of operation: "))
    print(num1/num2)
 except ValueError:
    print("please enter a valid number")
 exit()
if operation=="Power":
 try:
    num1=int(input("enter first number of operation: "))
    num2=int(input("enter first number of operation: "))
    print(num1**num2)
 except ValueError:
    print("please enter a valid number")
 exit()
if operation=="power root":
 try:
    num1=int(input("enter first number of operation: "))
    num2=int(input("enter first number of operation: "))
    print(num1**(1/num2))
 except ValueError:
    print("please enter a valid number")
 exit()
if operation=="modulus":
 try:
    num1=int(input("enter first number of operation: "))
    num2=int(input("enter first number of operation: "))
    print(num1%num2)
 except ValueError:
    print("please enter a valid number")
 exit()

#program ends if no registered operation is inserted 
else:
       print(f"{operation}, is not an available operation currently in this program,")
       print("kindly input 'request-list' to see all available operation input")

       
 
 