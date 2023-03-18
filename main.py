# Python Program to convert temperature in celsius to fahrenheit
#Also detects global warming

# change this value for a different result
#e.g celsius = 37.5
celsius = float(input("Please enter the temperature in celsius: "))


# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))

temp = fahrenheit


if (temp <= 95.0): #Degrees fahrenheit
  print("Its not global warming")
else:
  print("There is global warming.")