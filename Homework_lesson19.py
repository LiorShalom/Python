def exit_program(argument): # FUNCTION FOR EXITING THE PROGRAM OR QUESTIONS.
                argument = argument.lower()
                argument = argument.strip()
                if argument == "exit()":
                    raise SystemExit

def invalid():
    print("Invalid input! Please try again...")

while True: #   MAIN SYSTEM
    try:
        def welcome():
            print("Hi!\nWelcome to Lior's homework for lesson 19!\n")
            print("\tPLEASE KEEP IN MIND!\n\tYOU CAN EXIT THE PROGRAM AT ANY TIME USING THE COMMAND - 'exit()'\n")
            
            def quest_ops():
                print("from the following options choose the question you want to view:")
                print(" [1] - question1\n [2] - question2\n [3] - question3\n")
            
            while True:
                quest_ops()
                quest_num = input("Please enter your choise: ")
                quest_num = quest_num.strip() # to remove leading and trailing whitespaces.
                exit_program(quest_num)

                if quest_num.isnumeric():
                    quest_num = int(quest_num)
                    if not quest_num in range(1, 4):
                        print("The number you entered is out of range!\n( Only numbers between 1-3 is allowed! )")
                        continue
                    elif quest_num == 1:
                        question1()
                    elif quest_num == 2:
                        question2()
                    elif quest_num == 3:
                        question3()
                    else:
                        print("WHAT???")
                        continue
                else:
                    invalid()


                
        def question1():

            # AFUNCTION THAT MAKES THE FINAL CALCULATIONS TO GET THE MAX NUMBER.
            def len_max(num_list):
                answer_no = False
                
                # checks how many numbers the user typed and prints max number.
                
                if len(num_list) == 3:

                    # prints the numbers in detail for the user.
                    print("Those are the numbers you entered:")
                    [print(f"number{i+1} = {number}") for i, number in enumerate(num_list)]
                    

                    # makes sure that the user want to use those numbers.
                    print("Are you sure you want to use them?")
                    answer_no = yes_no()
                    if answer_no:
                        return True
                    
                    # the main goal of the mission - print the max number from the three that the user provided.
                    max_num = max(num_list)
                    print(f"The maximum number is: {max_num}")
                    print("\nThats it for question number 1!\nYou can stay in this question and play with it as long as you want.")
                    print("To go back to the main page use the 'exit()' command...")
                
                

                else:
                    print("I asked for only 3 numbers!\nPlease try again...")
                    return True




            # a function that askes the user is 'yes' or 'no'.
            def yes_no():
                while True:
                    yes_no = input("Yes or No: ")
                    print("")
                    exit_program(yes_no)
                    yes_no = yes_no.strip()
                    if yes_no.isalpha():
                        if yes_no == 'y' or yes_no == 'yes':
                            return False
                        elif yes_no == 'n' or yes_no == 'no':
                            print("Ok, so try again...")
                            return True
                        else:
                            invalid()


            while True:     # QUESTION 1 SYSTEM
                try:
                    separation_symbols = " ,-/."
                    valid_characters = "1234567890"

                    print("\nWelcome to question number 1!")
                    print("In this question I need to recieve three numbers from the user and to print the max number between them.")
                    
                    while True:
                        AlphaError = False
                        
                        number = input("\nPlease enter 3 different numbers: ")
                        
                        # an option to exit the question to the main page.
                        exit_program(number)

                        number = number.strip()

                        if number.isdigit():
                            num_list = list(map(int, number))

                            # this function will check how much numbers the user typed and will make the final max calculations.
                            AlphaError = len_max(num_list)

                            if AlphaError:
                                continue


                        # will check if the input contains only numbers and separation symbols.
                        elif any(symbol in (separation_symbols + valid_characters) for symbol in number):

                            # remove symbols between the numbers and replace with spaces.
                            for symbol in separation_symbols:
                                number = number.replace(symbol, ' ')
                            
                            # split the input into seperate elements (a list of elements)
                            # it also removes leading and trailing whitespaces.
                            # each element is converted to an integer.
                            num_list = list(map(int, number.split()))

                            # this function will check how much numbers the user typed and will make the final max calculations.
                            AlphaError = len_max(num_list)

                            if AlphaError:
                                continue


                        # if the input contains invalid characters like alphabetical chracters and special symbols that has not been defined as separation symbols.
                        else:
                            invalid()
                            continue

                except SystemExit:
                    print("Exiting question 1...")
                    break   



        def question2():
            print("\nWelcome to question number 2!")
            print("In this question I need to get a number from the user and to check if the number is even or add.")

            while True:
                try:
                    number = input("\nEnter a number: ")

                    exit_program(number)

                    if number.isdigit():
                        print(f"Your input was: {number}")

                        number = int(number)

                        # if the number is divisible without a remainder.
                        if number % 2 == 0:
                            print(f"The number {number} is an even number.")
                            print("To go back to the main page use the 'exit()' command...")
                        else:
                            print(f"The number {number} is an odd number.")
                            print("To go back to the main page use the 'exit()' command...")
                    # if the input is not a number.
                    else:
                        invalid()
                        continue
                except SystemExit:
                    print("Exiting question 2...")
                    break   

        
        def question3():
            # a function to check if the input is a number or not.
            def if_number(number):
                if not number.isdigit():
                    return True

            print("\nWelcome to question number 3!")
            print("In this question I need to create a basic calculator that gets two numbers and a sign from the user.")
            print("Then te program claculates the required action.")

            while True:
                try:
                    ready_to_calculate = False
                    print("")

                    # NUMBER 1
                    while True:
                        not_number = False
                        # take first number from user.
                        number1 = input("Enter number 1: ")
                        nuumber1 = number1.strip() # clean leading and traling spaces from input.

                        # an option to exit question 3.
                        exit_program(number1)
                        not_number = if_number(number1) # checks if the input is a number or not.
                        if not_number:
                            print("Only numbers required!")
                            invalid()
                            continue
                        break
                    
                    # NUMBER 2
                    while True:
                        not_number = False
                        # take second number from user.
                        number2 = input("Enter number 2: ")
                        number2 = number2.strip() # clean leading and traling spaces from input.

                        # an option to exit question 3.
                        exit_program(number2)
                        not_number = if_number(number2) # checks if the input is a number or not.
                        if not_number:
                            print("Only numbers required!")
                            invalid()
                            continue
                        break
                    
                    number1 = int(number1)
                    number2 = int(number2)

                    # CALCULATIONS
                    while True:
                        not_sign = False
                        # a dictionary with all the calculate operation ready to use.
                        main_calculations = {
                            '+'  :  number1 +  number2,
                            '-'  :  number1 -  number2,
                            '*'  :  number1 *  number2,
                            '**' :  number1 ** number2,
                            '/'  :  number1 /  number2,
                            '//' :  number1 // number2,
                            '%'  :  number1 %  number2
                            }

                        print("Choose a calculation sign from the following:\n+, -, *, **, /, //, %")
                        calculation_sign = input("Enter operation: ")
                        calculation_sign = calculation_sign.strip()

                        # an option to exit question 3.
                        exit_program(calculation_sign)

                        # checks if the input is a valid operation.
                        if calculation_sign in main_calculations:
                            result = main_calculations[calculation_sign]
                            print("\nCalculating...")
                            print(f"{number1} {calculation_sign} {number2} = {result}")
                            break
                        else:
                            invalid()
                            continue
                    
                        break
                except SystemExit:
                    print("Exiting question 3...")
                    break   



        # call for main function.
        welcome()
    except SystemExit:
        print("Exiting the program...")
        break