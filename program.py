# age =int(input("Enter your age:"))
# if age>18:
#     print("Your are eligible to vote")
# else:
#     year_left=18-age
#     print("You have to wait for "+ str(year_left)+" year to cast your vote")

# num1 = int(input("enter first number:"))
# num2 = int(input("enter second numbeer:"))
# if num1 >num2:
#     print(num1,"is greater")
# else:
#     print(num2,"is greater ")


# num = int(input("enter a number :"))
# if num%2 == 0:
#     print(num," is a even number")
# else:
#     print(num," is a odd number")


# char = input("enter any alphabet:")
# if char>="A" and char <="Z":
#     char = char.lower()
#     print("The enter character was in upper case . Its lower case  is:"+char)
# else:
#     char = char.upper()
#     print("The enter character was in lower case.Its upper case is"+char)


# ch = input("enter the sex of employee (m or f):")
# sal = float(input("enter the salary of employee:"))
# if(ch=='m'):
#     bonus = 0.05*sal
# else:
#     bonus = 0.10*sal
# amount_to_be_paid = bonus+sal
# print("Your salary is:" ,sal)
# print("You received a bonus :",bonus,"thousand")
# print("Your total salary  is ",amount_to_be_paid)


# num = int(input("enter any number:"))
# if num > 0:
#     print("Enter number is positive")
# elif num==0:
#     print("Enter number is zero")
# else:
#     print("Enter number is negative")


# ch=input("Enter any character:")
# if (ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u"):
#      print("It is a vowel")
# elif (ch=="A"or ch=="E"or ch=="I"or ch=="O"or ch=="U"):
#     print("It is a vowel")
# else:
#     print("Its not a vowel .It is a consonant")


# num1 = int(input("enter first number:"))
# num2 = int(input("enter second number:"))
# num3 = int(input("enter third number:"))
# if num1>num2 and num3:
#     print(num1,"is greater")
# elif num2>num3:
#     print(num2,"is greater")
# elif num3>num1 and num2:
#     print(num3,"is greater")
# else:
#     print("all are equal")


# x = int(input("enter number between 1 to7:"))
# if x==1:
#     print("its a sunday")
# elif x==2:
#     print("its a monday")
# elif x==3:
#     print("its a tuesday")
# elif x==4:
#     print("its a wednesday")
# elif x==5:
#     print("its a thusday")
# elif x==6:
#     print("its friday")
# elif x==7:
#     print("its a saturday")
# else:
#     print("invalid input")


# marks1 = float(input("enter first subject mark:"))
# marks2 = float(input("enter second subject mark:"))
# marks3 = float(input("enter third subject marks:"))
# marks4 = float(input("enter fourth subject marks:"))
# total = marks1+marks2+marks3+marks4
# avg=float(total)/4
# print("Total:",total,"\taggregate = ",avg)
# if avg >=75:
#     print("Distinstion")
# elif avg >=60 and avg<75:
#     print("first class")
# elif avg >=50 and avg<60:
#     print("second class")
# elif avg >=40 and avg<50:
#     print("third class")
# else:
#     print("you are fail")


# i =0
# while i<=10:
#     print(i,end=" ")
#     i+=1


# i = 0
# s = 0
# while i<=10:
#     s = s+i
#     i=i+1
# avg = float(s)/10
# print("sum of first 10 number is :",s ,"average of first 10 number is :",avg)


# i =1
# while i<=20:
#     print("*",end="")
#     i=i+1


# m = int(input("enter the value of m:"))
# n = int(input("enter the value of n:"))
# s = 0
# while m<=n:
#     s = s+m
#     m = m+1
# print("sum: ",s)


# negatives = positives = zeros =0
# print("print -1 to exit....")
# while(1):
#     num = int(input("enter any number:"))
#     if num == -1:
#         break
#     elif num == 0:
#         zeros = zeros+1
#     elif num >0:
#         positives=positives+1
#     else:
#         negatives=negatives+1
# print("count of negative number is ",negatives)
# print("count of positive number is ",positives)
# print("count of zeroes is",zeros)


# negative = 0
# negative_s = 0
# positive = 0
# positive_s = 0
# print("print -1 to exit....")
# num =int(input("enter any number:"))
# while num!=-1:
#     if num==-1:
#         break
#     elif num<0:
#         negative = negative+1
#         negative_s=negative_s+num
#     else:
#         positive = positive+1
#         positive_s = positive_s+num
#     num = int(input("enter the number: "))
# neg_avg = negative_s/negative
# pos_avg = positive_s/positive
# print("the avg of negative number is :",neg_avg)
# print("the avg of positive number is :",pos_avg)


# colors = ["red","green","yellow","blue"]
# for color in colors :
#     print(color)
#     for i in color:
#         print(i )


# for i in range(0,2001):
#     print(i)



# for i in range(0,2000):
#     print(i+1)


# i = 0
# while (i<5):
#     print(i)
#     i=i+1
# print("done with the loop")



# i = int(input("enter the number:"))
# while (i<5):
#     print(i)
#     i=i+1
# print("done with the loop")



# i = int(input("enter the number:"))
# while (i<20):
#     i = int(input("enter the number:"))
#     print(i)
#     i=i+1
# print("done with the loop")


# count = 10
# while(count > 5):
#     print(count)
#     count = count - 1


# count = 10
# while(count > 5):
#     print(count)
#     count = count - 1
# else:
#     print("i am in else")


# def func():
#     for i in range (5):
#         print("hello world")
# func()


def total (a,b):
    result=a+b
    print("sum of ",a, "and", b,"=", result)