# calculate salaries for part time employees

def calculator():
    print('Please enter the Full Time Salary. Do not enter commas.') #ask for salary
    salary = float(input())

    print('Please enter the number of hours per week.') #ask for hrs per week
    hrsPerWk = int(input())

    # define a function that calculates the part time salary
    def PTS():
        hourlyRate = salary/2080 # get hourly rate
        hrsPerYear = int(hrsPerWk)*52 # get number of hours in a year
        partTime = hourlyRate*hrsPerYear # get Part time salary
        print('$',partTime)

         
    print('Salary for reduced hours at', hrsPerWk, 'hrs per week is:') 
    PTS() #Print Part Time Salary
    print('Full Time Salary = $', salary) #Print Full Time Salary     
    print()
    print()
    print('restarting...To quit type Exit')
while True:
    calculator()
