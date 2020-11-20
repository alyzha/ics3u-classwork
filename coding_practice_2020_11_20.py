# Ask for favourite colour
print("What is your favourite colour?")
colour = input()
print(f"{colour} ?! Oh why, that's my favourite colour too!")

print()

# Ask for number of cans
in_pack = int(input("How many cans are in your pack?: "))
packs = int(input("How many packs do you have?: "))

print("You have a total of {} cans.".format(in_pack * packs))

print()

# Volume of rectangular prism
print("Find out the volume of a rectangular prism.")
length = int(input("What is the length?: "))
width = int(input("What is the width?: "))
height = int(input("What is the height?: "))

print("The volume of the rectangular prism is {} units cubed.".format(length * width * height))

print()

# Google meet
print("Joined the Google meet! Would you like to mute the teacher?")

answer = input("Enter yes or no: ")

if answer == "yes":
  print("That's probably not a good idea")

elif answer == "no": 
  print("Ok. Good.")

else:
  print("Please enter yes or no.")


