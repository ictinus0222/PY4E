
inp = input('Enter Farenheit Temperature: ')
try:
    farh = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')