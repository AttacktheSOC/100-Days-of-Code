#!/usr/bin/env python3
##
## Day1 - Python 100 Days of Code
## writing to a file
from datetime import date

print("Hello!\n\nPlease answer the following questions to complete your user bio.\n")

firstName = input("What is your first name?\n")
lastName = input("What is you surname?\n")
age = int(input("Please enter you age?\n"))
locationCity = input("\nPlease tell us the current City of your residence:  ")
locationState = input("\nPlease enter the abbreviation for the State of your residence(ex. New York = NY):  ")
bio = input("\n\nOK, now tell us a little bit about yourself and why you want this opportunity:\n")

print("\n\nThank you, {0}! We look forward to reading your bio.\n\nOnce we have made a decision, a snailmail letter will be sent to your residence in {1}, {2}".format(firstName.title(), locationCity.title(), locationState.upper()))

todaydate = date.today()

#Generate unique filename
filename = lastName+"_"+firstName+"_bio"+str(todaydate)+".txt"

File_object = open(filename,'w')

# Aggregate user responses and prep to be psuhed into the txt file
Linestowrite = "Candidate: {0} {1}\n{0}'s Age: {2}\nResidence: {3}, {4}\n\nCandidate summary: {5}".format(firstName.title(), lastName.title(), age, locationCity.title(), locationState.upper(), bio)

File_object.writelines(Linestowrite)
File_object.close()
