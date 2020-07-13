import pygame
import numpy as np

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




#OBERFLÄCHE 1
def draw(surface):
    surface.fill((197, 142, 97))
    font = pygame.font.SysFont('arial', 40, bold=True)
    label = font.render('Mill by JJ and Mika', 1, (0, 0, 0))
    surface.blit(label, (mill_x + mill_middle_x / 2 - (label.get_width() / 2), 30))  # (1600-705)/2   || (900-705)/2'''
    win.blit(mill_bg, (mill_x, mill_y))
    pygame.transform.scale(black_stone, (30, 30))
    pygame.transform.scale(white_stone, (30, 30))
    win.blit(black_stone, (black_stone_x, black_stone_y))
    win.blit(white_stone, (white_stone_x, white_stone_y))
    instructionWhite('Weiß [Linke Maustaste]', 20, (255, 255, 255), win)
    instructionBlack('Schwarz [Rechte Maustaste]', 20, (255, 255, 255), win)
    pygame.display.flip()

    # win.blit(black_stone, pos1)
    # win.blit(black_stone, pos2)
    # win.blit(black_stone, pos3)
    # win.blit(black_stone, pos4)
    # win.blit(black_stone, pos5)
    # win.blit(black_stone, pos6)
    # win.blit(black_stone, pos7)
    # win.blit(black_stone, pos8)
    # win.blit(black_stone, pos9)
    # win.blit(black_stone, pos10)
    # win.blit(black_stone, pos11)
    # win.blit(black_stone, pos12)
    # win.blit(black_stone, pos13)
    # win.blit(black_stone, pos14)
    # win.blit(black_stone, pos15)
    # win.blit(black_stone, pos16)
    # win.blit(black_stone, pos17)
    # win.blit(black_stone, pos18)
    # win.blit(black_stone, pos19)
    # win.blit(black_stone, pos20)
    # win.blit(black_stone, pos21)
    # win.blit(black_stone, pos22)
    # win.blit(black_stone, pos23)
    # win.blit(black_stone, pos24)


#ÖBERFLÄCHE 2
def drawGrid():
    blockSize = 38
    for x in range(mill_x):
        for y in range(mill_y):
            rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
            pygame.draw.rect(mill_bg, BLACK, rect, 1)


#PRESS ANY KEY SCREEN FUNKTION
def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont('arial', size, bold=True)
    label = font.render(text, 1, color)
    surface.blit(label, (
        mill_x + mill_middle_x / 2 - (label.get_width() / 2), mill_y + mill_middle_y / 2 - label.get_height() / 2))


def instructionWhite(text, size, color, surface):
    font = pygame.font.SysFont('arial', size, bold=True)
    label = font.render(text, 1, (0,0,0))
    surface.blit(label, ((white_stone_x - 100), (white_stone_y - 145)))

def instructionBlack(text, size, color, surface):
    font = pygame.font.SysFont('arial', size, bold=True)
    label = font.render(text, 1, (0,0,0))
    surface.blit(label, ((black_stone_x - 100), (black_stone_y - 145)))

def beginningOV(text, size, color, surface):
    font = pygame.font.SysFont('arial', size, bold=True)
    label = font.render(text, 1, color)
    surface.blit(label, (
        mill_x + mill_middle_x / 2 - (label.get_width() / 2), (mill_y + mill_middle_y / 2 - label.get_height() / 2) + 225))

def positionSearch(search):
    lst = [pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos11, pos12, pos13,
            pos14, pos15, pos16, pos17, pos18, pos19, pos20, pos21, pos22, pos23, pos24]
    search = list(pygame.mouse.get_pos())

    lst_np = np.asarray(lst)
    distances = np.linalg.norm(search - lst_np, axis=1)
    nearest_pos_idx = np.argmin(distances)
    nearest_pos = lst_np[nearest_pos_idx]
    return nearest_pos

#AUSFÜHRUNG
def main():
    left_mouse_down = False
    right_mouse_down = False
    count = 9
    pygame.mouse.set_visible(True)

    draw(win)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    left_mouse_down = True
                    if left_mouse_down:
                        gesucht = pygame.mouse.get_pos()
                        pos = list(positionSearch(gesucht))
                        win.blit(white_stone, pos)
                        pygame.display.update()

                if event.button == 3:
                    right_mouse_down = True
                    if right_mouse_down:
                        gesucht = pygame.mouse.get_pos()
                        pos = list(positionSearch(gesucht))
                        win.blit(black_stone, pos)
                        pygame.display.update()


    clock.tick(FPS)

#START
def startingscreen():
    run = True
    win.fill((0, 0, 0))
    draw_text_middle('Drücke sie die Leertaste, um das Spiel zu starten', 30, (255, 255, 255), win)
    pygame.display.update()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    draw(win)
                    beginning()

def beginning():

   run = True
   while run:
    beginningOV("Weiss beginnt [beliebige Taste]", 60, (0, 0, 0), win)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
        if event.type == pygame.KEYDOWN:
            main()

#SPIELLOGIK

startingscreen()
