# calculate salaries for part time employees
import sys

def calculator():
    print('')
    print('*******************************')
    print('*                             *')
    print('* Part Time Salary Calculator *')
    print('*                             *')
    print('*******************************')
    print('')
    print('Please enter the Full Time Salary.')
    print('Do not enter commas!')
    
    # get user input for Full Time Salary and check that it's a valid float
    while True:

        salary = input('$: ')
        try:
            val = float(salary)
            break;
        except ValueError:
            print('Invalid Input.\n Please enter a valid number without commas.\n Ex. 50300.42')


    # define variable to get user input if they want to quit
    #endProgram = (input())

    # get user input for Hours per Week and check that it's a valid int
    while True:

        hrsPerWk = input('Please enter the number of hours per week: ')
        try:
            valHrs = int(hrsPerWk)
            break;
        except ValueError:
            print('Invalid Input. Please enter a valid, whole number.')
    

    # define a function that calculates the part time salary
    def PTS():
        hourlyRate = val/2080 # get hourly rate
        hrsPerYear = int(valHrs)*52 # get number of hours in a year
        partTime = hourlyRate*hrsPerYear # get Part time salary
        print('$',partTime)


    print('Full Time Salary: $', salary) #Print Full Time Salary       
    print('Salary for reduced hours at', hrsPerWk, 'hrs per week is: ', end = '') 
    PTS() #Print Part Time Salary    
    print()
    print()
    print('Restarting...To quit type Exit')

    # get user input, make it lowercase and assign to a variable
    close = input().lower()

    # check if user input is == to 'exit' & if it is exit the program.
    # Otherwise program will restart
    if close == 'exit':
        sys.exit('Exiting Program...')


while True:
    calculator()

