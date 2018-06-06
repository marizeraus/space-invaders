from PPlay.window import *
from PPlay.gameimage import *
import jogo


def ranking(janela):
    mouse = Window.get_mouse()
    janela.clear()
    janela.set_background_color((0,0,0))
    janela.set_title('Ranking')
    rankk=GameImage('images/ranking title.png')
    rankk.set_position(155,0)
    back = GameImage('images/back button.png')
    back2 = GameImage('images/back button2.png')
    back.set_position(193,600)
    back2.set_position(193,600)
    while True:
        janela.update()
        rankk.draw()
        if mouse.is_over_object(back):
            back2.draw()
            if mouse.is_button_pressed(1):
                inicio(janela)
        else:
            back.draw()


def dificuldade(janela, dif):
    mouse = Window.get_mouse()
    janela.clear()
    janela.set_background_color((0,0,0))
    janela.set_title('Dificuldades')
    diff = GameImage('images/dif title.png')
    diff.set_position(91,0)
    easy = GameImage('images/easy button.png')
    easy2 = GameImage('images/easy button2.png')
    medium = GameImage('images/medium button.png')
    medium2 = GameImage('images/medium button2.png')
    hard = GameImage('images/hard button.png')
    hard2 = GameImage('images/hard button2.png')
    back = GameImage('images/back button.png')
    back2 = GameImage('images/back button2.png')
    easy2.set_position(193,150)
    easy.set_position(193,150)
    medium2.set_position(193,230)
    medium.set_position(193,230)
    hard2.set_position(193,310)
    hard.set_position(193,310)
    back.set_position(193,600)
    back2.set_position(193,600)
    start_button=GameImage('images/start button.png')
    start_button2=GameImage('images/start button2.png')
    start_button.set_position(193,525)
    start_button2.set_position(193,525)
    while True:
        janela.update()
        diff.draw()
        hard.draw()
        if mouse.is_over_object(easy):
            easy2.draw()
            if mouse.is_button_pressed(1):
                dif=1
        else:
            easy.draw()
        if mouse.is_over_object(medium):
            medium2.draw()
            if mouse.is_button_pressed(1):
                dif=2
        else:
            medium.draw()
        if mouse.is_over_object(hard):
            hard2.draw()
            if mouse.is_button_pressed(1):
                dif=3
        else:
            hard.draw()
        if mouse.is_over_object(back):
            back2.draw()
            if mouse.is_button_pressed(1):
                inicio(janela)
        else:
            back.draw()
        if dif==1:
            easy2.draw()
        elif dif==2:
            medium2.draw()
        elif dif==3:
            hard2.draw()
        if mouse.is_over_object(start_button):
            start_button2.draw()
            if mouse.is_button_pressed((1)):
                jogo.game(dif)
        else:
            start_button.draw()


def inicio(janela):
    janela.clear
    janela.set_title('Menu')
    janela.set_background_color((0,0,0))
    titulo = GameImage('images/logo.png')
    titulo.set_position(65,60)
    mouse = Window.get_mouse()
    #initial buttons
    start_button=GameImage('images/start button.png')
    dif_button=GameImage('images/dificuldades.png')
    rank_button=GameImage('images/ranking button.png')
    exit_button=GameImage('images/exit button.png')
    #colorful buttons
    start_button2=GameImage('images/start button2.png')
    dif_button2=GameImage('images/dificuldades2.png')
    rank_button2=GameImage('images/ranking button2.png')
    exit_button2=GameImage('images/exit button2.png')
    #setting button positions
    start_button.set_position(193,320)
    dif_button.set_position(193,390)
    rank_button.set_position(193,460)
    exit_button.set_position(193,530)

    #por default, dificuldade = easy:
    dif=1

    while True:
        janela.update()
        titulo.draw()
        if mouse.is_over_object(start_button):
            start_button2.set_position(193,320)
            start_button2.draw()
            if mouse.is_button_pressed((1)):
                jogo.game(dif)
        else:
            start_button.draw()
        if mouse.is_over_object(dif_button):
            dif_button2.set_position(193,390)
            dif_button2.draw()
            if mouse.is_button_pressed((1)):
                dif=dificuldade(janela, dif)
        else:
            dif_button.draw()
        if mouse.is_over_object(rank_button):
            rank_button2.set_position(193,460)
            rank_button2.draw()
            if mouse.is_button_pressed((1)):
                ranking(janela)
        else:
            rank_button.draw()
        if mouse.is_over_object(exit_button):
            exit_button2.set_position(193,530)
            exit_button2.draw()
            if mouse.is_button_pressed((1)):
                janela.close()
        else:
            exit_button.draw()

janela = Window(630,700)
janela.set_title('Menu')
janela.set_background_color((0,0,0))
dif = inicio(janela)
