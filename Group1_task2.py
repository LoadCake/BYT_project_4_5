import re
states = {"menu", "emailChecking", "PESELChecking", "AlphanumericChecking", "NameChecking", "exit"} #purely for informational purposes

state = "menu"

def menu():
    global state
    while state == "menu":
        print("Choose the mode (enter the number):","\n1. Check for Email", "\n2. Check for PESEL", "\n3. Check for Alphanumeric", "\n4. Check for a Name", "\n0.Exit")
        choice = int(input())
        if choice == 1:
            state = "emailChecking"
        elif choice == 2:
            state = "PESELChecking"
        elif choice == 3:
            state = "AlphanumericChecking"
        elif choice == 4:
            state = "NameChecking"
        elif choice == 0:
            state = "exit"
        else:
            print("please choose a correct option")

def checkEmail():
    global state
    while state == "emailChecking":
        word = input("enter a word to check\n")
        print("The result is:",True if re.search("""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""", word) is not None else False,".Type \"1\" to continue checking or \"0\" to go back to menu")
        if int(input()) == 0:
            state = "menu"

def checkPESEL():
    global state
    while state == "PESELChecking":
        word = input("enter a word to check\n")
        print("The result is:", True if re.search("""^\d{11}$""", word) is not None else False, ".Type \"1\" to continue checking or \"0\" to go back to menu")
        if int(input()) == 0:
            state = "menu"

def checkAlphanumeric():
    global state
    while state == "AlphanumericChecking":
        word = input("enter a word to check\n")
        print("The result is:", True if re.search("""^[A-Za-z0-9]+$""", word) is not None else False, ".Type \"1\" to continue checking or \"0\" to go back to menu")
        if int(input()) == 0:
            state = "menu"

def checkName():
    global state
    while state == "NameChecking":
        word = input("enter a word to check\n")
        print("The result is:",True if re.search("""^[A-Z][a-z]*$""", word) is not None else False,".Type \"1\" to continue checking or \"0\" to go back to menu")
        if int(input()) == 0:
            state = "menu"


while state != "exit":
    if state == "menu":
        menu()
    elif state == "emailChecking":
        checkEmail()
    elif state == "PESELChecking":
        checkPESEL()
    elif state == "AlphanumericChecking":
        checkAlphanumeric()
    elif state == "NameChecking":
        checkName()

