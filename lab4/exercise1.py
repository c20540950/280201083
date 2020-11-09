a = input("enter a number: ")
if len(a) > 1:
  output = int(a[len(a)-1]) + int(a[len(a)-2])
else:
  output = int(a)
print(output)