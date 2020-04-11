# Write a program to get the name and age of a person. Print out the year the person will turn 100,
# or the year that the person turned 100

name = input('Please enter your name: ') #Asks user for name

#Function that asks user for age, then calculates the year they will turn/ already turned 100
def getAge():
    age = int(input('Please enter your age: '))
    if (age < 100):
        return (2020 + (100-age))
    else:
        return (2020 - (age-100))

year_100 = getAge() #calling the function

# Function to use the correct print statement, based on whether the person will be 100 in the future,
# or if the person already turned 100

def theYear(year_100):
    if (year_100 > 2020):
        print(name + ', you will become a hundred years old in the year '+ str(year_100) )
    else:
        print(name + ', you turned a hundred years old in the year '+ str(year_100) )

theYear(year_100) #calling function
