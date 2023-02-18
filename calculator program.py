operator = input("Enter An Operator ")
num1=int(input("Enter a Number "))
num2=int(input("Enter Another Number "))
#calculations
if operator=="+":
 result= num1+num2
 print(result)
elif operator=="-":
 result=num1-num2
 print(result)
elif operator=="*":
 result=num1*num2
 print(result)
elif operator=="/":
 result=num1/num2
 print(result)

else:
 print(f"{operator}Is Not a Valid Operator")


