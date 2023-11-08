inp_hours = input("How many hours? ")
inp_rate = input("What's the rate? ")

def computepay(hours, rate):
  try:
    return (float(hours) * float(rate))
  except: 
    print("Error. Please enter numeric input")

print(computepay(inp_hours, inp_rate))