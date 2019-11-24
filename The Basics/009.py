#Write a program that will ask for a
#number of day sand then will
#show how many hours, minutes
#and seconds are in that number of days.
days = int(input("How many days? "))
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print(" In", days, "days there are...\n",hours, "hours\n", minutes, "minutes\n", seconds, "seconds")
