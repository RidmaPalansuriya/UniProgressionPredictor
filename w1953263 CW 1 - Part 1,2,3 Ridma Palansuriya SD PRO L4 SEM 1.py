# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1953263
# Date: 14 th December 2022

Allowed_Credit_Inputs = [0,20,40,60,80,100,120]    #Allow Credit List for Inputs (Tuple - Immutable Values)
OutComesList =[]                                   #Out Come List to print the list
Pass=0                  #Credit Pass Variable
Fail=0                  #Credit Fail Variable
Defer=0                 #Credit Defer Variable
Progress=0              #Output - Progress,Initial Count
Module_Trailer=0        #Output - Module Trailer,Initial Count
Module_Retriever=0      #Output - Module Retriever,Initial Count
Exclude=0               #Output - Exclude,Initial Count
Progression_Data =[]    #Empty Lists to add Progression Data

# Part 1 (D) - Horizontal Histogram
def H_HISTOGRAM():
    """
    The program produce a ‘Horizontal Histogram’ where each star represents a student who achieved a progress outcome in the category range: progress, trailing, module
retriever and exclude.

    Display the number of students for each progression category and the total number of
students.

    Print OutComes List Elements in to the List.
            Last modified 14/12/2022
    """
    global Question
    print('Progress        ', Progress,':', Progress*'*')
    print('Module Retriever', Module_Retriever,':', Module_Retriever*'*')
    print('Module Trailer  ', Module_Trailer,':',Module_Trailer*'*')
    print('Exclude         ', Exclude,':',Exclude*'*',"\n")
    print("------------------------------------- ")
    print(Progress+Module_Retriever+Module_Trailer+Exclude, "Outcomes in Total.")
    print("------------------------------------- ")

def LIST():                                        # Part 2 List
    def LIST():
        """ Print OutComes List Elements in to the List.

            The program saves the input progression data to a list.
            Then access the stored data from the list and print the data.

        Last modified 14/12/2022.
        """

    for elements in range(0,len(OutComesList),4):
        print(str(OutComesList[elements]), str(OutComesList[elements+1]), str(OutComesList[elements+2]), str(OutComesList[elements+3]))
    return

def TEXT_FILE():                                  # Part 3 Text File
    """
        Program save any inputted progression data to a text file.
        Later in the program, access the stored data and print.
        Write, Append and Read OutComes Data in to the Text File "Outcome_Data.txt").
        
        Last modified 14/12/2022.
    """

    file = open('Outcome_Data.txt', 'w+')         #Write to the text file
    file.truncate(0)
    for c in range(0, len(OutComesList), 4):
        file = open('Outcome_Data.txt', 'a')      #Append data to the text file
        file.write(str(OutComesList[c])+' '+' '+str(OutComesList[c+1])+' '+' '+str(OutComesList[c+2])+' '+' '+str(OutComesList[c+3])+'\n' )
        file.close()
    file = open('Outcome_Data.txt', 'r')          #Write data to the text file
    print(file.read())
    file.close()

def INPUTS():
    """
    The program prompt for the number of credits at pass, defer and fail and validate them.

    The program display ‘Integer required’ if a credit input is the wrong data type.

    The program display ‘Out of range’ if credits entered are not in the range 0, 20, 40,60, 80, 100 and 120.

    The program display ‘Total incorrect’ if the total of the pass, defer and fail credits is not 120.

        Last modified 14/12/2022
    """

    global Pass, Defer, Fail                     
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
    """ Depending on the prompt values for the number of credits at pass, defer and fail
this part display the appropriate progression outcome for an individual student.
    (i.e., progress, trailing, module retriever or exclude)...

    Maintaining the counts and appending values to the lists and histograms also happening here.

    Last modified 14/12/2022
    """

    global OutComesList                                                       #Adding Global variables to access them with in the User Defined Function
    global Pass,Defer,Fail                                                    #global-keyword used
    global Progress, Module_Retriever, Module_Trailer,Exclude                 
    Total = Pass + Defer + Fail
    if Total == 120:
        if Pass == 120:
            print('____________________________________\n\n Progress \n____________________________________\n')
            Progress += 1
            OutComesList.append('Progress')
            OutComesList.append(Pass)
            OutComesList.append(Defer)
            OutComesList.append(Fail)

        elif (Defer + Fail) == 20 and Pass == 100:
            print('____________________________________\n\n Progress (Module Trailer) \n____________________________________\n')
            Module_Trailer += 1
            OutComesList.append('Trailer')
            OutComesList.append(Pass)
            OutComesList.append(Defer)
            OutComesList.append(Fail)

        elif (Fail >= 80) and (Fail > Defer) and (Pass <= 40):
            print('____________________________________\n\n Exclude \n____________________________________\n')
            Exclude += 1
            OutComesList.append('Exclude')
            OutComesList.append(Pass)
            OutComesList.append(Defer)
            OutComesList.append(Fail)
        
        elif (Pass < 100):
            print('____________________________________\n\n Do not progress (Module Retriever) \n____________________________________\n')
            Module_Retriever += 1
            OutComesList.append('Retriever')
            OutComesList.append(Pass)
            OutComesList.append(Defer)
            OutComesList.append(Fail)

        elif (Pass + Defer + Fail) != 120:
            print('________________________________\n Incorrect Total! \n________________________________\n')

        else:
            print('________________________________\n Out of range! \n________________________________\n')
    else:
        print('________________________________\n\n Total Incorrect! \n________________________________\n')
position = ' '

def MENU():
    """
        The program loops to allow a staff member to predict progression outcomes for multiple
students.

        The program should prompt for credits at pass, defer and fail and display the appropriate
progression for each individual student until the staff member enters ‘q’ to quit.

        Input ‘y’ to continue.

        Last modified 14/12/2022
    """

    cont = 'y'
    while True:
        Question = input('Enter "y" to Enter More Values \nEnter "q" to Quit and View Results \nPlease Enter your Choice:  ')
        if Question == 'y':
            print('')
            INPUTS()
            print('')    
            CONDITIONS()
            print('')

        elif Question == 'q':
            # H Histogram Banner and Calling the Function
            print('____________________________________\n')
            print("\n",'You have chosen to quit. Bye Bye!!!',"\n","\n")    #Bye Bye Message
            print('*' * 6, ' Horizontal Histogram ', '*' * 6,"\n")                            #H Histogram Banner
            #print('')
            H_HISTOGRAM()
            print('')

            #List Banner and Calling the Function
            #print('')
            print('\n','*' * 14, ' List ', '*' * 14,'\n')
            #print('')
            LIST()
            print('')

            #Text File Banner and Calling the Function
            print('\n','*' * 12, ' Text File ', '*' * 11,'\n')
            TEXT_FILE()

            print('\n',' ~ ' * 1, ' Quited with results  ', ' ~ ' * 1,'\n')
            
            break
        else:
            print('\nWrong input!\n')

#Student and Staff Version Controll Part
choice = 0
choices = [1, 2] #List for initial menu choices2
while choice not in choices:
    try:
        choice = int(input('____________________________________\n\nFor Student version Press:  1 \nFor   Staff Version Press:  2  \n____________________________________\n\n'))
        if choice == 1:
            print('____________________________________\n\n Welcome to the Student Version \n____________________________________\n')
            INPUTS()
            print('')
            CONDITIONS()

        if choice == 2:
            print('____________________________________\n\n Welcome to the Staff Version \n____________________________________\n')
            INPUTS()
            print('')
            CONDITIONS()
            print('')
            MENU()
    except ValueError:
        print('________________________________\n Invalid Input! \n________________________________\n')
