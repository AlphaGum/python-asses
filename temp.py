print("Enter:")
print("1 For Fahrenheit to Celsius")
print("2 For Celsius to Fahrenheit")
while True:
  process = input("Choose ")
  if process.isdigit():
    if process == "1":
      print("You have chosen Fahrenheit to Celsius")
      f = int(input("Enter Fahrenheit:"))
      c = (f - 32) * 5 / 9
      print(f"{f} Degrees Fahrenheit converted into celsius is {c} degrees")
      break
    elif process == "2":
      print("You have chosen Celsius to Fahrenheit")
      c = int(input("Enter Celsius:"))
      f = (c * 9 / 5) + 32
      print(f"{c} Degrees Celsius converted into fahrenheit is {f} degrees")
      break
    else:
      print("Input valid number")
      continue
  else:
    print("Invalid Input")
    continue
print("Thank you for using this converter")