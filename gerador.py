from PPlay.window import *
from PPlay.gameobject import *
from PPlay.gameimage import *
from PPlay.sprite import *
import random

def generate_shots(dif):
    shots=[]
    count_tiros=0
    if dif==1:
        for i in range(150):
            shots.append(Sprite('images/shot.png', frames=1))
        count_tiros=150
    elif dif==2:
        for i in range(100):
            shots.append(Sprite('images/shot.png', frames=1))
        count_tiros=100
    if dif==3:
        for i in range(75):
            shots.append(Sprite('images/shot.png', frames=1))
        count_tiros=75
    return shots, count_tiros

def randomize_monsters(monsters, dif):
    print(len(monsters))
    print(len(monsters[1]))
    monsters2=[]
    for j in range(dif*8):
        linha=[]
        for i in range(6):
            z=random.randint(0,30)
            linha.append(monsters[j][z])
        monsters2.append(linha)
        print(len(linha))
    print(monsters2)
    return monsters2

def generate_monsters(dif):
    monsters=[]
    for j in range(6):
        linha=[]
        for i in range(10):
            linha.append(Sprite('images/monster1 sprite.png', 2))
        monsters.append(linha)
        #linha=[]
        #for i in range(11):
         #   linha.append(Sprite('images/monster2 sprite.png', 2))
#        monsters.append(linha)
  #      linha=[]
 #       for i in range(11):
   #         linha.append(Sprite('images/monster3 sprite.png', 2))
    #    monsters.append(linha)
#        linha=[]
 #       for i in range(11):
  #          linha.append(Sprite('images/monster4 sprite.png', 2))
   #     monsters.append(linha)
   #     linha=[]
   #     for i in range(11):
   #         linha.append(Sprite('images/monster5 sprite.png', 2))
   #     monsters.append(linha)
   #     linha=[]
   #     for i in range(11):
   #         linha.append(Sprite('images/monster6 sprite.png', 2))
   #     monsters.append(linha)
    #    linha=[]
    return monsters