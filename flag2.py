import console
import datetime
from rich import print
cores = ['💖','💜','💙'] 
linha = 15
coluna = 3
def horizontal():
    for cor in cores:
      for i in range(coluna):
         print(cor*linha)

def vertical():
    for i in range(linha):
     print(coluna*cores[0]+coluna*cores[1]+coluna*cores[2])


def resposta(resposta):  
    if resposta == 'v':
      vertical()
    elif resposta == 'h':
        horizontal()
    elif resposta == 's':
        console.exit()
    else:    
      print('Use uma resposta valida: "v" ou "h" ou "s" para sair') 
    return resposta
  

while True:
  
  console.clear()       
  resposta = input('Vertical ou Horizontal? (V/H)')
  resposta(resposta)
  

  


