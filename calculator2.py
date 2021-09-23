import math
#Hmmmmm, yes math for calculator

#Wordlists for you know, words that control what 
#operation is executed, these are self explanatory
addlist=["add","addition","plus","sum","+",]
sublist=["sub","minus","subtraction","subtract","difference","-"]
mullist=["multiply","multiplication","mult","multi","times","*"]
divlist=["divide","division","fraction","div","/",":"]
modlist=["mod","%","modulus"]
sqrtlist=["square root","sqrt","sqrrot",]
faclist=["factorial","!","fac"]
exilist=["exit","esc","sisu"]
#"sisu" is what i call an inside joke

#Defines getnumbers functions to get numbers for the calculations
def getnum0():
    num0=input("Number 0? ")
    success = True
    try:
        float(num0)
    except:
        success = False
        print("Fuck you, NaN")
        exit
    if success==True:
        num0=float(num0)
        return num0

def getnum1():
    num1=input("Number 1? ")
    success = True
    try:
        float(num1)
    except:
        success = False
        print("Fuck you, NaN")
    if success==True:
        num1=float(num1)
        return num1
    else: exit
    
#Defines the calculation functions, they are almost identical
def add(num0,num1):
    #Uses the global answ variable
    global answ
    #Sets answ to num0+num1
    answ=num0+num1

def sub(num0,num1):
    global answ
    answ=num0-num1

def mul(num0,num1):
    global answ
    answ=num0*num1

def div(num0,num1):
    global answ
    answ=num0/num1

def mod(num0,num1):
    global answ
    answ=num0%num1

def sqrt(num0):
    global answ
    #Uses the math library for the sqrt function
    answ=math.sqrt(num0)

def fac(num0):
    global answ
    #Uses the math library factorial function instead of
    #the on integrated in python (**) because fuk u
    answ=math.factorial(int(num0))

#Placeholder functions for future calculations
def l(num0,num1):
    global answ
    answ=num0-num1

def l(num0,num1):
    global answ
    answ=num0-num1
#End of placeholder functions

#Calc is set to False because no calculations 
#is succsessful (yet)
calc=False

#I felt smart when i wrote this function.
#It asks if user wants more calculation
#and exits if they don't and calculates
#more if the user wants to
def more():
    #Yes, more as function and variable,
    #what are you gonna do about it?
    more=input("More calculations (y/n)? ")
    if "y" in more: calculate()
    elif "n" in more: print("Exit");exit 

#Defines the main function, calculate(),
#this function is the brain of the operation
#and connects it all together.
def calculate():
    #Uses the global calc variable (duh)
    global calc
    
    #Requests a calculation type and and converts 
    #it to lowercase so the user can write 
    #"DiViSIoN" and get to the division function
    req=input("What calculation? ")
    req=req.lower()
    
    #Spagetthi i guess
    if req in addlist: add(getnum0(),getnum1());calc=True
    elif req in sublist: sub(getnum0(),getnum1());calc=True
    elif req in mullist: mul(getnum0(),getnum1());calc=True
    elif req in divlist: div(getnum0(),getnum1());calc=True
    elif req in modlist: mod(getnum0(),getnum1());calc=True
    elif req in faclist: fac(getnum0());calc=True
    elif req in sqrtlist: sqrt(getnum0());calc=True
    #Makes an exit from the calculation question.
    elif req in exilist: return
    
    #Checks if a calculation was succsessful
    #and if it is, prints answer and does more() 
    #and if not it says fuck you and returns to
    #calculate()
    if calc is True:
        print("The answer is:",answ)
        calc=False
        more()
    else: 
        print("Fuck you, not a calculation")
        return calculate()

#Yes, calculate
calculate()