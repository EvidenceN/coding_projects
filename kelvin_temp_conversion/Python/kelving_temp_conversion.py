import math

#The consant value for Kelvin temperature
kelvin = 293

#The constant value for Celsius
celsius = kelvin - 273
print(f'The temperature is {celsius} degrees Celsius.')

#value for Fahrenheit 
Fahrenheit = celsius * (9/5) + 32
print(f'The temperature is {Fahrenheit} degrees Fahrenheit when not rounded.')

#rounding Fahrenheit
Fahrenheit = math.floor(Fahrenheit)
print(f'The temperature is {Fahrenheit} degrees Fahrenheit.')
Fahrenheit_round = round(Fahrenheit)
print(f'Fahrenheit rounded = {Fahrenheit_round}')

#Convert temperature to newton scale
newton = math.floor(celsius * (33/100))
print(f'The temperature is {newton} degrees newton.')
newton_round = round(celsius * (33/100))
print(f'new rounded value is {newton_round}')
newton_no_round = celsius * (33/100)
print(f'newton no rounded value is {newton_no_round}')

print(round(6.9)) # result is 7
print(math.floor(6.9)) # result is 6

print(math.ceil(6.9)) # result is 7
print(math.ceil(6.1)) # result is 7