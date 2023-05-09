"""
i have a menu for the test navigate to the desired module
and then to the desired task

function for testing each module is seperate and i have a function 
to check if the input is an int

i didnt create a function for col.py because it is just 3 line of print
"""

import number.comp
import number.simp   #importing the modules
import col

def isInt(num):   #checking if the input is an int
    try: 
        int(num)
        return num
    except: 
        return "invalid input", menu() #if not an int return to menu

def comp():
    while True: #created a loop to have it on repeat
        print("to test sum_of_digits press 1")
        print("to test isPal press 2")
        task_choice = input()

        if task_choice == "1":
            num = input("type a number to calculate the sum of its digits: ")
            isInt(num)
            print(f'the sum of {num} is {number.comp.sum_of_digits(num)}')
            menu() #going back to menu after test
        elif task_choice == "2":
            num = input("type a number to check if its a palindrome: ")
            isInt(num)
            print(number.comp.isPal(num))
            menu() #going back to menu after test
        else:      #if the input isn't 1 or 2 it's not valid and will return to the beginning of the loop
            print("invalid input")

def simp():
    while True: #created a loop to have it on repeat
        print("to test addition press 1")
        print("to test subtraction press 2")
        task_choice = input()

        if task_choice == "1":
            num1 = input("num1 = ")
            num2 = input("num2 = ")
            isInt(num1)
            isInt(num2)
            print(f'{num1} + {num2} = {number.simp.add(num1,num2)}')
            menu() #going back to menu after test
        elif task_choice == "2":
            num1 = input("num1 = ")
            num2 = input("num2 = ")
            isInt(num1)
            isInt(num2)
            print(f'{num1} - {num2} = {number.simp.sub(num1,num2)}')
            menu()  #going back to menu after test
        else:       #if the input isn't 1 or 2 it's not valid and will return to the beginning of the loop
            print("invalid input") 

def menu():
    while True: #created a loop to have it on repeat
        print("to test simp.py press 1")
        print("to test comp.py press 2")
        print("to test col.py press 3")
        module_choice = input()

        if module_choice == "1":
            simp() #calling the simple function
        elif module_choice == "2":
            comp() #calling the comp function
        elif module_choice == "3":
            print(f'array 1:{col.array1_index}')
            print(f'array 2:{col.array2_names}')
            print(f'zipped array:{col.myzip(col.array1_index, col.array2_names)}')
            menu()
        else:
            print("invalid input")

if __name__ == "__main__":
    menu()