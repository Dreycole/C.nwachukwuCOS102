#compound interest calculator
def compound_interest(P,R,n,t):
    A=P*(1+R/(n*100))**(n*t)
    return  A

    #example usage 
    P=float(input("enter principal amount:"))
    R=float(input("enter annual interest rate(%):"))
    n=int(input("enter the number of times interest is compounded per year"))
    t=float(input("enter time(years):"))

    A=compound_interest(P,R,n,t)
    print(f"total amount after{t} years:{A}")
    