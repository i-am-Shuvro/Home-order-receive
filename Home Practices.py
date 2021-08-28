print("Hi there!\nSuppose you are about to join a company where you will be paid salary each day two times of your previous day!")
First_day_salary = int(input("\t* Now please input the salary amount the company is offering you for your first day in the job (in BDT): "))
How_long_you_want_to_work_there = int(input("\t* How long you wish to work there (in BDT): "))

Salary_will_be = First_day_salary ** How_long_you_want_to_work_there

print("\nYour salary will become", Salary_will_be, "BDT on the", How_long_you_want_to_work_there,"th day of working there!")


# sum of series of power of 2

# function to calculate sum of series
def calculateSum(n):
    sum = 0

    # loop to calculate sum of series
    for i in range(0, n):
        # calculate 2 ^ i
        sum = sum + 2**i    #(1<<i)
    #When n=3, Sum = 0 + 1
    # Sum = 1 + 2
    # Sum = 1 + 2 + 4

    return sum


# Driver code
n = How_long_you_want_to_work_there
print("& on the", How_long_you_want_to_work_there,"th day, your total salary will be", calculateSum(n), "BDT!")

input("press enter to exit")