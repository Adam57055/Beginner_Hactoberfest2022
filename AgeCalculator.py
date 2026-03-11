#Imports time utilities
import datetime
from datetime import date
#Age is calculated through current year subtracted from the birth year
def Cal_Age(bday):
	n= date.today()
	age= n.year - bday.year
	return age
#Asks user for their birthdate
birthday=input("Enter your BirthDate as yyyy/mm/dd:")
n="%Y/%m/%d"
#Executes function
bday=datetime.datetime.strptime(birthday,n)
print("You are",Cal_Age(bday), "years")
