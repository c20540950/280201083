age = int(input("How old are you? "))
price = 3
if age < 6 or age > 60:
  price =  0
elif age >=6 and age <= 18:
  price *= 0.5
print(price)