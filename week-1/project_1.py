#simple interest calculator
def simple_interest(P,R,T);
A=P*(1+(R/100)*T)
return a

#example usage 
P=float(input("enter principal amount:"))
R=float(input("enter annual interest rate(%):"))
T=float(input("enter time(years):"))

A=simple_interest(P,R,T)
print(f"total amount after {T}:{}")