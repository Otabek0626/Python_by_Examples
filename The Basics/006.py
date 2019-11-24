#Ask how many slices of pizza the user started with and ask
#how many slices they have eaten. Work out how many
#slices they have left and display the
#answer in a userfriendly format.
first_time = int(input("Enter the number of slices of pizza you started with: "))
last_time = int(input("How many slices have you eaten? "))
slices_left = first_time - last_time
print("You have", slices_left, "slices remaining")
