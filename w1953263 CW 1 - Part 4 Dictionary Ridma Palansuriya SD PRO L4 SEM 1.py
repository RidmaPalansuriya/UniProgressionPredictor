# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1953263
# Date: 14 th December 2022
# Part 4 Dictionary

Allowed_Credit_Inputs = [0,20,40,60,80,100,120]     #Allow Credit List for Inputs (Tuple - Immutable Values)
OutComesList =[]                                    #Out Comes List
Pass=0                                              #Credit Pass Variable
Fail=0                                              #Credit Fail Variable
Defer=0                                             #Credit Defer Variable
Progress=0                                          #Output - Progress,Initial Count
Module_Trailer=0                                    #Output - Module Trailer,Initial Count
Module_Retriever=0                                  #Output - Module Retriever,Initial Count
Exclude=0                                           #Output - Exclude,Initial Count
Progression_Data =[]                                #Empty Lists to add Progression Data
Progression_Data_Dictionary = {}                    #Progression dara Dictionary identifing

def STUDENT_ID_LOOP():
    while True:
        global Student_ID
        Student_ID = input("Enter your student ID : ").lower()          #Book - Beginning Programming with Python® 2nd Edition by John Paul Mueller
        try:
            int(Student_ID[1:])
            if Student_ID[0] != 'w':
                print('Invalid and try again - The Student ID starts with the letter "w".')
                continue
            else:
                if len(Student_ID)==7:
                    print('Invalid - Please Enter the "Seven-digit Student ID" including the "w".')
                    continue
                else:
                    if Student_ID in Progression_Data_Dictionary.keys():
                        print("University ID already exists.")
                    else:
                        break
        except ValueError:
            print("Invalid Student ID.")
            continue

    #return Student_ID

def DICTIONARY():
    print("_"*40,'\n')
    for student_ID, Value in Progression_Data_Dictionary.items():
        print(student_ID, ' : ', Value)
    print("_" * 40,)


def INPUTS():
    global Pass, Defer, Fail                                #https://www.programiz.com/python-programming/global-keyword
    while True:
        try:
            Pass = int(input('Enter credits for  Pass: '))
        except ValueError:
            print('\nInteger Required!\n')
            continue
        if Pass not in Allowed_Credit_Inputs:
            print('\nOut of range!\n')
        else:
            break
    while True:
        try:
            Defer = int(input('Enter credits for Defer: '))
        except ValueError:
            print('\nInteger Required!\n')
            continue
        if Defer not in Allowed_Credit_Inputs:
            print('\nOut of range!\n')
        else:
            break
    while True:
        try:
            Fail = int(input('Enter credits for  Fail: '))
        except ValueError:
            print('\nInteger Required!\n')
            continue
        if Fail not in Allowed_Credit_Inputs:
            print('\nOut of range!\n')
        else:
            break 

def CONDITIONS():
    global OutComesList
    global Pass,Defer,Fail                                                    #https://www.programiz.com/python-programming/global-keyword
    global Progress, Module_Retriever, Module_Trailer,Exclude                 #https://www.programiz.com/python-programming/global-keyword
    Total = Pass + Defer + Fail
    if Total == 120:
        if Pass == 120:
            print('_______________________________________\n\n Progress \n_______________________________________\n')
            Progress += 1
            global Student_ID
            Progression_Data_Dictionary[Student_ID] = 'Progress - ' + str(Pass) + ', ' + str(Defer) + ', ' + str(Fail)
            OutComesList.append('Progress')
            OutComesList.append(Pass)
            OutComesList.append(Defer)
            OutComesList.append(Fail)

        elif (Defer + Fail) == 20 and Pass == 100:
            print('_______________________________________\n\n Progress (Module Trailer) \n_______________________________________\n')
            Module_Trailer += 1
            #global Student_ID
            Progression_Data_Dictionary[Student_ID] = 'Progress (Module Trailer) - ' + str(Pass) + ', ' + str(Defer) + ', ' + str(Fail)
            OutComesList.append('Trailer')
            OutComesList.append(Pass)
            OutComesList.append(Defer)
            OutComesList.append(Fail)

        elif (Fail >= 80) and (Fail > Defer) and (Pass <= 40):
            print('_______________________________________\n\n Exclude \n_______________________________________\n')
            Exclude += 1
            #global Student_ID
            Progression_Data_Dictionary[Student_ID] = 'Exclude - ' + str(Pass) + ', ' + str(Defer) + ', ' + str(Fail)
            OutComesList.append('Exclude')
            OutComesList.append(Pass)
            OutComesList.append(Defer)
            OutComesList.append(Fail)
        
        elif (Pass < 100):
            print('_______________________________________\n\n Do not progress (Module Retriever) \n_______________________________________\n')
            Module_Retriever += 1
            #global Student_ID
            Progression_Data_Dictionary[Student_ID] = 'Do not progress (Module Retriever) - ' + str(Pass) + ', ' + str(Defer) + ', ' + str(Fail)
            OutComesList.append('Retriever')
            OutComesList.append(Pass)
            OutComesList.append(Defer)
            OutComesList.append(Fail)

        elif (Pass + Defer + Fail) != 120:
            print('_______________________________________\n Incorrect Total! \n_______________________________________\n')

        else:
            print('_______________________________________\n Out of range! \n_______________________________________\n')
    else:
        print('_______________________________________\n Incorrect Total! \n_______________________________________\n')
position = ' '


def MENU():
    #cont = 'y'
    while True:
        Question = input('Enter "y" to Enter More Values \nEnter "q" to Quit and Print The Dictionary\nPlease Enter your Choice:  ')
        if Question == 'y':
            print('')
            INPUTS()
            print('')
            CONDITIONS()
            DICTIONARY()
            print('')

        elif Question == 'q':
            print('_____________________________________________\n')
            print("\n", "\n", " " * 10, 'You have chosen to quit. Bye Bye!!!', " " * 10, "\n", "\n")

            print('')
            print('*' * 18, ' Dictionary ', '*' * 17)
            print('')
            DICTIONARY()
            print('')
            print('\n',' ~ ' * 7, ' Quited with results  ', ' ~ ' * 6)
            break

        else:
            print('\nWrong input!\n')

#choice = 0
#choices = [1, 2] #List for initial menu choices2
#while choice not in choices:
    #try:
        #choice = int(input('______________________________\nFor Student version Press:  1 \nFor   Staff Version Press:  2  \n______________________________\n'))
        #if choice == 1:
            #print('________________________________\n Welcome to the Student Version \n________________________________\n')
            #STUDENT_ID_LOOP()
            #INPUTS()
            #print('')
            #CONDITIONS()

        #if choice == 2:
            #print('________________________________\n Welcome to the Staff Version \n________________________________\n')

###Correct from below


STUDENT_ID_LOOP()
INPUTS()
print('')
CONDITIONS()
while True:
    if input('Enter "y" to Enter More Values \nEnter "q" to Quit and Print The Dictionary\nPlease Enter your Choice:  ') == 'y':
        STUDENT_ID_LOOP()
        INPUTS()
        print('')
        CONDITIONS()

    elif input('Enter "y" to Enter More Values \nEnter "q" to Quit and Print The Dictionary\nPlease Enter your Choice:  ') == 'q':
        print('________________________________________\n')
        print("\n", "\n", "~" * 1, 'You have chosen to quit. Bye Bye!!!', "~" * 1, "\n")

        print('')
        print('*' * 13, ' Dictionary ', '*' * 13)
        print('')
        DICTIONARY()
        print('')
        break
    else:
        print('\nWrong input!\n')

#print('')
#print('*' * 18, ' Dictionary ', '*' * 17)
#print('')
#DICTIONARY()
#print('')
