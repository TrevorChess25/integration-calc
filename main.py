import time
_author_ = "Trevor Chessnoe"
# Professor Michael Osheroff
# Course: COP1500


'''
todo:
* fix quit value error
* dec to bin converter
* fix PEP 8 issues
    * Add descriptive paragraph below each func
    * research PEP 8 issues 
'''
'''
ways to increase robustness
* add detection for valid operators with spaces
or other formatting issues 
* add detection for use of multiple operators
'''


# tc stands for test code
def invalidBinMsg():
    print(
        "Invalid input: "
        "Some of your numbers "
        "are not binary. "
        "Please enter 0's or 1's only. "
            )


def invalidNumMsg():
    print(
        "Invalid input: Input "
        "must only contain numbers. "
        "Please enter 0's or 1's only."
            )


def binCheck(input):
    failedCheck = None
    currentChar = ""
    checkIndex = 0
    validInputs = {'0','1'}
    inputSet = set(input)
    if input == "q" or input == "Q":
        return
    # set() gets unordered list of characters
    if (inputSet != validInputs and
        inputSet != {'0'} and
        inputSet != {'1'}):
        try:
            for character in input:
                currentChar = input[checkIndex]
                int(currentChar)
                checkIndex = checkIndex + 1
            invalidBinMsg()
            failedCheck = True
            return failedCheck
        except:
            invalidNumMsg()
        failedCheck = True
    else:
        failedCheck = False
    return failedCheck
# Checks binary input for non-binary characters
# returns value to converter after assessment

def binToDec():
    binaryInput = ""
    while binaryInput != "q" and binaryInput != "Q":
        quitInfo()
        binaryInput = input("Binary value: ")
        failedCheck = binCheck(binaryInput)
        if not failedCheck:
            stringEnd = len(binaryInput) - 1
            index = stringEnd
            power = 0
            decimalValue = 0
            for binaryChar in binaryInput:
                binaryChar = binaryInput[index]
                binaryDigit = int(binaryChar)
                decimalDigit = binaryDigit * (2 ** power)
                decimalValue = (decimalValue +
                decimalDigit)
                index = index - 1
                power = power + 1
            print("Decimal value:", decimalValue)
# Reads each digit of binary input string in reverse
# Multiplies each digit by increasing powers of 2
# and adds them to the accumulator

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

    Q4 = input("7 * (4 - 2) = ")
    if int(Q4) == 14:
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

    Q7 = input("7 // 3 = ")
    if int(Q7) == -3:
        print("Correct!")
        total_pts = total_pts + 1
    else:
        print("Incorrect.")

    Q8 = input("(22*4) - 11= ")
    if int(Q8) == 87:
        print("Correct!")
        total_pts = total_pts + 1
    else:
        print("Incorrect.")

    Q9 = input("2/(11%3) = ")
    if int(Q9) == 1:
        print("Correct!")
        total_pts = total_pts + 1
    else:
        print("Incorrect.")
    return total_pts


def quitInfo():
    print("Enter 'q' to quit at any time.")

def quitMsg():
    print("Program quit successfully.")

def returnMsg():
    print("Returning to last screen")

def introMessage():
    print("Welcome to", _author_ + "'s",
          "calculator application!")
    quitInfo()
    time.sleep(2)


def basicInfo():
    print(
        "Menu Options:\n"
        "1. calculator\n"
        "2. help\n"
        "3. binary-decimal converter \n"
            )


def nameGet():
    yourName = ""
    # loops indefinitely until return
    while yourName != "q" and yourName != "Q":
        yourName = input("What is your name?: ")
        nameLength = len(yourName)
        if yourName == "q" or yourName == "Q":
            exit()
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
    menuInput = ""
    operationsList = ["+", "-", "*", "/", "**", "//",
                      "%"]
    menuOptions = ["1","2","3"]
    while menuInput != "q" and menuInput != "Q":
        # prompts the user to select a menu option
        basicInfo()
        menuInput = input("Enter 1, 2, or 3: ")
        if menuInput == menuOptions [0]:
            print(yourName, "entered CALC mode. ")
            calculator(operationsList)
        # If the user inputs the word 'help'
        # they receive information on operators
        # used if bc elif never allows help to run
        elif menuInput == menuOptions [1]:
            print(yourName, "entered HELP mode")
            quitInfo()
            calcHelp(operationsList)
        elif menuInput == menuOptions [2]:
            print(
                yourName,
                  "entered binary converter.\n"
                  "Please enter "
                  "numbers that only contain"
                  " zeroes or ones"
                  )
            # goes to function for binary input
            binToDec()
        elif menuInput == "q" or menuInput == "Q":
                quitMsg()
        else:
            print("Invalid option: "
                  "Please type 1, 2, or 3\n")
    return operationsList

def main():
    introMessage()
    yourName = nameGet()
    calcMenu(yourName)
# displays greeeting
# gets name with nameGet function

def dotCheck(string,validList):
    if "." in string:
        if any(elements in string for elements in validList):
            print("Invalid Format: Try typing that again"
                  " without a dot.\n")
            print("updated vbf to true")
        else:
            print("Invalid option: Please try again.\n")


def bracketCheck(string,validList):
    invalidMsgDisplayed = False
    if "[" or "]" in string:
        if any(elements in string for elements in validList):
            print("Invalid Operator: Try typing that again"
                  " without brackets.\n")
            # print("updated vbf to true")
        else:
            print("Invalid Operator and"
                  " Formatting: Please try again.\n")
            # print("updated vbf to false")
        invalidMsgDisplayed = True
    return invalidMsgDisplayed
    # Checks if the input contains square brackets
    # and if the input contains a valid operator
    # If both conditions are true,
    # Ask the user to remove the brackets
    # If the input contains brackets but does NOT
    # contain a valid operator then
    # print a different message
    # Creates variable to make sure multiple
    # error messages are not displayed


def calcHelp(operationsList):
    help_operator = None
    operationsList = ["+", "-", "*", "/", "**", "//",
                      "%"]
    while help_operator != "q" and help_operator != "Q":
        print(
            "Which operator would you like to know "
              "more about?"
                )
        print("[+] [-] [*] [/] [**] [//]")
        help_operator = input("Enter your choice: ")
        invalidMsgDisplayed = bracketCheck(
            help_operator, operationsList)
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
            if not invalidMsgDisplayed:
                print("Invalid Operator: "
                      "Please try again.\n ")


def calculator(operationsList):
    strNum1 = ""
    strNum2 = ""
    result = "no result"
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
        bracketCheck(calcOperator,
                     operationsList, )
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
            elif calcOperator not in operationsList:
                print("Invalid Operator: Please try again.")
                return
        # if user tries to divide by zero call zeroDiv
        except ZeroDivisionError:
            zeroDiv(num1)
        print(result)
    calcMenu(yourName)


def zeroDiv(num1):
    #Gets input numerator from ZeroDivisionError
    invalid_num = str(num1) + "/" + "0" + "."
    print(
        invalid_num, "Error: Divide by Zero\n"
                       "Activating "
                       "ENJOYABLE DIVERSION", sep = ""
            )
    # creates five dots in three seconds
    for iteration in range(5):
        print(".", end = "")
        time.sleep(0.4)
    # assigns number of correct answers to return
    # of quiz function
    print("\nThis quiz has 10 questions. \n "
          "There is no time limit.\n "
          "All answers are whole numbers.\n "
          "Good luck!")
    total_pts = calcQuiz()
    print("You got", total_pts, "/ 10 answers correct")
    return
#call to main
main()
