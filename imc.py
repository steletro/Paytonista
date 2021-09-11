
print('Welcome')
#print('08-15-2021')
h = float(input("What is your hight?"))
w = float(input('What is your weight?'))
imc = round(w/(h*h),1)
meta = round(float(25*h*h),1)
print('IMC')
print(imc)
if imc > 25.0:
  print('Over weight')
  print('Your target is: ')
  print(f"{meta}Kg")
else: 
  print('You got it!')   
print(' ')  
print('End the program!')

