from PPlay.window import *
from PPlay.gameobject import *
from PPlay.gameimage import *
from PPlay.sprite import *
import gerador

def move_ship(ship, janela, teclado):
    vel_ship=190
    if ship.x>-2*ship.width/3 and ship.x<janela.width+ship.width/3:
        if teclado.key_pressed('LEFT'):
            ship.x-=vel_ship*janela.delta_time()
        if teclado.key_pressed('RIGHT'):
            ship.x+=vel_ship*janela.delta_time()
    elif ship.x>janela.width+ship.width/3:
        ship.x=0-5
    else:
        ship.x=janela.width

def shoot(shots, teclado, ship,i):
    shots[i].set_position(ship.x+ship.width/2-1.5, ship.y-ship.height/3)
    shots[i].draw()

def move_shot(i, shots, janela):
    vel_shot=200
    shots[i].y-=vel_shot*janela.delta_time()
    shots[i].draw()

def stop_shot(shots,i):
    if shots[i].y<-10:
        shots.pop(i)

def move_monsters(monsters,time, virou, vel_monster, count_turn):
    for i in range(len(monsters)):
        if len(monsters[i])>0:
            if monsters[i][0].x<0 or (monsters[i][0].x+monsters[i][0].width)>janela.width or (monsters[i][-1].x)<0 or (monsters[i][-1].x+monsters[i][-1].width) >janela.width:
                if not virou[i]:
                    vel_monster[i]=-vel_monster[i]
                    virou[i]=True
                    for j in range(len(monsters[i])):
                        monsters[i][j].y+=10
            if virou:
                count_turn[i]+=1
                if count_turn[i] == 15:
                    virou[i]=False
                    count_turn[i]=0
            for j in range(len(monsters[i])):
                monsters[i][j].x+=vel_monster[i]*time
    return virou, vel_monster, count_turn

def kill_monster(monsters, shots, i):
    for c in range(i):
        if shots[i].y<janela.height/2:
            print('aaa')
            for j in range(len(monsters)-1,-1,-1):
                for w in range(len(monsters[j])):
                    if shots[c].collided(monsters[j][w]):
                        shots.pop(c)
                        monsters[j][w].x=100000000
                        monsters[j].pop(w)
                        break



def did_you_win(monsters):
    ganhou=True
    for i in range(len(monsters)):
        if len(monsters[i])!=0:
            ganhou = False
    return ganhou

def game(dif):
    conta_tempo=0
    janela.clear()
    janela.set_title('Jogo')
    janela.set_background_color((0,0,0))
    teclado = Window.get_keyboard()
    shots, count=gerador.generate_shots(dif)
    ship = GameImage('images/ship.png')
    ship.set_position(janela.width / 2 - ship.width, janela.height - ship.height - 10)
    foi = False
    count=0
    monsters = gerador.generate_monsters(dif)
    virou=[False]*len(monsters)
    count_turn=[0]*len(monsters)
    vel_monster=[30]*len(monsters)
    for j in range(len(monsters)):
        for i in range(len(monsters[j])):
            monsters[j][i].set_position(10+52*i,44*j)
            monsters[j][i].set_sequence_time(0,2,500,True)

    while True:
        janela.update()
        janela.set_background_color((0,0,0))
        ship.draw()
        move_ship(ship,janela,teclado)
        for i in range(len(monsters)):
            for j in range(len(monsters[i])):
                monsters[i][j].draw()
                monsters[i][j].update()

        if teclado.key_pressed('space') and conta_tempo==0:
            shoot(shots, teclado, ship,count)
            foi=True
            count+=1
        if foi:
            conta_tempo+=janela.delta_time()
            if conta_tempo>0.4:
                conta_tempo=0
                foi = False
        for i in range(count):
            shots[i].draw()
            move_shot(i,shots, janela)
            #kill_monster(monsters, shots, i)
        virou, vel_monster, count_turn=move_monsters(monsters, janela.delta_time(), virou, vel_monster, count_turn)
        if did_you_win(monsters):
            print('woooooooo')


janela = Window(630,700)
janela.set_title('Space Invaders')
janela.set_background_color((0,0,0))


#o que fazer:
#pra mexer, usar só um virou, que vira todos de uma vez só
#o monstro mais a direita e o mais a esquerda são o parametro
#1) tiro do player matar monstros e otimizar
#2) caso o player mate todos os monstros, muda a fase
#3) placar
#4) tiro do monstro(aleatorio)
#5) 3 vidas para o player, perde vida se tomar tiro, game over se monstros chegarem no fundo