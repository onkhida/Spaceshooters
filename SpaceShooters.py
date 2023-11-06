# WRITTEN BY DANIEL ETA
# Ntoe, if you're reading this, please help me continue development
# I believe the UI can be enhanced. There are also several bugs int the game

import pygame
import time
import sys

pygame.init()

width = 1000
height = 600

screen = pygame.display.set_mode((width,height))
myimg = pygame.image.load("assets/alien101.png")
pygame.display.set_icon(myimg)

def text_objects(text, font):
    textSurface = font.render(text, True, [0,255,255])
    return textSurface, textSurface.get_rect()

def text_objects2(text, font):
    textSurface = font.render(text, True, [255,255,255])
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((width/2),(height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(3)

    # run the next screen!
    play_again()
    
x_list = ['34','34']
y_list = ['500','500']
yes_no = [False, False, True, False]

x_list2 = ['34','34']
y_list2 = ['500','500']
yes_no2 = [False, False, True, False]
deduct_p2 = []

pygame.display.set_caption("SpaceShooters")

clock = pygame.time.Clock()

img = pygame.image.load("assets/player.png")
img = pygame.transform.scale(img, (80,80))

img2 = pygame.image.load("assets/player2.png")
img2 = pygame.transform.scale(img2, (80,80))

background = pygame.image.load("assets/background.png")
background = pygame.transform.scale(background, (width,height))

# loading the bullet
bulletImg = pygame.image.load("assets/defaultbullet.png")
bulletImg_trans = pygame.transform.scale(bulletImg, (10,30))

bulletImg2 = pygame.image.load("assets/defaultbullet2.png")
bulletImg_trans2 = pygame.transform.scale(bulletImg2, (10,30))

# i need some bullet picker for power-up mechanism
#def whichBullet(bullet):
 #   if bullet == 

def blit_obj(x,y):
    screen.blit(img, (x,y))

def blit_obj2(x,y):
    screen.blit(img2, (x,y))

def blit_bg(x,y):
    screen.blit(background, (x,y))

def bullet_obj(objx, objy, objspeed):
    screen.blit(bulletImg_trans, (objx, objy))

def bullet_obj2(objx2, objy2, objspeed2):
    screen.blit(bulletImg_trans2, (objx2, objy2))

def drawing_bad(posx, posy):
    pygame.draw.rect(screen, [255,0,0], (posx, posy, 20, 20), 5)

def drawing_good(posx, posy):
    pygame.draw.rect(screen, [0,255,255], (posx, posy, 20, 20), 5)

def draw_over_all_p1():
    drawing_bad(790, 550)
    drawing_bad(820, 550)
    drawing_bad(850, 550)
    drawing_bad(880, 550)
    drawing_bad(910, 550)
    drawing_bad(940, 550)
    drawing_bad(970, 550)

def draw_over_six_p1():
    drawing_bad(790, 550)
    drawing_bad(820, 550)
    drawing_bad(850, 550)
    drawing_bad(880, 550)
    drawing_bad(910, 550)
    drawing_bad(940, 550)

def draw_over_five_p1():
    drawing_bad(790, 550)
    drawing_bad(820, 550)
    drawing_bad(850, 550)
    drawing_bad(880, 550)
    drawing_bad(910, 550)

def draw_over_four_p1():
    drawing_bad(790, 550)
    drawing_bad(820, 550)
    drawing_bad(850, 550)
    drawing_bad(880, 550)

def draw_over_three_p1():
    drawing_bad(790, 550)
    drawing_bad(820, 550)
    drawing_bad(850, 550)

def draw_over_two_p1():
    drawing_bad(790, 550)
    drawing_bad(820, 550)

def draw_over_one_p1():
    drawing_bad(790, 550)

# Now for player 2
def draw_over_all_p2():
    drawing_bad(790, 50)
    drawing_bad(820, 50)
    drawing_bad(850, 50)
    drawing_bad(880, 50)
    drawing_bad(910, 50)
    drawing_bad(940, 50)
    drawing_bad(970, 50)

def draw_over_six_p2():
    drawing_bad(790, 50)
    drawing_bad(820, 50)
    drawing_bad(850, 50)
    drawing_bad(880, 50)
    drawing_bad(910, 50)
    drawing_bad(940, 50)

def draw_over_five_p2():
    drawing_bad(790, 50)
    drawing_bad(820, 50)
    drawing_bad(850, 50)
    drawing_bad(880, 50)
    drawing_bad(910, 50)

def draw_over_four_p2():
    drawing_bad(790, 50)
    drawing_bad(820, 50)
    drawing_bad(850, 50)
    drawing_bad(880, 50)

def draw_over_three_p2():
    drawing_bad(790, 50)
    drawing_bad(820, 50)
    drawing_bad(850, 50)

def draw_over_two_p2():
    drawing_bad(790, 50)
    drawing_bad(820, 50)

def draw_over_one_p2():
    drawing_bad(790, 50)

def play_again():
    play = True
    area = pygame.draw.rect(screen,[255,255,255],(200,500,100,50))

    while play:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if area.collidepoint(event.pos):
                    main()
                
        screen.fill([255,255,255])
        blit_bg(0,0)

        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("SpaceShooters", largeText)
        TextRect.center = ((width/2),(height/2))
        screen.blit(TextSurf, TextRect)


        smallText = pygame.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = text_objects("Play Again?", smallText)
        TextRect.center = ((width/2),((height/2)+100))
        screen.blit(TextSurf, TextRect)

        pygame.draw.rect(screen,[0,255,64],(200,500,100,50))

        yesText = pygame.font.Font('freesansbold.ttf',40)
        TextSurf, TextRect = text_objects2("YES", yesText)
        TextRect.center = (250,525)
        screen.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(15)


def main():
    draw_over_one_var_p1 = False
    draw_over_two_var_p1 = False
    draw_over_three_var_p1 = False
    draw_over_four_var_p1 = False
    draw_over_five_var_p1 = False
    draw_over_six_var_p1 = False
    draw_over_all_var_p1 = False


    draw_over_one_var_p2 = False
    draw_over_two_var_p2 = False
    draw_over_three_var_p2 = False
    draw_over_four_var_p2 = False
    draw_over_five_var_p2 = False
    draw_over_six_var_p2 = False
    draw_over_all_var_p2 = False
    
    x = 450
    x2 = 450
    y2 = 30
    y = 500
    x_change = 0
    x2_change = 0
    game_over_for_p1 = False
    game_over_for_p2 = False

    # lives and scores for both players
    p1_score = 0
    p2_score = 0
    p1_life = 7
    p2_life = 7

    # getting the center of the current player for the objx ==> This will be constant
    objx = x + (80/5.3)
    # bullet starts at the top of the player 
    objy = y - 40

    objx2 = x + (80/5.3)
    objy2 = y2 + 40 
    
    objspeed = 7
    objspeed2 = 7

    
    start = True

    while start:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                start = False
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    yes_no.append(True)

                # for player2
                if event.key == pygame.K_a:
                    x2_change = -5
                if event.key == pygame.K_d:
                    x2_change = 5
                if event.key == pygame.K_SPACE:
                    yes_no2.append(True)

                    

            # i need some type of stopping mechanism
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    x_list.append(str(x))
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x2_change = 0
                    x_list2.append(str(x2))

        x+=x_change
        x2+=x2_change

        objx = int(x_list[len(x_list) - 1]) + 35
        objx2 = int(x_list2[len(x_list2) - 1]) + 35

        img = pygame.image.load("assets/player.png")
        img = pygame.transform.scale(img, (80,80))

        screen.fill([255,255,255])

        blit_bg(0,0)

        blit_obj(x,y)
        blit_obj2(x2,y2)
        
        pygame.draw.line(screen, [0,128,64], (0,295), (1000,295), 5)
        pygame.draw.line(screen, [255,255,255], (0,300), (1000,300), 5)
        pygame.draw.line(screen, [0,128,64], (0,305), (1000,305), 5)

        # Constantly check if game is over
        if game_over_for_p1:
            message_display("Player 2 wins!")
            game_over_for_p1 = False

        if game_over_for_p2:
            message_display("Player 1 wins!")
            game_over_for_p2 = False

        # find the x value from x_list
        bullet_obj(int(x_list[len(x_list) - 1]) + 35, objy, objspeed)
        if yes_no[len(yes_no)-1] == True:
            objy -= 10


        if objy < -20:
            objy = 500
            yes_no.append(False)

        # now i handle the bullet for p2
        bullet_obj2(int(x_list2[len(x_list2) - 1]) + 35, objy2, objspeed2)
        if yes_no2[len(yes_no2)-1] == True:
            objy2 += 10

        if objy2 > 620:
            objy2 = 30
            yes_no2.append(False)

        # add boundaries
        if x+80 > 1000:
            x = 1000-100
        elif x < 0:
            x = 0 + 20

        # player2
        if x2+80 > 1000:
            x2 = 1000-100
        elif x2 < 0:
            x2 = 0 + 20

        drawing_good(790, 550)
        drawing_good(820, 550)
        drawing_good(850, 550)
        drawing_good(880, 550)
        drawing_good(910, 550)
        drawing_good(940, 550)
        drawing_good(970, 550)

        drawing_good(790, 50)
        drawing_good(820, 50)
        drawing_good(850, 50)
        drawing_good(880, 50)
        drawing_good(910, 50)
        drawing_good(940, 50)
        drawing_good(970, 50)

        if draw_over_one_var_p1:
            draw_over_one_p1()

        if draw_over_two_var_p1:
            draw_over_two_p1()

        if draw_over_three_var_p1:
            draw_over_three_p1()

        if draw_over_four_var_p1:
            draw_over_four_p1()

        if draw_over_five_var_p1:
            draw_over_five_p1()

        if draw_over_six_var_p1:
            draw_over_six_p1()

        if draw_over_all_var_p1:
            draw_over_all_p1()

        # Draw over player 2

        if draw_over_one_var_p2:
            draw_over_one_p2()

        if draw_over_two_var_p2:
            draw_over_two_p2()

        if draw_over_three_var_p2:
            draw_over_three_p2()

        if draw_over_four_var_p2:
            draw_over_four_p2()

        if draw_over_five_var_p2:
            draw_over_five_p2()

        if draw_over_six_var_p2:
            draw_over_six_p2()

        if draw_over_all_var_p2:
            draw_over_all_p2()

        # now for collissions with bullets

        # p1.bullet hits p2.player #
        if objy >= y2 and objy <= y2+80:
            
            # the bullet is in the y zone
            # need more accuracy so wil use '=='
            if objx >= x2 and objx <= x2+80:
                
                # also in the x zone
                print("Ouch")
                p1_score += 5
                p2_life -= 0.1

                print(p1_score)
                print(p2_life)

                # were i stopped

                if p2_life < 0:
                    draw_over_all_var_p2 = True

                if p2_life < 1:
                    draw_over_six_var_p2 = True
                    
                if p2_life < 2:
                    draw_over_five_var_p2 = True
                    
                if p2_life < 3:
                    draw_over_four_var_p2 = True
                    
                if p2_life < 4:
                    draw_over_three_var_p2 = True
                    
                if p2_life < 5:
                    draw_over_two_var_p2 = True
                    
                if p2_life < 6:
                    draw_over_one_var_p2 = True

                if p2_life < 0:
                    game_over_for_p2 = True

        # p2.bullet hits p1.player #
        if objy2 >= y and objy2 <= y+80:
            
            # the bullet is in the y zone
            # need more accuracy so wil use '=='
            if objx2 >= x and objx2 <= x+80:
                
                # also in the x zone
                print("Ouchiee")
                p2_score += 5
                p1_life -= 0.1

                print(p1_life)

                if p1_life < 0:
                    draw_over_all_var_p1 = True

                if p1_life < 1:
                    draw_over_six_var_p1 = True
                    
                if p1_life < 2:
                    draw_over_five_var_p1 = True
                    
                if p1_life < 3:
                    draw_over_four_var_p1 = True
                    
                if p1_life < 4:
                    draw_over_three_var_p1 = True
                    
                if p1_life < 5:
                    draw_over_two_var_p1 = True
                    
                if p1_life < 6:
                    draw_over_one_var_p1 = True

                if p1_life < 0:
                    game_over_for_p1 = True

        pygame.display.update()

if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()

