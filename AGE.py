# Write a program to check whether a person is elector or not
age= int(input("Enter the age of the person :"))
#If user's age is above 18, they are eligible
if age>=18:
    print("The elector is VALID")
#If user's age is below 18, they are ineligible
else:
    print("NOT VALID AGE")
#Program urges user to reprompt a sufficient reponse if age inputted is negative
while age < 0:
    print("Invalid response. Please try again.")
    age = int(input("Enter the age of the person: "))
