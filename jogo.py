from PPlay.window import *
from PPlay.gameobject import *
from PPlay.gameimage import *
from PPlay.sprite import *
import gerador
import random

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
                monsters[i][j].y+=17
            monsters[i][j].x+=(monster_speed+(20*fase))*time

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

def shoot(tiros_disponiveis, tiros_dados, object):
    if len(tiros_disponiveis)>0:
        tiros_dados.append(tiros_disponiveis[0])
        tiros_disponiveis.pop(0)
        tiros_dados[-1].set_position(object.x+object.width/2-1.5, object.y-object.height/3)
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
                break


def move_shot_monster(tiros_dados, time, ship, vidas):
    clean_shots(tiros_dados)
    for i in range(len(tiros_dados)):
        tiros_dados[i].y+=200*time
        tiros_dados[i].draw()
        stop_shot(tiros_dados , i)
        vidas = kill_ship(ship,tiros_dados, i, vidas)
        i+=1
    return vidas



def kill_ship(ship, tiros_dados, i, vidas):
    if tiros_dados[i].collided(ship):
        tiros_dados[i].y=100000
        vidas-=1
    return vidas

def supershot(super_bullet, object):
    super_bullet.set_position(object.x+object.width/2-1.5, object.y-object.height/3)
    super_bullet.draw()

def move_supershot(super_bullet, time):
    if super_bullet.y>-40:
        super_bullet.y-=200*time
        super_bullet.draw()
        return True
    return False

def super_kill(super_bullet, monsters):
    global pontuacao
    for j in range(len(monsters)):
        count = 0
        for object in monsters[j]:
            if super_bullet.collided(object):
                object.x=100000
                monsters[j].pop(count)
                pontuacao+=1
            else:
                count+=1


def end_game():
    arq=open('ranking.txt', 'a')
    nome=input()
    pont=str(pontuacao)+' '+nome+'/n'
    arq.close()


def game(dif, fase, vidas):
    janela = Window(630,700)
    janela.clear()
    janela.set_title('Space Invaders')
    teclado = Window.get_keyboard()

    #preparar os game objects
    fundo = GameImage('images/fundo2.png')
    monsters = gerador.generate_monsters(fase)
    monster_speed = 210*dif/3
    tiros_dados = []
    tiros_disponiveis, contagem_de_tiros = gerador.generate_shots(dif)
    ship = GameImage('images/ship.png')
    ship.set_position(janela.width / 2 - ship.width, janela.height - ship.height - 10)
    tiros_dados_monstros = []
    tiros_disponiveis_monstros, contagem_de_tiros_monstro = gerador.generate_shots_monsters(dif)
    gameover = GameImage('images/game over.png')
    gameover.set_position(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    super_bullet = GameImage('images/super_bullet.png')

    #variaveis para serem usadas durante o jogo
    virou = False
    count_turn = 0
    foi = False
    count_shoot = 0
    count_monster_shoot = 0
    super_tiro = False
    super_count = 0
    loading = False

    for j in range(len(monsters)):
        for i in range(len(monsters[j])):
            monsters[j][i].set_position(10+52*i,44*j)
            monsters[j][i].set_sequence_time(0,2,500,True)
    while True:
        janela.update()
        fundo.draw()
        ship.draw()
        time = janela.delta_time()
        count_monster_shoot+=janela.delta_time()
        for i in range(len(monsters)):
            for j in range(len(monsters[i])):
                monsters[i][j].draw()
                monsters[i][j].update()
        if teclado.key_pressed('SPACE') and count_shoot==0:
            shoot(tiros_disponiveis, tiros_dados, ship)
            foi = True
            count_shoot+=time
            loading = True
        if teclado.key_pressed('SPACE') and loading:
            print(super_count)
            super_count+=time
            foi = True
            count_shoot = 0
            if super_count>1.5:
                super_tiro = True
                loading = False
                count_shoot = 0
                foi = True
                supershot(super_bullet, ship)
                super_count = 0
        if not teclado.key_pressed('SPACE'):
            loading = False
        if foi:
            count_shoot+=time
            if count_shoot>0.4:
                foi = False
                count_shoot=0
        if super_tiro:
            super_tiro = move_supershot(super_bullet, time)
            super_kill(super_bullet, monsters)
        if not super_tiro and not loading:
            super_count = 0
        if count_monster_shoot>3:
            x=random.randint(0,len(monsters)-1)
            y=random.randint(0,len(monsters[x])-1)
            shoot(tiros_disponiveis_monstros, tiros_dados_monstros, monsters[x][y])
            count_monster_shoot = 0
        if len(tiros_dados)>0:
            move_shot(tiros_dados,time, monsters)
        if len(tiros_dados_monstros)>0:
            vidas = move_shot_monster(tiros_dados_monstros,time, ship, vidas)
        move_ship(ship, teclado, time)
        count_turn, virou, monster_speed = move_monsters(monsters,virou, count_turn, monster_speed, time, fase)
        janela.draw_text("%d vidas"%vidas, 0,0, 30, (200, 200, 200), 'Arial', False, False)
        if len(monsters)==0:
            if fase==6:
                end_game()
            else:
                game(dif, fase+1, vidas)
            break
        if vidas==0 or monsters[-1][0].y+monsters[-1][0].height>=ship.y:
            janela.clear()
            janela.delay(100)
            return pontuacao
