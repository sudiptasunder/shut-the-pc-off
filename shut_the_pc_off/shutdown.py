#Importing the modules
import os
import animation
import animation_switch

#Importing the cheatcode
import cheatcode

#File Path
file_path = os.getcwd() 

#Fetching file name
file_name = os.path.basename(__file__)

#Logo for the program
if animation_switch.animation_switch == True:
    animation.logo_animation()
if animation_switch.animation_switch == False:
    animation.logo_only()

# Displays addition details
print("Current Directory- ",file_path)
print("File Path- ", __file__)
print("File Name: ",file_name,"\n\n")

#This variable helps to run the program continiously...
run = True

#User selection menu
print('1. DIRECT SHUTDOWN (LESS THAN 1 MIN)\n2. DIRECT RESTART (LESS THAN 1 MIN)\n3. TIMED SHUTDOWN\n4. TIMED RESTART\n5. ABORT SHUTDOWN OR RESTART\n6. TYPE "000" FOR IMMEDIATE SHUTDOWN OR RESTART\n7. TYPE "001" TO DELETE THIS PROGRAM\n8. TYPE "002" TO PERFORM OPERATION(S) ON OTHER COMPUTER(S) CONNECTED TO THE SAME NETWORK\n9. TYPE "003" TO PERFORM OPERATION(S) BY LEAVING A MESSAGE\n10. PRESS "999" TO EXIT\n\n*****ENTER YOUR CHEAT CODE(S) TO SHUTDOWN OR RESTART IN 0S*****\n\n')
print("\nTYPE LETTER(S) IN UPPER CASE IN NEXT PROCESS ONLY IF GO WITH THE (6,7,8 & 9) OPTION(S)\n")
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
    time = str(input("ENTER YOUR TIME(in seconds):\n"))
    os.system(f'cmd /k "shutdown -s -t {time}"')

#What will happen if you select 4
elif user_input == '4':
    print("THE COMPUTER WILL RESTART AS PER THE TIME PROVIDED BY THE USER.\n")
    time = str(input("ENTER YOUR TIME(in seconds):\n"))
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
        os.remove(animation.animation_path)
        os.remove(animation_switch.animation_switch_path)
        run = False
    elif confirm_deletion == "NO":
        print("THE PROCESS WAS NOT EXECUTED...\n")
    else:
        print("TYPE 'YES' OR 'NO' IN UPPER CASE TO EXECUTE THE COMMANDS")
        print('PROCESS 001 HAS BEEN CANCELLED...\n')

#What will happen if you select 002
#Open ups the GUI shutdown menu
elif user_input == "002":
    print("PLEASE WAIT. WE ARE OPENING THE INTERFACE FOR YOU.\n")
    os.system('cmd /k "shutdown -i"')

#What will happen if you select 003
#Perform the operations by leaving a message for the user
elif user_input == "003":
    print("PLEASE ENTER YOUR MESSAGE BELOW\n")
    user_msg = str(input("LEAVE A MESSAGE:\n"))
    operation_time = str(input("ENTER YOUR TIME(in seconds):    "))
    operation_type = str(input("TYPE '1' FOR SHUTDOWN AND '2' FOR RESTART\n"))
    if operation_type == "1":
        os.system(f'cmd /k "shutdown -s -t {operation_time} -c "{user_msg}""')
    elif operation_time == "2":
        os.system(f'cmd /k "shutdown -r -t {operation_time} -c "{user_msg}""')
    else:
        print("TYPE '1' OR '2' ONLY. OTHER CHARACTERS ARE NOT ALLOWED. THE PROCESS WAS NOT EXECUTED...\n")

#What will happen if you select 999
#Terminates the application
elif user_input == "999":
    print("TERMINATING APPLICATION...\n")
    run = False

#What will happen if you enter your Cheat Code(s)
# Shut down the computer
elif user_input == cheatcode.codex_s:
    os.system('cmd /k "shutdown -s -t 0"')

# Restarts the computer
elif user_input == cheatcode.codex_r:
    os.system('cmd /k "shutdown -r -t 0"')

# Deletes the entire program
elif user_input == cheatcode.codex_d:
    run = False
    os.remove(__file__)
    os.remove(cheatcode.cheatcode_path)
    os.remove(animation.animation_path)
    os.remove(animation_switch.animation_switch_path)

# Terminates the session and exits
elif user_input == cheatcode.codex_exit:
    print("TERMINATING APPLICATION...\n")
    run = False

#What will happen if you type something which is not in the menu
else:
    print("\nYOU CAN ONLY CHOOSE THE ABOVE FOLLOWING OPTIONS.\n")
    print("***IN CASE IF THE CHEATCODE(S) ISN'T WORKING, TRY CHECKING THE NAME OF THE VARIABLE OR CHECK IF THE CODEX_S OR CODEX_R HAS BEEN CHANGED OR NOT IN 'CHEATCODE.PY'***")

#This will keep the program running...Stop it using CTRL + C
while run:
    os.system(file_name)
