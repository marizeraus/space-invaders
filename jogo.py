from PPlay.window import *
from PPlay.gameobject import *
from PPlay.gameimage import *
from PPlay.sprite import *
import gerador

WINDOW_HEIGHT = 700
WINDOW_WIDTH = 630
pontuacao = 0

def move_ship(ship, teclado, time):
    #funcao para movimentar a nave seguindo o input do teclado
    vel_ship=190

    if ship.x>-2*ship.width/3 and ship.x<WINDOW_WIDTH+ship.width/3:
        if teclado.key_pressed('LEFT'):
            ship.x-=vel_ship*time
        if teclado.key_pressed('RIGHT'):
            ship.x+=vel_ship*time

    elif ship.x>WINDOW_WIDTH+ship.width/3:
        ship.x=0-5

    else:
        ship.x=WINDOW_WIDTH


def move_monsters(monsters, virou, count_turn, monster_speed, time, fase):
    #funcao para movimentar os monstros
    clean_monsters(monsters)
    if virou:
        count_turn+=1
        if count_turn==40:
            virou = False
            count_turn=0
    else:
        virou = should_i_stay_or_should_i_turn(monsters)
        count_turn = 0
        if virou:
            monster_speed=-monster_speed

    for i in range(len(monsters)):
        for j in range(len(monsters[i])):
            if virou and count_turn==0:
                monsters[i][j].y+=10
            monsters[i][j].x+=monster_speed*time*fase/2

    return count_turn, virou, monster_speed


def clean_monsters(monsters):
    count=0
    for linha in monsters:
        if len(linha)==0:
            monsters.pop(count)
        else:
            count+=1

def should_i_stay_or_should_i_turn(monsters):
    #identifica se os monstros devem virar

    for i in range(len(monsters)):
        if monsters[i][0].x<0 or (monsters[i][0].x+monsters[i][0].width)>WINDOW_WIDTH or (monsters[i][-1].x)<0 or (monsters[i][-1].x+monsters[i][-1].width) >WINDOW_WIDTH:
            return True

    return False


def move_shot(tiros_dados, time, monsters):
    clean_shots(tiros_dados)
    for i in range(len(tiros_dados)):
        tiros_dados[i].y-=200*time
        tiros_dados[i].draw()
        stop_shot(tiros_dados , i)
        kill_monster(monsters,tiros_dados, i)
        i+=1

def clean_shots(tiros_dados):
    count=0
    for i in tiros_dados:
        if i.y>10000:
            tiros_dados.pop(count)
        else:
            count+=1

def shoot(tiros_disponiveis, tiros_dados, ship):
    if len(tiros_disponiveis)>0:
        tiros_dados.append(tiros_disponiveis[0])
        tiros_disponiveis.pop(0)
        tiros_dados[-1].set_position(ship.x+ship.width/2-1.5, ship.y-ship.height/3)
        tiros_dados[-1].draw()


def stop_shot(tiros_dados, i):
    if tiros_dados[i].y<-10:
        tiros_dados[i].y=100000



def kill_monster(monsters, tiros_dados, i):
    global pontuacao
    for j in range(len(monsters)):
        for w in range(len(monsters[j])):
            if tiros_dados[i].collided(monsters[j][w]):
                tiros_dados[i].y=100000
                monsters[j][w].x=100000
                monsters[j].pop(w)
                pontuacao+=1
                print(pontuacao)
                break


def game(dif, fase, vidas):
    janela = Window(630,700)
    janela.clear()
    janela.set_title('Space Invaders')
    teclado = Window.get_keyboard()

# preparar os game objects
    fundo = GameImage('images/fundo2.png')
    monsters = gerador.generate_monsters(fase)
    monster_speed = 220*dif/3
    tiros_dados = []
    tiros_disponiveis, contagem_de_tiros = gerador.generate_shots(dif)
    ship = GameImage('images/ship.png')
    ship.set_position(janela.width / 2 - ship.width, janela.height - ship.height - 10)

    #variaveis para serem usadas durante o jogo
    virou = False
    count_turn = 0
    foi = False
    count_shoot = 0

    for j in range(len(monsters)):
        for i in range(len(monsters[j])):
            monsters[j][i].set_position(10+52*i,44*j)
            monsters[j][i].set_sequence_time(0,2,500,True)
    while True:
        janela.update()
        fundo.draw()
        ship.draw()
        time = janela.delta_time()
        for i in range(len(monsters)):
            for j in range(len(monsters[i])):
                monsters[i][j].draw()
                monsters[i][j].update()
        if teclado.key_pressed('SPACE') and count_shoot==0:
            shoot(tiros_disponiveis, tiros_dados, ship)
            foi = True
            count_shoot+=time
        if foi:
            count_shoot+=time
            if count_shoot>0.4:
                foi = False
                count_shoot=0
        if len(tiros_dados)>0:
            move_shot(tiros_dados,time, monsters)
        move_ship(ship, teclado, time)
        count_turn, virou, monster_speed = move_monsters(monsters,virou, count_turn, monster_speed, time, fase)
        if len(monsters)==0:
            if fase==6:
                win()
            else:
                game(dif, fase+1, vidas)
            break
    if vidas==0:
        arq=open('ranking.txt', 'a')
        nome=input()
        pont=str(pontuacao)+' '+nome+'/n'
        arq.close()
