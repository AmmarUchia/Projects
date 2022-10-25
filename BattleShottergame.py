import pygame
import os
pygame.font.init()
WIDTH, HEIGHT = 1380, 840
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SpaceShip Game")

# color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Border
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

# position
Yellow_Spaceship_pos = (260, 329)
Red_Spaceship_pos = (900, 329)

# FPS And Velocity
VEL = 7


FPS = 60

# scale
Scale = 55, 40

# bullet speed
bullet_speed = 15

# Ammo
MAX_BULLETS = 10
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

# Implemting spaceships

Yellow_Spaceship_Image = pygame.image.load(
    '/home/ammar/Downloads/Python/spaceship_yellow.png')
Red_Spaceship_Image = pygame.image.load(
    '/home/ammar/Downloads/Python/spaceship_red.png')
Yellow_Spaceship = pygame.transform.rotate(
    pygame.transform.scale(Yellow_Spaceship_Image, Scale), 90)
Red_Spaceship = pygame.transform.rotate(
    pygame.transform.scale(Red_Spaceship_Image, Scale), -90)

# Add BackGround
BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(
    '/home/ammar/Downloads/Python/space.png'), (WIDTH, HEIGHT))

# Helth
RED_HEALTH = 100
YELLOW_HEALTH = 100


# FONTws
HEALTH_FONT = pygame.font.SysFont('cosmicsan', 40)
winner_font = pygame.font.SysFont('bold', 100)


def draw(red, yellow, red_bullets, yellow_bullets, YELLOW_HEALTH, RED_HEALTH):
    WIN.blit(BACKGROUND_IMAGE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    RED_HEALTH_text = HEALTH_FONT.render("Health: "+str(RED_HEALTH), 1, WHITE)
    YELLOW_HEALTH_text = HEALTH_FONT.render(
        "Health: " + str(YELLOW_HEALTH), 1, WHITE)
    WIN.blit(YELLOW_HEALTH_text, (WIDTH - RED_HEALTH_text.get_width() - 10, 10))
    WIN.blit(RED_HEALTH_text, (10, 10))

    WIN.blit(Yellow_Spaceship, (yellow.x, yellow.y))
    WIN.blit(Red_Spaceship, (red.x, red.y))
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()


def yellow_movment(yellow, key):
    key = pygame.key.get_pressed()
    if key[pygame.K_a] and yellow.x - VEL > 0:  # left
        yellow.x -= VEL
    if key[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  # Right
        yellow.x += VEL
    if key[pygame.K_w] and yellow.y - VEL > 0:  # UP
        yellow.y -= VEL
    if key[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 8:  # DOWN
        yellow.y += VEL


def red_movment(red, key):
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # left
        red.x -= VEL
    if key[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # Right
        red.x += VEL
    if key[pygame.K_UP] and red.y - VEL > 0:  # UP
        red.y -= VEL
    if key[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 8:  # DOWN
        red.y += VEL


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += bullet_speed
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= bullet_speed
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def draw_winner(text):
    draw_text = winner_font.render(text,  1, WHITE)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width() /
             2, HEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(2000)


def main():
    red = pygame.Rect(700, 300, *Scale)
    red_bullets = []
    yellow_bullets = []
    RED_HEALTH = 10
    YELLOW_HEALTH = 10
    yellow = pygame.Rect(100, 300, *Scale)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)

                elif event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
            if event.type == RED_HIT:
                RED_HEALTH -= 1

            elif event.type == YELLOW_HIT:
                YELLOW_HEALTH -= 1
        winner = ''
        if RED_HEALTH <= 0:

            winner = "Yellow Wins"

        if YELLOW_HEALTH <= 0:

            winner = "Red Wins"
        if winner != '':
            draw_winner(winner)
        key = pygame.key.get_pressed()
        yellow_movment(yellow, key)
        red_movment(red, key)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        draw(red, yellow, red_bullets, yellow_bullets, RED_HEALTH, YELLOW_HEALTH)

    main()


if __name__ == "__main__":
    main()
