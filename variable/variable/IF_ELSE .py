#Q.1 3 greatest number

A=25
B=35
C=15
if(A>B):
    print("A is greater number")
elif(B>C):
    print("B is greater number")
else:
    print("c is greater number") 

          
# Q 2. TWO MAXIMUM NUMBER
num=int(input("enter a number"))
Num=int(input("enter a number"))
if(Num>num):
    print(Num,"is maximum number")
else:
    print(" num is not maximum number")    


#Q.3 3 GREATEST NUMBER
A=int(input("enter a number"))
B=int(input("enter a number"))
C=int(input("enter a number"))
if(A>B):
    print("A is greater number")
elif(B>C):
    print("B is greater number")
elif(C>A):
    print("C is greater number ")
else:
    print(" number is equal")   

#Q4.THE NUMBER IS POSITIVE,NEAGETIVE OR zero
a=int(input("enter any number"))
if a>0:
   print("the number is positive ")
elif a<0:
   print("the number is negative ")
else:
    print("the number is zero")     

#Q5. THE  NUMBER IS DIVISIBLE BY 5 AND 11 OR NOT
number=int(input("enter any positive number"))
if(number%5==0) and (number%11==0):
    print("given number is divisible by 5 and 11")
else:
    print("given number is not divisible by 5 and 11")    

#Q6. EVEN  OR ODD NUMBER
a=int(input("enter a number"))
if(a%2==0):
    print("the number is even")
else:
    print("number is odd")  

#Q7.YEAR IS LEAP YEAR OR NOT
year=int(input("enter a year"))
if(year%4==0):
   print("this year is leap  year")
elif(year%400==0):
    print("this year is leap  year")
elif(year%100==0):
    print("this year is leap  year")
else:
    print("year is not leap year")    

#Q8 .THE CHARACTER IS AN ALPHABET OR NOT
char=(input("enter any alphabet :"))
if(char>='a' and char<='z') or (char>='A' and char<='Z'):
  print("The character is an alphabet")
else:
    print("The character is not an alphabet")



#Q9.THE CHARACTER IS AN OVEL OR NOT
char=input("enter any charater")
if(char=='a' or char=='e' or char=='i' or  char=='o' or char=='u'):
    print("the character is ovel")
else:
    print("character is not ovel")



#Q10 ALPHABET IS UPPERCASE OR LOWER CASE
char=input("enter any alphabet")
if(char>='A' and char<='Z'):
    print("the alphabet is in upper case")
else:
    print("the alphabet is in lower case")


#Q11. WEEKDAY CODE
day=input("enter any day\n")
if(day=="monday"):
    print("rajma chawal")
elif(day=="tuesday"):
     print("pav bhaji") 
elif(day=="wednesday"):
       print("biryani")
elif(day=="thursday"):
  print("palak panir")
elif(day=="friday"):
   print("chole bature")
elif(day=="saturday"):
   print("litti chokka")
else:
   print("poha")

    


          

#Q12.SALARY AND YEAR SERVICE
salary=int(input("enter your salary:"))
years=int(input("enter years of service"))
if(years>5):
  print("your salary(+bonus)=",salary+(salary)*5/100)
else:
  print("no bonus")


#Q13.LENGTH AND BREADTH REACTANGLE  FROM USER AND CHECK IT IS SQUARE OR NOT.
length=int(input("enter length"))
breadth=int(input("enter breadth"))
if(length==breadth):
  print("it is square")
else:
  print("it is not a square")  



#Q14.TWO NUMBER GREATEST NUMBER
num1=input("enter first number")
num2=input("enter second number")
if(num1>num2):
  print("first number is greatest")
elif(num1<num2):
  print("second number is greatest")
else:
  print("both number are equal")

#Q15.ARMSTRONG OR NOT
num=int(input("enter the choice 1 to 12"))
sum=0
if temp==num:
  print(num,"is armstrong number")
else:
  print(num," is not armstrong number")



#Q16.GIRLS 
room=int(input("enter the number"))
if room==12:
  print("no beds")
elif( room<12):
   print("need girls")
else:
   print("less girl")

#Q17.OUTPUT
num=int(input("enter a number"))
if num%5==0:
   print("hello")
else:
   print("bye")   


#Q18.ELECTRIC UNIT
amt=0
nu=int(input("enter number electric unit"))
if nu<=100:
  amt=0
if nu>100 and nu<=200: 


#Q19. CALCULATOR
num1=int(input("enter your first number:"))
num2=int(input("enter your second number:"))
oper=(input("enter any operator:"))
if oper=='+' or oper=="addition":
   print(num1+num2)
elif oper=='-' or oper=="substraction":
   print(num1-num2)
elif oper =='*' or oper=="multiplication":
   print(num1*num2)
elif oper=='/' or oper== "division":
   print(num1 / num2)
else:
   print("enter valid operator")

num=int(input("enter any number :"))
print("the last digit of number :",num%10)


#Q20.REVERSE NUMBER
num=int(input("enter the number"))
A=num%10
B=(num//10)%10
C=(num//100)%10
D=(num//1000)%10
name=(A*1000)+(B*100)+(C*10)+(D*1)
if num>0:
    print(name)


#Q21.bike price
Tax=0
pr=int(input("enter the price of bike:" ))
if pr>100000*pr:
    tax=15/100*pr
elif pr>50000 and pr<= 10000:
     tax=10/1000*pr
else:
    tax=5/100*pr
    print("tax to be paid",tax)



