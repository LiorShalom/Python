import sys

def print_result(result):
    print(f"The result is: {result}")


def exit_calculator(all_input):
    if all_input.lower() == 'exit()':
            raise SystemExit

def input_for_action(action, result):
    while True:
        number = input(f"Enter the number to {action} {result} with: ")
        exit_calculator(number)

        if number.isnumeric():
            number = int(number)
            return number
        else:
            invalid_Input()
            continue

# Actions:
def division(result):
    action = 'divide'
    result = result / input_for_action(action, result)
    print_result(result)
    return result

def multiplication(result):
    action = 'multiply'
    result = result * input_for_action(action, result)
    print_result(result)
    return result

def subtraction(result):
    action = 'subtract'
    result = result - input_for_action(action, result)
    print_result(result)
    return result

def addition(result):
    action = 'add'
    result = result + input_for_action(action, result)
    print_result(result)
    return result





def from_now_on(result):
    print("\nWhat do you wish to do now?")
    print("Enter a number from the following options: ")
    
    def available_actions():
        print("1 - Division\n2 - Multiplication\n3 - Subtraction\n4 - Addition")
    available_actions()     # prints available actions.

    while True:
        
        chosen_action = input("Enter the number of action from the list above (1-4, 5 to see the list of options again)\nYour choise: ")
        exit_calculator(chosen_action)

        if not chosen_action.isalpha() and int(chosen_action) <= 5 and int(chosen_action) >= 1:
            chosen_action = int(chosen_action)
            if chosen_action == 1:
                result = division(result)
                continue
            elif chosen_action == 2:
                result = multiplication(result)
                continue
            elif chosen_action == 3:
                result = subtraction(result)
                continue
            elif chosen_action == 4:
                result = addition(result)
                continue
            else:
                available_actions()
                continue

        else:
            invalid_Input()







def max_num(num_list):
    if num_list[0] > num_list[1] and num_list[0] > num_list[2]:
        print(f"The maximum number is: {num_list[0]}")
        result = num_list[0]
    elif num_list[1] > num_list[0] and num_list[1] > num_list[2]:
        print(f"The maximum number is: {num_list[1]}")
        result = num_list[1]
    else:
        print(f"The maximum number is: {num_list[2]}")
        result = num_list[2]
    return result



def invalid_Input():
    return print("Invalid input!\n{ If you want to exit, type 'exit()' to exit the calculator }")

def the_number(num_list):
    
    if len(num_list) == 3:
        print("you entered 3 numbers! great!")
        print("Those are the numbers you want to use?")
        [print(f"number{index+1} = {number}") for index, number in enumerate(num_list)]

        while True:
                yes_no = input("Yes or No: ")
                exit_calculator(yes_no)
                yes_no = yes_no.lower()
                yes_no = yes_no.strip()
                if yes_no == "yes" or yes_no == "y":
                    print('Ok!')
                    return False
                elif yes_no == "no" or yes_no == "n":
                    print("Ok, so enter the numbers again!")
                    return True
                else:
                    invalid_Input()
                    continue
    else:
        print("You didn't provide 3 numbers!")
        return True     # Will ask the user for new numbers.




print("Welcome to the maximum calculator!")
while True:
    try:
        num_list = []
        each_number = []
        clean_numbers = ''

        enter_again = False
        valid_input = False

        valid_characters = '1234567890 '
        
        numbers = input("Enter three different numbers: ")
        exit_calculator(numbers)
            
        numbers = numbers.strip()
        for char in numbers:
            if char in valid_characters:
                valid_input = True
            else:
                valid_input = False
                break
        if valid_input == True:
            if ' ' in numbers:
                each_number = numbers.split()
                num_list = list(map(int, each_number))

                enter_again = the_number(num_list)
                if enter_again:
                    print("ENTER AGAIN")
                    continue
                else:
                    result = max_num(num_list)
                    from_now_on(result)
            
            

            else: # if no ' ' in numbers:
                
                clean_numbers = ''.join(numbers.split())    
                num_list = list(map(int, clean_numbers))
                # the_number(num_list)
                enter_again = the_number(num_list) #checks if the input contains three numbers and asks the user if he want to continue with those numbers.
                if enter_again:
                    print("ENTER AGAIN")
                    continue
                else:
                    result = max_num(num_list)
                    from_now_on(result)
        else:
            invalid_Input()
            print("Input must contain only numbers!")
    except SystemExit:
        print("Exiting calculator...")
        break