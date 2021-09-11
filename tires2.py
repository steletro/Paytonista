import console
print('Welcome\n') 

total = int(input('How many tires? '))
prack = int(input('Tires per rack? '))

  
def line(x):
  print(15*x)
  
              
def rack(total,prack):
    nrack = total//prack
    parcial = total - (nrack*prack)
    if prack <= 12:
	    player = 2
    elif prack > 12 and prack <= 24:
      player = 4
    else:
      player = 5
    layers = prack//player
    console.clear()
    x = '🟪'
    line(x)
    print(f'Racks: {nrack}')
    print(f'Per hack: {prack}')
    print(f'Per layer: {player}')
    print(f'Num layers: {layers}')
    print(f'Parcial: {parcial}')
    line(x)
    return nrack, player, parcial
               
            
def change(total):
  player = int(input('How many per layer? '))
  layers = int(input('How many layres? '))
  rack = player*layers
  nrack = total//rack
  parcial =total - nrack*rack
  x = '🟥'
  console.clear()
  line(x)
  print(f'New setup({player}x{layers}):')
  print(f'Racks: {nrack}')
  print(f'Parcial: {parcial}')
  print(f'Tires per rack: {rack}')
  line(x)
  return rack, nrack, parcial
  
  
rack(total, prack)


check = input('Is it fit?(y/n) ')
if check == 'y':  
  console.clear()
  x = '🌷'
  line(x)
  print('Thanks for chose my program.\n End de program \n by Sergio')
  line(x)
else:
  console.clear()
  change(total)
x = '🌟'
line(x)
print('Thanks for chose my program.\n End de program \nby Sergio')
line(x)


