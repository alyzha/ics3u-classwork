# Ask for favourite colour
print("What is your favourite colour?")
colour = input()
print(f"{colour} ?! Oh why, that's my favourite colour too!")

# Ask for number of cans
in_pack = int(input("How many cans are in your pack?: "))
packs = int(input("How many packs do you have?: "))

print("You have a total of {} cans.".format(in_pack * packs))

# Volume of rectangular prism
print("Find out the volume of a rectangular prism.")
length = int(input("What is the length?: "))
width = int(input("What is the width?: "))
height = int(input("What is the height?: "))

print("The volume of the rectangular prism is {} units cubed.".format(length * width * height))
