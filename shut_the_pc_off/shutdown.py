#Importing the modules
import os

#Importing the cheatcode
import cheatcode

#File Path
file_path = os.getcwd() 

#Logo for the program
print('''
╔═══╦╗────╔╗──╔╗╔╗─────╔═══╦═══╗────╔═╗╔═╗
║╔═╗║║───╔╝╚╗╔╝╚╣║─────║╔═╗║╔═╗║────║╔╝║╔╝
║╚══╣╚═╦╗╠╗╔╝╚╗╔╣╚═╦══╗║╚═╝║║─╚╝╔══╦╝╚╦╝╚╗
╚══╗║╔╗║║║║║──║║║╔╗║║═╣║╔══╣║─╔╗║╔╗╠╗╔╩╗╔╝
║╚═╝║║║║╚╝║╚╗─║╚╣║║║║═╣║║──║╚═╝║║╚╝║║║─║║
╚═══╩╝╚╩══╩═╝─╚═╩╝╚╩══╝╚╝──╚═══╝╚══╝╚╝─╚╝\nDeveloped By Sudipta Sunder''')
print("Current Directory: ",file_path)
print("File Path: ", __file__,"\n\n")

#This variable helps to run the program continiously...
run = True

#User selection menu
print("WARNING!\nDON'T TRY TO CHANGE THE NAME OF THIS PROGRAM, OTHERWISE THE PROGRAM WON'T WORK AND WILL STUCK IN A CONTINIOUS LOOP!\n")
print('1. DIRECT SHUTDOWN (LESS THAN 1 MIN)\n2. DIRECT RESTART (LESS THAN 1 MIN)\n3. TIMED SHUTDOWN\n4. TIMED RESTART\n5. ABORT SHUTDOWN OR RESTART\n6. TYPE "000" FOR IMMEDIATE SHUTDOWN OR RESTART\n7. TYPE "001" TO DELETE THIS PROGRAM\n\nENTER YOUR CHEAT CODE(S) TO SHUTDOWN OR RESTART IN 0S]\n')
print("\nTYPE LETTER(S) IN UPPER CASE IN NEXT PROCESS ONLY IF GO WITH THE 6TH OPTION\n")
user_input = input("SELECT ONE OF THE FOLLOWING OPERATIONS:    \n")

#What will happen if you select 1
if user_input == '1':
    print("THE COMPUTER WILL SHUTDOWN IN LESS THAN 60S...\n")
    os.system('cmd /k "shutdown -s"')

#What will happen if you select 2
elif user_input == '2':
    print("THE COMPUTER WILL RESTART IN LESS THAN 60S...\n")
    os.system('cmd /k "shutdown -r"')

#What will happen if you select 3
elif user_input == '3':
    print("THE COMPUTER WILL SHUTDOWN AS PER THE TIME PROVIDED BY THE USER.\n")
    time = str(input("ENTER YOUR TIME:\n"))
    os.system(f'cmd /k "shutdown -s -t {time}"')

#What will happen if you select 4
elif user_input == '4':
    print("THE COMPUTER WILL RESTART AS PER THE TIME PROVIDED BY THE USER.\n")
    time = str(input("ENTER YOUR TIME:\n"))
    os.system(f'cmd /k "shutdown -r -t {time}"')

#What will happen if you select 5
elif user_input == '5':
    print("WE ARE ABORTING THE PROCESS...\n")
    os.system('cmd /k "shutdown -a"')

#What will happen if you select 000
elif user_input == '000':
    print("ARE YOU SURE YOU WANT TO CONTINUE?\n")
    print("WARNING!: \nMAKE SURE YOU HAVE YOUR PROGRESS OR ANY WORK SAVED BEFORE PERFORMING THIS.\n")
    confirmation = str(input("TYPE 'YES' OR 'NO' TO CONTINUE:\n"))
    if confirmation == "YES":
        print("SELECT THE FOLLOWING PROCESS:\n1. SHUTDOWN\n2. RESTART")
        selection = input("ENTER YOUR SELECTION:\n")
        if selection == "1":
            print("PROCESS 000 HAS BEEN STARTED...\n")
            os.system('cmd /k "shutdown -s -t 0"')
        elif selection == "2":
            print("PROCESS 000 HAS BEEN STARTED...\n")
            os.system('cmd /k "shutdown -r -t 0"')
        else:
            print("TYPE '1' OR '2' ONLY. THE PROCESS WAS NOT EXECUTED.\n")
    elif confirmation == "NO":
        print("SEEMS LIKES YOU FORGOT TO SAVE SOME OF THE WORK IN YOUR COMPUTER. PROCESS 000 WAS NOT EXECUTED.\n")
    else:
        print("\nTYPE 'YES' OR 'NO' TO EXECUTE THE PROCESS FURTHER.")
        print("MAKE SURE TO TYPE EVERYTHING IN UPPER CASE. LOWERCASE IS NOT ALLOWED.")
        print("PROCESS 000 HAS BEEN CANCELLED.")
        
#What will happen if you select 001
elif user_input == '001':
    print('ARE YOU SURE YOU WANT TO DELETE THIS PROGRAM?\n')
    print("THIS STEP IS IRREVERSIBLE. ONCE DELETED, YOU CAN'T RECOVER THE FILES.\n")
    confirm_deletion = str(input("TYPE 'YES' OR 'NO' TO CONTINUE:\n"))
    if confirm_deletion == "YES":
        os.remove(__file__)
        os.remove(cheatcode.cheatcode_path)
        run = False
    elif confirm_deletion == "NO":
        print("THE PROCESS WAS NOT EXECUTED...\n")
    else:
        print("TYPE 'YES' OR 'NO' IN UPPER CASE TO EXECUTE THE COMMANDS")
        print('PROCESS 001 HAS BEEN CANCELLED...\n')
        run = False

#What will happen if you enter your Cheat Code
elif user_input == cheatcode.codex_s:
    os.system('cmd /k "shutdown -s -t 0"')

elif user_input == cheatcode.codex_r:
    os.system('cmd /k "shutdown -r -t 0"')

elif user_input == cheatcode.codex_d:
    run = False
    os.remove(__file__)
    os.remove(cheatcode.cheatcode_path)

#What will happen if you type something which is not in the menu
else:
    print("\nYOU CAN ONLY CHOOSE THE ABOVE FOLLOWING OPTIONS.\n")
    print("***IN CASE IF THE CHEATCODE(S) ISN'T WORKING, TRY CHECKING THE NAME OF THE VARIABLE OR CHECK IF THE CODEX_S OR CODEX_R HAS BEEN CHANGED OR NOT IN 'CHEATCODE.PY'***")
    run = False

#This will keep the program running...Stop it using CTRL + C
while run:
    os.system('shutdown.py')
