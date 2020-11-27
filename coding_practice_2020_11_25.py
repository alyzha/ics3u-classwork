#1
number = int(input("Enter the number: "))
if number % 2 == 0:
  print("The number is even.")
else:
  print("The number is odd.")

#2
age = int(input("How old is the dog? "))
if age <= 2:
  dog_age = age * 10.5
elif age < 0:
  print("INVALID NUMBER")
else:
  dog_age = 21 + (age - 2)*7

print(f"The dog is {dog_age} dog years old.")

#3
letter = input("Enter a letter: ").lower()
if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
  print("This letter is a vowel.")
elif letter == "y":
  print("This letter can sometimes be a vowel")
else:
  print("This letter is a consonant")

#4
shape = int(input("How many sides does your shape have?: "))
if shape == 3:
  print("It is a triangle")
elif shape == 4:
  print("It is a quadrilateral")
elif shape == 5:
  print("It is a pentagon")
elif shape == 6:
  print("It is a hexagon")
elif shape == 7:
  print("It is a heptagon")
elif shape == 8:
  print("It is a octogon")
elif shape == 9:
  print("It is a nonogon")
elif shape == 10:
  print("It is a decogon")
else:
  print("INVALID")

#5
