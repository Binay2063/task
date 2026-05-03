#1
n= int(input("Enter a number: "))
if n>0 and n<=100:
    print("The number is between 1 and 100.")
else:
    print("The number is not between 1 and 100.")

#2
n= int(input("Enter a number: "))
if n %2 ==0:
    print("The number is even.")
else:
    print("the number is odd")

#3
n= int(input("Enter a month number: "))
if n==1:
    print("january")
elif n==2:
    print("february")
elif n==3:
    print("march")
elif n==4:
    print("april")
elif n==5:
    print("may")
elif n==6:
    print("june")
elif n==7:
    print("july")   
elif n==8:
    print("august") 
elif n==9:
    print("september")
elif n==10:
    print("october")
elif n==11:
    print("november")   
elif n==12:
    print("december")
else:
    print("invalid month number")

#anotehr way
months = {1:"january", 2:"february", 3:"march", 4:"april", 5:"may", 6:"june", 7:"july", 8:"august", 9:"september", 10:"october", 11:"november", 12:"december"}
n = int(input("Enter a month number: "))
if n in months:
    print(months[n])
else:
    print("invalid month number")

#4
n= int(input("Enter your marks: "))
if n < 25:
    print("grade : F")
elif n>=25 and n<45:
    print("grade : E")
elif n>=45 and n<50:
    print("grade : D")
elif n>=50 and n<60:
    print("grade : C")
elif n>=60 and n<80:
    print("grade : B")
elif n>=80 and n<=100:
    print("grade : A")
else:
    print("invalid marks")

#5
n = int(input("Enter a number: "))
if n % 7 == 0:
    print("The number is divisible by 7.")
else:   
    print("The number is not divisible by 7.")

