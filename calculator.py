# Author: <Ty Wenrick>
# Assignment #2 - Calculator
# Date due: 2021-03-11
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.


#converts numbers to floats and rounds to get most accurate answer for all do_addition, subtraction etc funtions
#prints the answer in a string so that it can concat with the result messages
def do_addition():
    print()
    print("You have chosen the addition operation.")
    first_num = float(input("Enter first number: "))
    second_num = float(input("Enter second number: "))
    answer = first_num + second_num

    print("The sum is", str(round(answer, 1)) + '.')


def do_subtraction():
    print()
    print("You have chosen the subtraction operation.")
    first_num = float(input("Enter first number: "))
    second_num = float(input("Enter second number: "))
    answer = first_num - second_num

    print("The difference is", str(round(answer, 1)) + '.')


def do_multiplication():
    print()
    print("You have chosen the multiplication operation.")
    first_num = float(input("Enter first number: "))
    second_num = float(input("Enter second number: "))
    answer = first_num * second_num

    print("The product is", str(round(answer, 2)) + '.')


def do_division():
    print()
    print("You have chosen the division operation.")
    first_num = float(input("Enter first number: "))
    second_num = float(input("Enter second number: "))
    answer = first_num / second_num

    print("The result of the division of the two numbers is", str(round(answer, 2)) + '.')


#prints menu with one blank line before it
def print_menu():
    print()
    print("1) Perform addition")
    print("2) Perform subtraction")
    print("3) Perform multiplication")
    print("4) Perform division")

#checks if operation is a digit and calls apprpriate function
#else it just returns the input as a string
def do_calculation():
    user_operation_str = input("Please enter an option (1-4) or 'q' to quit: ")
    if user_operation_str.isdigit():
        user_operation = int(user_operation_str)
        if user_operation == 1:
            do_addition()
        elif user_operation == 2:
            do_subtraction()
        elif user_operation == 3:
            do_multiplication()
        elif user_operation == 4:
            do_division()
        else:
            print()
            print('That was not a valid choice. Try again.')

    return user_operation_str


#displays welcome message and displays the first menu
#while the do calculation input is a digit it will continue to print the menu and run do_calculation
def run_calculator():
    print("Welcome to the CS 1114 Calculator!")
    print_menu()

    while do_calculation().isdigit():
        print_menu()
    else:
        print()
        print('Goodbye.')


def main():
    """Runs a program for performing basic arithmetic
    operations between two numbers
    """
    # call run_calculator()
    run_calculator()


####### DO NOT REMOVE IF STATEMENT BELOW ########

if __name__ == '__main__':
    # Remove comments for next 4 lines to run doctests
    # print("Running doctests...")
    # import doctest
    # doctest.testmod(verbose=True)

    # print("\nRunning program...\n")

    main()
