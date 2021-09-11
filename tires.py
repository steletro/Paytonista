import console
linha = 32*'_'
print(linha)
print(' ')
print('Welcome')
print(linha)
total = int(input('How many tires? '))
prack = int(input('Tires per rack? '))
nrack = total//prack
parcial = total - (nrack*prack)
if prack == 10:
	player = 2
elif prack > 10 and prack <= 24:
	player = 4
else:
  player = 5
  
console.clear()
print('Data:')
layers = int(prack/player)
print(linha)
print(" ")
print(f"| Rack: {nrack} Racks of {prack} tires      ")
print(f"| Parcials: {parcial} tires.             ")
print(f"| Tires per layer: {player} tires       ")
print(f'| Layers: {layers}')
print(f"| Total: {total} tires")
print(linha)
print(" ")
print("End of program")
print('by Sergio')

