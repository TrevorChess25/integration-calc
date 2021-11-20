import time

_author_ = "Trevor Chessnoe"
# Professor Michael Osheroff
# Course: COP1500


'''
todo: 
* fix PEP 8 issues
    * Add descriptive paragraph below each func
    * research PEP 8 issues 
* add means of exiting 
    * to last func
* if yourName is q prompt user if that is their name
    or if they want to quit
* fix broken and unncessary returns
* add try-excepts for invalid inputs 
* add decimal to binary converter
* add time open counter
'''


# tc stands for test code
# Main calculator interface:
# Looks at user input for 4 strings.
# Use 'calc' to use the calculator
# or 'help' for more information
# or 'bin' for binary decimal conversion
# Entering 'q' quits the program


####bin-dec converter defs#####
def strToList(string):
    # initializes index value
    index = 0
    List = []
    # converts string length to an int b4 iterating
    str_length = len(string)
    for index in range(str_length):
        str_index = string[index]
        List.append(str_index)
        index = index + 1
    return List


def binToDec(List):
    # initializes accumulator
    deci_total = 0
    # power of right most digit is 0
    power = 0
    # number of for loop executions
    iterations = 0
    # starts one before last character
    index = len(List) - 1
    for digit in List:
        # sets digit to value of integer at 1st index
        listDigit = int(List[index])
        # transforms list values so they can be added
        decDigit = listDigit * (2 ** power)
        # adds converted values to accumulator
        deci_total = deci_total + decDigit
        # decrements index of binList
        index = index - 1
        # increments exponent
        power = power + 1
    print("Decimal value:", deci_total)
    # returns to call in binGet
    return


def binGet():
    # initialize variables used in binGet
    binInput = ""
    isNum = "True"
    isBinary = "True"
    # Loop until user inputs "q"
    while binInput != "q" and binInput != "Q":
        binInput = input("Enter binary number or "
                         "enter 'q' to quit: ")
        # when the user types q return to last call
        # (in calcMenu)
        if binInput == "q" or binInput == "Q":
            return
        # converts binary input string into list,
        # assigns to List
        List = strToList(binInput)
        # if any item in the list cannot be converted
        # to an integer isNum is set to "False"
        try:
            index = 0
            numcheck = List[index]
            for item in List:
                int(numcheck)
                index = index + 1
        except:
            isNum = "False"
        # if a number that is NOT 0 or 1 is in the List
        # then the number is not binary
        if not "0" or not "1" in List:
            isBinary = "False"
            # if a list contains a non-number and
            # non-binary digit
            # ask for only numbers
            if isNum == "False" and isBinary == "False":
                print("Invalid input: Input "
                      "must only contain numbers. "
                      "Please enter 0's or 1's only.")
            # if a list only contains numbers but some
            # are not binary
            # ask for only binary input
            elif isNum == "True" and isBinary == "False":
                print("Invalid input: "
                      "Some of your numbers "
                      "are not binary.\n"
                      "Please enter 0's or 1's only. ")
        else:
            # print(List) #tc
            # convert list from binGet into decimal
            binToDec(List)


#### end of bin-dec converter defs#####

def calcQuiz():
    # total_pts is number of correct answers
    total_pts = 0
    Q1 = input("2 +10 = ")
    if int(Q1) == 12:
        print("Correct!")
        total_pts = total_pts + 1
    else:
        print("Incorrect.")

    Q2 = input("12 % 5 = ")
    if int(Q2) == 2:
        print("Correct!")
        total_pts = total_pts + 1
    else:
        print("Incorrect.")

    Q3 = input("17 // 2 = ")
    if int(Q3) == 8:
        print("Correct!")
        total_pts = total_pts + 1
    else:
        print("Incorrect.")

    Q4 = input("7 * 4 -2 = ")
    if int(Q4) == 26:
        print("Correct!")
        total_pts = total_pts + 1
    else:
        print("Incorrect.")

    Q5 = input("2**5 = ")
    if int(Q5) == 32:
        print("Correct!")
        total_pts = total_pts + 1
    else:
        print("Incorrect.")

    Q6 = input("144**1/2 = ")
    if int(Q6) == 12:
        print("Correct!")
        total_pts = total_pts + 1
    else:
        print("Incorrect.")

    Q7 = input("(6 -14) // 3 = ")
    if int(Q7) == -3:
        print("Correct!")
        total_pts = total_pts + 1
    else:
        print("Incorrect.")

    Q8 = input("22*4-11//10 = ")
    if int(Q8) == 87:
        print("Correct!")
        total_pts = total_pts + 1
    else:
        print("Incorrect.")

    Q9 = input("(8%3)/(50%3) = ")
    if int(Q9) == 1:
        print("Correct!")
        total_pts = total_pts + 1
    else:
        print("Incorrect.")
    return total_pts


def quitInfo():
    print("Enter 'q' to quit at any time.")


def introMessage():
    print("Welcome to", _author_ + "'s",
          "calculator application!")
    quitInfo()
    time.sleep(2)


def basicInfo():
    print("Type 'calc' to switch to calculator mode.\n"
          "Type 'help' for information.\n"
          "Type 'bin' for a decimal-binary converter.\n")


def nameGet():
    yourName = ""
    # loops indefinitely until return
    while yourName != "q" and yourName != "Q":
        yourName = input("What is your name?: ")
        nameLength = len(yourName)
        if yourName == "q" or yourName == "Q":
            return
        if nameLength <= 0:
            print("I didn't catch that.\n"
                  "Please try again.")
        elif nameLength == 0 or nameLength >= 22:
            print("Too long to display.\n "
                  "Enter a shorter name")
        else:
            print("Hello", yourName + "!" + "\n")
            return yourName


def calcMenu(yourName):
    calcInput = ""
    while calcInput != "q" and calcInput != "Q":
        # prompts the user to select a menu option
        basicInfo()
        calcInput = input("Enter your choice: ")
        if calcInput == "calc":
            print(yourName, "entered CALC mode. ")
            regCalc()
        # If the user inputs the word 'help';
        # they receive information on operators
        # used if bc elif never allows help to run
        if calcInput == "help":
            print(yourName, "entered HELP mode")
            quitInfo()
            calcHelp()
        if calcInput == "bin":
            print(
                yourName,
                  "entered binary converter.\n"
                  "Please only enter "
                  "numbers that contain zeroes or ones "
                  )
            # goes to function for binary input
            binGet()
        elif calcInput == "q" or "Q":
            return
        else:
            print("Invalid option: Please try again.")


def main():
    # assigns return of nameGet to variable in
    # scope where it is used
    introMessage()
    yourName = nameGet()
    calcMenu(yourName)


def calcHelp():
    help_operator = ""
    while help_operator != "q" and help_operator != "Q":
        print(
            "Which operator would you like to know "
              "more about?"
                )
        print("[+] [-] [*] [/] [**] [/]")
        help_operator = input("Enter your choice: ")
        if help_operator == "+":
            print("(+) addition:",
                  "The sum of the numbers is taken.")
        elif help_operator == "-":
            print("(-) subtraction:",
                  "The difference of the numbers is taken.")
        elif help_operator == "*":
            print("(*) multiplication:",
                  "The product of the numbers is taken.")
        elif help_operator == "**":
            print(
                "(**) exponentiation:",
                "The first number is multiplied by itself;\n",
                "the number of times is determined\n",
                "by the next number.")
        elif help_operator == "/":
            print("(/) division:",
                  "The quotient of the numbers is taken.")
        elif help_operator == "//":
            print(
                "(//) floor division:",
                "The quotient is taken and rounded down"
                "to the nearest integer.\n"
                "In effect, this excludes the remainder.")
        elif help_operator == "%":
            print(
                "(%) modulus: The quotient is"
                "calculated, but ONLY the remainder"
                "is taken."
                    )
        elif help_operator == "q" or help_operator == "Q":
            return
        else:
            print(
                "Invalid Operator: Please try again.")
    print("\n")


def regCalc():
    strNum1 = ""
    strNum2 = ""
    result = 0
    while strNum1 != "q" and strNum2 != "q":
        quitInfo()
        strNum1 = (input("\n""Enter first number: "))
        if strNum1 == "q" or strNum1 == "Q":
            return
        try:
            num1 = int(strNum1)
        except:
            print("Invalid input: Only enter whole "
                  "numbers.")
            return
        calcOperator = input("Enter the operation: ")
        strNum2 = input("And the second number?: ")
        if strNum2 == "q" or strNum2 == "Q":
            return
        try:
            num1 = int(strNum1)
        except:
            print("Invalid input: Only enter whole "
                  "numbers.")
            return
        num2 = int(strNum2)
        try:
            if calcOperator == "+":
                result = num1 + num2
            elif calcOperator == "-":
                result = num1 - num2
            elif calcOperator == "*":
                result = num1 * num2
            elif calcOperator == "/":
                result = num1 / num2
            elif calcOperator == "**":
                result = num1 ** num2
            elif calcOperator == "//":
                result = num1 // num2
            elif calcOperator == "%":
                result = num1 % num2
            else:
                print("Invalid operator: Please try again.")
        # if user tries to divide by zero call zeroDiv
        except ZeroDivisionError as e:
            zeroDiv(num1)
        print(result)
    calcMenu(yourName)


def zeroDiv(num1):
    #Gets input numerator from ZeroDivisionError
    invalid_num = str(num1) + "/" + "0" + "."
    print(
        invalid_num, "Error: Divide by Zero\n"
                       "Activating "
                       "ENJOYABLE DIVERSION.exe\n",
          sep = "")
    # creates five dots in three seconds
    for iteration in range(5):
        print(".")
        time.sleep(0.6)

    # assigns number of correct answers to return
    # of quiz function
    total_pts = calcQuiz()
    print("You got", total_pts, "/ 10 answers correct")
    return
#call to main
main()
