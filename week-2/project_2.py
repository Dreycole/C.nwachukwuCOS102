import numpy as np

def solve_quadratic():
    print("\nSolving Quadratic Equation (Ax² + Bx + C = 0)")
    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = float(input("Enter C: "))

    roots = np.roots([a, b, c])
    print("Roots of the quadratic equation:", roots)

def solve_cubic():
    print("\nSolving Cubic Equation (Ax³ + Bx² + Cx + D = 0)")
    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = float(input("Enter C: "))
    d = float(input("Enter D: "))

    roots = np.roots([a, b, c, d])
    print("Roots of the cubic equation:", roots)

def solve_quartic():
    print("\nSolving Quartic Equation (Ax⁴ + Bx³ + Cx² + Dx + E = 0)")
    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = float(input("Enter C: "))
    d = float(input("Enter D: "))
    e = float(input("Enter E: "))

    roots = np.roots([a, b, c, d, e])
    print("Roots of the quartic equation:", roots)

# Main menu
while True:
    print("\nChoose an equation type to solve:")
    print("1. Quadratic (Ax² + Bx + C = 0)")
    print("2. Cubic (Ax³ + Bx² + Cx + D = 0)")
    print("3. Quartic (Ax⁴ + Bx³ + Cx² + Dx + E = 0)")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        solve_quadratic()
    elif choice == "2":
        solve_cubic()
    elif choice == "3":
        solve_quartic()
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please select 1, 2, 3, or 4.")
