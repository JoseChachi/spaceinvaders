import pygame
import sys
import random as rd
pygame.init()

# INTEGRANTES:
# → Nicolás Mateo Arroyo Chávez
# → José Rafael Chachi Rodriguez
# → Nicolás de Loayza
# → José Eduardo Condori Palomino

# LINK DEL VIDEO:
# → https://acortar.link/qHjuiY

# Set the resolution
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Set the bg
DISPLAY = pygame.display.set_mode(WINDOW_SIZE)
bgMenu = pygame.image.load("screenpantalla.png")

#Set the bgeasy
bgeasy = pygame.image.load("bgeasy.png")
BGEASY = pygame.transform.scale(bgeasy,WINDOW_SIZE)

bgmedium = pygame.image.load("bgmedium.jpg")
BGMEDIUM = pygame.transform.scale(bgmedium,WINDOW_SIZE)

bghard = pygame.image.load("bghard.jpg")
BGHARD = pygame.transform.scale(bghard,WINDOW_SIZE)

bghardcore = pygame.image.load("bghardcore.jpg")
BGHARDCORE = pygame.transform.scale(bghardcore,WINDOW_SIZE)

easyBG = pygame.transform.scale(bgeasy, (180, 80) )

mediumBG = pygame.transform.scale(bgmedium, (180, 80))

hardBG = pygame.transform.scale(bghard,(180, 80))

hardcoreBG = pygame.transform.scale(bghardcore,(180, 80))
#Set the ship
sizeSHIPX, sizeSHIPY = 50,50
ship = pygame.image.load("ship.png")
SHIP = pygame.transform.scale(ship,(sizeSHIPX,sizeSHIPY))


#Set the bullet
bullet = pygame.image.load("bullet.png")
BULLET = pygame.transform.scale(bullet,(15,15))

#Set the bullet of the st monster
bulletmonster1 = pygame.image.load("bullet_1.png")
bulletmonster2 = pygame.image.load("bullet_2.png")
bulletmonster3 = pygame.image.load("bullet_3.png")
bulletmonster4 = pygame.image.load("bullet_4.png")
# Resize the image
resizedBgMenu = pygame.transform.scale(bgMenu, WINDOW_SIZE)

DISPLAY.blit(resizedBgMenu, (0, 0))

pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()

title_font = pygame.font.Font("04B_30__.TTF", 52)
other_font = pygame.font.Font("ARCADEPI.TTF", 24)
other_font2 = pygame.font.Font("ARCADEPI.TTF", 36)
other_font3 = pygame.font.Font("ARCADEPI.TTF", 120)

options_font = pygame.font.Font("04B_30__.TTF", 48)
ranking_font = pygame.font.Font("04B_30__.TTF", 48)
credits_font = pygame.font.Font("04B_30__.TTF", 48)
resolution_options_font = pygame.font.Font("04B_30__.TTF", 48)


shoot_sound = pygame.mixer.Sound("shoot.wav")
music_status = 1




def main_menu():
    point = 0

    while True:
        DISPLAY.blit(resizedBgMenu, (0, 0))

        title = title_font.render('SPACE INVADERS', True, (255, 255, 255))

        if point == 0:
            start_option = other_font.render('START GAME', True, (255, 255, 0))
            options_option = other_font.render('OPTIONS', True, (255, 255, 255))
            ranking_option = other_font.render('RECORD', True, (255, 255, 255))
            credits_option = other_font.render('CREDITS', True, (255, 255, 255))
            exit_option = other_font.render('EXIT GAME', True, (255, 255, 255))
        elif point == 1:
            start_option = other_font.render('START GAME', True, (255, 255, 255))
            options_option = other_font.render('OPTIONS', True, (255, 255, 0))
            ranking_option = other_font.render('RECORD', True, (255, 255, 255))
            credits_option = other_font.render('CREDITS', True, (255, 255, 255))
            exit_option = other_font.render('EXIT GAME', True, (255, 255, 255))

        elif point == 2:
            start_option = other_font.render('START GAME', True, (255, 255, 255))
            options_option = other_font.render('OPTIONS', True, (255, 255, 255))
            ranking_option = other_font.render('RECORD', True, (255, 255, 0))
            credits_option = other_font.render('CREDITS', True, (255, 255, 255))
            exit_option = other_font.render('EXIT GAME', True, (255, 255, 255))

        elif point == 3:
            start_option = other_font.render('START GAME', True, (255, 255, 255))
            options_option = other_font.render('OPTIONS', True, (255, 255, 255))
            ranking_option = other_font.render('RECORD', True, (255, 255, 255))
            credits_option = other_font.render('CREDITS', True, (255, 255, 0))
            exit_option = other_font.render('EXIT GAME', True, (255, 255, 255))

        elif point == 4:
            start_option = other_font.render('START GAME', True, (255, 255, 255))
            options_option = other_font.render('OPTIONS', True, (255, 255, 255))
            ranking_option = other_font.render('RECORD', True, (255, 255, 255))
            credits_option = other_font.render('CREDITS', True, (255, 255, 255))
            exit_option = other_font.render('EXIT GAME', True, (255, 255, 0))
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 200))
        start_option_rect = start_option.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
        options_option_rect = options_option.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 ))
        ranking_option_rect = ranking_option.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
        credits_option_rect = credits_option.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100))
        exit_option_rect = exit_option.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 150))

        DISPLAY.blit(title, title_rect)
        DISPLAY.blit(start_option, start_option_rect)
        DISPLAY.blit(options_option, options_option_rect)
        DISPLAY.blit(ranking_option, ranking_option_rect)
        DISPLAY.blit(credits_option, credits_option_rect)
        DISPLAY.blit(exit_option, exit_option_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    point = point + 1
                elif event.key == pygame.K_UP:
                    point = point - 1
                elif event.key == pygame.K_RETURN:

                    if point == 0:
                        selectDiff()

                    if point == 1:
                        options_menu()

                    if point == 2:
                        record_menu()

                    if point == 3:
                        credits_menu()

                    if point == 4:
                        pygame.quit()
                        sys.exit()

        point = point % 5
        pygame.display.update()

def record_menu():
    with open('ranking.txt') as f:
        lines = f.readlines()
    names = ["", "", "", "", ""]
    for line in lines:
        names.insert(0, line[0: len(line) - 1])
    #print(names)
    while True:
        DISPLAY.blit(resizedBgMenu, (0, 0))

        record_title = title_font.render("LAST 5 PLAYERS", True, (255, 255, 255))
        record_title_rect = record_title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 300))
        DISPLAY.blit(record_title, record_title_rect)

        first_player = other_font2.render("1. " + names[0], True, (255, 255, 255))
        second_player = other_font2.render("2. " + names[1], True, (255, 255, 255))
        third_player = other_font2.render("3. " + names[2], True, (255, 255, 255))
        fourth_player = other_font2.render("4. " + names[3], True, (255, 255, 255))
        fifth_player = other_font2.render("5. " + names[4], True, (255, 255, 255))
        back_button = other_font2.render("BACK", True, (255, 255, 0))

        first_player_rect = first_player.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 100))
        DISPLAY.blit(first_player, first_player_rect)

        second_player_rect = second_player.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
        DISPLAY.blit(second_player, second_player_rect)

        third_player_rect = third_player.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        DISPLAY.blit(third_player, third_player_rect)

        fourth_player_rect = fourth_player.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
        DISPLAY.blit(fourth_player, fourth_player_rect)

        fifth_player_rect = fifth_player.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100))
        DISPLAY.blit(fifth_player, fifth_player_rect)

        back_button_rect = back_button.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 200))
        DISPLAY.blit(back_button, back_button_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main_menu()
        pygame.display.update()

def options_menu():
    global music_status
    point = 0

    while True:

        
        DISPLAY.blit(resizedBgMenu, (0, 0))

        options_title = options_font.render("OPTIONS", True, (255, 255, 255))

        if point == 0:
            volume_option = other_font.render('MUSIC ON/OFF', True, (255, 255, 0))

            back_option = other_font.render('BACK', True, (255, 255, 255))
        elif point == 1:
            volume_option = other_font.render('MUSIC ON/OFF', True, (255, 255, 255))

            back_option = other_font.render('BACK', True, (255, 255, 0))


        options_title_rect = options_title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 200))
        volume_option_rect = volume_option.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

        back_option_rect = back_option.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100))

        DISPLAY.blit(options_title, options_title_rect)
        DISPLAY.blit(volume_option, volume_option_rect)

        DISPLAY.blit(back_option, back_option_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    point = point + 1
                elif event.key == pygame.K_UP:
                    point = point - 1
                elif event.key == pygame.K_RETURN:

                    if point == 0 and music_status == 1:
                        pygame.mixer.music.pause()
                        music_status = 0

                    elif point == 0 and music_status == 0:
                        pygame.mixer.music.unpause()
                        music_status = 1

                    if point == 1:
                        main_menu()

        point = point % 2
        pygame.display.update()

def credits_menu():
    point = 0
    

    while True:

        DISPLAY.blit(resizedBgMenu, (0, 0))

        credits_title = credits_font.render("CREDITS", True, (255, 255, 255))
        integrante1 = other_font.render("NICOLAS ARROYO", True, (255, 255, 255))
        integrante2 = other_font.render("JOSE CHACHI", True, (255, 255, 255))
        integrante3 = other_font.render("NICOLAS DE LOAYZA", True, (255, 255, 255))
        integrante4 = other_font.render("JOSE CONDORI", True, (255, 255, 255))

        if point == 0:
            back_option = other_font.render("BACK", True, (255, 255, 0))

        credits_title_rect = credits_title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 200))
        integrante1_rect = integrante1.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
        integrante2_rect = integrante2.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        integrante3_rect = integrante3.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
        integrante4_rect = integrante4.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100))
        back_option_rect = back_option.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 175))

        DISPLAY.blit(credits_title, credits_title_rect)
        DISPLAY.blit(integrante1, integrante1_rect)
        DISPLAY.blit(integrante2, integrante2_rect)
        DISPLAY.blit(integrante3, integrante3_rect)
        DISPLAY.blit(integrante4, integrante4_rect)
        DISPLAY.blit(back_option, back_option_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    point = point + 1
                elif event.key == pygame.K_UP:
                    point = point - 1
                elif event.key == pygame.K_RETURN:

                    if point == 0:
                        main_menu()
        point = point % 1
        pygame.display.update()



def game_easy():
    global tempo
    mov_ship = 0
    shipX = (WINDOW_WIDTH//2)-25
    bulletX = shipX
    mov_bullet = 0
    bulletY = -50
    tempo = 0
    mov_bullet1 = 0
    mov_bullet2 = 0
    mov_bullet3 = 0
    mov_bullet4 = 0
    mov_bullet5 = 0
    mov_bullet6 = 0
    pos1X = rd.randint(526,626)
    pos2X = rd.randint(426,526)
    pos3X = rd.randint(626,726)
    pos4X = rd.randint(426,476)
    pos5X = rd.randint(526,626)
    pos6X = rd.randint(676,717)
    bullet1X = pos1X + 18
    bullet1Y = 850

    bullet2X = pos2X + 18
    bullet2Y = 850

    bullet3X = pos3X + 18
    bullet3Y = 850

    bullet4X = pos4X + 18
    bullet4Y = 850

    bullet5X = pos5X + 18
    bullet5Y = 850

    bullet6X = pos6X + 18
    bullet6Y = 850

    life = 100
    m1 = 0
    m2 = 0
    m3 = 0
    m4 = 0
    m5 = 0
    m6 = 0

    

    monster1 = pygame.Rect(pos1X,100,50,50)
    monster2 = pygame.Rect(pos2X,200,50,50)
    monster3 = pygame.Rect(pos3X,200,50,50)
    monster4 = pygame.Rect(pos4X,300,50,50)
    monster5 = pygame.Rect(pos5X,300,50,50)
    monster6 = pygame.Rect(pos6X,300,50,50)

    life1 = 100
    life2 = 100
    life3 = 100
    life4 = 100
    life5 = 100
    life6 = 100

    attack = False
    while True:
        
        DISPLAY.blit(BGEASY, (0, 0))
        DISPLAY.blit(BULLET,(bulletX + 18,bulletY+10))
        
        pygame.draw.rect(DISPLAY, (255,255,255), (shipX, (WINDOW_HEIGHT//2)+110+200, 50, 10),8)
        pygame.draw.rect(DISPLAY, (255,0,0), (shipX, (WINDOW_HEIGHT//2)+110+200, 50, 10))
        pygame.draw.rect(DISPLAY, (0,255,0), (shipX, (WINDOW_HEIGHT//2)+110+200, 50* life/100 , 10))

        pygame.draw.rect(DISPLAY,(255,255,255),(390, 0,10,800))
        pygame.draw.rect(DISPLAY,(255,255,255),(800, 0,10,800))

        DISPLAY.blit(SHIP, (shipX,(WINDOW_HEIGHT//2)+50+200))

        
        
        bullet_rect2 = pygame.Rect(bulletX+18,bulletY+10,15,15)

        ship_rect = pygame.Rect(shipX,(WINDOW_HEIGHT//2)+110+140, 50, 50)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_a:
                    mov_ship = -5
                    
                if event.key == pygame.K_d and (shipX < (WINDOW_WIDTH - 50)):
                    mov_ship = 5
                if event.key == pygame.K_SPACE and bulletY < 0:

                    shoot_sound.play()
                    
                    bulletX = shipX
                    bulletY = (WINDOW_HEIGHT//2)+50+200
                    mov_bullet = -15

                    
                    if bullet_probability("easy") == True:
                        attack = True
                    else:
                        pass

                


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    mov_ship = 0
                if event.key == pygame.K_d:
                    mov_ship = 0

        shipX += mov_ship

        if shipX <= 400:
            shipX = 400
        
        if shipX >= 750:
            shipX = 750

        bulletY += mov_bullet

        if  pygame.Rect.colliderect(bullet_rect2, monster1) == True:

            m1 += 1
            bulletY = -50
            monster1 = pygame.Rect(0,0,0,0)
        elif pygame.Rect.colliderect(bullet_rect2, monster2) == True:

            m2 += 1
            bulletY = -50
            monster2 = pygame.Rect(0,0,0,0)
        elif pygame.Rect.colliderect(bullet_rect2, monster3) == True:

            m3 += 1
            bulletY = -50
            monster3 = pygame.Rect(0,0,0,0)
        elif pygame.Rect.colliderect(bullet_rect2, monster4) == True:
            
            m4 += 1
            bulletY = -50
            monster4 = pygame.Rect(0,0,0,0)
        elif pygame.Rect.colliderect(bullet_rect2, monster5) == True:

            m5 += 1
            bulletY = -50
            monster5 = pygame.Rect(0,0,0,0)           
        elif pygame.Rect.colliderect(bullet_rect2, monster6) == True:

            m6 += 1
            bulletY = -50
            monster6 = pygame.Rect(0,0,0,0)

        if not(m1 == 1):

            DISPLAY.blit(monsterOne1(), (pos1X,100))
            pygame.draw.rect(DISPLAY, (255,255,255), (pos1X, 155, 50, 10),8)
            pygame.draw.rect(DISPLAY, (255,0,0), (pos1X, 155, 50, 10))
            pygame.draw.rect(DISPLAY, (0,255,0), (pos1X, 155, 50* life1/100 , 10))
        
        if not(m2 == 1):

            DISPLAY.blit(monsterOne2(), (pos2X,200))
            pygame.draw.rect(DISPLAY, (255,255,255), (pos2X, 255, 50, 10),8)
            pygame.draw.rect(DISPLAY, (255,0,0), (pos2X, 255, 50, 10))
            pygame.draw.rect(DISPLAY, (0,255,0), (pos2X, 255, 50* life2/100 , 10))

        if not(m3 == 1):
            
            DISPLAY.blit(monsterOne2(), (pos3X,200))
            pygame.draw.rect(DISPLAY, (255,255,255), (pos3X, 255, 50, 10),8)
            pygame.draw.rect(DISPLAY, (255,0,0), (pos3X, 255, 50, 10))
            pygame.draw.rect(DISPLAY, (0,255,0), (pos3X, 255, 50* life3/100 , 10))
        
        if not(m4 == 1):
            
            DISPLAY.blit(monsterOne1(), (pos4X,300))
            pygame.draw.rect(DISPLAY, (255,255,255), (pos4X, 355, 50, 10),8)
            pygame.draw.rect(DISPLAY, (255,0,0), (pos4X, 355, 50, 10))
            pygame.draw.rect(DISPLAY, (0,255,0), (pos4X, 355, 50* life4/100 , 10))
                    
        if not(m5 == 1):
            
            DISPLAY.blit(monsterOne1(), (pos5X,300))
            pygame.draw.rect(DISPLAY, (255,255,255), (pos5X, 355, 50, 10),8)
            pygame.draw.rect(DISPLAY, (255,0,0), (pos5X, 355, 50, 10))
            pygame.draw.rect(DISPLAY, (0,255,0), (pos5X, 355, 50* life5/100 , 10))
        
        if not(m6 == 1):
            
            DISPLAY.blit(monsterOne1(), (pos6X,300))
            pygame.draw.rect(DISPLAY, (255,255,255), (pos6X, 355, 50, 10),8)
            pygame.draw.rect(DISPLAY, (255,0,0), (pos6X, 355, 50, 10))
            pygame.draw.rect(DISPLAY, (0,255,0), (pos6X, 355, 50* life6/100 , 10))
        
        if attack == True:
            if bullet_probability("easy") == True and bullet1Y > 800 and not(m1 == 1):
                mov_bullet1 = rd.randint(7,12)
                bullet1Y = 140
            if bullet_probability("easy") == True and bullet2Y > 800 and not(m2 == 1):
                mov_bullet2 = rd.randint(6,11)
                bullet2Y = 240
            if bullet_probability("easy") == True and bullet3Y > 800 and not(m3 == 1):
                mov_bullet3 = rd.randint(6,11)
                bullet3Y = 240
            if bullet_probability("easy") == True and bullet4Y > 800 and not(m4 == 1):
                mov_bullet4 = rd.randint(5,10)
                bullet4Y = 340
            if bullet_probability("easy") == True and bullet5Y > 800 and not(m5 == 1):
                mov_bullet5 = rd.randint(5,10)
                bullet5Y = 340
            if bullet_probability("easy") == True and bullet6Y > 800 and not(m6 == 1):
                mov_bullet6 = rd.randint(5,10)
                bullet6Y = 340
            attack = False

        bullet1Y += mov_bullet1
        bullet2Y += mov_bullet2
        bullet3Y += mov_bullet3
        bullet4Y += mov_bullet4
        bullet5Y += mov_bullet5
        bullet6Y += mov_bullet6

        bullet1_rect = pygame.Rect(bullet1X,bullet1Y,15,15) 
        bullet2_rect = pygame.Rect(bullet2X,bullet2Y,15,15)   
        bullet3_rect = pygame.Rect(bullet3X,bullet3Y,15,15)      
        bullet4_rect = pygame.Rect(bullet4X,bullet4Y,15,15)       
        bullet5_rect = pygame.Rect(bullet5X,bullet5Y,15,15)
        bullet6_rect = pygame.Rect(bullet6X,bullet6Y,15,15)
        
        if pygame.Rect.colliderect(bullet1_rect, ship_rect):
            life -= 20
            bullet1Y = 850
        if pygame.Rect.colliderect(bullet2_rect, ship_rect):
            life -= 20
            bullet2Y = 850
        if pygame.Rect.colliderect(bullet3_rect, ship_rect):
            life -= 20
            bullet3Y = 850
        if pygame.Rect.colliderect(bullet4_rect, ship_rect):
            life -= 20
            bullet4Y = 850
        if pygame.Rect.colliderect(bullet5_rect, ship_rect):
            life -= 20
            bullet5Y = 850
        if pygame.Rect.colliderect(bullet6_rect, ship_rect):
            life -= 20
            bullet6Y = 850
        
        DISPLAY.blit(bulletmonster1,(bullet1X,bullet1Y))
        DISPLAY.blit(bulletmonster1,(bullet2X,bullet2Y))
        DISPLAY.blit(bulletmonster1,(bullet3X,bullet3Y))
        DISPLAY.blit(bulletmonster1,(bullet4X,bullet4Y))
        DISPLAY.blit(bulletmonster1,(bullet5X,bullet5Y))
        DISPLAY.blit(bulletmonster1,(bullet6X,bullet6Y))
        
        if life == 0:
            game_over("easy")
            

        if m1 == 1 and m2 == 1 and m3 == 1 and m4 == 1 and m5 == 1 and m6 == 1:
            askName("EASY")
        
        pygame.display.update()
        clock.tick(60)

def game_medium():
    global tempo
    mov_ship = 0
    shipX = (WINDOW_WIDTH//2)-25
    bulletX = shipX
    mov_bullet = 0
    bulletY = -50
    tempo = 0

    life = 100
    mov_bullet1 = 0
    mov_bullet2 = 0
    mov_bullet3 = 0
    mov_bullet4 = 0
    mov_bullet5 = 0
    mov_bullet6 = 0

    pos1X = rd.randint(526,626)
    pos2X = rd.randint(426,526)
    pos3X = rd.randint(626,726)
    pos4X = rd.randint(426,476)
    pos5X = rd.randint(526,626)
    pos6X = rd.randint(676,717)
    bullet1X = pos1X + 18
    bullet1Y = 850

    bullet2X = pos2X + 18
    bullet2Y = 850

    bullet3X = pos3X + 18
    bullet3Y = 850

    bullet4X = pos4X + 18
    bullet4Y = 850

    bullet5X = pos5X + 18
    bullet5Y = 850

    bullet6X = pos6X + 18
    bullet6Y = 850

    m1 = 0
    m2 = 0
    m3 = 0
    m4 = 0
    m5 = 0
    m6 = 0

    monster1 = pygame.Rect(pos1X,100,50,50)
    monster2 = pygame.Rect(pos2X,200,50,50)
    monster3 = pygame.Rect(pos3X,200,50,50)
    monster4 = pygame.Rect(pos4X,300,50,50)
    monster5 = pygame.Rect(pos5X,300,50,50)
    monster6 = pygame.Rect(pos6X,300,50,50)

    life1 = 100
    life2 = 100
    life3 = 100
    life4 = 100
    life5 = 100
    life6 = 100

    attack = False
    while True:
        
        DISPLAY.blit(BGMEDIUM, (0, 0))
        DISPLAY.blit(BULLET,(bulletX + 18,bulletY+10))
        
        pygame.draw.rect(DISPLAY, (255,255,255), (shipX, (WINDOW_HEIGHT//2)+110+200, 50, 10),8)
        pygame.draw.rect(DISPLAY, (255,0,0), (shipX, (WINDOW_HEIGHT//2)+110+200, 50, 10))
        pygame.draw.rect(DISPLAY, (0,255,0), (shipX, (WINDOW_HEIGHT//2)+110+200, 50* life/100 , 10))

        pygame.draw.rect(DISPLAY,(255,255,255),(390, 0,10,800))
        pygame.draw.rect(DISPLAY,(255,255,255),(850, 0,10,800))

        DISPLAY.blit(SHIP, (shipX,(WINDOW_HEIGHT//2)+50+200))

        bullet_rect2 = pygame.Rect(bulletX+18,bulletY+10,15,15)
        
        ship_rect = pygame.Rect(shipX,(WINDOW_HEIGHT//2)+110+140, 50, 50)
    
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_a:
                    mov_ship = -5
                    
                if event.key == pygame.K_d and (shipX < (WINDOW_WIDTH - 50)):
                    mov_ship = 5
                if event.key == pygame.K_SPACE and bulletY < 0:

                    shoot_sound.play()
                    
                    bulletX = shipX
                    bulletY = (WINDOW_HEIGHT//2)+50+200
                    mov_bullet = -15

                    if bullet_probability("medium") == True:
                        attack = True
                    else:
                        pass

                


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    mov_ship = 0
                if event.key == pygame.K_d:
                    mov_ship = 0

        shipX += mov_ship

        if shipX <= 400:
            shipX = 400
        
        if shipX >= 800:
            shipX = 800

        bulletY += mov_bullet

        if  pygame.Rect.colliderect(bullet_rect2, monster1) == True:

            m1 += 1
            bulletY = -50
            life1 -= 50
            if m1 == 2:
                monster1 = pygame.Rect(0,0,0,0)
        elif pygame.Rect.colliderect(bullet_rect2, monster2) == True:

            m2 += 1
            bulletY = -50
            life2 -= 50
            if m2 == 2:
                monster2 = pygame.Rect(0,0,0,0)
        elif pygame.Rect.colliderect(bullet_rect2, monster3) == True:

            m3 += 1
            bulletY = -50
            life3 -= 50
            if m3 == 2:
                monster3 = pygame.Rect(0,0,0,0)
        elif pygame.Rect.colliderect(bullet_rect2, monster4) == True:
            
            m4 += 1
            bulletY = -50
            life4 -= 50
            if m4 == 2:
                monster4 = pygame.Rect(0,0,0,0)

        elif pygame.Rect.colliderect(bullet_rect2, monster5) == True:

            m5 += 1
            bulletY = -50
            life5 -= 50
            if m5 == 2:
                monster5 = pygame.Rect(0,0,0,0)
            
        elif pygame.Rect.colliderect(bullet_rect2, monster6) == True:

            m6 += 1
            bulletY = -50
            life6 -= 50
            if m6 == 2:
                monster6 = pygame.Rect(0,0,0,0)

        if not(m1 == 2):

            DISPLAY.blit(monsterTwo1(), (pos1X,100))
            pygame.draw.rect(DISPLAY, (255,255,255), (pos1X, 155, 50, 10),8)
            pygame.draw.rect(DISPLAY, (255,0,0), (pos1X, 155, 50, 10))
            pygame.draw.rect(DISPLAY, (0,255,0), (pos1X, 155, 50* life1/100 , 10))
        
        if not(m2 == 2):

            DISPLAY.blit(monsterTwo2(), (pos2X,200))
            pygame.draw.rect(DISPLAY, (255,255,255), (pos2X, 255, 50, 10),8)
            pygame.draw.rect(DISPLAY, (255,0,0), (pos2X, 255, 50, 10))
            pygame.draw.rect(DISPLAY, (0,255,0), (pos2X, 255, 50* life2/100 , 10))
        if not(m3 == 2):
            
            DISPLAY.blit(monsterTwo2(), (pos3X,200))
            pygame.draw.rect(DISPLAY, (255,255,255), (pos3X, 255, 50, 10),8)
            pygame.draw.rect(DISPLAY, (255,0,0), (pos3X, 255, 50, 10))
            pygame.draw.rect(DISPLAY, (0,255,0), (pos3X, 255, 50* life3/100 , 10))
        if not(m4 == 2):
            
            DISPLAY.blit(monsterTwo1(), (pos4X,300))
            pygame.draw.rect(DISPLAY, (255,255,255), (pos4X, 355, 50, 10),8)
            pygame.draw.rect(DISPLAY, (255,0,0), (pos4X, 355, 50, 10))
            pygame.draw.rect(DISPLAY, (0,255,0), (pos4X, 355, 50* life4/100 , 10))
        
        if not(m5 == 2):
            
            DISPLAY.blit(monsterTwo1(), (pos5X,300))
            pygame.draw.rect(DISPLAY, (255,255,255), (pos5X, 355, 50, 10),8)
            pygame.draw.rect(DISPLAY, (255,0,0), (pos5X, 355, 50, 10))
            pygame.draw.rect(DISPLAY, (0,255,0), (pos5X, 355, 50* life5/100 , 10))
        if not(m6 == 2):
            
            DISPLAY.blit(monsterTwo1(), (pos6X,300))
            pygame.draw.rect(DISPLAY, (255,255,255), (pos6X, 355, 50, 10),8)
            pygame.draw.rect(DISPLAY, (255,0,0), (pos6X, 355, 50, 10))
            pygame.draw.rect(DISPLAY, (0,255,0), (pos6X, 355, 50* life6/100 , 10))


        if attack == True:
            if bullet_probability("medium") == True and bullet1Y > 800 and not(m1 == 2):
                mov_bullet1 = rd.randint(7,12)
                bullet1Y = 140
            if bullet_probability("medium") == True and bullet2Y > 800 and not(m2 == 2):
                mov_bullet2 = rd.randint(6,11)
                bullet2Y = 240
            if bullet_probability("medium") == True and bullet3Y > 800 and not(m3 == 2):
                mov_bullet3 = rd.randint(6,11)
                bullet3Y = 240
            if bullet_probability("medium") == True and bullet4Y > 800 and not(m4 == 2):
                mov_bullet4 = rd.randint(5,10)
                bullet4Y = 340
            if bullet_probability("medium") == True and bullet5Y > 800 and not(m5 == 2):
                mov_bullet5 = rd.randint(5,10)
                bullet5Y = 340
            if bullet_probability("medium") == True and bullet6Y > 800 and not(m6 == 2):
                mov_bullet6 = rd.randint(5,10)
                bullet6Y = 340
            attack = False

        bullet1Y += mov_bullet1
        bullet2Y += mov_bullet2
        bullet3Y += mov_bullet3
        bullet4Y += mov_bullet4
        bullet5Y += mov_bullet5
        bullet6Y += mov_bullet6

        bullet1_rect = pygame.Rect(bullet1X,bullet1Y,15,15) 
        bullet2_rect = pygame.Rect(bullet2X,bullet2Y,15,15)   
        bullet3_rect = pygame.Rect(bullet3X,bullet3Y,15,15)      
        bullet4_rect = pygame.Rect(bullet4X,bullet4Y,15,15)       
        bullet5_rect = pygame.Rect(bullet5X,bullet5Y,15,15)
        bullet6_rect = pygame.Rect(bullet6X,bullet6Y,15,15)
        
        if pygame.Rect.colliderect(bullet1_rect, ship_rect):
            life -= 20
            bullet1Y = 850
        if pygame.Rect.colliderect(bullet2_rect, ship_rect):
            life -= 20
            bullet2Y = 850
        if pygame.Rect.colliderect(bullet3_rect, ship_rect):
            life -= 20
            bullet3Y = 850
        if pygame.Rect.colliderect(bullet4_rect, ship_rect):
            life -= 20
            bullet4Y = 850
        if pygame.Rect.colliderect(bullet5_rect, ship_rect):
            life -= 20
            bullet5Y = 850
        if pygame.Rect.colliderect(bullet6_rect, ship_rect):
            life -= 20
            bullet6Y = 850
        
        DISPLAY.blit(bulletmonster2,(bullet1X,bullet1Y))
        DISPLAY.blit(bulletmonster2,(bullet2X,bullet2Y))
        DISPLAY.blit(bulletmonster2,(bullet3X,bullet3Y))
        DISPLAY.blit(bulletmonster2,(bullet4X,bullet4Y))
        DISPLAY.blit(bulletmonster2,(bullet5X,bullet5Y))
        DISPLAY.blit(bulletmonster2,(bullet6X,bullet6Y))
        
        if life == 0:
            game_over("medium")

        if m1 == 2 and m2 == 2 and m3 == 2 and m4 == 2 and m5 == 2 and m6 == 2:
            askName("MEDIUM")
        pygame.display.update()
        clock.tick(60)

def game_hard():
    global tempo
    mov_ship = 0
    shipX = (WINDOW_WIDTH//2)-25
    bulletX = shipX
    mov_bullet = 0
    bulletY = -50
    tempo = 0

    life = 100
    mov_bullet1 = 0
    mov_bullet2 = 0
    mov_bullet3 = 0
    mov_bullet4 = 0
    mov_bullet5 = 0
    mov_bullet6 = 0

    pos1X = rd.randint(526,626)
    pos2X = rd.randint(426,526)
    pos3X = rd.randint(626,726)
    pos4X = rd.randint(426,476)
    pos5X = rd.randint(526,626)
    pos6X = rd.randint(676,717)
    bullet1X = pos1X + 18
    bullet1Y = 850

    bullet2X = pos2X + 18
    bullet2Y = 850

    bullet3X = pos3X + 18
    bullet3Y = 850

    bullet4X = pos4X + 18
    bullet4Y = 850

    bullet5X = pos5X + 18
    bullet5Y = 850

    bullet6X = pos6X + 18
    bullet6Y = 850
    m1 = 0
    m2 = 0
    m3 = 0
    m4 = 0
    m5 = 0
    m6 = 0

    monster1 = pygame.Rect(pos1X,100,50,50)
    monster2 = pygame.Rect(pos2X,200,50,50)
    monster3 = pygame.Rect(pos3X,200,50,50)
    monster4 = pygame.Rect(pos4X,300,50,50)
    monster5 = pygame.Rect(pos5X,300,50,50)
    monster6 = pygame.Rect(pos6X,300,50,50)

    life1 = 100
    life2 = 100
    life3 = 100
    life4 = 100
    life5 = 100
    life6 = 100

    attack = False
    while True:
        
        DISPLAY.blit(BGHARD, (0, 0))
        DISPLAY.blit(BULLET,(bulletX + 18,bulletY+10))
        
        pygame.draw.rect(DISPLAY, (255,255,255), (shipX, (WINDOW_HEIGHT//2)+110+200, 50, 10),8)
        pygame.draw.rect(DISPLAY, (255,0,0), (shipX, (WINDOW_HEIGHT//2)+110+200, 50, 10))
        pygame.draw.rect(DISPLAY, (0,255,0), (shipX, (WINDOW_HEIGHT//2)+110+200, 50* life/100 , 10))

        pygame.draw.rect(DISPLAY,(255,255,255),(390, 0,10,800))
        pygame.draw.rect(DISPLAY,(255,255,255),(850, 0,10,800))

        DISPLAY.blit(SHIP, (shipX,(WINDOW_HEIGHT//2)+50+200))
        
        ship_rect = pygame.Rect(shipX,(WINDOW_HEIGHT//2)+110+140, 50, 50)
        
        bullet_rect2 = pygame.Rect(bulletX+18,bulletY+10,15,15)
                 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_a:
                    mov_ship = -5
                    
                if event.key == pygame.K_d and (shipX < (WINDOW_WIDTH - 50)):
                    mov_ship = 5
                if event.key == pygame.K_SPACE and bulletY < 0:

                    shoot_sound.play()
                    
                    bulletX = shipX
                    bulletY = (WINDOW_HEIGHT//2)+50+200
                    mov_bullet = -15

                    if bullet_probability("hard") == True:
                        attack = True
                    else:
                        pass


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    mov_ship = 0
                if event.key == pygame.K_d:
                    mov_ship = 0

        shipX += mov_ship

        if shipX <= 400:
            shipX = 400
        
        if shipX >= 800:
            shipX = 800

        bulletY += mov_bullet

        if  pygame.Rect.colliderect(bullet_rect2, monster1) == True:

            m1 += 1
            bulletY = -50
            life1 -= 34
            if m1 == 3:
                monster1 = pygame.Rect(0,0,0,0)
        elif pygame.Rect.colliderect(bullet_rect2, monster2) == True:

            m2 += 1
            bulletY = -50
            life2 -= 34
            if m2 == 3:
                monster2 = pygame.Rect(0,0,0,0)
        elif pygame.Rect.colliderect(bullet_rect2, monster3) == True:

            m3 += 1
            bulletY = -50
            life3 -= 34
            if m3 == 3:
                monster3 = pygame.Rect(0,0,0,0)
        elif pygame.Rect.colliderect(bullet_rect2, monster4) == True:
            
            m4 += 1
            bulletY = -50
            life4 -= 34
            if m4 == 3:
                monster4 = pygame.Rect(0,0,0,0)

        elif pygame.Rect.colliderect(bullet_rect2, monster5) == True:

            m5 += 1
            bulletY = -50
            life5 -= 34
            if m5 == 3:
                monster5 = pygame.Rect(0,0,0,0)
            
        elif pygame.Rect.colliderect(bullet_rect2, monster6) == True:

            m6 += 1
            bulletY = -50
            life6 -= 34
            if m6 == 3:
                monster6 = pygame.Rect(0,0,0,0)

        if not(m1 == 3):

            DISPLAY.blit(monsterThree1(), (pos1X,100))
            pygame.draw.rect(DISPLAY, (255,255,255), (pos1X, 155, 50, 10),8)
            pygame.draw.rect(DISPLAY, (255,0,0), (pos1X, 155, 50, 10))
            pygame.draw.rect(DISPLAY, (0,255,0), (pos1X, 155, 50* life1/100 , 10))
        
        if not(m2 == 3):

            DISPLAY.blit(monsterThree2(), (pos2X,200))
            pygame.draw.rect(DISPLAY, (255,255,255), (pos2X, 255, 50, 10),8)
            pygame.draw.rect(DISPLAY, (255,0,0), (pos2X, 255, 50, 10))
            pygame.draw.rect(DISPLAY, (0,255,0), (pos2X, 255, 50* life2/100 , 10))

        if not(m3 == 3):
            
            DISPLAY.blit(monsterThree2(), (pos3X,200))
            pygame.draw.rect(DISPLAY, (255,255,255), (pos3X, 255, 50, 10),8)
            pygame.draw.rect(DISPLAY, (255,0,0), (pos3X, 255, 50, 10))
            pygame.draw.rect(DISPLAY, (0,255,0), (pos3X, 255, 50* life3/100 , 10))
        
        if not(m4 == 3):
            
            DISPLAY.blit(monsterThree1(), (pos4X,300))
            pygame.draw.rect(DISPLAY, (255,255,255), (pos4X, 355, 50, 10),8)
            pygame.draw.rect(DISPLAY, (255,0,0), (pos4X, 355, 50, 10))
            pygame.draw.rect(DISPLAY, (0,255,0), (pos4X, 355, 50* life4/100 , 10))
            
        
        if not(m5 == 3):
            
            DISPLAY.blit(monsterThree1(), (pos5X,300))
            pygame.draw.rect(DISPLAY, (255,255,255), (pos5X, 355, 50, 10),8)
            pygame.draw.rect(DISPLAY, (255,0,0), (pos5X, 355, 50, 10))
            pygame.draw.rect(DISPLAY, (0,255,0), (pos5X, 355, 50* life5/100 , 10))
        
        if not(m6 == 3):
            
            DISPLAY.blit(monsterThree1(), (pos6X,300))
            pygame.draw.rect(DISPLAY, (255,255,255), (pos6X, 355, 50, 10),8)
            pygame.draw.rect(DISPLAY, (255,0,0), (pos6X, 355, 50, 10))
            pygame.draw.rect(DISPLAY, (0,255,0), (pos6X, 355, 50* life6/100 , 10))

        if attack == True:
            if bullet_probability("hard") == True and bullet1Y > 800 and not(m1 == 3):
                mov_bullet1 = rd.randint(7,12)
                bullet1Y = 140
            if bullet_probability("hard") == True and bullet2Y > 800 and not(m2 == 3):
                mov_bullet2 = rd.randint(6,11)
                bullet2Y = 240
            if bullet_probability("hard") == True and bullet3Y > 800 and not(m3 == 3):
                mov_bullet3 = rd.randint(6,11)
                bullet3Y = 240
            if bullet_probability("hard") == True and bullet4Y > 800 and not(m4 == 3):
                mov_bullet4 = rd.randint(5,10)
                bullet4Y = 340
            if bullet_probability("hard") == True and bullet5Y > 800 and not(m5 == 3):
                mov_bullet5 = rd.randint(5,10)
                bullet5Y = 340
            if bullet_probability("hard") == True and bullet6Y > 800 and not(m6 == 3):
                mov_bullet6 = rd.randint(5,10)
                bullet6Y = 340
            attack = False

        bullet1Y += mov_bullet1
        bullet2Y += mov_bullet2
        bullet3Y += mov_bullet3
        bullet4Y += mov_bullet4
        bullet5Y += mov_bullet5
        bullet6Y += mov_bullet6

        bullet1_rect = pygame.Rect(bullet1X,bullet1Y,15,15) 
        bullet2_rect = pygame.Rect(bullet2X,bullet2Y,15,15)   
        bullet3_rect = pygame.Rect(bullet3X,bullet3Y,15,15)      
        bullet4_rect = pygame.Rect(bullet4X,bullet4Y,15,15)       
        bullet5_rect = pygame.Rect(bullet5X,bullet5Y,15,15)
        bullet6_rect = pygame.Rect(bullet6X,bullet6Y,15,15)
        
        if pygame.Rect.colliderect(bullet1_rect, ship_rect):
            life -= 20
            bullet1Y = 850
        if pygame.Rect.colliderect(bullet2_rect, ship_rect):
            life -= 20
            bullet2Y = 850
        if pygame.Rect.colliderect(bullet3_rect, ship_rect):
            life -= 20
            bullet3Y = 850
        if pygame.Rect.colliderect(bullet4_rect, ship_rect):
            life -= 20
            bullet4Y = 850
        if pygame.Rect.colliderect(bullet5_rect, ship_rect):
            life -= 20
            bullet5Y = 850
        if pygame.Rect.colliderect(bullet6_rect, ship_rect):
            life -= 20
            bullet6Y = 850
        
        DISPLAY.blit(bulletmonster3,(bullet1X,bullet1Y))
        DISPLAY.blit(bulletmonster3,(bullet2X,bullet2Y))
        DISPLAY.blit(bulletmonster3,(bullet3X,bullet3Y))
        DISPLAY.blit(bulletmonster3,(bullet4X,bullet4Y))
        DISPLAY.blit(bulletmonster3,(bullet5X,bullet5Y))
        DISPLAY.blit(bulletmonster3,(bullet6X,bullet6Y))
        
        if life == 0:
            game_over("hard")

        if m1 == 3 and m2 == 3 and m3 == 3 and m4 == 3 and m5 == 3 and m6 == 3:
            askName("HARD")
        pygame.display.update()
        clock.tick(60)

def game_hardcore():
    global tempo
    mov_ship = 0
    shipX = (WINDOW_WIDTH//2)-25
    bulletX = shipX
    mov_bullet = 0
    bulletY = -50
    tempo = 0

    life = 100

    mov_bullet1 = 0
    mov_bullet2 = 0
    mov_bullet3 = 0
    mov_bullet4 = 0
    mov_bullet5 = 0
    mov_bullet6 = 0

    pos1X = rd.randint(526,626)
    pos2X = rd.randint(446,526)
    pos3X = rd.randint(626,726)
    pos4X = rd.randint(426,476)
    pos5X = rd.randint(526,626)
    pos6X = rd.randint(676,717)

    bullet1X = pos1X + 18
    bullet1Y = 850

    bullet2X = pos2X + 18
    bullet2Y = 850

    bullet3X = pos3X + 18
    bullet3Y = 850

    bullet4X = pos4X + 18
    bullet4Y = 850

    bullet5X = pos5X + 18
    bullet5Y = 850

    bullet6X = pos6X + 18
    bullet6Y = 850
    m1 = 0
    m2 = 0
    m3 = 0
    m4 = 0
    m5 = 0
    m6 = 0

    monster1 = pygame.Rect(pos1X,100,50,50)
    monster2 = pygame.Rect(pos2X,200,50,50)
    monster3 = pygame.Rect(pos3X,200,50,50)
    monster4 = pygame.Rect(pos4X,300,50,50)
    monster5 = pygame.Rect(pos5X,300,50,50)
    monster6 = pygame.Rect(pos6X,300,50,50)

    life1 = 100
    life2 = 100
    life3 = 100
    life4 = 100
    life5 = 100
    life6 = 100
    attack = False
    while True:
        
        DISPLAY.blit(BGHARDCORE, (0, 0))
        DISPLAY.blit(BULLET,(bulletX + 18,bulletY+10))
        
        pygame.draw.rect(DISPLAY, (255,255,255), (shipX, (WINDOW_HEIGHT//2)+110+200, 50, 10),8)
        pygame.draw.rect(DISPLAY, (255,0,0), (shipX, (WINDOW_HEIGHT//2)+110+200, 50, 10))
        pygame.draw.rect(DISPLAY, (0,255,0), (shipX, (WINDOW_HEIGHT//2)+110+200, 50* life/100 , 10))

        pygame.draw.rect(DISPLAY,(255,255,255),(390, 0,10,800))
        pygame.draw.rect(DISPLAY,(255,255,255),(850, 0,10,800))

        DISPLAY.blit(SHIP, (shipX,(WINDOW_HEIGHT//2)+50+200)) 

        ship_rect = pygame.Rect(shipX,(WINDOW_HEIGHT//2)+110+140, 50, 50)
        
        bullet_rect2 = pygame.Rect(bulletX+18,bulletY+10,15,15)
        
        
    
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_a:
                    mov_ship = -5
                    
                if event.key == pygame.K_d and (shipX < (WINDOW_WIDTH - 50)):
                    mov_ship = 5
                if event.key == pygame.K_SPACE and bulletY < 0:

                    shoot_sound.play()
                    
                    bulletX = shipX
                    bulletY = (WINDOW_HEIGHT//2)+50+200
                    mov_bullet = -15

                    if bullet_probability("hardcore") == True:
                        attack = True
                    else:
                        pass

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    mov_ship = 0
                if event.key == pygame.K_d:
                    mov_ship = 0

        shipX += mov_ship

        if shipX <= 400:
            shipX = 400
        
        if shipX >= 800:
            shipX = 800

        bulletY += mov_bullet

        if  pygame.Rect.colliderect(bullet_rect2, monster1) == True:

            m1 += 1
            bulletY = -50
            life1 -= 25
            if m1 == 4:
                monster1 = pygame.Rect(0,0,0,0)
        elif pygame.Rect.colliderect(bullet_rect2, monster2) == True:

            m2 += 1
            bulletY = -50
            life2 -= 25
            if m2 == 4:
                monster2 = pygame.Rect(0,0,0,0)
        elif pygame.Rect.colliderect(bullet_rect2, monster3) == True:

            m3 += 1
            bulletY = -50
            life3 -= 25
            if m3 == 4:
                monster3 = pygame.Rect(0,0,0,0)
        elif pygame.Rect.colliderect(bullet_rect2, monster4) == True:
            
            m4 += 1
            bulletY = -50
            life4 -= 25
            if m4 == 4:
                monster4 = pygame.Rect(0,0,0,0)

        elif pygame.Rect.colliderect(bullet_rect2, monster5) == True:

            m5 += 1
            bulletY = -50
            life5 -= 25
            if m5 == 4:
                monster5 = pygame.Rect(0,0,0,0)
            
        elif pygame.Rect.colliderect(bullet_rect2, monster6) == True:

            m6 += 1
            bulletY = -50
            life6 -= 25
            if m6 == 4:
                monster6 = pygame.Rect(0,0,0,0)

        if not(m1 == 4):

            DISPLAY.blit(monsterFour1(), (pos1X,100))
            pygame.draw.rect(DISPLAY, (255,255,255), (pos1X, 155, 50, 10),8)
            pygame.draw.rect(DISPLAY, (255,0,0), (pos1X, 155, 50, 10))
            pygame.draw.rect(DISPLAY, (0,255,0), (pos1X, 155, 50* life1/100 , 10))
        
        if not(m2 == 4):

            DISPLAY.blit(monsterFour2(), (pos2X,200))
            pygame.draw.rect(DISPLAY, (255,255,255), (pos2X, 255, 50, 10),8)
            pygame.draw.rect(DISPLAY, (255,0,0), (pos2X, 255, 50, 10))
            pygame.draw.rect(DISPLAY, (0,255,0), (pos2X, 255, 50* life2/100 , 10))

        if not(m3 == 4):
            
            DISPLAY.blit(monsterFour2(), (pos3X,200))
            pygame.draw.rect(DISPLAY, (255,255,255), (pos3X, 255, 50, 10),8)
            pygame.draw.rect(DISPLAY, (255,0,0), (pos3X, 255, 50, 10))
            pygame.draw.rect(DISPLAY, (0,255,0), (pos3X, 255, 50* life3/100 , 10))
        
        if not(m4 == 4):
            
            DISPLAY.blit(monsterFour1(), (pos4X,300))
            pygame.draw.rect(DISPLAY, (255,255,255), (pos4X, 355, 50, 10),8)
            pygame.draw.rect(DISPLAY, (255,0,0), (pos4X, 355, 50, 10))
            pygame.draw.rect(DISPLAY, (0,255,0), (pos4X, 355, 50* life4/100 , 10))
            
        
        if not(m5 == 4):
            
            DISPLAY.blit(monsterFour1(), (pos5X,300))
            pygame.draw.rect(DISPLAY, (255,255,255), (pos5X, 355, 50, 10),8)
            pygame.draw.rect(DISPLAY, (255,0,0), (pos5X, 355, 50, 10))
            pygame.draw.rect(DISPLAY, (0,255,0), (pos5X, 355, 50* life5/100 , 10))
        
        if not(m6 == 4):
            
            DISPLAY.blit(monsterFour1(), (pos6X,300))
            pygame.draw.rect(DISPLAY, (255,255,255), (pos6X, 355, 50, 10),8)
            pygame.draw.rect(DISPLAY, (255,0,0), (pos6X, 355, 50, 10))
            pygame.draw.rect(DISPLAY, (0,255,0), (pos6X, 355, 50* life6/100 , 10))
        
        if attack == True:
            if bullet_probability("hardcore") == True and bullet1Y > 800 and not(m1 == 4):
                mov_bullet1 = rd.randint(7,12)
                bullet1Y = 140
            if bullet_probability("hardcore") == True and bullet2Y > 800 and not(m2 == 4):
                mov_bullet2 = rd.randint(6,11)
                bullet2Y = 240
            if bullet_probability("hardcore") == True and bullet3Y > 800 and not(m3 == 4):
                mov_bullet3 = rd.randint(6,11)
                bullet3Y = 240
            if bullet_probability("hardcore") == True and bullet4Y > 800 and not(m4 == 4):
                mov_bullet4 = rd.randint(5,10)
                bullet4Y = 340
            if bullet_probability("hardcore") == True and bullet5Y > 800 and not(m5 == 4):
                mov_bullet5 = rd.randint(5,10)
                bullet5Y = 340
            if bullet_probability("hardcore") == True and bullet6Y > 800 and not(m6 == 4):
                mov_bullet6 = rd.randint(5,10)
                bullet6Y = 340
            attack = False

        bullet1Y += mov_bullet1
        bullet2Y += mov_bullet2
        bullet3Y += mov_bullet3
        bullet4Y += mov_bullet4
        bullet5Y += mov_bullet5
        bullet6Y += mov_bullet6

        bullet1_rect = pygame.Rect(bullet1X,bullet1Y,15,15) 
        bullet2_rect = pygame.Rect(bullet2X,bullet2Y,15,15)   
        bullet3_rect = pygame.Rect(bullet3X,bullet3Y,15,15)      
        bullet4_rect = pygame.Rect(bullet4X,bullet4Y,15,15)       
        bullet5_rect = pygame.Rect(bullet5X,bullet5Y,15,15)
        bullet6_rect = pygame.Rect(bullet6X,bullet6Y,15,15)
        
        if pygame.Rect.colliderect(bullet1_rect, ship_rect):
            life -= 20
            bullet1Y = 850
        if pygame.Rect.colliderect(bullet2_rect, ship_rect):
            life -= 20
            bullet2Y = 850
        if pygame.Rect.colliderect(bullet3_rect, ship_rect):
            life -= 20
            bullet3Y = 850
        if pygame.Rect.colliderect(bullet4_rect, ship_rect):
            life -= 20
            bullet4Y = 850
        if pygame.Rect.colliderect(bullet5_rect, ship_rect):
            life -= 20
            bullet5Y = 850
        if pygame.Rect.colliderect(bullet6_rect, ship_rect):
            life -= 20
            bullet6Y = 850
        
        DISPLAY.blit(bulletmonster4,(bullet1X,bullet1Y))
        DISPLAY.blit(bulletmonster4,(bullet2X,bullet2Y))
        DISPLAY.blit(bulletmonster4,(bullet3X,bullet3Y))
        DISPLAY.blit(bulletmonster4,(bullet4X,bullet4Y))
        DISPLAY.blit(bulletmonster4,(bullet5X,bullet5Y))
        DISPLAY.blit(bulletmonster4,(bullet6X,bullet6Y))
        
        if life == 0:
            game_over("hardcore")

        if m1 == 4 and m2 == 4 and m3 == 4 and m4 == 4 and m5 == 4 and m6 == 4:
            askName("HARDCORE")

        pygame.display.update()
        clock.tick(60)



def monsterOne1():
    global tempo
    
    if -1 < tempo < 60:
        oneMonster = pygame.image.load("1_normal.png")
        ONEMONSTER = pygame.transform.scale(oneMonster,(50,50))
        tempo = tempo + 1
    elif tempo == 60:
        oneMonster = pygame.image.load("1_normal.png")
        ONEMONSTER = pygame.transform.scale(oneMonster,(50,50))
        tempo = -1



    if -60 < tempo < 0:
        oneMonster = pygame.image.load("1_disparo.png")
        ONEMONSTER = pygame.transform.scale(oneMonster,(50,50))
        tempo = tempo - 1
    elif tempo == -60:
        oneMonster = pygame.image.load("1_disparo.png")
        ONEMONSTER = pygame.transform.scale(oneMonster,(50,50))
        tempo = 1

    return ONEMONSTER

def monsterOne2():
    global tempo
    if -1 < tempo < 60:
        oneMonster = pygame.image.load("1_disparo.png")
        ONEMONSTER = pygame.transform.scale(oneMonster,(50,50))
        tempo = tempo + 1
    elif tempo == 60:
        oneMonster = pygame.image.load("1_disparo.png")
        ONEMONSTER = pygame.transform.scale(oneMonster,(50,50))
        tempo = -1

    if -60 < tempo < 0:
        oneMonster = pygame.image.load("1_normal.png")
        ONEMONSTER = pygame.transform.scale(oneMonster,(50,50))
        tempo = tempo - 1
    elif tempo == -60:
        oneMonster = pygame.image.load("1_normal.png")
        ONEMONSTER = pygame.transform.scale(oneMonster,(50,50))
        tempo = 1

    return ONEMONSTER
        
def monsterTwo1():

    global tempo
    
    if -1 < tempo < 60:
        monstertwo = pygame.image.load("2_normal.png")
        MONSTERTWO = pygame.transform.scale(monstertwo,(50,50))
        tempo = tempo + 1
    elif tempo == 60:
        monstertwo = pygame.image.load("2_normal.png")
        MONSTERTWO = pygame.transform.scale(monstertwo,(50,50))
        tempo = -1



    if -60 < tempo < 0:
        monstertwo = pygame.image.load("2_disparo.png")
        MONSTERTWO = pygame.transform.scale(monstertwo,(50,50))
        tempo = tempo - 1
    elif tempo == -60:
        monstertwo = pygame.image.load("2_disparo.png")
        MONSTERTWO = pygame.transform.scale(monstertwo,(50,50))
        tempo = 1

    return MONSTERTWO

def monsterTwo2():

    global tempo
    
    if -1 < tempo < 60:
        monstertwo = pygame.image.load("2_disparo.png")
        MONSTERTWO = pygame.transform.scale(monstertwo,(50,50))
        tempo = tempo + 1
    elif tempo == 60:
        monstertwo = pygame.image.load("2_disparo.png")
        MONSTERTWO = pygame.transform.scale(monstertwo,(50,50))
        tempo = -1



    if -60 < tempo < 0:
        monstertwo = pygame.image.load("2_normal.png")
        MONSTERTWO = pygame.transform.scale(monstertwo,(50,50))
        tempo = tempo - 1
    elif tempo == -60:
        monstertwo = pygame.image.load("2_normal.png")
        MONSTERTWO = pygame.transform.scale(monstertwo,(50,50))
        tempo = 1

    return MONSTERTWO

def monsterThree1():
    global tempo
    
    if -1 < tempo < 60:
        threeMonster = pygame.image.load("3_normal.png")
        THREEMONSTER = pygame.transform.scale(threeMonster,(50,50))
        tempo = tempo + 1
    elif tempo == 60:
        threeMonster = pygame.image.load("3_normal.png")
        THREEMONSTER = pygame.transform.scale(threeMonster,(50,50))
        tempo = -1



    if -60 < tempo < 0:
        threeMonster = pygame.image.load("3_disparo.png")
        THREEMONSTER = pygame.transform.scale(threeMonster,(50,50))
        tempo = tempo - 1
    elif tempo == -60:
        threeMonster = pygame.image.load("3_disparo.png")
        THREEMONSTER = pygame.transform.scale(threeMonster,(50,50))
        tempo = 1

    return THREEMONSTER

def monsterThree2():
    global tempo
    if -1 < tempo < 60:
        threeMonster = pygame.image.load("3_disparo.png")
        THREEMONSTER = pygame.transform.scale(threeMonster,(50,50))
        tempo = tempo + 1
    elif tempo == 60:
        threeMonster = pygame.image.load("3_disparo.png")
        THREEMONSTER = pygame.transform.scale(threeMonster,(50,50))
        tempo = -1

    if -60 < tempo < 0:
        threeMonster = pygame.image.load("3_normal.png")
        THREEMONSTER = pygame.transform.scale(threeMonster,(50,50))
        tempo = tempo - 1
    elif tempo == -60:
        threeMonster = pygame.image.load("3_normal.png")
        THREEMONSTER = pygame.transform.scale(threeMonster,(50,50))
        tempo = 1

    return THREEMONSTER
 
def monsterFour1():
    global tempo
    
    if -1 < tempo < 60:
        threeMonster = pygame.image.load("4_normal.png")
        THREEMONSTER = pygame.transform.scale(threeMonster,(50,50))
        tempo = tempo + 1
    elif tempo == 60:
        threeMonster = pygame.image.load("4_normal.png")
        THREEMONSTER = pygame.transform.scale(threeMonster,(50,50))
        tempo = -1



    if -60 < tempo < 0:
        threeMonster = pygame.image.load("4_disparo.png")
        THREEMONSTER = pygame.transform.scale(threeMonster,(50,50))
        tempo = tempo - 1
    elif tempo == -60:
        threeMonster = pygame.image.load("4_disparo.png")
        THREEMONSTER = pygame.transform.scale(threeMonster,(50,50))
        tempo = 1

    return THREEMONSTER

def monsterFour2():
    global tempo
    if -1 < tempo < 60:
        threeMonster = pygame.image.load("4_disparo.png")
        THREEMONSTER = pygame.transform.scale(threeMonster,(50,50))
        tempo = tempo + 1
    elif tempo == 60:
        threeMonster = pygame.image.load("4_disparo.png")
        THREEMONSTER = pygame.transform.scale(threeMonster,(50,50))
        tempo = -1

    if -60 < tempo < 0:
        threeMonster = pygame.image.load("4_normal.png")
        THREEMONSTER = pygame.transform.scale(threeMonster,(50,50))
        tempo = tempo - 1
    elif tempo == -60:
        threeMonster = pygame.image.load("4_normal.png")
        THREEMONSTER = pygame.transform.scale(threeMonster,(50,50))
        tempo = 1

    return THREEMONSTER
 

def selectDiff():
    pointX = 0
    pointY = 0
    while True:
        DISPLAY.blit(resizedBgMenu, (0, 0))

        difficulty_title = options_font.render("DIFFICULTY", True, (255, 255, 255))

        if pointX == 0 and pointY == 0:
            pygame.draw.rect(DISPLAY, (255,255,0), (WINDOW_WIDTH // 2 - 100 - 100 - 50, WINDOW_HEIGHT // 2 - 50 - 50 -50, 200, 110))
            pygame.draw.rect(DISPLAY, (255,255,255), (WINDOW_WIDTH // 2  + 50, WINDOW_HEIGHT // 2 - 50 - 50 -50, 200, 110))
            pygame.draw.rect(DISPLAY, (255,255,255), (WINDOW_WIDTH // 2  - 250 , WINDOW_HEIGHT // 2 + 70 - 50, 200, 110))
            pygame.draw.rect(DISPLAY, (255,255,255), (WINDOW_WIDTH // 2  + 50, WINDOW_HEIGHT // 2 + 70 - 50, 200, 110))
            

            easy_diff = other_font.render('EASY', True, (0, 0, 0)) #THIS
            medium_diff = other_font.render('MEDIUM', True, (0, 0, 0))
            hard_diff = other_font.render('HARD', True, (0, 0, 0))
            hardcore_diff = other_font.render('HARDCORE', True, (0, 0, 0))
            back_button = other_font.render('BACK', True, (255, 255, 255))

        elif pointX == 1 and pointY == 0:
            pygame.draw.rect(DISPLAY, (255,255,255), (WINDOW_WIDTH // 2 - 100 - 100 - 50, WINDOW_HEIGHT // 2 - 50 - 50 -50, 200, 110))
            pygame.draw.rect(DISPLAY, (255,255,0), (WINDOW_WIDTH // 2  + 50, WINDOW_HEIGHT // 2 - 50 - 50 -50, 200, 110))
            pygame.draw.rect(DISPLAY, (255,255,255), (WINDOW_WIDTH // 2  - 250 , WINDOW_HEIGHT // 2 + 70 - 50, 200, 110))
            pygame.draw.rect(DISPLAY, (255,255,255), (WINDOW_WIDTH // 2  + 50, WINDOW_HEIGHT // 2 + 70 - 50, 200, 110))
            easy_diff = other_font.render('EASY', True, (0, 0, 0))
            medium_diff = other_font.render('MEDIUM', True, (0, 0, 0)) #THIS
            hard_diff = other_font.render('HARD', True, (0, 0, 0))
            hardcore_diff = other_font.render('HARDCORE', True, (0, 0, 0))
            back_button = other_font.render('BACK', True, (255, 255, 255))

        elif pointX == 0 and pointY == 1:
            pygame.draw.rect(DISPLAY, (255,255,255), (WINDOW_WIDTH // 2 - 100 - 100 - 50, WINDOW_HEIGHT // 2 - 50 - 50 -50, 200, 110))
            pygame.draw.rect(DISPLAY, (255,255,255), (WINDOW_WIDTH // 2  + 50, WINDOW_HEIGHT // 2 - 50 - 50 -50, 200, 110))
            pygame.draw.rect(DISPLAY, (255,255,0), (WINDOW_WIDTH // 2  - 250 , WINDOW_HEIGHT // 2 + 70 - 50, 200, 110))
            pygame.draw.rect(DISPLAY, (255,255,255), (WINDOW_WIDTH // 2  + 50, WINDOW_HEIGHT // 2 + 70 - 50, 200, 110))
            easy_diff = other_font.render('EASY', True, (0, 0, 0))
            medium_diff = other_font.render('MEDIUM', True, (0, 0, 0))
            hard_diff = other_font.render('HARD', True, (0, 0, 0)) #THIS
            hardcore_diff = other_font.render('HARDCORE', True, (0, 0, 0))
            back_button = other_font.render('BACK', True, (255, 255, 255))

        elif pointX == 1 and pointY == 1:
            pygame.draw.rect(DISPLAY, (255,255,255), (WINDOW_WIDTH // 2 - 100 - 100 - 50, WINDOW_HEIGHT // 2 - 50 - 50 -50, 200, 110))
            pygame.draw.rect(DISPLAY, (255,255,255), (WINDOW_WIDTH // 2  + 50, WINDOW_HEIGHT // 2 - 50 - 50 -50, 200, 110))
            pygame.draw.rect(DISPLAY, (255,255,255), (WINDOW_WIDTH // 2  - 250 , WINDOW_HEIGHT // 2 + 70 - 50, 200, 110))
            pygame.draw.rect(DISPLAY, (255,255,0), (WINDOW_WIDTH // 2  + 50, WINDOW_HEIGHT // 2 + 70 - 50, 200, 110))
            easy_diff = other_font.render('EASY', True, (0, 0, 0))
            medium_diff = other_font.render('MEDIUM', True, (0, 0, 0))
            hard_diff = other_font.render('HARD', True, (0, 0, 0))
            hardcore_diff = other_font.render('HARDCORE', True, (0, 0, 0)) #THIS
            back_button = other_font.render('BACK', True, (255, 255, 255))

        elif pointX == 0 or 1 and pointY == 2:
            pygame.draw.rect(DISPLAY, (255,255,255), (WINDOW_WIDTH // 2 - 100 - 100 - 50, WINDOW_HEIGHT // 2 - 50 - 50 -50, 200, 110))
            pygame.draw.rect(DISPLAY, (255,255,255), (WINDOW_WIDTH // 2  + 50, WINDOW_HEIGHT // 2 - 50 - 50 -50, 200, 110))
            pygame.draw.rect(DISPLAY, (255,255,255), (WINDOW_WIDTH // 2  - 250 , WINDOW_HEIGHT // 2 + 70 - 50, 200, 110))
            pygame.draw.rect(DISPLAY, (255,255,255), (WINDOW_WIDTH // 2  + 50, WINDOW_HEIGHT // 2 + 70 - 50, 200, 110))

            easy_diff = other_font.render('EASY', True, (0, 0, 0))
            medium_diff = other_font.render('MEDIUM', True, (0, 0, 0))
            hard_diff = other_font.render('HARD', True, (0, 0, 0))
            hardcore_diff = other_font.render('HARDCORE', True, (0, 0, 0))
            back_button = other_font.render('BACK', True, (255, 255, 0)) #THIS

        difficulty_title_rect = difficulty_title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 200 - 40))
        easy_diff_rect = easy_diff.get_rect(center=(WINDOW_WIDTH // 2 -100 - 50, WINDOW_HEIGHT // 2 - 10 - 40 ))
        medium_diff_rect = medium_diff.get_rect(center=(WINDOW_WIDTH // 2 +100 + 50, WINDOW_HEIGHT // 2 - 10 - 40))
        hard_diff__rect = hard_diff.get_rect(center=(WINDOW_WIDTH // 2-100 - 50, WINDOW_HEIGHT // 2 + 160 - 40))
        hardcore_diff__rect = hardcore_diff.get_rect(center=(WINDOW_WIDTH // 2 +100 + 50, WINDOW_HEIGHT // 2 + 160 - 40))
        back_button_rect = back_button.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 200))

        DISPLAY.blit(easyBG, (WINDOW_WIDTH // 2 - 100 - 50 - 90, WINDOW_HEIGHT // 2 - 90 - 50 ) )
        DISPLAY.blit(mediumBG, (WINDOW_WIDTH // 2 - 80 + 50 + 90, WINDOW_HEIGHT // 2 - 90 - 50 ) )
        DISPLAY.blit(hardBG, (WINDOW_WIDTH // 2 - 100 - 50 - 90, WINDOW_HEIGHT // 2 + 0 + 30 ) )
        DISPLAY.blit(hardcoreBG, (WINDOW_WIDTH // 2 - 80 + 50 + 90, WINDOW_HEIGHT // 2 + 0 + 30 ) )

        DISPLAY.blit(difficulty_title, difficulty_title_rect)
        DISPLAY.blit(easy_diff, easy_diff_rect)
        DISPLAY.blit(medium_diff, medium_diff_rect)
        DISPLAY.blit(hard_diff, hard_diff__rect)
        DISPLAY.blit(hardcore_diff, hardcore_diff__rect)
        DISPLAY.blit(back_button, back_button_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    pointY = pointY + 1
                elif event.key == pygame.K_UP:
                    pointY = pointY - 1
                elif event.key == pygame.K_LEFT:
                    pointX = pointX + 1
                elif event.key == pygame.K_RIGHT:
                    pointX = pointX - 1
                elif event.key == pygame.K_RETURN:
                    if pointX == 0 and pointY == 0:
                        game_easy()
                    elif pointX == 1 and pointY == 0:
                        game_medium()
                    elif pointX == 0 and pointY == 1:
                        game_hard()
                    elif pointX == 1 and pointY == 1:
                        game_hardcore()
                    elif pointX == 0 or 1 and pointY == 2:
                        main_menu()
                    
        pointX = pointX % 2
        pointY = pointY % 3
        pygame.display.update()

def askName(difficulty="TEST"):
    name = ""

    while True:
        DISPLAY.blit(resizedBgMenu, (0, 0))

        title = title_font.render(difficulty + " COMPLETED", True, (255, 255, 255))
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 200))
        DISPLAY.blit(title, title_rect)

        name_input = other_font2.render("Enter your name: " + name, True, (255, 255, 0))
        name_input_rect = name_input.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        DISPLAY.blit(name_input, name_input_rect)




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    name = name + "A"
                if event.key == pygame.K_b:
                    name = name + "B"
                if event.key == pygame.K_c:
                    name = name + "C"
                if event.key == pygame.K_d:
                    name = name + "D"
                if event.key == pygame.K_e:
                    name = name + "E"
                if event.key == pygame.K_f:
                    name = name + "F"
                if event.key == pygame.K_g:
                    name = name + "G"
                if event.key == pygame.K_h:
                    name = name + "H"
                if event.key == pygame.K_i:
                    name = name + "I"
                if event.key == pygame.K_j:
                    name = name + "J"
                if event.key == pygame.K_k:
                    name = name + "K"
                if event.key == pygame.K_l:
                    name = name + "L"
                if event.key == pygame.K_m:
                    name = name + "M"
                if event.key == pygame.K_n:
                    name = name + "N"
                if event.key == pygame.K_o:
                    name = name + "O"
                if event.key == pygame.K_p:
                    name = name + "P"
                if event.key == pygame.K_q:
                    name = name + "Q"
                if event.key == pygame.K_r:
                    name = name + "R"
                if event.key == pygame.K_s:
                    name = name + "S"
                if event.key == pygame.K_t:
                    name = name + "T"
                if event.key == pygame.K_u:
                    name = name + "U"
                if event.key == pygame.K_v:
                    name = name + "V"
                if event.key == pygame.K_w:
                    name = name + "W"
                if event.key == pygame.K_x:
                    name = name + "X"
                if event.key == pygame.K_y:
                    name = name + "Y"
                if event.key == pygame.K_z:
                    name = name + "Z"
                if event.key == pygame.K_BACKSPACE:
                    name = name[0:len(name) - 1]
                if event.key == pygame.K_RETURN:
                    f = open("ranking.txt", "a")
                    f.write(name + " - " + difficulty + "\n")
                    f.close()
                    main_menu()

        pygame.display.update()

def bullet_probability(difficulty):
    probability = rd.randint(1,5)
    if difficulty == "easy" and (probability == 1 or probability == 2):
        return True
    if difficulty == "medium" and (probability == 1 or probability == 2 or probability == 3):
        return True
    if difficulty == "hard" and (probability == 1 or probability == 2 or probability == 3 or probability == 4):
        return True
    if difficulty == "hardcore" and (probability == 1 or probability == 2 or probability == 3 or probability == 4 or probability == 5):
        return True

def game_over(difficulty):
    point = 0
    while True:
        DISPLAY.fill((0, 0, 0))

        title = other_font3.render('GAME OVER', True, (255, 255, 255))
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
        DISPLAY.blit(title, title_rect)

        if point == 0:
            over_option = other_font.render('RETRY', True, (255, 255, 0))
            back_option = other_font.render("BACK", True, (255, 255, 255))
        if point == 1:
            over_option = other_font.render('RETRY', True, (255, 255, 255))
            back_option = other_font.render("BACK", True, (255, 255, 0))


        over_option_rect = over_option.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100))
        back_option_rect = back_option.get_rect(center=(WINDOW_WIDTH // 2 , WINDOW_HEIGHT // 2 + 150))

        DISPLAY.blit(over_option, over_option_rect)
        DISPLAY.blit(back_option, back_option_rect)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    point = point + 1
                elif event.key == pygame.K_DOWN:
                    point = point - 1
                elif event.key == pygame.K_RETURN:
                    if point == 0:
                        if difficulty == "easy":
                            game_easy()
                        if difficulty == "medium":
                            game_medium()
                        if difficulty == "hard":
                            game_hard()
                        if difficulty == "hardcore":
                            game_hardcore()
                    if point == 1:
                        selectDiff()

        point = point % 2
        pygame.display.update()

pygame.mixer.music.load('MainMusic.mp3')
pygame.mixer.music.play(-1)



main_menu()







