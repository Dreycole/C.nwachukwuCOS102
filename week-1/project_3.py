# Annuity Plan Calculator
def annuity_plan(PMT, R, n, t):
    R_decimal = R / (n * 100)  # Convert percentage to decimal
    A = PMT * (((1 + R_decimal)**(n * t) - 1) / R_decimal)
    return A

# Example Usage
PMT = float(input("Enter Periodic Payment: "))
R = float(input("Enter Annual Interest Rate (%): "))
n = int(input("Enter Number of Payments per Year: "))
t = float(input("Enter Total Years: "))

A = annuity_plan(PMT, R, n, t)
print(f"Future Value of Annuity after {t} years: {A}")
