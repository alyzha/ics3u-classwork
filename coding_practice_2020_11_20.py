# Ask for favourite colour
print("What is your favourite colour?")
colour = input()
print(f"{colour} ?! Oh why, that's my favourite colour too!")

# Ask for number of cans
in_pack = int(input("How many cans are in your pack?: "))
packs = int(input("How many packs do you have?: "))

print("You have a total of {} cans.".format(in_pack * packs))
