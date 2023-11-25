from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2

def modulus(n1, n2):
    return n1 % n2

def square(n1, n2):
    return n1 ** n2

calculation_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": modulus,
    "^": square
}

def calc(user, user_op, user_pick):
    if user_op in calculation_dict:
        total = calculation_dict[user_op](float(user), float(user_pick))
        return total
    else:
        return "Invalid operator"
print(logo)

def calculator():
    user = input("What's the first number?: ")
    print("+\n-\n*\n/\n%\n^")
    user_op1 = input("Pick an operation: ")
    user_pick1 = input("What's the next number?: ")
    total1 = calc(user, user_op1, user_pick1)
    print(f"{user} {user_op1} {user_pick1} = {total1}")
    
    calc_final = False
    while not calc_final:
        continue_calc = input("Do you want to add another number? Type 'yes' or 'no': ")
        if continue_calc.lower() == 'no':
            calc_final = True
            calculator()
        elif continue_calc.lower() == 'yes':
            user_op2 = input("Pick an operation: ")
            user_pick2 = input("What's the next number?: ")
            total2 = calc(total1, user_op2, user_pick2)
            print(f"{total1} {user_op2} {user_pick2} = {total2}")
            total1 = total2


calculator()