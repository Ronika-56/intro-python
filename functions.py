from conditions import weight

print(34)
x =round(67.43)
print(x)
print(round(20.99))

#int , float , string ,list ,dictionary ,boolean
#params
#use a function ==call a function
#data==parameters
#return value
w = input("Enter your weight in kgs")
h = input("Enter your height in meters")

print(type(w))

weight =float(w)
height = float(h)

print(type(height))

bmi = weight / (height * height)
print(bmi)