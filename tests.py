from scene import *

class MyScene (Scene):
    def setup(self):
        self.background_color = '#c046c6'
        self.ship = SpriteNode('spc:PlayerShip3Orange')
        self.ship.position = self.size / 2
        self.add_child(self.ship)

run(MyScene())

#num = int(input('Escolha um numero inteiro: '))
#harts = '💖💜💙'

#for i in range(num):
 # print(f'{i+1} - Suh, I love you!')
 # print(3*harts)
 
  
  
