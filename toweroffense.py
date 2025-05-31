import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))
clock  = pygame.time.Clock()
gameIsRunning = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while gameIsRunning:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameIsRunning = False

    #fill screen background
    screen.fill("blue")

    pygame.draw.circle(screen, "red", player_pos, 40)

    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_w]:
        player_pos.y -= 300 * dt
    if userInput[pygame.K_s]:
        player_pos.y += 300 * dt
    if userInput[pygame.K_a]:
        player_pos.x -= 300 * dt
    if userInput[pygame.K_d]:
        player_pos.x += 300 *dt


    pygame.display.flip()

    #delta time
    dt = clock.tick(60) / 1000

pygame.quit()
           
