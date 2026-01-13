import math

def factorial():
    n = int(input("Enter a number: "))
    print("Factorial: ", math.factorial(n))
    print("==============================")


def compound_interest():
    p = float(input("Principal: "))
    r = float(input("Rate (in %): "))
    t = float(input("Time (in Years): "))
    ci = p * (1 + r/100) ** t
    print("Compound interest: ", round(ci, 2))
    print("==============================")


def trigonometry():
    angle = math.radians(float(input("Angle: ")))
    print("sin: ", math.sin(angle))
    print("cos: ", math.cos(angle))
    print("==============================")


def area_shapes():
    r = float(input("Radius: "))
    print("Area of Circle: ", math.pi * r * 2)
    print("==============================")


def math_menu():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        ch = int(input("Enter your choice: "))
        if ch == 1:
            factorial()
        elif ch == 2:
            compound_interest()
        elif ch == 3:
            trigonometry()
        elif ch == 4:
            area_shapes()
        elif ch == 5:
            break