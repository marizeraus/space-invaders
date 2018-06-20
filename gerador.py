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
        count_tiros=50
    elif dif==2:
        for i in range(100):
            shots.append(Sprite('images/shot.png', frames=1))
        count_tiros=100
    if dif==3:
        for i in range(75):
            shots.append(Sprite('images/shot.png', frames=1))
        count_tiros=75
    return shots, count_tiros


def generate_shots_monsters(dif):
    shots=[]
    count_tiros=0
    if dif==1:
        for i in range(10):
            shots.append(Sprite('images/shot.png', frames=1))
        count_tiros=50
    elif dif==2:
        for i in range(20):
            shots.append(Sprite('images/shot.png', frames=1))
        count_tiros=100
    if dif==3:
        for i in range(30):
            shots.append(Sprite('images/shot.png', frames=1))
        count_tiros=75
    return shots, count_tiros


def generate_monsters(fase):
    f1_3_x = 3
    f1_3_y = 6
    f3_6_x = 6
    f3_6_y = 11
    if fase<4:
        x=f1_3_x
        y=f1_3_y
    else:
        x=f3_6_x
        y=f3_6_y

    monsters=[]
    for j in range(x):
        linha=[]
        for i in range(y):
            if fase==1:
                linha.append(Sprite('images/monster1 sprite.png', 2))
            elif fase==2:
                linha.append(Sprite('images/monster2 sprite.png', 2))
            elif fase==3:
                linha.append(Sprite('images/monster3 sprite.png', 2))
            elif fase==4:
                linha.append(Sprite('images/monster4 sprite.png', 2))
            elif fase==5:
                linha.append(Sprite('images/monster5 sprite.png', 2))
            elif fase==6:
                linha.append(Sprite('images/monster6 sprite.png', 2))
        monsters.append(linha)
    return monsters
