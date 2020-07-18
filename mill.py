import pygame
import numpy as np
import time

#INITIALISIERUNG
pygame.font.init()
pygame.init()

#MUSIK
pygame.mixer.music.load('Jazz_Club.mp3')
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(.025)

#VARIABLEN
FPS = 60
s_width = 1100      #Größe des Fensters
s_height = 700      #Größe des Fensters
mill_middle_x = 500    #Koordinaten des Mühlefelds
mill_middle_y = 600   #Koordinaten des Mühlefelds
BLACK = (0,0,0)
block_size = 80


#STEINE GRÖßE
b_stone_width = 200
b_stone_height = 200

#FELD UND STEIN KOORDINATEN IM FENSTER
mill_x = (s_width - mill_middle_x) // 2
mill_y = s_height - mill_middle_y
white_stone_x = mill_x // 2
white_stone_y = mill_y + b_stone_height
black_stone_x = mill_x * 3
black_stone_y = mill_y + b_stone_height

#FENSTER ERSTELLUNG UD CLOCK
win = pygame.display.set_mode((s_width, s_height))  # pygame.FULLSCREEN
pygame.display.set_caption("Mill by JJ and Mika")
clock = pygame.time.Clock()

#BILDER: SPIELFELD & STEINE
mill_bg = pygame.image.load('bg_mill.png')
white_stone = pygame.image.load('stone_white.png')
black_stone = pygame.image.load('stone_black.png')

#ABFRAGE DER MÖGLICHEN POSITIONEN
pos1 = [(mill_x + 10), mill_y]
pos2 = [(mill_middle_x + 25), mill_y]
pos3 = [(mill_middle_x + 240), mill_y]

pos4 = [((mill_middle_x + 25) - 145), mill_y + 80]
pos5 = [(mill_middle_x + 25), (mill_y + 80)]
pos6 = [((mill_middle_x + 25) + 145), (mill_y + 80)]

pos7 = [((mill_middle_x + 25) - 80), (mill_y + 145)]
pos8 = [(mill_middle_x + 25), (mill_y + 145)]
pos9 = [((mill_middle_x + 25) + 80), (mill_y + 145)]

pos10 = [(mill_x + 10), (mill_y + 225)]
pos11 = [((mill_middle_x + 25) - 145), (mill_y + 225)]
pos12 = [((mill_middle_x + 25) - 80), (mill_y + 225)]
pos13 = [((mill_middle_x + 25) + 80), (mill_y + 225)]
pos14 = [((mill_middle_x + 25) + 145), (mill_y + 225)]
pos15 = [(mill_middle_x + 240), (mill_y + 225)]

pos16 = [((mill_middle_x + 25) - 80), ((mill_y + 450) - 145)]
pos17 = [(mill_middle_x + 25), ((mill_y + 450) - 145)]
pos18 = [((mill_middle_x + 25) + 80), (mill_y + 450) - 145]

pos19 = [((mill_middle_x + 25) - 145), (mill_y + 450) - 80]
pos20 = [(mill_middle_x + 25), (mill_y + 450) - 80]
pos21 = [((mill_middle_x + 25) + 145), (mill_y + 450) - 80]

pos22 = [(mill_x + 10), (mill_y + 450)]
pos23 = [(mill_middle_x + 25), (mill_y + 450)]
pos24 = [(mill_middle_x + 240), (mill_y + 450)]

poslst = [None] * 25
neighbourlst = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11), (12, 13, 14), (15, 16, 17), (18, 19, 20), (21, 22, 23),
                (0, 9, 21), (3, 10, 18), (6, 11, 15), (1, 4, 7), (16, 19, 22), (8, 12, 17), (5, 13, 20), (2, 14, 23)]
listTrueFalse = [False] * 16


#OBERFLÄCHE 1
def draw(surface):
    surface.fill((197, 142, 97))
    font = pygame.font.SysFont('hooge 05_54', 40, bold=False)
    label = font.render('Mill by JJ and Mika', 1, (0, 0, 0))
    surface.blit(label, (mill_x + mill_middle_x / 2 - (label.get_width() / 2), 30))  # (1600-705)/2   || (900-705)/2'''
    win.blit(mill_bg, (mill_x, mill_y))
    pygame.transform.scale(black_stone, (30, 30))
    pygame.transform.scale(white_stone, (30, 30))
    win.blit(black_stone, (black_stone_x, black_stone_y))
    win.blit(white_stone, (white_stone_x, white_stone_y))
    instructionWhite('Weiß [Linke Maustaste]', 20, (0, 0, 0), win)
    instructionBlack('Schwarz [Rechte Maustaste]', 20, (0, 0, 0), win)
    pygame.display.update()


#ÖBERFLÄCHE 2
def drawGrid():
    blockSize = 38
    for x in range(mill_x):
        for y in range(mill_y):
            rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
            pygame.draw.rect(mill_bg, BLACK, rect, 1)

#PRESS ANY KEY SCREEN FUNKTION
def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont('hooge 05_54', size, bold=False)
    label = font.render(text, 1, color)
    surface.blit(label, (
        mill_x + mill_middle_x / 2 - (label.get_width() / 2), mill_y + mill_middle_y / 2 - label.get_height() / 2))

def instructionWhite(text, size, color, surface):
    font = pygame.font.SysFont('arial', size, bold=True)
    label = font.render(text, 1, color)
    surface.blit(label, ((white_stone_x - 100), (white_stone_y - 145)))

def instructionBlack(text, size, color, surface):
    font = pygame.font.SysFont('arial', size, bold=True)
    label = font.render(text, 1, color)
    surface.blit(label, ((black_stone_x - 100), (black_stone_y - 145)))

def beginningOV(text, size, color, surface):
    font = pygame.font.SysFont('hooge 05_54', size, bold=False)
    label = font.render(text, 1, color)
    surface.blit(label, (
        mill_x + mill_middle_x / 2 - (label.get_width() / 2), (mill_y + mill_middle_y / 2 - label.get_height() / 2) + 225))

def quitScreen1(text, size, color, surface):
    font = pygame.font.SysFont('arial', size, bold=True)
    label = font.render(text, 1, color)
    surface.blit(label, (
        mill_x + mill_middle_x / 2 - (label.get_width() / 2), (mill_y - 80) + mill_middle_y / 2 - label.get_height() / 2))

def quitScreen2(text, size, color, surface):
    font = pygame.font.SysFont('arial', size, bold=True)
    label = font.render(text, 1, color)
    surface.blit(label, (
        mill_x + mill_middle_x / 2 - (label.get_width() / 2), (mill_y - 10) + mill_middle_y / 2 - label.get_height() / 2))


def positionSearch(search):
    lst = [pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos11, pos12, pos13,
            pos14, pos15, pos16, pos17, pos18, pos19, pos20, pos21, pos22, pos23, pos24]
    search = list(pygame.mouse.get_pos())

    lst_np = np.asarray(lst)
    distances = np.linalg.norm(search - lst_np, axis=1)
    nearest_pos_idx = np.argmin(distances)
    nearest_pos = lst_np[nearest_pos_idx]
    return nearest_pos, nearest_pos_idx


#AUSFÜHRUNG
def gameCycle():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameQuit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                gesucht = pygame.mouse.get_pos()
                cord, idx = positionSearch(gesucht)
                pos = list(cord)
                if poslst[idx] == None:
                    if event.button == 1:
                        win.blit(white_stone, pos)
                        poslst[idx] = "W"
                        pygame.display.update()
                    if event.button == 3:
                        win.blit(black_stone, pos)
                        poslst[idx] = "B"
                        pygame.display.update()
                print(poslst)
                for index in range(len(neighbourlst)):
                    counterWhite = 0
                    counterBlack = 0
                    placing_W_Stone = 9
                    placing_B_Stone = 9
                    for tupleValue in neighbourlst[index]:
                        if poslst[tupleValue] == "W":
                            counterWhite += 1
                            if counterWhite == 3 and not (listTrueFalse[index]):
                                listTrueFalse[index] = True
                                print("Mühle weiß")
                                counterWhite = 0
                                placing_W_Stone -= 1
                        if poslst[tupleValue] == "B":
                            counterBlack += 1
                            if counterBlack == 3 and not (listTrueFalse[index]):
                                listTrueFalse[index] = True
                                print("Mühle schwarz")
                                counterBlack = 0
                                placing_B_Stone -= 1


clock.tick(FPS)

#START
def startingscreen():
    start = True
    win.fill((0, 0, 0))
    draw_text_middle('Drücke sie die Leertaste, um das Spiel zu starten', 40, (255, 255, 255), win)
    pygame.display.update()
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                start = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    draw(win)
                    beginning()



def beginning():
    begin = True
    while begin:
        beginningOV("Weiss beginnt [beliebige Taste]", 30, (0, 0, 0), win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                draw(win)
                gameCycle()

def gameQuit():
    quit = True
    while quit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Willst du das Souek wirklich beenden? \n JA[ENTER] || NEIN[SPACE] ")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    gameCycle()
        pygame.display.update()

        #quitScreen ausblenden

#SPIELLOGIK

startingscreen()