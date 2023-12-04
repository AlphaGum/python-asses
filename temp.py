#print("Enter:")
#print("1 For Fahrenheit to Celsius")
#print("2 For Celsius to Fahrenheit")#menu
#while True:
  #process = input("Choose ")
  #if process.isdigit():
    #if process == "1":
      #print("You have chosen Fahrenheit to Celsius")
      #f = int(input("Enter Fahrenheit:")) # changing the input into a int
      #c = (f - 32) * 5 / 9 #math to do the conversions
      #print(f"{f} Degrees Fahrenheit converted into celsius is {c} degrees")#printing out the result
      #break
    #elif process == "2":
      #print("You have chosen Celsius to Fahrenheit")
      #c = int(input("Enter Celsius:"))
      #f = (c * 9 / 5) + 32
      #print(f"{c} Degrees Celsius converted into fahrenheit is {f} degrees")
      #break
    #else:
      #print("Input valid number")
      #continue
  #else:
    #print("Invalid Input")
    #continue
#print("Thank you for using this converter")

print("enter")
print("1. celsius to fahrenhiet")
print("2. fahrenhiet to celsuis")
selection = int(input())
def calculations():
  if selection == 1:
    print("you have chosen celsius to fahrenhiet")
    c = input("enter celsius: ")
    if c.isdigit():  #checks whether int inputed temp is a digit
      c = int(c)
      f = c * 9 / 5 + 32  #does the calculations for the conversions
      print(f"fahrenhiet is {f}")
    else:
      print("invalid choice ")  # end the prgram if the choice is invalid
  if selection == 2:
    print("you have chosen fahrenheit to celsius")
    f = input("enter fahrenheit: ")
    if f.isdigit():
      f = int(f)
      c = f - 32 * 5 / 9
      print(f"celcius is {c}")
    else:
      print("invalid selection")
  elif selection > 2:
    print("invalid selection")
  print("thank you for using the program")
print(calculations())